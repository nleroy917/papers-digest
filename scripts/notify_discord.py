"""Post a newly published research digest to a Discord webhook."""

import argparse
import json
import mimetypes
import re
import secrets
import sys
import urllib.error
import urllib.request
from pathlib import Path


MAX_MESSAGE_LENGTH = 1_900
TITLE_PATTERN = re.compile(r"^### \[(.+?)\]\(")


def extract_titles(markdown: str) -> list[str]:
    """Return paper titles from the rendered digest in display order."""
    return [match.group(1) for line in markdown.splitlines() if (match := TITLE_PATTERN.match(line))]


def split_title_messages(week: str, titles: list[str], digest_url: str) -> list[str]:
    """Split a titles-only digest announcement into Discord-safe messages."""
    header = f"📚 **Research Digest — {week}**\n\n"
    footer = f"\n\nFull digest: {digest_url}\n`digest.md` is attached below."
    messages = []
    current = header

    for index, title in enumerate(titles, start=1):
        line = f"{index}. {title}\n"
        if len(current) + len(line) + len(footer) > MAX_MESSAGE_LENGTH and current != header:
            messages.append(current.rstrip())
            current = ""
        current += line

    if not titles:
        current += "No paper titles were found in this digest.\n"
    messages.append((current + footer).strip())
    return messages


def post_json(webhook_url: str, payload: dict) -> None:
    """Post a JSON Discord webhook message and raise on a failed response."""
    body = json.dumps(payload).encode("utf-8")
    request = urllib.request.Request(
        webhook_url,
        data=body,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(request, timeout=30):
        pass


def post_attachment(webhook_url: str, content: str, digest_path: Path) -> None:
    """Post the final Discord message with digest.md attached."""
    boundary = f"----paper-digest-{secrets.token_hex(16)}"
    payload = json.dumps({"content": content, "allowed_mentions": {"parse": []}}).encode("utf-8")
    mime_type = mimetypes.guess_type(digest_path.name)[0] or "text/markdown"
    body = b"".join([
        f"--{boundary}\r\n".encode(),
        b'Content-Disposition: form-data; name="payload_json"\r\n',
        b"Content-Type: application/json\r\n\r\n",
        payload,
        b"\r\n",
        f'--{boundary}\r\nContent-Disposition: form-data; name="files[0]"; filename="{digest_path.name}"\r\n'.encode(),
        f"Content-Type: {mime_type}\r\n\r\n".encode(),
        digest_path.read_bytes(),
        b"\r\n",
        f"--{boundary}--\r\n".encode(),
    ])
    request = urllib.request.Request(
        webhook_url,
        data=body,
        headers={"Content-Type": f"multipart/form-data; boundary={boundary}"},
        method="POST",
    )
    with urllib.request.urlopen(request, timeout=30):
        pass


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--digest", type=Path, required=True)
    parser.add_argument("--digest-url", required=True)
    parser.add_argument("--webhook-url", required=True)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    markdown = args.digest.read_text(encoding="utf-8")
    first_line = markdown.splitlines()[0] if markdown else ""
    week = first_line.removeprefix("# Research Digest — ").strip() or "Latest"
    messages = split_title_messages(week, extract_titles(markdown), args.digest_url)

    if args.dry_run:
        print(f"would send {len(messages)} Discord message(s) and attach {args.digest.name}")
        return

    try:
        for message in messages[:-1]:
            post_json(args.webhook_url, {"content": message, "allowed_mentions": {"parse": []}})
        post_attachment(args.webhook_url, messages[-1], args.digest)
    except urllib.error.HTTPError as error:
        raise SystemExit(f"Discord webhook rejected the notification (HTTP {error.code}).") from error
    except urllib.error.URLError as error:
        raise SystemExit("Could not reach the Discord webhook.") from error

    print(f"sent {len(messages)} Discord message(s) and attached {args.digest.name}")


if __name__ == "__main__":
    main()

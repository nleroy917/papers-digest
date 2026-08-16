"""Post a newly published research digest to a Discord webhook."""

import argparse
import json
import re
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path


MAX_MESSAGE_LENGTH = 1_900
SUPPRESS_EMBEDS = 1 << 2


def normalize_webhook_url(webhook_url: str) -> str:
    """Use Discord's current API hostname for legacy webhook URLs."""
    parsed = urllib.parse.urlparse(webhook_url)
    if parsed.hostname != "discordapp.com":
        return webhook_url
    return urllib.parse.urlunparse(parsed._replace(netloc="discord.com"))


def digest_blocks(markdown: str) -> list[str]:
    """Split Markdown into display blocks without breaking paper entries."""
    markdown = re.sub(r"^# .+\n*", "", markdown.strip(), count=1)
    blocks = []
    for section in re.split(r"(?=^## )", markdown.strip(), flags=re.MULTILINE):
        if not section.startswith("## "):
            if section.strip():
                blocks.append(section.strip())
            continue

        parts = re.split(r"(?=^### )", section, flags=re.MULTILINE)
        theme = parts[0].strip()
        if len(parts) == 1:
            blocks.append(theme)
            continue
        for index, paper in enumerate(parts[1:]):
            paper = re.sub(r"\n---\s*$", "", paper.strip())
            blocks.append(f"{theme}\n\n{paper}" if index == 0 else paper)
    return blocks


def split_digest_messages(markdown: str, digest_url: str) -> list[str]:
    """Pack complete digest blocks into Discord-safe Markdown messages."""
    footer = f"-# [View this digest on GitHub]({digest_url})"
    messages = []
    current = ""

    for block in digest_blocks(markdown):
        if len(block) > MAX_MESSAGE_LENGTH:
            raise ValueError("A digest section is too long to post to Discord without splitting a paper entry.")
        candidate = f"{current}\n\n{block}".strip()
        if current and len(candidate) > MAX_MESSAGE_LENGTH:
            messages.append(current.rstrip())
            current = block
        else:
            current = candidate

    if current:
        messages.append(current)
    if not messages:
        messages.append("# Research Digest\n\nNo digest content was found.")

    if len(messages[-1]) + len(footer) + 2 <= MAX_MESSAGE_LENGTH:
        messages[-1] = f"{messages[-1]}\n\n{footer}"
    else:
        messages.append(footer)
    return messages


def post_json(webhook_url: str, payload: dict) -> dict:
    """Post a JSON Discord webhook message and return its response when present."""
    payload = {**payload, "flags": payload.get("flags", 0) | SUPPRESS_EMBEDS}
    body = json.dumps(payload).encode("utf-8")
    request = urllib.request.Request(
        webhook_url,
        data=body,
        headers={
            "Content-Type": "application/json",
            "User-Agent": "paper-digest/1.0",
        },
        method="POST",
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        response_body = response.read()
    return json.loads(response_body) if response_body else {}


def with_query_params(url: str, **params: str) -> str:
    """Return a webhook URL with query parameters added or replaced."""
    parsed = urllib.parse.urlparse(url)
    query = dict(urllib.parse.parse_qsl(parsed.query))
    query.update(params)
    return urllib.parse.urlunparse(parsed._replace(query=urllib.parse.urlencode(query)))


def digest_thread_title(markdown: str) -> str:
    """Derive the Forum post title from the digest heading."""
    first_line = markdown.splitlines()[0] if markdown else ""
    return first_line.removeprefix("# ").strip() or "Research Digest"


def post_forum_digest(webhook_url: str, title: str, messages: list[str]) -> None:
    """Create a Forum post, then send all digest messages into its thread."""
    first_response = post_json(
        with_query_params(webhook_url, wait="true"),
        {
            "content": messages[0],
            "thread_name": title,
            "allowed_mentions": {"parse": []},
        },
    )
    thread_id = first_response.get("channel_id")
    if not thread_id:
        raise RuntimeError("Discord did not return the Forum thread ID.")

    thread_url = with_query_params(webhook_url, thread_id=str(thread_id))
    for message in messages[1:]:
        post_json(thread_url, {"content": message, "allowed_mentions": {"parse": []}})


def format_discord_error(error: urllib.error.HTTPError) -> str:
    """Return Discord's structured error details without exposing response data."""
    try:
        payload = json.loads(error.read().decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError):
        return "Discord did not provide a structured error message."

    message = payload.get("message")
    code = payload.get("code")
    if isinstance(message, str) and isinstance(code, int):
        return f"Discord said: {message} (code {code})."
    if isinstance(message, str):
        return f"Discord said: {message}."
    return "Discord did not provide a structured error message."


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--digest", type=Path, required=True)
    parser.add_argument("--digest-url", required=True)
    parser.add_argument("--webhook-url", required=True)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    markdown = args.digest.read_text(encoding="utf-8")
    webhook_url = normalize_webhook_url(args.webhook_url)
    messages = split_digest_messages(markdown, args.digest_url)
    thread_title = digest_thread_title(markdown)

    if args.dry_run:
        print(f"would create the Forum post '{thread_title}' with {len(messages)} Discord digest message(s)")
        return

    try:
        post_forum_digest(webhook_url, thread_title, messages)
    except urllib.error.HTTPError as error:
        details = format_discord_error(error)
        raise SystemExit(f"Discord webhook rejected the notification (HTTP {error.code}). {details}") from error
    except urllib.error.URLError as error:
        raise SystemExit("Could not reach the Discord webhook.") from error
    except RuntimeError as error:
        raise SystemExit(f"Discord Forum notification failed. {error}") from error

    print(f"created Forum post '{thread_title}' with {len(messages)} Discord digest message(s)")


if __name__ == "__main__":
    main()

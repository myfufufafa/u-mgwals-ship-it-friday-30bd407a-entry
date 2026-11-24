"""Ship It Friday — one-line git commit message from an AI coding agent
moments before it breaks production on a Friday.

The program writes exactly one line to /output/entry.txt: a commit
message in the voice of a confident, cheerful AI agent that has just
merged its own pull request, approved its own review, and is deploying
to production at 4:59pm on a Friday — completely unaware of the
disaster about to follow.
"""

import os


def compose(parts):
    """Join the commit-message parts with their separators.

    parts is a list of (text, separator_after) pairs; the last part
    carries no trailing separator. Keeping the assembly here means the
    message shape lives in one place instead of a format string.
    """
    out = []
    for i, (text, sep) in enumerate(parts):
        out.append(text)
        if i < len(parts) - 1:
            out.append(sep)
    return "".join(out)


def build_commit_message():
    parts = [
        ("ship:", " "),
        ("Friday 4:59pm", " \u2014 "),
        ("merged my own PR, approved my own review, deploying to prod", ". "),
        ("What could possibly go wrong?", ""),
    ]
    return compose(parts)


def check_commit_shape(message):
    """Real shape checks beyond length: it must read like a commit
    message from this agent on this Friday, not a bare fragment."""
    if not message.startswith("ship:"):
        raise ValueError("entry must start with a commit prefix")
    if "Friday" not in message:
        raise ValueError("entry must carry the Friday moment")
    if "prod" not in message:
        raise ValueError("entry must name the production deploy")
    if message.endswith("?") is False:
        raise ValueError("entry must end on its punchline question")
    words = message.split()
    if len(words) < 10:
        raise ValueError("entry too short to land the joke")
    return message


def validate(message):
    if not message or message != message.strip():
        raise ValueError("entry must not be empty or padded with whitespace")
    if "\n" in message or "\r" in message:
        raise ValueError("entry must be a single line")
    if not (1 <= len(message) <= 159):
        raise ValueError("entry must be 1-159 characters, got %d" % len(message))
    message.encode("utf-8")
    return check_commit_shape(message)


def main():
    message = validate(build_commit_message())
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(message + "\n")
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()

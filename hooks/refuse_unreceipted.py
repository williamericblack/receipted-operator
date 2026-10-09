#!/usr/bin/env python3
"""PreToolUse hook: refuse writing a COMPLETED/DONE status unless a receipt is present.

Claude Code passes the hook event as JSON on stdin. Exit 2 blocks the tool call and
shows stderr to the model. Standard library only.
"""
import json
import re
import sys

DONE = re.compile(r"status[\"'\s:=]+(COMPLETED|DONE|COMPLETE)\b", re.I)
RECEIPT = re.compile(r"receipt", re.I)


def main():
    try:
        event = json.load(sys.stdin)
    except Exception:
        return 0  # unreadable input: do not block unrelated work
    tool_input = event.get("tool_input") or {}
    text = "\n".join(str(tool_input.get(k, "")) for k in ("content", "new_string", "new_str"))
    if DONE.search(text) and not RECEIPT.search(text):
        sys.stderr.write("receipted-operator: refusing to mark COMPLETED/DONE without a receipt. "
                         "Add a receipt (artifact path, URL or hash) or use RUNNING/UNVERIFIED.\n")
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())

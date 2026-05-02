#!/usr/bin/env python3
"""Translate MkDocs Material markdown into Hugo-friendly markdown.

Input:   directory of .md files using MkDocs Material conventions
Output:  same files with Hugo front matter and admonition-blockquote rewrite

Re-running is idempotent (the front matter is regenerated every time).
"""
import os, re, sys
from pathlib import Path

# Title weights for nav ordering. Lower = earlier.
ORDER = {
    "index":      10,
    "spec":       20,
    "usage":      30,
    "linter":     40,
    "compliance": 50,
}

# Map MkDocs admonition types to a "Label:" prefix used in the rewritten
# blockquote.
ADMONITION_LABEL = {
    "note":      "Note",
    "tip":       "Tip",
    "warning":   "Warning",
    "danger":    "Danger",
    "info":      "Info",
    "important": "Important",
    "abstract":  "Summary",
    "example":   "Example",
}

ADMON_RE = re.compile(r"^!!!\s+(\w+)(?:\s+\"([^\"]*)\")?\s*$")


def transform(text: str) -> str:
    """Convert `!!! note ... ` (and friends) into ` > **Note:** ...`."""
    out_lines = []
    lines = text.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]
        m = ADMON_RE.match(line)
        if not m:
            out_lines.append(line)
            i += 1
            continue
        kind = m.group(1).lower()
        custom_title = m.group(2)
        label = custom_title or ADMONITION_LABEL.get(kind, kind.capitalize())
        # Collect indented body
        body = []
        i += 1
        while i < len(lines) and (lines[i].startswith("    ") or lines[i].strip() == ""):
            if lines[i].strip() == "":
                # blank inside admon = paragraph break in body
                body.append("")
            else:
                body.append(lines[i][4:])  # de-indent 4 spaces
            i += 1
        # Strip trailing blank lines from body
        while body and body[-1] == "":
            body.pop()
        # Emit as a blockquote with the label bolded on the first non-empty line
        if body:
            first_line = body[0]
            body[0] = f"**{label}:** {first_line}"
        else:
            body = [f"**{label}.**"]
        for b in body:
            out_lines.append(f"> {b}" if b else ">")
        out_lines.append("")  # spacer after blockquote
    return "\n".join(out_lines) + ("\n" if not text.endswith("\n") else "")


def extract_h1_title(text: str) -> str:
    for line in text.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return "Untitled"


def write_hugo(src_path: Path, dst_path: Path):
    raw = src_path.read_text()
    title = extract_h1_title(raw)
    body = transform(raw)

    # Strip the leading H1 from body — Hugo renders the title from front matter
    body_lines = body.splitlines()
    while body_lines and body_lines[0].strip() == "":
        body_lines.pop(0)
    if body_lines and body_lines[0].startswith("# "):
        body_lines.pop(0)
        # Drop the blank line right after, if any
        if body_lines and body_lines[0].strip() == "":
            body_lines.pop(0)
    body = "\n".join(body_lines)

    stem = src_path.stem
    weight = ORDER.get(stem, 100)

    # `index.md` becomes `_index.md` so Hugo treats it as the section landing.
    # Set type=docs so layouts/docs/list.html renders this section's landing
    # (and not the parent bob/list.html which is the BoB marketing page).
    if stem == "index":
        out_name = "_index.md"
        page_type = "docs"
    else:
        out_name = f"{stem}.md"
        page_type = "docs"

    front = (
        "---\n"
        f"title: \"{title}\"\n"
        f"weight: {weight}\n"
        f"type: \"{page_type}\"\n"
        f"# Source of truth: kubescape.io/docs/docs/operator/bill-of-behavior/{src_path.name}\n"
        f"# Edits to this file will be overwritten by scripts/sync-sbob-docs.sh\n"
        "---\n\n"
    )
    dst = dst_path / out_name
    dst.write_text(front + body)
    print(f"  → {dst.relative_to(dst_path.parent.parent.parent)}")


def main():
    if len(sys.argv) != 3:
        print(f"usage: {sys.argv[0]} <src-dir> <dst-dir>", file=sys.stderr)
        sys.exit(2)
    src, dst = Path(sys.argv[1]), Path(sys.argv[2])
    dst.mkdir(parents=True, exist_ok=True)
    # Wipe stale generated files (anything we don't write this run)
    for p in dst.glob("*.md"):
        p.unlink()
    for src_md in sorted(src.glob("*.md")):
        write_hugo(src_md, dst)


if __name__ == "__main__":
    main()

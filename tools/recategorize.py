"""
One-off script: migrate all 128 posts' top-level category to new 3-category scheme.

Mapping:
  Retro                                           -> [日常雜談, Retro]
  (anything else, single-layer)  e.g. [Git]       -> [技術學習, Git]
  (anything else, multi-layer)   e.g. [Front-End, React]  -> [技術學習, Front-End, React]

Run:
  python3 tools/recategorize.py --dry-run [file1 file2 ...]
  python3 tools/recategorize.py                    # writes to all posts
"""

import os
import re
import sys
import argparse
import difflib

POSTS_DIR = "source/_posts"

TECH_TOP = "技術學習"
LIFE_TOP = "日常雜談"

# Top-level categories that belong to "雜談"
CHITCHAT_TOPS = {"Retro"}


def process_content(content):
    """Return (new_content, original_cats, new_cats) or (content, None, None) if unchanged."""
    cats_m = re.search(r"^(categories:\s*\n)((?:\s*-\s*.+\n)+)", content, re.M)
    if not cats_m:
        return content, None, None

    block_start = cats_m.group(1)
    block_body = cats_m.group(2)

    original_cats = [
        re.sub(r"^\s*-\s*", "", line).strip()
        for line in block_body.strip().split("\n")
        if line.strip()
    ]
    if not original_cats:
        return content, None, None

    # Already migrated — skip
    if original_cats[0] in (TECH_TOP, LIFE_TOP, "日本生活"):
        return content, original_cats, None

    top = original_cats[0]
    new_top = LIFE_TOP if top in CHITCHAT_TOPS else TECH_TOP
    new_cats = [new_top] + original_cats

    new_block_body = "".join(f"  - {c}\n" for c in new_cats)
    new_content = content[: cats_m.start()] + block_start + new_block_body + content[cats_m.end():]

    return new_content, original_cats, new_cats


def show_diff(filename, original, updated):
    diff = difflib.unified_diff(
        original.splitlines(keepends=True),
        updated.splitlines(keepends=True),
        fromfile=f"a/{filename}",
        tofile=f"b/{filename}",
        n=2,
    )
    sys.stdout.writelines(diff)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true", help="Preview changes without writing")
    ap.add_argument("files", nargs="*", help="Specific files (relative to repo root); default: all")
    args = ap.parse_args()

    if args.files:
        targets = args.files
    else:
        targets = sorted(
            os.path.join(POSTS_DIR, f)
            for f in os.listdir(POSTS_DIR)
            if f.endswith(".md")
        )

    changed = 0
    skipped = 0
    no_cats = 0

    for path in targets:
        with open(path, encoding="utf-8") as fp:
            original = fp.read()

        updated, orig_cats, new_cats = process_content(original)

        if orig_cats is None:
            no_cats += 1
            continue
        if new_cats is None:
            skipped += 1
            continue

        changed += 1
        if args.dry_run:
            print(f"\n### {path}")
            print(f"  {orig_cats}  ->  {new_cats}")
            show_diff(path, original, updated)
        else:
            with open(path, "w", encoding="utf-8") as fp:
                fp.write(updated)

    print(
        f"\n[{'DRY-RUN' if args.dry_run else 'DONE'}] "
        f"changed={changed}, already-migrated={skipped}, no-categories={no_cats}, total={len(targets)}"
    )


if __name__ == "__main__":
    main()

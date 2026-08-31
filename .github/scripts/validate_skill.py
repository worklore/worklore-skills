#!/usr/bin/env python3
"""Validate every skills/<name>/SKILL.md against the repo's contract.

Runs in CI on each PR. Emits GitHub ::error:: annotations so problems show
inline on the pull request, and exits non-zero if anything is wrong — so a
maintainer only ever reviews well-formed skills.
"""
import re
import sys
import pathlib

try:
    import yaml
except ImportError:
    print("::error::pyyaml is required (pip install pyyaml)")
    sys.exit(1)

ROOT = pathlib.Path("skills")
NAME_RE = re.compile(r"^[a-z0-9-]+$")
RESERVED = ("anthropic", "claude")
XML_RE = re.compile(r"<[^>]+>")
errors = []


def err(msg):
    errors.append(msg)
    print(f"::error::{msg}")


def parse_frontmatter(text):
    m = re.match(r"^---\n(.*?)\n---\n?(.*)$", text, re.S)
    if not m:
        return None, None
    try:
        fm = yaml.safe_load(m.group(1)) or {}
    except yaml.YAMLError as e:
        return f"__yamlerror__{e}", None
    return fm, m.group(2)


def main():
    if not ROOT.exists():
        print("No skills/ directory yet — nothing to validate.")
        return 0

    folders = sorted(p for p in ROOT.iterdir() if p.is_dir())
    if not folders:
        print("skills/ is empty — nothing to validate.")
        return 0

    for folder in folders:
        skill = folder / "SKILL.md"
        rel = f"skills/{folder.name}/SKILL.md"
        if not skill.exists():
            err(f"{folder.name}/ has no SKILL.md")
            continue

        fm, body = parse_frontmatter(skill.read_text(encoding="utf-8"))
        if fm is None:
            err(f"{rel}: missing or malformed frontmatter (needs a --- ... --- block)")
            continue
        if isinstance(fm, str) and fm.startswith("__yamlerror__"):
            err(f"{rel}: YAML parse error: {fm[len('__yamlerror__'):]}")
            continue

        name = fm.get("name")
        desc = fm.get("description")

        if not name:
            err(f"{rel}: frontmatter is missing required field 'name'")
        elif not isinstance(name, str):
            err(f"{rel}: 'name' must be a string")
        else:
            if not NAME_RE.match(name):
                err(f"{rel}: 'name' must be lowercase letters, numbers, and hyphens only")
            if len(name) > 64:
                err(f"{rel}: 'name' exceeds 64 characters")
            if any(r in name.lower() for r in RESERVED):
                err(f"{rel}: 'name' may not contain 'anthropic' or 'claude'")
            if name != folder.name:
                err(f"{rel}: folder '{folder.name}' must equal frontmatter name '{name}'")
            if XML_RE.search(name):
                err(f"{rel}: 'name' must not contain XML/HTML tags")

        if not desc:
            err(f"{rel}: frontmatter is missing required field 'description'")
        elif not isinstance(desc, str) or not desc.strip():
            err(f"{rel}: 'description' must be a non-empty string")
        else:
            if len(desc) > 1024:
                err(f"{rel}: 'description' exceeds 1024 characters")
            if XML_RE.search(desc):
                err(f"{rel}: 'description' must not contain XML/HTML tags")

        if body is not None:
            if "## Instructions" not in body:
                err(f"{rel}: missing an '## Instructions' section")
            if "## Examples" not in body:
                err(f"{rel}: missing an '## Examples' section")

    if errors:
        print(f"\n{len(errors)} problem(s) found. See annotations above.")
        return 1
    print(f"All {len(folders)} skill(s) valid ✓")
    return 0


if __name__ == "__main__":
    sys.exit(main())

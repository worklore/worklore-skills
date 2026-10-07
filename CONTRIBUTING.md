# Contributing a skill

Thanks for adding to the library! Contributions are welcome year-round. The rules
below keep quality high and let a small
team review quickly — most are checked automatically by CI, so following them means
your PR is accepted fast.

## The 2-minute flow

1. **Copy the template.** `cp -r template skills/<your-skill-name>`
2. **Rename the folder** to your skill's name — lowercase letters, numbers, and
   hyphens only (e.g. `conventional-commit-message`).
3. **Fill `SKILL.md`:**
   - `name` — must **exactly match the folder name** (≤ 64 chars, `[a-z0-9-]`, and
     must not contain `anthropic` or `claude`).
   - `description` — one or two sentences stating **what the skill does AND when an
     agent should use it** (≤ 1024 chars). This is what the agent matches a request
     against, so make the trigger explicit.
   - Write a `## Instructions` section (concrete, imperative steps) and an
     `## Examples` section (at least one input → expected behavior).
4. **Open a PR.** Fill the checklist in the PR template.

## Hard rules (CI enforces these)

- **One skill per PR.** A PR adds exactly **one new** `skills/<name>/` folder and
  touches nothing else. This keeps review atomic.
- **Folder name === `name` frontmatter**, and the name must be **unique** (no
  existing folder with that name — no duplicates).
- **Both frontmatter fields present** and within the limits above; **no XML/HTML
  tags** in either.
- **`## Instructions` and `## Examples` sections must exist.**
- Squash-merge only.

## Quality bar (a human checks these)

- **Recommend it personally.** Only submit a skill you'd actually use. Copy-paste
  filler, thin wrappers, and "hello world" skills are closed.
- **Be tool-agnostic where possible.** If a skill needs a specific tool or key, say
  so explicitly and name it — never "an appropriate library".
- **No secrets, no private URLs, no employer internals.** Sanitize.
- **Optional bundled files** (`REFERENCE.md`, `scripts/`) are fine if they're needed
  and safe to run.

## Optional frontmatter (allowed, never required)

`author` (your GitHub handle), `tags` (a list), `license`. Requiring only `name` and
`description` keeps every skill drop-in compatible with the official spec.

## Not sure it fits?

Open a **skill-request** issue and ask before writing. A `good first issue` is a
skill we've already scoped for you — the easiest place to start.

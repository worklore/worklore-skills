---
name: conventional-commit-message
description: Write a Conventional Commits message from the currently staged git changes. Use when the user asks to "commit", "write a commit message", or has staged changes and wants a well-formed message (feat/fix/docs/etc., with an optional scope and body).
---

# Conventional Commit Message

Generate a commit message that follows the Conventional Commits spec from the
staged diff, then commit on approval.

## Instructions

1. Read the staged changes: `git diff --cached`. If nothing is staged, tell the
   user and stop (or offer to `git add -A` first).
2. Choose the type from the change: `feat` (new capability), `fix` (bug fix),
   `docs`, `refactor`, `test`, `perf`, `build`, `ci`, `chore`, `style`.
3. Choose an optional scope — the area touched (e.g. `api`, `auth`, a module
   name). Omit it if the change spans many areas.
4. Write the subject: `type(scope): summary` — imperative mood, lowercase after
   the colon, no trailing period, ≤ 72 characters.
5. For non-trivial changes, add a body: a blank line, then *what* and *why*
   wrapped at ~72 columns. Add a `BREAKING CHANGE:` footer when applicable.
6. Show the message to the user and get approval before committing. On approval:
   `git commit -m "<subject>" -m "<body>"`.

## Examples

- **Input:** staged diff adds rate limiting to the login endpoint.
  **Expected:** `feat(auth): add rate limiting to the login endpoint` + a short
  body explaining the threshold and why.

- **Input:** staged diff fixes an off-by-one in pagination.
  **Expected:** `fix(api): correct off-by-one in page offset calculation`

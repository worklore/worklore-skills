# agent skills — a community library of `SKILL.md` files

A curated, open collection of **agent skills** — each a `SKILL.md` that teaches an
AI coding agent (Claude Code, Cursor, Codex, and anything that reads skills) to do
one task well. Drop a skill into `~/.claude/skills/` (or a project's
`.claude/skills/`) and your agent gains that capability.

Format-compatible with [Anthropic's Agent Skills](https://github.com/anthropics/skills):
**folder-per-skill, two-field frontmatter**. If a skill lives here, it installs there.

Built and maintained by the people behind **[worklore.dev](https://worklore.dev)** —
*stories your agent can run.*

## Use a skill

```bash
git clone https://github.com/worklore/worklore-skills
cp -r worklore-skills/skills/<skill-name> ~/.claude/skills/
```
Restart your agent (or open a new session). That's it.

## Contribute a skill (about 2 minutes)

1. Copy the `template/` folder to `skills/<your-skill-name>/`.
2. Fill the two frontmatter fields (`name`, `description`) and write the
   `## Instructions` and `## Examples` sections.
3. Open a pull request — **one skill per PR**.

CI validates the format automatically, so a maintainer only reviews PRs that are
already well-formed. The flow is designed so your **first PR just works** — see
[CONTRIBUTING.md](CONTRIBUTING.md).

## What counts as a skill (scope)

A **reusable, task-focused capability** with concrete instructions an agent can
follow — and, ideally, that you'd personally recommend. Not: personal dotfiles,
one-line prompts, secrets, or link lists to other tools. Unsure? Open a
**skill-request** issue first.

## Got it working? Tell the story

A skill is the *how*. The *proof it works for someone else* lives on worklore: when
a skill lands a real result for you, publish a short, reproducible story at
[worklore.dev](https://worklore.dev) — narrative + a "Reproduce this" contract other
people's agents can run.

## Hacktoberfest

This repo takes part in **Hacktoberfest**. Look for [`good first issue`](../../labels/good%20first%20issue)
— each is one specific skill to write. Quality is enforced by CI; low-effort or spam
PRs are labeled `spam`/`invalid`. One skill per PR, please.

## License

MIT — see [LICENSE](LICENSE). By contributing, you agree your skill is released
under it.

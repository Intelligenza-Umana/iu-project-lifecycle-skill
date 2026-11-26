# Project Lifecycle Skill — v0.3.0

**An [Intelligenza Umana](https://github.com/fabiozagaria/intelligenza-umana) project.** [Official project registry](https://github.com/fabiozagaria/intelligenza-umana/blob/main/docs/PROJECT_REGISTRY.md).

A reusable skill for project context, decisions, documentation, audits and session handoffs. The method lives here and project-specific context stays in the target repository. Operations are instructions for an agent rather than deterministic CLI commands.

## Install

Clone this repository, then run the installer from its root. Python 3.9 or newer is required for installation. The skill itself has no runtime dependency.

```sh
python3 scripts/install.py --host codex --project /path/to/project
python3 scripts/install.py --host claude --project /path/to/project
```

Omit `--project` to install for your user in `~/.agents/skills/project-lifecycle` for Codex or `~/.claude/skills/project-lifecycle` for Claude Code. Project installations go under the corresponding `.agents/skills` or `.claude/skills` directory. Install both if you use both tools. Restart the host after installation.

The installer copies `SKILL.md`, `references/` and `templates/`. Running it again with identical content is a no-op. If an installation differs, it stops and preserves your files. To update, review and back up or remove the old skill directory, then rerun the installer. It does not modify project instructions or create project documents.

Claude Code can also load this repository as a plugin with `claude --plugin-dir /path/to/iu-project-lifecycle-skill`. For details see [Codex](integrations/codex/README.md) and [Claude Code](integrations/claude/README.md).

## Use

Ask the agent to use `project-lifecycle` for a target repository and an operation: bootstrap, resume, handoff, audit, sync, migrate, status, plan or decision. In Codex invoke `$project-lifecycle`; in Claude Code invoke `/project-lifecycle` for an installed skill, or `/iu-project-lifecycle:project-lifecycle` for the plugin. The agent reads [SKILL.md](SKILL.md), the [Context Integrity Protocol](references/context-integrity.md), and the relevant references. Review generated changes before committing.

## Verify

Run `python3 -m unittest discover -s tests -v`. Installation tests use temporary directories. The agent workflows remain subject to host behavior and human review; see [tests](tests/README.md) for acceptance scenarios and limitations.

[MIT license](LICENSE).

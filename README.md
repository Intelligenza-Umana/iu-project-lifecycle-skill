# Project Lifecycle Skill — v0.3.1

**An [Intelligenza Umana](https://github.com/Intelligenza-Umana/intelligenza-umana) project.** [Official project registry](https://github.com/Intelligenza-Umana/intelligenza-umana/blob/main/docs/PROJECT_REGISTRY.md).

A reusable skill for project context, decisions, documentation, audits and session handoffs. The method lives here and project-specific context stays in the target repository. Operations are instructions for an agent rather than deterministic CLI commands.

## Install

If you already use the [Intelligenza Umana marketplace](https://github.com/Intelligenza-Umana/iu-marketplace#add-the-marketplace), run `claude plugin install iu-project-lifecycle@intelligenza-umana` to install this plugin from the shared catalog.

**Claude Code plugin** (2.1.275 or later), inside a session:

```text
/plugin install iu-project-lifecycle --marketplace Intelligenza-Umana/iu-project-lifecycle-skill
```

Or from a terminal: `claude plugin marketplace add Intelligenza-Umana/iu-project-lifecycle-skill`, then `claude plugin install iu-project-lifecycle@iu-project-lifecycle`. The skill is then `/iu-project-lifecycle:project-lifecycle`.

**Skill installer** (Codex, or Claude Code without the plugin system):

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

## Intelligenza Umana community

**Human intelligence. Artificial assistance.**

[Organization](https://github.com/Intelligenza-Umana) · [Website](https://intelligenza-umana-web.vercel.app/) · [Discord](https://discord.gg/Zt85ZYEXAA) · [Onboarding](https://github.com/Intelligenza-Umana/intelligenza-umana/blob/main/community/ONBOARDING.md) · [Good first issues](https://github.com/search?q=org%3AIntelligenza-Umana+is%3Apublic+is%3Aissue+is%3Aopen+no%3Aassignee+label%3A%22good+first+issue%22&type=issues)

Contributions to public projects are welcome from everyone, regardless of experience. Organization membership and Discord are optional. Discuss scope in an issue before starting work, then submit a focused pull request with verification evidence and limitations. Use English for shared GitHub discussions.

To become an organization member, [submit a membership request](https://github.com/Intelligenza-Umana/intelligenza-umana/issues/new?template=membership_request.md). The Discord numeric user ID is optional; the issue is public, so you may provide it privately instead. A maintainer reviews requests manually and sends an official GitHub invitation if approved. Sentinel is configured to assign the Contributor role on Discord entry; the Member role is assigned manually only after identity and accepted GitHub membership are verified. Neither membership nor a Discord role automatically grants repository write access.

Follow the [code of conduct](https://github.com/Intelligenza-Umana/intelligenza-umana/blob/main/community/CODE_OF_CONDUCT.md) and [private security reporting policy](https://github.com/Intelligenza-Umana/intelligenza-umana/blob/main/SECURITY.md). Each project retains its own license, maturity and verification requirements.

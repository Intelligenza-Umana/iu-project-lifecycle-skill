# Claude Code

Run `python3 scripts/install.py --host claude --project /path/to/project` from the skill repository, or omit `--project` for a user-wide installation. Restart Claude Code and invoke `/project-lifecycle` or ask Claude to use it.

Alternatively load the repository directly with `claude --plugin-dir /path/to/iu-project-lifecycle-skill` and invoke `/iu-project-lifecycle:project-lifecycle`. The plugin manifest identifies the root skill. The skill includes references and templates, and the installer preserves existing files. It does not change the target project's `CLAUDE.md`.

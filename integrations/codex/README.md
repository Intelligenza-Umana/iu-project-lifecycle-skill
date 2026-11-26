# Codex

Run `python3 scripts/install.py --host codex --project /path/to/project` from the skill repository. Omit `--project` for user-wide installation. Restart Codex and invoke `$project-lifecycle` or ask it to use the skill for a lifecycle task. Codex discovers repository skills in `.agents/skills` and user skills in `~/.agents/skills`.

The installer includes references and templates. It stops if the target differs and preserves existing instructions and files. In cloud environments the installed files must be available in the environment. Installation does not itself change the target project's `AGENTS.md`.

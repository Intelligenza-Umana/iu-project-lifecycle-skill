# Handoff — 2026-11-26

## Status
v0.3.0 adds a native skill installer for Codex and Claude Code, a Claude plugin manifest and installer tests. Existing method, references and templates are retained. The installer preserves different existing installations and is idempotent for identical content.

## Verification
Automated installer tests cover both project paths, repeat installation, preservation of modified files and symlink destinations. See tests/README.md for agent workflow acceptance scenarios.

## Open work
Live discovery and workflow execution with authenticated Codex and Claude Code remain unverified. Adopt the skill in target projects only after the user identifies them. Keep each target's existing conventions and instructions.

Attribution: Intelligenza Umana. This is a project identity, not a cryptographic signature.

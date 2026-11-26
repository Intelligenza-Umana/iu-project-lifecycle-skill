#!/usr/bin/env python3
"""Install the complete skill in a Codex or Claude Code discovery directory."""
import argparse
import filecmp
import os
from pathlib import Path
import shutil
import tempfile

SOURCE = Path(__file__).resolve().parent.parent
FILES = ('SKILL.md', 'references', 'templates')


def same_contents(source, target):
    expected = {p.relative_to(source) for p in source.rglob('*') if p.is_file()}
    actual = {p.relative_to(target) for p in target.rglob('*') if p.is_file()}
    return (expected == actual and not any(p.is_symlink() for p in target.rglob('*'))
            and all(filecmp.cmp(source / p, target / p, shallow=False) for p in expected))


def install(host, project=None):
    if host not in ('codex', 'claude'):
        raise ValueError('Unsupported host')
    base = Path(project).resolve() if project else Path.home()
    parent = base / ('.agents/skills' if host == 'codex' else '.claude/skills')
    target = parent / 'project-lifecycle'
    parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix='.project-lifecycle-', dir=parent) as temp:
        staged = Path(temp) / 'project-lifecycle'
        staged.mkdir()
        for name in FILES:
            item = SOURCE / name
            if item.is_dir():
                shutil.copytree(item, staged / name)
            else:
                shutil.copy2(item, staged / name)
        if target.is_symlink():
            raise FileExistsError(f'Refusing to replace symlink: {target}')
        if target.exists():
            if target.is_dir() and same_contents(staged, target):
                return target, False
            raise FileExistsError(f'Existing installation differs: {target}. Review it before updating.')
        try:
            os.rename(staged, target)
        except FileExistsError:
            raise FileExistsError(f'Installation appeared concurrently: {target}') from None
    return target, True


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--host', required=True, choices=('codex', 'claude'))
    parser.add_argument('--project', type=Path, help='Install in this existing project directory; omit for your user')
    args = parser.parse_args()
    if args.project and not args.project.is_dir():
        parser.error('Project must be an existing directory')
    try:
        target, created = install(args.host, args.project)
    except (OSError, ValueError) as error:
        parser.exit(1, f'Installation failed: {error}\n')
    print(f"{'Installed' if created else 'Already installed'}: {target}")


if __name__ == '__main__':
    main()

import importlib.util
from pathlib import Path
import tempfile
import unittest

ROOT = Path(__file__).resolve().parent.parent
spec = importlib.util.spec_from_file_location('installer', ROOT / 'scripts/install.py')
installer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(installer)


class InstallTests(unittest.TestCase):
    def test_project_install_for_both_hosts_is_complete_and_idempotent(self):
        with tempfile.TemporaryDirectory() as tmp:
            for host, directory in (('codex', '.agents'), ('claude', '.claude')):
                target, created = installer.install(host, tmp)
                self.assertTrue(created)
                self.assertEqual(target, Path(tmp) / directory / 'skills/project-lifecycle')
                self.assertTrue((target / 'SKILL.md').is_file())
                self.assertTrue((target / 'references/context-integrity.md').is_file())
                self.assertTrue((target / 'templates/HANDOFF.md').is_file())
                self.assertEqual(installer.install(host, tmp), (target, False))

    def test_bundled_skills_match_fresh_installations(self):
        with tempfile.TemporaryDirectory() as tmp:
            for host in ('codex', 'claude'):
                with self.subTest(host=host):
                    installed, _ = installer.install(host, tmp)
                    bundled = ROOT / installed.relative_to(tmp)
                    self.assertTrue(installer.same_contents(installed, bundled), bundled)

    def test_preserves_modified_installation_and_project_files(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / 'AGENTS.md').write_text('existing instructions')
            target, _ = installer.install('codex', root)
            (target / 'SKILL.md').write_text('local edits')
            with self.assertRaises(FileExistsError):
                installer.install('codex', root)
            self.assertEqual((target / 'SKILL.md').read_text(), 'local edits')
            self.assertEqual((root / 'AGENTS.md').read_text(), 'existing instructions')

    def test_refuses_symlink_destination(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            parent = root / '.agents/skills'
            parent.mkdir(parents=True)
            (parent / 'project-lifecycle').symlink_to(root / 'missing')
            with self.assertRaises(FileExistsError):
                installer.install('codex', root)


if __name__ == '__main__':
    unittest.main()

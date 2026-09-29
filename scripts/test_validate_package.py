#!/usr/bin/env python3
"""Unit-test the local package checker with temporary faults; never run a model."""
from __future__ import annotations

import json
from pathlib import Path
import shutil
import tempfile
import unittest

from validate_package import validate

SOURCE = Path(__file__).resolve().parents[1]


class PackageCheckerTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name) / 'engineering-bridge'
        shutil.copytree(SOURCE, self.root, ignore=shutil.ignore_patterns('__pycache__', '*.pyc'))

    def rewrite(self, path: str, old: str, new: str) -> None:
        target = self.root / path
        text = target.read_text(encoding='utf-8')
        self.assertIn(old, text)
        target.write_text(text.replace(old, new, 1), encoding='utf-8')

    def reject(self, check: str) -> None:
        result = validate(self.root)
        self.assertFalse(result['passed'])
        self.assertTrue(any(c['check'] == check and not c['passed'] for c in result['checks']))

    def edit_cases(self, fn) -> None:
        p = self.root / 'evals/cases.json'
        data = json.loads(p.read_text(encoding='utf-8'))
        fn(data)
        p.write_text(json.dumps(data, ensure_ascii=False), encoding='utf-8')

    def test_good_package(self) -> None:
        self.assertTrue(validate(self.root)['passed'])

    def test_managed_skill_directory(self) -> None:
        renamed = self.root.with_name('skill-' + 'a' * 32)
        self.root.rename(renamed)
        self.root = renamed
        self.assertTrue(validate(self.root)['passed'])

    def test_unrelated_directory_name(self) -> None:
        renamed = self.root.with_name('unrelated-package')
        self.root.rename(renamed)
        self.root = renamed
        self.reject('name_matches_folder')

    def test_missing_discovery_reference(self) -> None:
        (self.root / 'references/open-source-discovery.md').unlink()
        self.reject('required_files')

    def test_bad_skill_name(self) -> None:
        self.rewrite('SKILL.md', 'name: engineering-bridge', 'name: Broken_Name')
        self.reject('name_matches_folder')

    def test_broken_link(self) -> None:
        self.rewrite('SKILL.md', '(references/open-source-discovery.md)', '(references/missing.md)')
        self.reject('relative_links_resolve_inside_package')

    def test_duplicate_eval_id(self) -> None:
        self.edit_cases(lambda d: d['cases'].append(d['cases'][0].copy()))
        self.reject('eval_ids_unique')

    def test_claimed_model_execution(self) -> None:
        self.edit_cases(lambda d: d.update(status='all_model_tests_passed'))
        self.reject('eval_execution_status_honest')

    def test_inconsistent_eval_version(self) -> None:
        self.edit_cases(lambda d: d.update(version='1.0.0'))
        self.reject('eval_version_consistency')

    def test_cross_before_local(self) -> None:
        p = self.root / 'SKILL.md'
        s = p.read_text(encoding='utf-8')
        a = '### 3. 本领域开源检索'
        b = '### 4. 仅在进入跨域分支后'
        s = s.replace(a, '__TEMP_HEADING__', 1).replace(b, a, 1).replace('__TEMP_HEADING__', b, 1)
        p.write_text(s, encoding='utf-8')
        self.reject('discovery_phase_order')

    def test_missing_second_search(self) -> None:
        self.rewrite('SKILL.md', '### 5. 跨域之后，再找对应领域的开源实现', '### 5. 跳过第二次检索')
        self.reject('discovery_phase_order')

    def test_default_prompt_skips_gate(self) -> None:
        self.rewrite('agents/openai.yaml', '保留事实、假设和硬约束；先检索本领域', '保留事实、假设和硬约束；直接发散')
        self.reject('default_prompt_keeps_gate')

    def test_empty_description(self) -> None:
        p = self.root / 'SKILL.md'
        lines = p.read_text(encoding='utf-8').splitlines()
        lines = ['description: ""' if line.startswith('description:') else line for line in lines]
        p.write_text('\n'.join(lines)+'\n', encoding='utf-8')
        self.reject('description_1_to_1024')

    def test_path_outside_package(self) -> None:
        p = self.root / 'README.md'
        p.write_text(p.read_text(encoding='utf-8') + '\n[escape](../outside.txt)\n', encoding='utf-8')
        self.reject('relative_links_resolve_inside_package')


if __name__ == '__main__':
    unittest.main(verbosity=2)

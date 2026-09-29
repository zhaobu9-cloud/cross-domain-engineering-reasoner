#!/usr/bin/env python3
"""Check local structure only. Does not run models, network requests or engineering tasks.

The frontmatter check targets this package's simple YAML representation; it is not
an implementation of the complete YAML standard. Python 3.9+; standard library only.
"""
from __future__ import annotations

import argparse
import ast
import json
from pathlib import Path
import re
import sys

REQUIRED = (
    'SKILL.md', 'README.md', 'SOURCES.md', 'agents/openai.yaml',
    'references/transfer-guide.md', 'references/evidence-and-experiments.md',
    'references/engineering-scenarios.md', 'assets/report-template.md',
    'assets/experiment-card.md', 'assets/handoff-template.md', 'assets/case-record.md',
    'examples/powder-inspection.md', 'examples/goal-reframing.md',
    'evals/cases.json', 'evals/README.md', 'scripts/validate_package.py',
    'CHANGELOG.md', 'references/open-source-discovery.md',
    'assets/project-reference-card.md', 'assets/search-log.md',
    'examples/open-source-routing.md', 'scripts/test_validate_package.py',
)


def validate(root: Path) -> dict:
    root = root.resolve()
    checks: list[dict] = []

    def add(name: str, passed: bool, detail: str = '') -> None:
        checks.append({'check': name, 'passed': bool(passed), 'detail': detail})

    missing = [name for name in REQUIRED if not (root / name).is_file()]
    add('required_files', not missing, ', '.join(missing))
    try:
        raw = (root / 'SKILL.md').read_bytes()
        text = raw.decode('utf-8')
    except (OSError, UnicodeError) as exc:
        add('read_skill_utf8', False, str(exc))
        return {'scope': 'package_structure_only', 'passed': False, 'checks': checks}
    add('utf8_without_bom', not text.startswith('\ufeff'))
    match = re.match(r'\A---\r?\n(.*?)\r?\n---(?:\r?\n|$)', text, re.S)
    add('frontmatter_delimiters', match is not None)
    front = match.group(1) if match else ''
    name_match = re.search(r'^name:\s*([a-z0-9-]+)\s*$', front, re.M)
    name = name_match.group(1) if name_match else ''
    valid_name = bool(re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', name))
    # ChatGPT retains an existing personal skill in its generated directory
    # when the frontmatter name changes. Keep ordinary package names strict.
    managed_folder = bool(re.fullmatch(r'skill-[a-f0-9]{32}', root.name))
    add('name_matches_folder', valid_name and 1 <= len(name) <= 64
        and (name == root.name or root.name == 'cross-domain-engineering-reasoner' or managed_folder), name)
    desc_match = re.search(r'^description:\s*(".*")\s*$', front, re.M)
    try:
        desc = json.loads(desc_match.group(1)) if desc_match else ''
    except json.JSONDecodeError:
        desc = ''
    add('description_1_to_1024', isinstance(desc, str) and 1 <= len(desc) <= 1024)
    version_match = re.search(r'^  version:\s*"(\d+\.\d+\.\d+)"\s*$', front, re.M)
    version = version_match.group(1) if version_match else ''
    add('semantic_version_present', bool(version))
    add('main_under_500_lines', len(text.splitlines()) < 500, str(len(text.splitlines())))
    add('core_contract_terms', all(word in text for word in (
        '事实', '假设', '待验证', '硬约束', '无法判断', '最小试验', '未取得', '授权')))
    headings = ('### 3. 本领域开源检索', '### 4. 仅在进入跨域分支后', '### 5. 跨域之后，再找对应领域的开源实现')
    positions = [text.find(h) for h in headings]
    add('discovery_phase_order', all(p >= 0 for p in positions) and positions == sorted(positions))
    add('discovery_branch_states_present', all(word in text for word in (
        'IN_DOMAIN_FOUND', 'IN_DOMAIN_NOT_FOUND_WITHIN_SCOPE',
        'IN_DOMAIN_SEARCH_INCONCLUSIVE', 'IN_DOMAIN_SEARCH_SKIPPED_BY_USER',
        'CROSS_DOMAIN_FOUND', 'CROSS_DOMAIN_NOT_FOUND_WITHIN_SCOPE',
        'CROSS_DOMAIN_SEARCH_INCONCLUSIVE')))
    try:
        agent_text = (root / 'agents/openai.yaml').read_text(encoding='utf-8')
        prompt_match = re.search(r'^  default_prompt:\s*(".*")\s*$', agent_text, re.M)
        try:
            default_prompt = json.loads(prompt_match.group(1)) if prompt_match else ''
        except json.JSONDecodeError:
            default_prompt = ''
        add('default_prompt_keeps_gate', all(w in default_prompt for w in (
            '$engineering-bridge', '先检索本领域', '本轮未找到', '对应领域的开源实现')))
        readme_text = (root / 'README.md').read_text(encoding='utf-8')
        changelog_text = (root / 'CHANGELOG.md').read_text(encoding='utf-8')
        add('document_version_consistency', bool(version) and f'版本：{version}' in readme_text and f'## {version}' in changelog_text)
    except (OSError, UnicodeError) as exc:
        add('supporting_metadata_readable', False, str(exc))

    bad_links: list[str] = []
    bad_files: list[str] = []
    symlinks = [str(p.relative_to(root)) for p in root.rglob('*') if p.is_symlink()]
    add('no_symlinks', not symlinks, ', '.join(symlinks))
    for path in root.rglob('*.md'):
        try:
            content = path.read_text(encoding='utf-8')
        except (OSError, UnicodeError):
            bad_files.append(str(path.relative_to(root)))
            continue
        for target in re.findall(r'\[[^\]]*\]\(([^)]+)\)', content):
            if target.startswith(('http:', 'https:', 'mailto:', '#')):
                continue
            target = target.split('#', 1)[0]
            resolved = (path.parent / target).resolve()
            inside = resolved == root or root in resolved.parents
            if not inside or not resolved.exists():
                bad_links.append(f'{path.relative_to(root)} -> {target}')
    add('all_markdown_utf8', not bad_files, '; '.join(bad_files))
    add('relative_links_resolve_inside_package', not bad_links, '; '.join(bad_links))

    try:
        data = json.loads((root / 'evals/cases.json').read_text(encoding='utf-8'))
        cases = data['cases']
        schema_ok = isinstance(cases, list) and all(
            isinstance(c, dict)
            and isinstance(c.get('id'), str)
            and isinstance(c.get('name'), str)
            and type(c.get('should_trigger')) is bool
            and isinstance(c.get('prompt'), str) and bool(c['prompt'])
            and isinstance(c.get('expected_behaviors'), list) and bool(c['expected_behaviors'])
            and all(isinstance(v, str) for v in c['expected_behaviors'])
            and isinstance(c.get('failure_patterns'), list) and bool(c['failure_patterns'])
            and all(isinstance(v, str) for v in c['failure_patterns'])
            for c in cases
        )
        add('eval_case_schema', schema_ok and data.get('skill_name') == name)
        add('eval_version_consistency', bool(version) and data.get('version') == version)
        ids = [c['id'] for c in cases] if schema_ok else []
        add('eval_ids_unique', schema_ok and len(ids) == len(set(ids)))
        add('discovery_eval_coverage', all(f'OSS{i:02d}' in ids for i in range(1, 17)))
        positives = sum(c['should_trigger'] for c in cases) if schema_ok else 0
        negatives = len(cases) - positives if schema_ok else 0
        add('positive_and_near_negative_cases', positives >= 6 and negatives >= 3,
            f'positive={positives}, negative={negatives}')
        add('eval_execution_status_honest', data.get('status') == 'designed_not_model_executed')
    except (OSError, UnicodeError, ValueError, KeyError, TypeError) as exc:
        add('eval_file_readable', False, str(exc))

    errors = []
    for path in root.rglob('*.py'):
        try:
            ast.parse(path.read_text(encoding='utf-8'), filename=str(path))
        except (OSError, UnicodeError, SyntaxError) as exc:
            errors.append(str(exc))
    add('python_syntax', not errors, '; '.join(errors))
    return {'scope': 'package_structure_only', 'passed': all(c['passed'] for c in checks),
            'check_count': len(checks), 'checks': checks}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    result = validate(args.root)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result['passed'] else 1


if __name__ == '__main__':
    sys.exit(main())

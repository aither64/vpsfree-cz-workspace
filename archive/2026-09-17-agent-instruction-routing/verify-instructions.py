#!/usr/bin/env python3
"""Check the recorded instruction relocation without invoking a model."""
import hashlib
import json
from pathlib import Path
import re
import subprocess

TRACKING = Path(__file__).resolve().parent
WORKSPACE = TRACKING.parents[1]
GROUP = WORKSPACE / 'worktrees' / TRACKING.name
inventory = json.loads((TRACKING / 'inventory.json').read_text())
reports = []
errors = []
for row in inventory:
    name = row['name']
    git = (['git', '-C', str(WORKSPACE)] if name == 'workspace' else
           ['git', '--git-dir', str(WORKSPACE / 'repos' / (name + '.git'))])
    source = subprocess.check_output(git + ['show', row['base'] + ':AGENTS.md'], text=True)
    changed = row['changed']
    root = GROUP / name
    files = {'AGENTS.md': source}
    if changed:
        files = {'AGENTS.md': (root / 'AGENTS.md').read_text()}
        for directory in ['docs/agent-instructions', 'doc/agent-instructions']:
            for file in sorted((root / directory).glob('*.md')):
                files[str(file.relative_to(root))] = file.read_text()
    rules = []
    # Every original nonblank paragraph must survive verbatim, not merely its keywords.
    for match in re.finditer(r'\S[\s\S]*?(?=\n\s*\n|\Z)', source):
        paragraph = match.group().rstrip()
        line = source[:match.start()].count('\n') + 1
        destinations = [path for path, text in files.items() if paragraph in text]
        if not destinations:
            errors.append(f'{name}: original paragraph at line {line} is missing')
        rules.append({'source_line': line, 'source_end_line': line + paragraph.count('\n'),
                      'sha256': hashlib.sha256(paragraph.encode()).hexdigest(),
                      'destinations': destinations})
    core = files['AGENTS.md']
    links = re.findall(r'\]\(([^)]+agent-instructions/[^)]+\.md)\)', core)
    if changed:
        for target in links:
            if target not in files:
                errors.append(f'{name}: missing route {target}')
        for path in files:
            if path != 'AGENTS.md' and path not in links:
                errors.append(f'{name}: unrouted procedure {path}')
        if len(core.encode()) >= 24 * 1024:
            errors.append(f'{name}: core lacks headroom under 32 KiB loader limit')
        result = subprocess.run(['git', '-C', str(root), 'diff', '--check'], capture_output=True, text=True)
        if result.returncode:
            errors.append(f'{name}: whitespace: {result.stdout}{result.stderr}')
    reports.append({**row, 'changed': changed, 'core_bytes': len(core.encode()),
                    'procedure_bytes': sum(len(text.encode()) for path, text in files.items() if path != 'AGENTS.md'),
                    'paragraphs': rules, 'routes': links})
report = {'errors': errors, 'repositories': reports}
(TRACKING / 'coverage.json').write_text(json.dumps(report, indent=2) + '\n')
lines = ['# Instruction coverage', '',
         'Every original nonblank paragraph is checked verbatim against its retained or',
         'relocated destination. This proves textual preservation; reviewers separately',
         'check applicability, precedence and the new mandatory routes. Baselines refer',
         'to the exact revisions in inventory.json. No requirement was summarized away.', '',
         '| Repository | Baseline bytes | Core bytes | Reduction | Original paragraphs |',
         '| --- | ---: | ---: | ---: | ---: |']
for r in reports:
    lines.append(f"| {r['name']} | {r['bytes']} | {r['core_bytes']} | {100*(1-r['core_bytes']/r['bytes']):.1f}% | {len(r['paragraphs'])} |")
for r in reports:
    if not r['changed']:
        continue
    lines += ['', '## ' + r['name'], '', '| Original AGENTS.md lines | Destination |', '| --- | --- |']
    for p in r['paragraphs']:
        lines.append(f"| {p['source_line']}–{p['source_end_line']} | {', '.join(p['destinations']) or '**MISSING**'} |")
lines += ['', '## Limits', '',
          'Core sizes are bytes, not billed tokens. A task also loads its applicable',
          'procedures. Static coverage cannot prove model compliance. Fourteen cohesive',
          'repositories remain unchanged after inspection; the workspace and two',
          'larger repository instruction files use mandatory routes.', '',
          'Renamed clone aliases vpsadmin-kb-captures and vpsfree-mail-templates were',
          'deduplicated to vpsfree-kb-contracts and vpsfree-notification-templates.', '']
(TRACKING / 'coverage.md').write_text('\n'.join(lines))
for r in reports:
    print(f"{r['name']}: {r['bytes']} -> {r['core_bytes']} bytes; {len(r['paragraphs'])} paragraphs")
for error in errors:
    print('ERROR:', error)
raise SystemExit(bool(errors))

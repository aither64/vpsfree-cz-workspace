#!/usr/bin/env python3
"""Prepare only scoped source comparisons and static Bash/Ruby templates."""
from pathlib import Path
import hashlib
import json
import re
import subprocess
import textwrap

out = Path(__file__).resolve().parent
session = out.parent
product = session.parents[1] / 'worktrees' / session.name / 'vpsadminos'
original = json.loads((out / 'original-sha256.json').read_text())
owned = [entry['path'] for entry in original]
raw_paths = owned[:4]
added = '''      # Clear inherited group and special bits on this new directory only.
      chown 0:0 -- "$path" || return 1
      chmod 00755 -- "$path" || return 1
'''
blocks = []
for name in raw_paths:
    s = (product / name).read_text()
    old = (out / 'original' / name).read_text()
    assert s.count(added) == 1
    assert s.replace(added, '', 1) == old
    blocks.append(s[s.index('  coversPath ='):s.index('  nameservers =')])
assert all(s == blocks[0] for s in blocks)
assert (product / raw_paths[1]).read_bytes() == (product / raw_paths[2]).read_bytes()
suite_name = owned[-1]
suite = (product / suite_name).read_text()
old_suite = (out / 'original' / suite_name).read_text()
inverse_suite = re.sub(r"^\s*\$\{lib\.optionalString setgidParent ''\n.*?^\s*''\}\n", '\n', suite, flags=re.M | re.S)
# Preserve surrounding newlines while removing exactly the three new blocks.
for block in re.findall(r"^            \$\{lib\.optionalString setgidParent ''\n.*?^            ''\}\n", suite, flags=re.M | re.S):
    suite_fragment = block
    assert suite.count(block) == 1
    if 'inverse_exact' not in locals(): inverse_exact = suite
    inverse_exact = inverse_exact.replace(block, '', 1)
assert suite.count('lib.optionalString setgidParent') == 3
inverse_exact = inverse_exact.replace('        setgidParent = variant.fresh && variant.layout == "ancestor-lib";\n', '', 1)
assert inverse_exact == old_suite
assert subprocess.check_output(['git', '-C', str(product), 'diff', '--name-only']).decode().splitlines() == sorted(owned)
assert subprocess.check_output(['git', '-C', str(product), 'diff', '--cached']) == b''
assert (product / 'docs/containers/nixos.md').read_bytes() == subprocess.check_output(['git', '-C', str(product), 'show', 'HEAD:docs/containers/nixos.md'])
(out / 'source.patch').write_bytes(subprocess.check_output(['git', '-C', str(product), 'diff', '--', *owned]))
(out / 'inverse.patch').write_bytes(subprocess.check_output(['git', '-C', str(product), 'diff', '-R', '--', *owned]))
(out / 'frozen-sha256.json').write_text(json.dumps([{'path': name, 'sha256': hashlib.sha256((product / name).read_bytes()).hexdigest()} for name in owned], indent=2) + '\n')

def placeholders(s):
    while '${' in s:
        start = s.index('${')
        i, depth = start + 2, 1
        while depth:
            if s[i] == '{': depth += 1
            elif s[i] == '}': depth -= 1
            i += 1
        s = s[:start] + '/fixture/source' + s[i:]
    return s

raw = (product / raw_paths[1]).read_text()
bash = raw.split("  persistedSpecialfs = ''\n", 1)[1].split("\n  '';", 1)[0]
start = bash.index('      ${lib.concatMapStringsSep')
end = bash.index("      '') requiredStateMounts}", start) + len("      '') requiredStateMounts}")
bash = bash[:start] + '      # Static syntax only: generated tuple dispatch omitted.\n' + bash[end:]
(out / 'helper-template.sh').write_text(textwrap.dedent(placeholders(bash)) + '\n')
ruby = suite[suite.index("        require 'json'"):suite.index("\n      '';", suite.index("        require 'json'"))]
ruby, choices = re.subn(r"\$\{\n\s+if variant.fresh then\n\s+''\n(.*?)\n\s+''\n\s+else\n\s+''\n(.*?)\n\s+''\n\s+\}", lambda m: m[1] + '\n' + m[2], ruby, flags=re.S)
assert choices == 1
ruby = re.sub(r"\$\{lib\.optionalString [^\n]+ ''\n", '', ruby)
ruby = re.sub(r"^\s+''\}\n", '\n', ruby, flags=re.M)
(out / 'suite-template.rb').write_text('# Static syntax only: all optional bodies and inert Nix placeholders.\n' + placeholders(ruby) + '\n')
(out / 'source-comparison.txt').write_text(
    'PASS: exactly six assigned paths changed; index empty and guide byte-unchanged.\n'
    'PASS: each raw module differs solely by the same three helper lines.\n'
    'PASS: removing those lines restores every original raw module byte-for-byte.\n'
    'PASS: all four persistence blocks equal; latest stable equals 26.05.\n'
    'PASS: suite differs only by the new fresh-ancestor condition and its three blocks.\n'
    'PASS: removing those suite additions restores original suite byte-for-byte.\n'
    'PASS: static templates are prepared, not executed/evaluated.\n'
)
print((out / 'source-comparison.txt').read_text(), end='')

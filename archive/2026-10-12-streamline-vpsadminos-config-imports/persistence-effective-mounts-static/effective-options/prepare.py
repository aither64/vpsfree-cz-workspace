#!/usr/bin/env python3
"""Static syntax extraction and scoped source inventory, never Nix evaluation."""
import hashlib
import json
from pathlib import Path
import re
import subprocess
import textwrap

out = Path(__file__).resolve().parent
session = out.parent
product = session.parents[1] / 'worktrees' / session.name / 'vpsadminos'
raw_paths = [
    'os/lib/nixos-container/stable/vpsadminos-25.11.nix',
    'os/lib/nixos-container/stable/vpsadminos-26.05.nix',
    'os/lib/nixos-container/stable/vpsadminos.nix',
    'os/lib/nixos-container/unstable/vpsadminos.nix',
]
owned = raw_paths + [
    'tests/nixos-container-persistence-eval.nix',
    'tests/nixos-container-persistence-shell.sh',
    'tests/nixos-container-persistence-check.nix',
    'tests/fixtures/nixos-persistence-guests.nix',
    'tests/suite/dist-config/nixos-persistence-upgrade.nix',
    'tests/nixos-container-modules-eval.nix',
]
def git(*args):
    return subprocess.check_output(['git', '-C', str(product), *args])

def nix_placeholders(s):
    while '${' in s:
        start = s.index('${')
        i, depth = start + 2, 1
        while depth:
            if s[i] == '{': depth += 1
            elif s[i] == '}': depth -= 1
            i += 1
        s = s[:start] + '/fixture/source' + s[i:]
    return s

blocks = []
for name in raw_paths:
    s = (product / name).read_text()
    blocks.append(s[s.index('  coversPath ='):s.index('  nameservers =')])
    old = git('show', 'HEAD:' + name).decode()
    assert s[:s.index('  coversPath =')] == old[:old.index('  persistedStateMounts =')]
    assert s[s.index('  nameservers ='):] == old[old.index('  nameservers ='):]
    # Promotion and the ordinary fallback are outside this change's mechanism.
    for first, last in [
        ('  boot.specialFileSystems =', '  system.activationScripts ='),
        ('      # Keep this fallback aligned', '    source ${config.system.build.earlyMountScript}'),
        ('    vpsadminosPrepareStateDirectory()', '    vpsadminosMount'),
    ]:
        assert s[s.index(first):s.index(last, s.index(first))] == old[old.index(first):old.index(last, old.index(first))], (name, first)
assert all(block == blocks[0] for block in blocks)
assert (product / raw_paths[1]).read_bytes() == (product / raw_paths[2]).read_bytes()
raw = (product / raw_paths[1]).read_text()
bash = raw.split("  persistedSpecialfs = ''\n", 1)[1].split("\n  '';", 1)[0]
start = bash.index('      ${lib.concatMapStringsSep')
end = bash.index("      '') requiredStateMounts}", start) + len("      '') requiredStateMounts}")
bash = bash[:start] + '      # Static syntax only: Nix-generated tuple dispatch omitted.\n' + bash[end:]
(out / 'helpers-template.sh').write_text(textwrap.dedent(nix_placeholders(bash)) + '\n')

suite = (product / 'tests/suite/dist-config/nixos-persistence-upgrade.nix').read_text()
old_suite = git('show', 'HEAD:tests/suite/dist-config/nixos-persistence-upgrade.nix').decode()
for first, last in [
    ('        wait_for_guest_ready =', '        switch ='),
    ('            # Use the declarative', '            ${lib.optionalString (variant.layout != "root")'),
]:
    assert suite[suite.index(first):suite.index(last, suite.index(first))] == old_suite[old_suite.index(first):old_suite.index(last, old_suite.index(first))]
ruby = suite[suite.index("        require 'json'"):suite.index("\n      '';", suite.index("        require 'json'"))]
ruby, choices = re.subn(r"\$\{\n\s+if variant.fresh then\n\s+''\n(.*?)\n\s+''\n\s+else\n\s+''\n(.*?)\n\s+''\n\s+\}", lambda m: m[1] + '\n' + m[2], ruby, flags=re.S)
assert choices == 1
ruby = re.sub(r"\$\{lib\.optionalString [^\n]+ ''\n", '', ruby)
ruby = re.sub(r"^\s+''\}\n", '\n', ruby, flags=re.M)
ruby = nix_placeholders(ruby)
(out / 'suite-template.rb').write_text('# Static syntax only: all optional bodies; inert Nix placeholders.\n' + ruby + '\n')
for marker, filename in [('SHELL', 'store-copy-template.sh'), ('GUEST', 'readiness-template.sh')]:
    opener = 'machine.succeeds(<<~SHELL)\n' if marker == 'SHELL' else "<<~'GUEST',\n"
    body = suite.split(opener, 1)[1].split('\n              ' + marker, 1)[0] if marker == 'GUEST' else suite.split(opener, 1)[1].split('\n            SHELL', 1)[0]
    body = nix_placeholders(body).replace('#{nix_root}', '/fixture/nix')
    (out / filename).write_text(textwrap.dedent(body) + '\n')

baseline_mock = git('show', 'HEAD:tests/nixos-container-modules-eval.nix').decode()
mock = (product / 'tests/nixos-container-modules-eval.nix').read_text()
assert mock.replace('      boot.specialFileSystems = { };\n', '', 1) == baseline_mock
assert git('diff', '--cached') == b''
inventory = [{'path': name, 'sha256': hashlib.sha256((product / name).read_bytes()).hexdigest()} for name in owned]
(out / 'owned-sha256.json').write_text(json.dumps(inventory, indent=2) + '\n')
(out / 'technical.patch').write_bytes(git('diff', '--', *owned))
(out / 'source-comparison.txt').write_text(
    'PASS: all four new persistence blocks are identical.\n'
    'PASS: latest stable is byte-equal to versioned 26.05.\n'
    'PASS: original promotion, ordinary callback and recursive directory helper are unchanged.\n'
    'PASS: raw content outside the selected adapter block is unchanged.\n'
    'PASS: native store-copy/profile setup and failure-only readiness wrapper are unchanged.\n'
    'PASS: selector mock adds only the inert boot.specialFileSystems field.\n'
    'PASS: index is empty; lead guide is excluded from the technical patch/inventory.\n'
)
print((out / 'source-comparison.txt').read_text(), end='')
print('Static Bash/Ruby templates and ten-path SHA256 inventory prepared.')

"""Change only the two evaluated mount call paths; preserve every other byte."""
from pathlib import Path
import hashlib
import json
import re
import shlex
import sys
import textwrap

snippet_path, output_path, state_source, state_target, log_source, log_target = sys.argv[1:]
original = Path(snippet_path).read_bytes()
text = original.decode('utf-8')
raw_path = Path('/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-12-streamline-vpsadminos-config-imports/vpsadminos/os/lib/nixos-container/stable/vpsadminos-26.05.nix')
raw = raw_path.read_text()
raw_helper = textwrap.dedent(raw[raw.index('    # Abort in the activation shell:'):raw.index('    ${lib.concatMapStringsSep')])
function_pattern = re.compile(r'^vpsadminosMountPersistedState\(\) \{\n.*?\n\}', re.M | re.S)
expected_function = function_pattern.search(raw_helper)[0]
actual_function = function_pattern.search(text)[0]
assert actual_function == expected_function, 'Evaluated literal helper must match frozen raw source'
pattern = re.compile(
    r'(?m)^([ \t]*if ! vpsadminosMountPersistedState[ \t]+)'
    r'(/persistent/var/lib/nixos|/persistent/var/log)([ \t]+)'
    r'(/var/lib/nixos|/var/log)([^\n]*; then[ \t]*)$'
)
matches = list(pattern.finditer(text))
assert len(matches) == 2, 'Expected exactly two evaluated call statements'
replacement_paths = {
    ('/persistent/var/lib/nixos', '/var/lib/nixos'): (state_source, state_target),
    ('/persistent/var/log', '/var/log'): (log_source, log_target),
}
assert {(m[2], m[4]) for m in matches} == set(replacement_paths)
restorations = []


def replace(match):
    source, target = replacement_paths[(match[2], match[4])]
    line = match[1] + shlex.quote(source) + match[3] + shlex.quote(target) + match[5]
    restorations.append((line, match[0]))
    return line


adapted = pattern.sub(replace, text)
restored = adapted
for changed, unchanged in restorations:
    assert restored.count(changed) == 1
    restored = restored.replace(changed, unchanged, 1)
assert restored.encode('utf-8') == original, 'Only configured call paths may change'
helper = text[:matches[0].start()].encode('utf-8')
adapted_helper = adapted[:adapted.index(restorations[0][0])].encode('utf-8')
assert helper == adapted_helper, 'Literal helper must remain unchanged'
Path(output_path).write_bytes(adapted.encode('utf-8'))
Path(output_path + '.provenance.json').write_text(json.dumps({
    'input': str(Path(snippet_path).resolve()),
    'input_sha256': hashlib.sha256(original).hexdigest(),
    'helper_sha256': hashlib.sha256(helper).hexdigest(),
    'helper_byte_identical': True,
    'raw_source': str(raw_path),
    'literal_function_matches_frozen_raw': True,
    'literal_function_sha256': hashlib.sha256(actual_function.encode()).hexdigest(),
    'restoring_only_two_call_paths_reproduces_input': True,
    'call_paths': {key[1]: list(value) for key, value in replacement_paths.items()},
}, indent=2) + '\n')

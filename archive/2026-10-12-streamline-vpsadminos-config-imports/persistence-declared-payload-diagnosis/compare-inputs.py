import copy, difflib, hashlib, json, re, textwrap, sys
from pathlib import Path
record = Path(__file__).resolve().parent
out = record / 'quick'
old = json.loads((record.parent/'runtime-effective.yf2uje2x/original-config.json').read_text())
data = json.loads((out / 'inputs.json').read_text())
new = data['config']
assert data['persistenceCheck'] == '/nix/store/6218pz068gff57gp72fjhw2b0ylh5msd-nixos-container-persistence.drv'
assert set(old) == set(new)
assert set(old['testScripts']) == set(new['testScripts']) and len(new['testScripts']) == 12
host_equal = {k:v for k,v in old.items() if k != 'testScripts'} == {k:v for k,v in new.items() if k != 'testScripts'}
if '--scripts-only' not in sys.argv:
    assert host_equal, 'Host/runner/machine inputs changed'
fragment_lines = (record/'proposal/insert.nix-fragment').read_text().splitlines(keepends=True)
expected_block = '    ' + textwrap.dedent(''.join(fragment_lines[1:-1]))
marker = '    # Initialize only the verified empty old-baseline fixture placeholder.\n'
anchor = '    exec_guest.call("printf \'%s'
provenance = re.compile(r"^    puts 'Candidate compatibility source: [^'\n]+'$", re.M)
summary = []
for name, item in new['testScripts'].items():
    old_item = old['testScripts'][name]
    assert {k:v for k,v in item.items() if k != 'script'} == {k:v for k,v in old_item.items() if k != 'script'}
    body = item['script']; previous = old_item['script']; stripped = body
    if name == 'declared-backing-26.05':
        assert body.count(marker) == 1
        start = body.index(marker); end = body.index('GUEST\n', start) + len('GUEST\n')
        assert body[start:end] == expected_block, 'Rendered correction differs from accepted block'
        stripped = body[:start] + body[end:]
    else:
        assert marker not in body
    assert len(provenance.findall(stripped)) == len(provenance.findall(previous)) == 1
    before, after = stripped.split(anchor, 1); old_before, old_after = previous.split(anchor, 1)
    # The added optional Nix block contributes only a blank line in other cases.
    equivalent = provenance.sub("    puts 'Candidate compatibility source: SOURCE'", before).rstrip(' \n') == provenance.sub("    puts 'Candidate compatibility source: SOURCE'", old_before).rstrip(' \n') and after == old_after
    if not equivalent:
        (out/(name+'.diff')).write_text(''.join(difflib.unified_diff(previous.splitlines(True),body.splitlines(True))))
    assert equivalent, name + ' changed outside the declared setup/provenance/adjacent blank line'
    (out/(name+'.rb')).write_text(body)
    summary.append(f'{name}: accepted insertion only' if name == 'declared-backing-26.05' else f'{name}: executable body identical')
summary += ['All generation and registration paths retained in compared script bodies.', ('All host/runner/machine fields and normal persistence check derivation identical.' if host_equal else 'Host equality NOT established: toplevel/squashfs differ; reuse gate remains open. Normal persistence check derivation is identical.'), 'Only candidate-source stdout provenance and the adjacent generated blank line are normalized.']
(out/'input-comparison.txt').write_text('\n'.join(summary)+'\n')
print('\n'.join(summary))

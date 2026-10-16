#!/usr/bin/env python3
"""Validate completed preparation and write exact retained-user approval requests."""
import json
from pathlib import Path
import uuid

tracking = Path('/home/aither/workspace/ai/vpsfree.cz/work/2026-10-14-i-d-like-the-dev-workspace')
runtime = '4ed9af55127743b7564cb4dd01d10c9f7fee5120'
expected = {'workspace': '750ab33c92d7b01e44152420ee5d2ab4c9493826',
            'vpsfree-cz-configuration': 'c90e56d5dd0e1ae3da1bf192ca88ab34b2f788a7',
            'dev-workspace': runtime}
quote = 'ok, proceed until it is implemented & verified. you can also deploy aitherdev using vpsfree-cz-configuration.'

for mode, name in [('machine', 'machine-prepared-feedback-4ed.json'),
                   ('profile', 'profile-prepared-4ed9af55.json')]:
    status = dict(line.split('=', 1) for line in (tracking / f'{mode}-prepare-feedback-4ed.status').read_text().splitlines())
    assert status['exit_status'] == '0'
    snapshot = json.loads((tracking / name).read_text())
    coverage = {item['repository']: item['revision'] for item in snapshot['operation']['coverage']}
    assert coverage['dev-workspace'] == runtime
    if mode == 'machine':
        assert coverage['vpsfree-cz-configuration'] == expected['vpsfree-cz-configuration']
        assert snapshot['operation']['configurationHead'] == expected['vpsfree-cz-configuration']
    else:
        assert coverage['workspace'] == expected['workspace']
        assert coverage['vpsfree-dev-workspace'] == '767dfd587e346168e1443e65ccdb67ce748f3fe3'
    request = {'schema': 1, 'requestId': str(uuid.uuid4()), 'kind': 'deploy',
               'scope': [{'machine': 'vpsfree:aitherdev', 'actions': ['switch', 'profile_activate'], 'reboot': False}],
               'source': {'kind': 'user_instruction', 'reference': 'Retained user deployment direction in this exact bound conversation', 'quote': quote},
               'reviewedSnapshot': snapshot['id']}
    with (tracking / f'{mode}-approval-feedback-4ed-request.json').open('x') as file:
        json.dump(request, file, indent=2)
        file.write('\n')
print('Prepared coverage validated and exact approval requests written; no approval/submission performed.')

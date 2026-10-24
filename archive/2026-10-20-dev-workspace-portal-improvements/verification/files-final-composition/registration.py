import json
import re
import sys
from pathlib import Path

registration, package, state, workspace = map(Path, sys.argv[1:])
plan = json.loads(registration.read_text())
assert plan['schema'] == 1 and plan['policy'] == 1
assert plan['required_native_child_threads'] == 0
assert plan['states'] == []
assert re.fullmatch(r'[0-9a-f]{64}', plan['digest'])
# Direct threads require no native child/role launch settings. The workspace
# CLI adds only these required reporting MCP overrides to the empty base plan.
reporting = [
    ('command', str(package / 'bin/workspace-portal')),
    ('args', ['team-mcp', '--user-state-root', str(state), '--workspace',
              str(workspace), '--host-profile', str(state / 'profile')]),
    ('required', True),
    ('enabled_tools', ['report_to_lead']),
    ('tools.report_to_lead.approval_mode', 'approve'),
]
expected_argv = []
for key, value in reporting:
    expected_argv.extend([
        '-c', 'mcp_servers.team_reporting.' + key + '=' +
        json.dumps(value, separators=(',', ':'), ensure_ascii=False),
    ])
assert plan['argv'] == expected_argv, ('unexpected launch arguments', plan['argv'])
print('Registration schema1/policy1: native child capacity0; states[]; exact required reporting MCP overrides; no native child/role launch arguments')

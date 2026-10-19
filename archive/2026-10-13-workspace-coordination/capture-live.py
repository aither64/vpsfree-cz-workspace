#!/usr/bin/env python3
"""Read-only rollout observations; stdout contains no credential material."""
import json
import os
import subprocess
from pathlib import Path

paths = [
    '/run/current-system',
    '/nix/var/nix/profiles/system',
    '/home/aither/.local/state/dev-workspaces/profile',
]
observed = {
    path: {'link': os.readlink(path), 'resolved': os.path.realpath(path)}
    for path in paths
}
observed['bootId'] = Path('/proc/sys/kernel/random/boot_id').read_text().strip()
observed['runningKernel'] = os.uname().release
services = [
    'workspace-router.service',
    'workspace-portal@vpsfree-cz.service',
    'workspace-codex@vpsfree-cz.service',
    'workspace-codex-provider@vpsfree-cz.service',
    'workspace-coordinator.service',
]
observed['services'] = {
    service: subprocess.run(
        ['systemctl', '--user', 'show', service, '-p', 'ActiveState', '-p', 'MainPID'],
        check=True, capture_output=True, text=True,
    ).stdout.strip()
    for service in services
}
print(json.dumps(observed, indent=2))

#!/usr/bin/env python3
"""Observe one portal-owned naming child; never request a naming operation."""
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import time

ALLOWED = {'/nix/store/m8bqmkdzgk85vng42hcsavqmaz56rwgc-dev-workspace-0.2.0', '/nix/store/4cn1hh88xdpql5jp9pyrnf5fvnqsc829-dev-workspace-0.2.0'}
PACKAGE = Path(sys.argv[2]) if len(sys.argv) == 5 and sys.argv[1] == '--package' else Path('/invalid')
UNIT = 'workspace-portal@vpsfree-cz.service'
CATALOG_SHA256 = '049042aaadcf2f19722fa1e893f926d2bdbd4d0ff092d80704ff4256e2a45fb1'
PREFIX = b'model_catalog_json='


class NotReady(Exception):
    pass


def main_pid():
    result = subprocess.run(
        ['systemctl', '--user', 'show', UNIT, '--property=MainPID', '--value'],
        stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, timeout=5, check=False,
    )
    value = result.stdout.strip()
    if result.returncode or not value.isdigit() or int(value) <= 0:
        raise NotReady('portal_main_pid_unavailable')
    return int(value)


def direct_children(pid, deadline):
    # Go may fork from any OS thread, so inspect every bounded task children list.
    tasks = sorted(Path(f'/proc/{pid}/task').iterdir())
    if len(tasks) > 1024:
        raise NotReady('task_observation_bound')
    children = set()
    for task in tasks:
        if time.monotonic() > deadline:
            raise NotReady('process_observation_bound')
        try:
            with (task / 'children').open('rb') as source:
                data = source.read(16385)
        except FileNotFoundError:
            continue
        if len(data) > 16384:
            raise NotReady('children_observation_bound')
        if any(not value.isdigit() for value in data.split()):
            raise NotReady('process_relation_unavailable')
        children.update(int(value) for value in data.split())
        if len(children) > 64:
            raise NotReady('children_observation_bound')
    return children


def catalog_arguments(pid, deadline):
    # Stream bytes; retain only the fixed catalog setting. Unknown provider or
    # authentication arguments are neither buffered as arguments nor printed.
    values = []
    previous_config = False
    position = 0
    prefix_matches = True
    flag_matches = True
    value = bytearray()
    total = 0
    with open(f'/proc/{pid}/cmdline', 'rb', buffering=0) as source:
        while True:
            byte = source.read(1)
            if not byte:
                break
            total += 1
            if total > 131072 or time.monotonic() > deadline:
                raise NotReady('argument_observation_bound')
            if byte == b'\0':
                if prefix_matches and position >= len(PREFIX):
                    if not previous_config:
                        raise NotReady('catalog_argument_not_config')
                    values.append(json.loads(value.decode('utf-8')))
                previous_config = flag_matches and position == 2
                position, prefix_matches, flag_matches = 0, True, True
                value = bytearray()
                continue
            if position < len(PREFIX):
                prefix_matches = prefix_matches and byte[0] == PREFIX[position]
            elif prefix_matches:
                if len(value) >= 4096:
                    raise NotReady('catalog_argument_bound')
                value.extend(byte)
            flag_matches = flag_matches and position < 2 and byte[0] == b'-c'[position]
            position += 1
    return values


def observe():
    if str(PACKAGE) not in ALLOWED or sys.argv[1:] != ['--package', str(PACKAGE), '--unit', UNIT]:
        raise NotReady('expected_package_and_unit_required')
    expected_portal = (PACKAGE / 'bin/workspace-portal').resolve(strict=True)
    expected_native = (PACKAGE / 'libexec/codex/libexec/codex/bin/codex').resolve(strict=True)
    expected_catalog = (PACKAGE / 'share/workspace-portal/codex-models.json').resolve(strict=True)
    with expected_catalog.open('rb') as source:
        catalog = source.read(1024 * 1024 + 1)
    if len(catalog) > 1024 * 1024:
        raise NotReady('catalog_observation_bound')
    digest = hashlib.sha256(catalog).hexdigest()
    if digest != CATALOG_SHA256:
        raise NotReady('candidate_catalog_hash_mismatch')
    portal = main_pid()
    if Path(f'/proc/{portal}/exe').resolve(strict=True) != expected_portal:
        raise NotReady('portal_executable_mismatch')
    deadline = time.monotonic() + 10
    matches = []
    native_count = 0
    for child in sorted(direct_children(portal, deadline)):
        try:
            if Path(f'/proc/{child}/exe').resolve(strict=True) != expected_native:
                continue
            native_count += 1
            if native_count > 4:
                raise NotReady('native_candidate_observation_bound')
            values = catalog_arguments(child, deadline)
        except FileNotFoundError:
            continue
        if values == [str(expected_catalog)]:
            matches.append(child)
        elif values:
            raise NotReady('catalog_argument_mismatch')
    if len(matches) != 1:
        raise NotReady('unique_owned_naming_child_not_observed')
    child = matches[0]
    if main_pid() != portal or child not in direct_children(portal, deadline):
        raise NotReady('process_relation_changed')
    if Path(f'/proc/{child}/exe').resolve(strict=True) != expected_native:
        raise NotReady('naming_executable_changed')
    return {
        'ready': True, 'scope': 'process_and_catalog_readiness_only',
        'unit': UNIT, 'package': str(PACKAGE), 'owned_child_verified': True,
        'naming_executable': str(expected_native),
        'catalog': str(expected_catalog), 'catalog_sha256': digest,
        'naming_turn_verified': False,
    }


if __name__ == '__main__':
    try:
        print(json.dumps(observe(), sort_keys=True))
    except NotReady as error:
        print(json.dumps({'ready': False, 'reason': str(error),
                          'scope': 'process_and_catalog_readiness_only'}))
        sys.exit(1)
    except (OSError, ValueError, subprocess.TimeoutExpired):
        print(json.dumps({'ready': False, 'reason': 'observation_unavailable',
                          'scope': 'process_and_catalog_readiness_only'}))
        sys.exit(1)

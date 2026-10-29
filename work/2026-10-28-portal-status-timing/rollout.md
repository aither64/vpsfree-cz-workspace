# Portal home split: one-time rollout

Prepared, not executed. This installation is the only consumer of this data
conversion. The scripts below are operational source, retained here because raw
tracking artifacts are disposable on archive. They are not installed in the
runtime. Extract each named fenced block unchanged into the private operation
directory and verify its SHA-256 before execution.

## Prepared ordering and recovery

1. Complete independent review and the exact native/package checks. Build the
   final system and workspace outputs, retaining their Nix roots. Repeat disk
   admission: the copy needs source-home bytes plus 8 GiB SQLite scratch and
   a 20 GiB free reserve. No reflinks or filesystem snapshots are assumed.
2. Acquire `vpsfree:aitherdev` for this initiative through normal coordination.
   Deploy the committed configuration through confctl; verify both live system
   identities and the stock executable. Keep the machine claim through deployed
   lineage integration; deployment does not grant master merge permission.
3. Export these exact files to a mode-0700 directory under
   `~/.local/state/dev-workspaces/maintenance/2026-10-28-portal-status-timing`.
   Keep `config.json` there with the held claim UUID, previous/candidate package,
   exact committed workspace source and revision, tested native SHA-256, and
   websocket-client Python library path. Retain the interpreter/library roots.
4. Launch `migration-cutover.py --root OPERATION_DIRECTORY` in a detached systemd
   user service, with an unlimited start/stop timeout and no forced signal.
   `journal.json`, `switch.log` and `acceptance.json` are durable status. The job
   waits for both native backends' loaded threads to become idle. It then holds
   stock daemon/startup locks and sends each managed stock process one SIGTERM.
   This chat may finish while the detached job waits; it is not the job's parent.
5. The ordinary claimed workspace switch owns transition/lifecycle admission,
   portal drain, terminal quiescence, selection and forward recovery. A temporary
   per-instance ExecStartPre hook runs the partition after old native shutdown.
   It refuses remaining source native processes or open DB/history descriptors.
   Root descriptor inspection is read-only via existing host SSH access.
   Recursive inotify observation rejects source writes during copying, including
   an embedded CLI process that starts and exits between descriptor scans. Queue
   overflow also refuses publication. A durable metadata fingerprint detects
   changes across a lost observer when the job resumes after publication intent.
6. The partition builds private SQLite files with the exact source schemas,
   checks every retained value, copies and checksums rollout bytes, preserves
   unknown stock records and independently provisioned portal settings/login.
   Source stays intact while copying. Durable inode identities precede Linux
   atomic directory exchanges, stock first and portal second. Original `.codex`
   remains at `partition/stock`; the original prepared private home remains at
   `partition/portal`. Do not delete either backup.
7. Acceptance checks selected native bytes/storage, all inventoried portal
   thread reads, both partition inventories and affected activity endpoints.
   The stock daemon starts through stock CLI. The original confctl message is
   reconciled and retried through the portal with the same browser attempt ID;
   acceptance requires its durable accepted receipt. Then the temporary drop-in
   is removed. Additional manual browser/tmux/provider/naming checks remain in
   the release acceptance brief, before calling the deployment usable.

Before profile selection, a refusal leaves original data authoritative and the
ordinary switch restores portal/terminal availability. The outer job restarts
stock after its locks unwind. Fix the reported refusal and resume the same job.
After profile selection, recover forward with the same source, claim and journal.
If the publication hook failed, the runner first verifies the selected pending
native target and starts its stopped service, re-entering the hook. This restores
the backend that ordinary switch admission needs; it never stops a running service.
Once publication intent exists, use its inode identities: do not start a new copy
or restore the old home over newer writes. A lost post-exchange journal update is
reconciled without another swap. An interrupted partial copy without publication
intent is disposable and rebuilt from the original source under renewed exclusion.
If the original source changes after publication intent, automatic recovery refuses.
Retain both homes and reconcile the extra writes before resuming; do not clear the
refusal marker or discard either copy to force progress.

A recorded signal intent prevents issuing a second potentially forced signal.
If interruption lands between recording intent and delivering SIGTERM, inspect
that exact process before resolving the pending drain; do not send a blind second
signal. No automatic rollback, archive, deletion, reboot or backup cleanup occurs.

## Source identities

## migration-inventory.py

SHA-256: `fe6b811a220dffd4629e49e0420ae3f0c339493255e3046d25bbe4959d0c32d8`

```python
#!/usr/bin/env python3
"""Read-only inventory for this installation's one-time Codex home split."""

import hashlib
import json
import sqlite3
import subprocess
from collections import defaultdict
from pathlib import Path

WORKSPACE = Path('/home/aither/workspace/ai/vpsfree.cz')
STATE = Path('/home/aither/.local/state/dev-workspaces')
SOURCE = Path('/home/aither/.codex')
OUTPUT = WORKSPACE / 'work/2026-10-28-portal-status-timing/migration-inventory.json'


def inventory():
    seeds = defaultdict(list)
    manifests = json.loads(subprocess.check_output([
        'ruby', '-rjson', '-ryaml', '-rdate', '-e',
        '''result = []
        %w[work archive].each do |area|
          Dir[File.join(ARGV[0], area, '*', 'portal.yml')].sort.each do |path|
            value = YAML.safe_load(File.read(path), permitted_classes: [Date, Time], aliases: true)
            next unless value.is_a?(Hash)
            result << {path: path, slug: value['slug'], codex: value['codex']}
          end
        end
        puts JSON.generate(result)''', str(WORKSPACE)]))
    for manifest in manifests:
        codex = manifest.get('codex') or {}
        if codex.get('thread_id'):
            seeds[codex['thread_id']].append(manifest['path'])
    team_root = STATE / 'codex-teams/vpsfree.cz-8a2a555cb2f65b33'
    for path in sorted(team_root.glob('*.json')):
        team = json.loads(path.read_text())
        if team.get('workspace') != str(WORKSPACE):
            raise ValueError(f'foreign team state: {path}')
        if team.get('rootThreadId'):
            seeds[team['rootThreadId']].append(str(path) + ':root')
        for member in (team.get('members') or []):
            if member.get('threadId') and member.get('state') != 'removed':
                seeds[member['threadId']].append(str(path) + ':' + member['address'])

    legacy_root = STATE / 'agent-teams/vpsfree.cz-8a2a555cb2f65b33'
    for path in sorted(legacy_root.glob('*.json')):
        team = json.loads(path.read_text())
        if team.get('workspace') != str(WORKSPACE) or team.get('pending_transition'):
            raise ValueError(f'foreign or transitioning legacy team: {path}')
        if team.get('root_thread_id'):
            seeds[team['root_thread_id']].append(str(path) + ':root')
        for member in team.get('members') or []:
            if member.get('thread_id') and member.get('state') != 'removed':
                seeds[member['thread_id']].append(str(path) + ':member')

    # Recovery and retained queues are workspace-owned even when their root is
    # absent from a currently displayed conversation list.
    digest = hashlib.sha256(str(WORKSPACE).encode()).hexdigest()
    for area in ('session-recovery', 'archived-prompts'):
        for path in sorted((STATE / area / digest).rglob('*.json')):
            value = json.loads(path.read_text())
            if value.get('workspace', str(WORKSPACE)) != str(WORKSPACE):
                raise ValueError(f'foreign recovery record: {path}')
            if value.get('thread_id'):
                seeds[value['thread_id']].append(str(path))
            for thread in value.get('active_threads') or []:
                if isinstance(thread, str):
                    seeds[thread].append(str(path) + ':active')
                elif isinstance(thread, dict) and thread.get('thread_id'):
                    seeds[thread['thread_id']].append(str(path) + ':active')

    connection = sqlite3.connect(f'file:{SOURCE}/state_5.sqlite?mode=ro', uri=True)
    connection.row_factory = sqlite3.Row
    threads = {row['id']: dict(row) for row in connection.execute(
        'select id, rollout_path, source, attached_thread_parent_id, project_id, archived from threads')}
    children = defaultdict(set)
    parents = defaultdict(set)
    for parent, child in connection.execute('select parent_thread_id, child_thread_id from thread_spawn_edges'):
        children[parent].add(child)
        parents[child].add(parent)
    missing_rollouts = []
    external_rollouts = []
    for thread_id, thread in threads.items():
        path = Path(thread['rollout_path'])
        if not path.is_relative_to(SOURCE):
            external_rollouts.append(thread_id)
            thread['bytes'] = path.stat().st_size if path.exists() else 0
            if not path.exists():
                missing_rollouts.append(thread_id)
            continue
        try:
            with path.open() as stream:
                line = stream.readline(4 * 1024 * 1024)
            metadata = json.loads(line)
            if metadata.get('type') != 'session_meta' or metadata['payload'].get('id') != thread_id:
                raise ValueError(f'rollout identity mismatch: {thread_id}')
            metadata = metadata['payload']
            for key in ('forked_from_id', 'parent_thread_id'):
                if metadata.get(key):
                    parents[thread_id].add(metadata[key])
            if metadata.get('parent_thread_id'):
                children[metadata['parent_thread_id']].add(thread_id)
            thread['bytes'] = path.stat().st_size
        except FileNotFoundError:
            missing_rollouts.append(thread_id)
            thread['bytes'] = 0
        if thread['attached_thread_parent_id']:
            parents[thread_id].add(thread['attached_thread_parent_id'])
            children[thread['attached_thread_parent_id']].add(thread_id)

    owned = set(seeds)
    todo = list(owned)
    while todo:
        for child in children[todo.pop()] - owned:
            owned.add(child)
            todo.append(child)
    # Fork/attached ancestors are dependencies, not evidence that their other
    # descendants belong to the portal. Preserve foreign ancestors in stock too.
    portal = set(owned)
    todo = list(portal)
    while todo:
        for parent in parents[todo.pop()] - portal:
            portal.add(parent)
            todo.append(parent)
    stock = set(threads) - owned
    todo = list(stock)
    while todo:
        for parent in parents[todo.pop()] - stock:
            stock.add(parent)
            todo.append(parent)
    result = {
        'schema': 1, 'source': str(SOURCE), 'workspace': str(WORKSPACE),
        'seeds': dict(seeds), 'owned': sorted(owned), 'portal': sorted(portal),
        'stock': sorted(stock), 'sharedDependencies': sorted(portal & stock),
        'missingRows': sorted(portal - set(threads)),
        'externalPortalRollouts': sorted(portal & set(external_rollouts)),
        'externalStockRollouts': sorted(set(external_rollouts) - portal),
        'missingPortalRollouts': sorted(portal & set(missing_rollouts)),
        'missingStockRollouts': sorted(set(missing_rollouts) - portal),
        'threads': threads,
    }
    connection.close()
    return result


if __name__ == '__main__':
    result = inventory()
    OUTPUT.write_text(json.dumps(result, indent=2) + '\n')
    OUTPUT.chmod(0o600)
    print(json.dumps({
        'indexedThreads': len(result['threads']),
        **{key: len(result[key]) for key in ('seeds', 'owned', 'portal', 'stock', 'sharedDependencies')},
        **{key: result[key] for key in ('missingRows', 'missingPortalRollouts', 'missingStockRollouts')},
        'portalRolloutBytes': sum(result['threads'][key]['bytes'] for key in result['portal'] if key in result['threads']),
        'inventorySHA256': hashlib.sha256(OUTPUT.read_bytes()).hexdigest(),
    }, indent=2))
```

## migration-partition.py

SHA-256: `32ee9e0610801d80916f8ff327d3e627d3ca12d106df6f90f9ec23ed66504273`

```python
#!/usr/bin/env python3
"""Offline data phase for the October 2026 one-instance Codex migration.

This is not installed by dev-workspace. The cutover runner owns writer exclusion,
publication and recovery. This module writes only new staging directories.
"""

import contextlib
import hashlib
import json
import os
import shutil
import sqlite3
from pathlib import Path

SCHEMAS = {
    'state_5.sqlite': '28746565d22f77f234482194675a9634653d59624f8fe700d1f11896a1226b77',
    'thread_history_1.sqlite': 'aa7bc79f517e9372ac6598b854663a9ea6ff2a77cb60ddae9822edd2836a957d',
    'queue_1.sqlite': '102a82c0ebbc433e187ff17854864d9fa963b73ff830ea9929c1e9d6c53044df',
    'goals_1.sqlite': '47b2811083cce8022181dcc319aaf937560cb7df5d936f1aa5f897e35b5c6d3d',
    'memories_1.sqlite': 'cf78c83293ee523b93ebcb76cc53a12a7d2c13dd4d33f05da17337b2acc6d9f8',
}
RUNTIME = {'app-server-daemon', 'app-server-control', 'thread-writer-locks',
           'tmp', '.tmp', '.sqlite-maintenance.lock'}


def quoted(value):
    return '"' + value.replace('"', '""') + '"'


def schema(connection):
    return list(connection.execute(
        'select type,name,tbl_name,sql from sqlite_master order by type,name'))


def schema_hash(rows):
    return hashlib.sha256(json.dumps(rows, separators=(',', ':')).encode()).hexdigest()


def partition_database(source, destination, ids, excluded_ids, portal, old_home, new_home):
    reader = sqlite3.connect(f'file:{source}?mode=ro', uri=True)
    definition = schema(reader)
    if schema_hash(definition) != SCHEMAS[source.name]:
        reader.close()
        raise ValueError(f'unsupported native schema: {source.name}')
    if reader.execute('pragma quick_check').fetchall() != [('ok',)]:
        reader.close()
        raise ValueError(f'source database is damaged: {source.name}')
    if source.name == 'memories_1.sqlite' and reader.execute('select count(*) from jobs').fetchone()[0]:
        reader.close()
        raise ValueError('memory jobs need explicit migration ownership')
    reader.close()
    writer = sqlite3.connect(str(destination), uri=True)
    os.chmod(destination, 0o600)
    writer.execute('pragma journal_mode=DELETE')
    writer.execute('pragma synchronous=FULL')
    writer.execute('attach database ? as original', (f'file:{source}?mode=ro',))
    writer.execute('create temp table selected(id text primary key)')
    writer.executemany('insert into selected values (?)', ((x,) for x in sorted(ids)))
    writer.execute('create temp table excluded(id text primary key)')
    writer.executemany('insert into excluded values (?)', ((x,) for x in sorted(excluded_ids)))
    rows = {}
    for kind, table, _, ddl in definition:
        if kind != 'table' or table.startswith('sqlite_'):
            continue
        writer.execute(ddl)
        columns = [row[1] for row in writer.execute(f'pragma original.table_info({quoted(table)})')]
        condition = '1'
        if table == 'threads':
            condition = 'id in selected'
        elif 'thread_id' in columns:
            condition = 'thread_id in selected' if portal else 'thread_id not in excluded'
        elif table == 'thread_spawn_edges':
            condition = ('parent_thread_id in selected and child_thread_id in selected' if portal else
                         'parent_thread_id not in excluded and child_thread_id not in excluded')
        elif table in ('projects', 'project_roots', 'project_idempotency_keys'):
            column = 'id' if table == 'projects' else 'project_id'
            # Unreferenced stock projects remain visible to stock CLI.
            if portal:
                condition = f'{column} in (select project_id from original.threads where id in selected)'
        elif table == 'remote_control_enrollments' and portal:
            condition = '0'
        elif table == 'rollout_migration_skipped_rollouts':
            condition = 'rollout_path in (select rollout_path from original.threads where id in selected)'
            if not portal:
                condition += ' or rollout_path not in (select rollout_path from original.threads)'
        elif table not in ('_sqlx_migrations', 'backfill_state', 'external_agent_config_imports',
                           'thread_sections', 'rollout_migration_state', 'remote_control_enrollments',
                           'jobs', 'consolidation_progress'):
            raise ValueError(f'unclassified native table: {source.name}/{table}')
        projection = []
        for column in columns:
            expression = quoted(column)
            if portal and column == 'rollout_path':
                expression = '? || substr(' + expression + ', ?)'
            projection.append(expression)
        args = (str(new_home), len(str(old_home)) + 1) if portal and 'rollout_path' in columns else ()
        writer.execute(f'insert into {quoted(table)} select {", ".join(projection)} '
                       f'from original.{quoted(table)} where {condition}', args)
        rows[table] = writer.execute(f'select count(*) from {quoted(table)}').fetchone()[0]
        expected = writer.execute(f'select count(*) from original.{quoted(table)} where {condition}').fetchone()[0]
        if rows[table] != expected:
            raise ValueError(f'row count mismatch: {table}')
        # Compare every retained value, including opaque native payloads. Install
        # triggers only after copying so timestamp triggers cannot alter history.
        mismatch = writer.execute(
            f'select {", ".join(projection)} from original.{quoted(table)} where {condition} '
            f'except select * from {quoted(table)} limit 1', args).fetchone()
        if mismatch is not None:
            raise ValueError(f'row content mismatch: {table}')
    for kind, name, _, ddl in definition:
        if ddl and kind in ('index', 'trigger', 'view'):
            writer.execute(ddl)
    if any(row[1] == 'sqlite_sequence' for row in definition):
        writer.execute('delete from sqlite_sequence')
        writer.execute('insert into sqlite_sequence select * from original.sqlite_sequence')
    writer.commit()
    if schema_hash(schema(writer)) != SCHEMAS[source.name]:
        raise ValueError(f'partition changed native schema: {source.name}')
    if writer.execute('pragma integrity_check').fetchall() != [('ok',)]:
        raise ValueError(f'partition database is damaged: {destination.name}')
    if writer.execute('pragma foreign_key_check').fetchall():
        raise ValueError(f'partition has broken native relations: {destination.name}')
    writer.close()
    return rows


def copy_file(source, destination):
    destination.parent.mkdir(mode=0o700, parents=True, exist_ok=True)
    if source.is_symlink():
        destination.symlink_to(os.readlink(source))
    elif source.is_dir():
        shutil.copytree(source, destination, symlinks=True)
    elif source.is_file():
        shutil.copy2(source, destination)
        with source.open('rb') as original, destination.open('rb') as copied:
            if hashlib.file_digest(original, 'sha256').digest() != hashlib.file_digest(copied, 'sha256').digest():
                raise ValueError(f'file copy mismatch: {source}')
            os.fsync(copied.fileno())
    else:
        raise ValueError(f'unexpected non-file in native state: {source}')


def filter_lines(source, destination, key, ids, include_unknown=False):
    with source.open('rb') as stream, destination.open('xb') as out:
        for line in stream:
            value = json.loads(line)
            if value.get(key) in ids or include_unknown and not value.get(key):
                out.write(line)
        out.flush()
        os.fsync(out.fileno())
    destination.chmod(0o600)


def partition(inventory, staging, final_portal, prepared_portal):
    source = Path(inventory['source'])
    if any(inventory[key] for key in ('missingRows', 'missingPortalRollouts', 'externalPortalRollouts')):
        raise ValueError('portal inventory contains missing or external history')
    if staging.exists():
        raise ValueError('staging already exists; inspect the journal before restarting data copy')
    needed = sum(path.stat().st_size for path in source.rglob('*') if path.is_file() and not path.is_symlink())
    reserve = 20 * 1024**3
    if shutil.disk_usage(staging.parent).free < needed + 8 * 1024**3 + reserve:
        raise ValueError('insufficient space for partition, database scratch and 20 GiB reserve')
    staging.mkdir(mode=0o700)
    stock = staging / 'stock'
    portal = staging / 'portal'
    stock.mkdir(mode=0o700)
    portal.mkdir(mode=0o700)
    portal_ids, stock_ids = set(inventory['portal']), set(inventory['stock'])
    indexed = {Path(value['rollout_path']): key for key, value in inventory['threads'].items()}
    if len(indexed) != len(inventory['threads']):
        raise ValueError('multiple threads point to the same rollout')
    hashes = {}
    for area in ('sessions', 'archived_sessions'):
        for path in (source / area).rglob('*'):
            if path.is_dir():
                continue
            relative = path.relative_to(source)
            thread_id = indexed.get(path)
            if path.is_symlink():
                raise ValueError(f'symlinked rollout: {relative}')
            # Retain old/duplicate rollouts with their owner, so native backfill
            # cannot rediscover a portal conversation in the stock home.
            with path.open('rb') as stream:
                first = json.loads(stream.readline(4 * 1024 * 1024))
            if first.get('type') != 'session_meta':
                raise ValueError(f'unknown rollout metadata: {relative}')
            metadata_id = first['payload']['id']
            if thread_id is not None and thread_id != metadata_id:
                raise ValueError(f'rollout ID mismatch: {relative}')
            thread_id = metadata_id
            if thread_id in portal_ids:
                copy_file(path, portal / relative)
                with path.open('rb') as original, (portal / relative).open('rb') as copied:
                    digest = hashlib.file_digest(original, 'sha256').hexdigest()
                    actual = hashlib.file_digest(copied, 'sha256').hexdigest()
                if actual != digest:
                    raise ValueError(f'rollout copy mismatch: {thread_id}')
                hashes[str(relative)] = digest
            if thread_id not in portal_ids or thread_id in stock_ids:
                copy_file(path, stock / relative)
    for path in source.iterdir():
        name = path.name
        if name in RUNTIME or name in ('sessions', 'archived_sessions') or '.sqlite' in name:
            continue
        if name in ('history.jsonl', 'session_index.jsonl'):
            key = 'session_id' if name == 'history.jsonl' else 'id'
            filter_lines(path, portal / name, key, portal_ids)
            # Preserve records unknown to the index in stock.
            with path.open('rb') as stream, (stock / name).open('xb') as out:
                for line in stream:
                    thread = json.loads(line).get(key)
                    if thread not in portal_ids or thread in stock_ids:
                        out.write(line)
                out.flush()
                os.fsync(out.fileno())
            (stock / name).chmod(0o600)
            continue
        if name in ('shell_snapshots', 'tui-thread-reference-capabilities'):
            (stock / name).mkdir(mode=0o700)
            (portal / name).mkdir(mode=0o700)
            for item in path.iterdir():
                thread_id = item.name[:36]
                if thread_id in portal_ids:
                    copy_file(item, portal / name / item.name)
                if thread_id not in portal_ids or thread_id in stock_ids:
                    copy_file(item, stock / name / item.name)
            continue
        copy_file(path, stock / name)
    # The independently authenticated home supplies portal settings and secrets.
    # It contains no copied native database, daemon package or writer ownership.
    for path in prepared_portal.iterdir():
        if path.name not in ('auth.json', 'config.toml', 'skills', 'plugins', 'rules',
                             'aither-on-snajpa-codex-lb.token'):
            continue
        copy_file(path, portal / path.name)
    if not (portal / 'auth.json').is_file() or not (portal / 'config.toml').is_file():
        raise ValueError('independent portal login/configuration is not prepared')
    report = {'databases': {}, 'rollouts': hashes}
    for name in SCHEMAS:
        report['databases'][name] = {}
        for label, destination, ids in [('stock', stock, stock_ids), ('portal', portal, portal_ids)]:
            report['databases'][name][label] = partition_database(
                source / name, destination / name, ids, portal_ids - stock_ids,
                label == 'portal', source, final_portal)
    for source_db in source.glob('*.sqlite'):
        if source_db.name in SCHEMAS:
            continue
        if source_db.name not in ('logs_1.sqlite', 'logs_2.sqlite'):
            raise ValueError(f'unclassified database: {source_db.name}')
        with contextlib.closing(sqlite3.connect(f'file:{source_db}?mode=ro', uri=True)) as reader:
            with contextlib.closing(sqlite3.connect(stock / source_db.name)) as writer:
                reader.backup(writer)
        os.chmod(stock / source_db.name, 0o600)
    for destination in (stock, portal):
        connection = sqlite3.connect(destination / 'state_5.sqlite')
        expected = stock_ids if destination == stock else portal_ids
        if set(row[0] for row in connection.execute('select id from threads')) != expected:
            raise ValueError('thread partition does not conserve inventory')
        connection.close()
    (staging / 'verification.json').write_text(json.dumps(report, indent=2) + '\n')
    # Flush nested copied trees and SQLite files before a later atomic exchange.
    for path in staging.rglob('*'):
        if path.is_symlink():
            continue
        descriptor = os.open(path, os.O_RDONLY)
        try:
            os.fsync(descriptor)
        finally:
            os.close(descriptor)
    descriptor = os.open(staging, os.O_RDONLY)
    try:
        os.fsync(descriptor)
    finally:
        os.close(descriptor)
    return report
```

## migration-cutover.py

SHA-256: `d7b69f8b57945974e659b9ec9391c217a6ae0864786c6dec1e16c3ff8f62a00b`

```python
#!/usr/bin/env python3
"""One-installation cutover. Run from a detached systemd user unit.

The ordinary workspace switch owns lifecycle admission and the transition lock.
Its temporary ExecStartPre hook invokes --publish after the old native stopped.
No installed project command or persistent native schema is added.
"""
import argparse
import contextlib
import ctypes
import fcntl
import hashlib
import importlib.util
import json
import os
import shutil
import shlex
import signal
import sqlite3
import struct
import subprocess
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = Path('/home/aither/.codex')
PORTAL = Path('/home/aither/.local/state/dev-workspaces/codex-homes/vpsfree-cz')
PROFILE = Path('/home/aither/.local/state/dev-workspaces/profile')
CODEX_CURRENT = PROFILE.parent / 'codex/current/bin/codex'
PENDING = PROFILE.parent / 'codex/pending'
UNIT = 'workspace-codex@vpsfree-cz.service'
DROPIN = Path('/home/aither/.config/systemd/user') / (UNIT + '.d') / '90-home-migration.conf'
SLUG = '2026-10-28-portal-status-timing'
WORKSPACE = '/home/aither/workspace/ai/vpsfree.cz'


def module(name):
    spec = importlib.util.spec_from_file_location(name, HERE / (name + '.py'))
    result = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result


def fsync_directory(path):
    descriptor = os.open(path, os.O_RDONLY)
    try:
        os.fsync(descriptor)
    finally:
        os.close(descriptor)


def save(path, value):
    temporary = path.with_suffix('.new')
    with temporary.open('w', encoding='utf-8') as stream:
        os.chmod(temporary, 0o600)
        json.dump(value, stream, indent=2)
        stream.write('\n')
        stream.flush()
        os.fsync(stream.fileno())
    os.replace(temporary, path)
    fsync_directory(path.parent)


def identity(path):
    stat = path.stat()
    return [stat.st_dev, stat.st_ino]


def exchange(left, right, before_left, before_right):
    """Reconcile either side of a lost journal write without repeating the swap."""
    actual = [identity(left), identity(right)]
    if actual == [before_right, before_left]:
        return
    if actual != [before_left, before_right]:
        raise RuntimeError('publication directory identity changed')
    libc = ctypes.CDLL(None, use_errno=True)
    rename = libc.renameat2
    rename.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.c_int, ctypes.c_char_p, ctypes.c_uint]
    rename.restype = ctypes.c_int
    if rename(-100, os.fsencode(left), -100, os.fsencode(right), 2):
        raise OSError(ctypes.get_errno(), 'atomic home exchange failed')
    fsync_directory(left.parent)
    fsync_directory(right.parent)


@contextlib.contextmanager
def lock(path):
    path.parent.mkdir(mode=0o700, parents=True, exist_ok=True)
    with path.open('a') as stream:
        if os.fstat(stream.fileno()).st_mode & 0o777 != 0o600:
            os.fchmod(stream.fileno(), 0o600)
        fcntl.flock(stream, fcntl.LOCK_EX | fcntl.LOCK_NB)
        yield stream


def native_processes(home):
    found = []
    for proc in Path('/proc').iterdir():
        if not proc.name.isdigit():
            continue
        try:
            if proc.stat().st_uid != os.getuid():
                continue
            args = (proc / 'cmdline').read_bytes().split(b'\0')
            if Path(os.readlink(proc / 'exe')).name != 'codex':
                continue
            env = dict(item.split(b'=', 1) for item in (proc / 'environ').read_bytes().split(b'\0') if b'=' in item)
            selected = env.get(b'CODEX_HOME', b'/home/aither/.codex').decode()
            if Path(selected) != home:
                continue
            # stat's comm may contain spaces; fields after the final ')' start at 3.
            start = (proc / 'stat').read_text().rsplit(')', 1)[1].split()[19]
            found.append({'pid': int(proc.name), 'start': start,
                          'managed': b'--managed-daemon' in args,
                          'updater': b'pid-update-loop' in args})
        except (FileNotFoundError, ProcessLookupError):
            continue
    return found


class SourceChanged(RuntimeError):
    pass


def source_fingerprint(home):
    """Durable change evidence across a lost inotify observer.

    Include inode, ctime and mtime so a write followed by content restoration
    still invalidates the copy. Root timestamps alone change on our exchange.
    Reads may update atime, so it is deliberately absent. This detects ordinary
    concurrent writes, not manipulation by the trusted machine administrator.
    """
    digest = hashlib.sha256()
    for directory, directories, files in os.walk(home):
        directories.sort()
        for name in sorted(directories + files):
            path = Path(directory) / name
            if path.parent == home and name.endswith('.sqlite-shm'):
                continue  # SQLite's derived WAL index/reader locks, not data.
            info = path.lstat()
            entry = [str(path.relative_to(home)), info.st_dev, info.st_ino,
                     info.st_mode, info.st_uid, info.st_gid, info.st_size,
                     info.st_mtime_ns, info.st_ctime_ns]
            digest.update(json.dumps(entry).encode() + b'\n')
    return digest.hexdigest()


def prepare_source_readers(home):
    # SQLite's read-only WAL reader can create empty -wal/-shm sidecars.
    # Materialize those before observing the copy; never checkpoint or alter
    # database content. Later reads must leave the observed source stable.
    for database in home.glob('*.sqlite'):
        with contextlib.closing(sqlite3.connect(f'file:{database}?mode=ro', uri=True)) as reader:
            reader.execute('pragma schema_version').fetchone()


def original_source(staging, publication):
    for path in (SOURCE, staging / 'stock'):
        if identity(path) == publication['stock'][0]:
            return path
    raise RuntimeError('original source identity changed')


class SourceWatch:
    """Detect even short-lived embedded/CLI writers throughout the data copy.

    Native lifecycle locks do not cover codex exec's in-process App Server.
    inotify watches the existing source tree; creation, removal or modification
    invalidates this attempt. Overflow also refuses, never weakens the proof.
    """
    def __init__(self, home):
        self.libc = ctypes.CDLL(None, use_errno=True)
        self.fd = self.libc.inotify_init1(os.O_NONBLOCK | os.O_CLOEXEC)
        if self.fd < 0:
            raise OSError(ctypes.get_errno(), 'cannot observe source stability')
        self.directories = {}
        try:
            for directory, _, _ in os.walk(home):
                # CLOSE_WRITE only means an O_RDWR descriptor closed; SQLite
                # readers use those for WAL coordination without writing data.
                mask = 0x2 | 0x4 | 0x40 | 0x80 | 0x100 | 0x200 | 0x400 | 0x800
                watch = self.libc.inotify_add_watch(self.fd, os.fsencode(directory), mask)
                if watch < 0:
                    raise OSError(ctypes.get_errno(), 'cannot watch source directory')
                self.directories[watch] = Path(directory).relative_to(home)
        except BaseException:
            self.close()
            raise

    def assert_stable(self, allow_exchange=False):
        while True:
            try:
                events = os.read(self.fd, 1024 * 1024)
            except BlockingIOError:
                return
            offset = 0
            while offset < len(events):
                watch, mask, _, size = struct.unpack_from('iIII', events, offset)
                name = os.fsdecode(events[offset + 16:offset + 16 + size].split(b'\0', 1)[0])
                offset += 16 + size
                if self.directories.get(watch) == Path('.') and name.endswith('.sqlite-shm'):
                    continue  # Read-only SQLite access updates its shared index.
                if allow_exchange and mask == 0x800 and self.directories.get(watch) == Path('.'):
                    continue  # Our atomic exchange moves the watched root inode.
                raise SourceChanged(f'source changed during migration (inotify mask {mask:#x})')

    def close(self):
        os.close(self.fd)


def assert_no_open_source_files(home):
    # Exclusion is operational, not protection against a hostile local operator.
    # Catch forgotten clients and tools holding source DBs or rollouts open.
    if os.geteuid() != 0:
        remote = shlex.join([sys.executable, str(HERE / 'migration-cutover.py'), '--scan-source', str(home)])
        subprocess.run(['ssh', '-o', 'BatchMode=yes', 'root@172.16.106.40', remote],
                       check=True, capture_output=True, text=True)
        return
    prefixes = tuple(str(home / name) for name in ('sessions/', 'archived_sessions/',
                                                 'thread-writer-locks/', 'log/'))
    for proc in Path('/proc').iterdir():
        if not proc.name.isdigit() or int(proc.name) == os.getpid():
            continue
        try:
            for fd in (proc / 'fd').iterdir():
                try:
                    target = os.readlink(fd)
                except FileNotFoundError:
                    continue
                if target.startswith(prefixes) or (target.startswith(str(home) + '/') and '.sqlite' in target
                                                   and not target.endswith('.sqlite-maintenance.lock')):
                    raise RuntimeError(f'source data still open in process {proc.name}')
        except (FileNotFoundError, ProcessLookupError):
            continue


def update(root, **fields):
    path = root / 'journal.json'
    journal = json.loads(path.read_text()) if path.exists() else {'schema': 1}
    journal.update(fields, updatedAt=time.time())
    save(path, journal)
    return journal


def publish(root, config):
    selected = str(PROFILE.resolve())
    if selected == config['previousPackage']:
        return  # An ordinary old-service restart before profile selection.
    if selected != config['candidatePackage']:
        raise RuntimeError('unexpected selected package at publication')
    with lock(root / 'publication.lock'):
        update(root, hookEntered=True)
        journal = json.loads((root / 'journal.json').read_text())
        if journal.get('sourceChangedAfterIntent'):
            raise RuntimeError('source changed during publication; retain both homes and reconcile before resuming')
        if journal.get('published'):
            return
        outer = journal.get('outer')
        if not outer or not Path(f"/proc/{outer['pid']}").exists():
            raise RuntimeError('resume the detached migration runner before starting native')
        start = Path(f"/proc/{outer['pid']}/stat").read_text().rsplit(')', 1)[1].split()[19]
        if start != outer['start']:
            raise RuntimeError('detached migration runner identity changed')
        staging = root / 'partition'
        observer = None
        if not journal.get('publication'):
            if native_processes(SOURCE):
                raise RuntimeError('source native writers are still running')
            assert_no_open_source_files(SOURCE)
            # No exchange can precede the durable publication intent. An older
            # partial copy is disposable; the untouched source is authoritative.
            if staging.exists():
                shutil.rmtree(staging)
            prepare_source_readers(SOURCE)
            observer = SourceWatch(SOURCE)
        try:
            if not journal.get('publication'):
                fingerprint = source_fingerprint(SOURCE)
                inventory = module('migration-inventory').inventory()
                save(root / 'inventory.json', inventory)
                update(root, phase='copying')
                module('migration-partition').partition(inventory, staging, PORTAL, PORTAL)
                assert_no_open_source_files(SOURCE)
                if native_processes(SOURCE):
                    raise RuntimeError('source native appeared during the copy')
                if source_fingerprint(SOURCE) != fingerprint:
                    raise SourceChanged('source changed during the copy')
                observer.assert_stable()
                publication = {
                    'stock': [identity(SOURCE), identity(staging / 'stock')],
                    'portal': [identity(PORTAL), identity(staging / 'portal')],
                    'sourceFingerprint': fingerprint,
                }
                journal = update(root, phase='publishing', publication=publication)
            else:
                # Re-establish observation before comparing durable evidence.
                # Never trust a pre-crash observer or recopy after intent.
                original = original_source(staging, journal['publication'])
                observer = SourceWatch(original)
                if source_fingerprint(original) != journal['publication'].get('sourceFingerprint'):
                    raise SourceChanged('original source changed after publication intent')
                assert_no_open_source_files(original)
                observer.assert_stable()
            # Stock first: if interrupted here, stock is already independent and
            # may accept writes. Recovery must never recopy or replace it.
            publication = journal['publication']
            exchange(SOURCE, staging / 'stock', *publication['stock'])
            if observer:
                observer.assert_stable(allow_exchange=True)
            update(root, phase='stock-published')
            exchange(PORTAL, staging / 'portal', *publication['portal'])
            assert_no_open_source_files(staging / 'stock')
            if observer:
                observer.assert_stable(allow_exchange=True)
            update(root, phase='homes-published', published=True)
        except SourceChanged:
            if journal.get('publication'):
                update(root, sourceChangedAfterIntent=True)
            raise
        finally:
            if observer:
                observer.close()


def command(args, **kwargs):
    return subprocess.run(args, check=True, **kwargs)


def require_claim(config):
    value = json.loads(subprocess.check_output([
        str(PROFILE / 'bin/dev-session'), 'coordination', 'claim-status', SLUG,
        '--as-is', '--id', config['claimId'], '--json'], cwd=WORKSPACE, text=True))
    if value['state'] != 'held' or 'machine:vpsfree:aitherdev' not in value['resources']:
        raise RuntimeError('this session no longer holds aitherdev')


def recover_selected_native(root, config):
    journal = json.loads((root / 'journal.json').read_text())
    if str(PROFILE.resolve()) != config['candidatePackage'] or not journal.get('hookEntered'):
        return
    # The ordinary reconciliation selected its native target before requesting
    # restart. The failed hook is durable evidence of reaching that boundary.
    # Restarting only a stopped service lets the next ordinary switch query it;
    # systemctl start never interrupts a running service.
    if not journal.get('published'):
        pending = json.loads(PENDING.read_text())
        if pending.get('package_root') != config['candidatePackage'] or \
                Path(pending['codex_path']).resolve() != CODEX_CURRENT.resolve():
            raise RuntimeError('selected native recovery no longer matches its pending target')
    command(['systemctl', '--user', 'start', UNIT])


def wait_for_idle(root, config):
    native_type = module('migration-acceptance').Native
    paths = [SOURCE / 'app-server-control/app-server-control.sock',
             Path('/run/user/1000/dev-workspaces/vpsfree-cz/app-server.sock')]
    while True:
        busy = []
        for path in paths:
            if not path.exists():
                continue  # Ordinary switch still requires its old backend.
            client = native_type(str(path), config['websocketPythonPath'])
            try:
                cursor = None
                seen = set()
                while True:
                    page = client.request('thread/loaded/list', {'limit': 100, 'cursor': cursor})
                    for thread in page['data']:
                        value = client.request('thread/read', {'threadId': thread, 'excludeTurns': True})['thread']
                        if value.get('status', {}).get('type') not in ('idle', 'notLoaded'):
                            busy.append(thread)
                    cursor = page.get('nextCursor')
                    if not cursor:
                        break
                    if cursor in seen:
                        raise RuntimeError('loaded-thread pagination repeated')
                    seen.add(cursor)
            finally:
                client.close()
        update(root, phase='waiting-for-idle', busyThreads=busy)
        if not busy:
            return
        time.sleep(15)


def run(root, config):
    with lock(root / 'runner.lock'):
        require_claim(config)
        if str(PROFILE.resolve()) not in (config['previousPackage'], config['candidatePackage']):
            raise RuntimeError('selected package changed outside this operation')
        actual = subprocess.check_output(['git', '-C', config['source'], 'rev-parse', 'HEAD'], text=True).strip()
        if actual != config['sourceRevision']:
            raise RuntimeError('workspace feature head changed')
        start = Path('/proc/self/stat').read_text().rsplit(')', 1)[1].split()[19]
        journal = update(root, outer={'pid': os.getpid(), 'start': start}, phase='preparing')
        selected_hook = str(PROFILE.resolve()) == config['candidatePackage'] and journal.get('hookEntered')
        if not journal.get('publication') and not selected_hook:
            wait_for_idle(root, config)
        require_claim(config)
        DROPIN.parent.mkdir(mode=0o700, parents=True, exist_ok=True)
        contents = ('[Service]\nTimeoutStartSec=infinity\nTimeoutStopSec=infinity\n'
                    'Restart=no\nExecStartPre=' + sys.executable + ' ' + str(HERE / 'migration-cutover.py') +
                    ' --root ' + str(root) + ' --publish\n')
        if DROPIN.exists() and DROPIN.read_text() != contents:
            raise RuntimeError('migration drop-in already has different contents')
        DROPIN.write_text(contents)
        fsync_directory(DROPIN.parent)
        command(['systemctl', '--user', 'daemon-reload'])
        with contextlib.ExitStack() as stack:
            if not journal.get('published'):
                for suffix in ('app-server-daemon/daemon.lock', 'app-server-control/app-server-startup.lock'):
                    stack.enter_context(lock(SOURCE / suffix))
                if not journal.get('publication'):
                    for process in native_processes(SOURCE):
                        if not (process['managed'] or process['updater']):
                            continue  # Portal and namer are stopped by normal switch.
                        key = f"{process['pid']}:{process['start']}"
                        signalled = journal.get('signalled', [])
                        if key not in signalled:
                            # Persist intent first: after an ambiguous interruption
                            # never issue a second signal that could force shutdown.
                            journal = update(root, phase='draining-stock', signalled=signalled + [key])
                            os.kill(process['pid'], signal.SIGTERM)
                    while any(p['managed'] or p['updater'] for p in native_processes(SOURCE)):
                        time.sleep(5)
            environment = os.environ.copy()
            environment.update(DEV_SESSION_SLUG=SLUG, DEV_SESSION_WORKSPACE=WORKSPACE,
                               DEV_WORKSPACE_CLAIM_ID=config['claimId'])
            recover_selected_native(root, config)
            update(root, phase='switching')
            # A refusal leaves ordinary recovery authoritative. Exit with retained
            # journal; a subsequent run resumes the same source and claim.
            with (root / 'switch.log').open('a') as log:
                result = subprocess.run([str(PROFILE / 'bin/workspace-host'), 'switch', '--source', config['source']],
                                        env=environment, stdout=log, stderr=subprocess.STDOUT)
            if result.returncode:
                update(root, phase='switch-refused' if str(PROFILE.resolve()) == config['previousPackage']
                       else 'forward-recovery-required', switchExit=result.returncode)
                raise RuntimeError('ordinary switch did not complete; inspect switch.log and resume this operation')
        update(root, phase='verifying')
        command([sys.executable, str(HERE / 'migration-acceptance.py'), '--root', str(root)])
        DROPIN.unlink()
        fsync_directory(DROPIN.parent)
        command(['systemctl', '--user', 'daemon-reload'])
        update(root, phase='accepted')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--root', type=Path)
    parser.add_argument('--publish', action='store_true')
    parser.add_argument('--scan-source', type=Path)
    args = parser.parse_args()
    if args.scan_source:
        assert_no_open_source_files(args.scan_source)
        sys.exit(0)
    if args.root is None:
        parser.error('--root is required')
    os.umask(0o077)
    configuration = json.loads((args.root / 'config.json').read_text())
    try:
        (publish if args.publish else run)(args.root, configuration)
    except Exception as error:
        update(args.root, error=str(error))
        if not args.publish and str(PROFILE.resolve()) == configuration['previousPackage']:
            # Preselection failures leave the original home authoritative. The
            # ordinary switch restores portal/terminal services; restore stock
            # availability only after the enclosing file locks have unwound.
            recovery_env = os.environ.copy()
            recovery_env.update(CODEX_HOME=str(SOURCE), CODEX_SQLITE_HOME=str(SOURCE))
            recovery = subprocess.run(['/run/current-system/sw/bin/codex', 'app-server', 'daemon', 'start'],
                                      env=recovery_env, stdout=subprocess.DEVNULL)
            update(args.root, stockRestorationExit=recovery.returncode)
        raise
```

## migration-acceptance.py

SHA-256: `7ea3997bf3caaca5c43f85dfee7c5c956c67097b657280c243602cbdc0415474`

```python
#!/usr/bin/env python3
"""Read migrated state and retry the one user-authorized original message."""
import argparse
import contextlib
import hashlib
import http.client
import importlib.util
import json
import os
import socket
import sqlite3
import subprocess
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('cutover', HERE / 'migration-cutover.py')
cutover = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cutover)
PORTAL_SOCKET = '/run/user/1000/dev-workspaces/vpsfree-cz/portal.sock'
NATIVE_SOCKET = '/run/user/1000/dev-workspaces/vpsfree-cz/app-server.sock'
HOST = 'vpsfree-cz.workspace.aitherdev.int.vpsfree.cz'
ATTEMPT = '2a2656f4-3d35-4bee-9a71-14e20bc35669'
THREAD = '01a14bb2-e3ad-7922-a5c9-bc1d07d5cbb8'
MESSAGE = 'yes go ahead'
LEDGER = Path('/home/aither/.local/state/dev-workspaces/submissions/'
              'bced879de15a05f23836072b53ea2860aa13a982415f07bf83ab93a6ee8c9ea6.sqlite')


class UnixHTTP(http.client.HTTPConnection):
    def connect(self):
        self.sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        self.sock.settimeout(self.timeout)
        self.sock.connect(PORTAL_SOCKET)


def http(path, payload=None):
    connection = UnixHTTP(HOST, timeout=180)
    try:
        body = json.dumps(payload) if payload is not None else None
        connection.request('POST' if body else 'GET', path, body=body,
                           headers={'Origin': 'https://' + HOST, 'Content-Type': 'application/json'})
        response = connection.getresponse()
        content = response.read()
        if response.status >= 300:
            raise RuntimeError(f'portal HTTP {response.status} on {path}: {content[:512].decode()}')
        return json.loads(content) if content else {}
    finally:
        connection.close()


class Native:
    def __init__(self, path, python_path):
        sys.path.insert(0, python_path)
        import websocket
        sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        sock.connect(path)
        self.ws = websocket.create_connection('ws://localhost/', socket=sock, timeout=120)
        self.number = 0
        self.info = self.request('initialize', {'clientInfo': {'name': 'portal-home-migration',
                                  'title': 'Portal home verification', 'version': '1'},
                                  'capabilities': {'experimentalApi': True}})
        self.ws.send(json.dumps({'method': 'initialized'}))

    def request(self, method, params):
        self.number += 1
        self.ws.send(json.dumps({'id': self.number, 'method': method, 'params': params}))
        while True:
            result = json.loads(self.ws.recv())
            if result.get('id') != self.number:
                continue
            if 'error' in result:
                raise RuntimeError(f'native {method}: {result["error"]}')
            return result['result']

    def close(self):
        self.ws.close()


def ledger():
    with contextlib.closing(sqlite3.connect(f'file:{LEDGER}?mode=ro', uri=True)) as db:
        row = db.execute('select payload from submission_records where kind=? and thread_id=? and attempt_id=?',
                         ('sends', THREAD, ATTEMPT)).fetchone()
    if row is None:
        raise RuntimeError('original submission receipt is absent; do not manufacture a new attempt')
    value = json.loads(row[0])
    if value.get('digest') != hashlib.sha256(MESSAGE.encode()).hexdigest():
        raise RuntimeError('original submission digest changed')
    return value


def accept(root):
    config = json.loads((root / 'config.json').read_text())
    journal = json.loads((root / 'journal.json').read_text())
    if not journal.get('published') or str(cutover.PROFILE.resolve()) != config['candidatePackage']:
        raise RuntimeError('migration is not published under the selected target')
    inventory = json.loads((root / 'inventory.json').read_text())
    report = {'schema': 1, 'startedAt': time.time(), 'threadsRead': 0}
    for label, home in [('portal', cutover.PORTAL), ('stock', cutover.SOURCE)]:
        with contextlib.closing(sqlite3.connect(f'file:{home}/state_5.sqlite?mode=ro', uri=True)) as db:
            actual = set(row[0] for row in db.execute('select id from threads'))
        expected = set(inventory[label])
        forbidden = set(inventory['stock' if label == 'portal' else 'portal']) - expected
        if not expected <= actual or forbidden & actual:
            raise RuntimeError(f'{label} thread partition changed or is incomplete')
        report[label + 'Threads'] = len(actual)
    for unit in ['workspace-codex@vpsfree-cz.service', 'workspace-portal@vpsfree-cz.service']:
        subprocess.run(['systemctl', '--user', 'is-active', '--quiet', unit], check=True)
    pid = subprocess.check_output(['systemctl', '--user', 'show', '-p', 'MainPID', '--value', cutover.UNIT], text=True).strip()
    env = dict(x.split(b'=', 1) for x in Path(f'/proc/{pid}/environ').read_bytes().split(b'\0') if b'=' in x)
    if env.get(b'CODEX_HOME') != str(cutover.PORTAL).encode() or env.get(b'CODEX_SQLITE_HOME') != str(cutover.PORTAL).encode():
        raise RuntimeError('portal native environment does not select private storage')
    executable = Path(os.readlink(f'/proc/{pid}/exe'))
    if hashlib.sha256(executable.read_bytes()).hexdigest() != config['nativeSHA256']:
        raise RuntimeError('portal native binary differs from the verified candidate')
    report['nativeExecutable'] = str(executable)
    http('/healthz')
    native = Native(NATIVE_SOCKET, config['websocketPythonPath'])
    try:
        for thread in inventory['portal']:
            value = native.request('thread/read', {'threadId': thread, 'excludeTurns': True})['thread']
            if value['id'] != thread or not str(value.get('path', '')).startswith(str(cutover.PORTAL) + '/'):
                raise RuntimeError(f'native thread has wrong identity/storage: {thread}')
            report['threadsRead'] += 1
            if report['threadsRead'] % 100 == 0:
                cutover.save(root / 'acceptance.json', report)
    finally:
        native.close()
    # The stock daemon starts through its own CLI, with no portal environment.
    stock_env = os.environ.copy()
    stock_env.update(CODEX_HOME=str(cutover.SOURCE), CODEX_SQLITE_HOME=str(cutover.SOURCE))
    subprocess.run(['/run/current-system/sw/bin/codex', 'app-server', 'daemon', 'start'],
                   env=stock_env, check=True, stdout=subprocess.DEVNULL)
    report['activity'] = {}
    for slug in ['2026-10-22-limit-autostart-alerts-to-boot', '2026-10-17-confctl-rust-rewrite-plan']:
        deadline = time.monotonic() + 600
        while True:
            activity = http('/api/sessions/' + slug + '/activity')
            if not activity.get('refreshing'):
                break
            if time.monotonic() > deadline:
                raise RuntimeError(f'history statistics did not finish loading: {slug}')
            time.sleep(5)
        if activity.get('currentState') in (None, '', 'unknown') or not activity.get('observedAtMs'):
            raise RuntimeError(f'activity remains unavailable: {slug}')
        report['activity'][slug] = activity
    cutover.save(root / 'acceptance.json', report)
    # SendAttempted in this same-ID portal path reconciles queue/transcript and
    # receipts before Send. Never create a new browser attempt or native turn.
    original = ledger()
    if original['state'] != 'accepted':
        if original['state'] not in ('prepared', 'submitting'):
            raise RuntimeError('original message is no longer eligible for retry')
        cutover.update(root, phase='retrying-original', originalAttempt=ATTEMPT)
        response = http('/codex/conversations/2026-10-17-confctl-rust-rewrite-plan/message',
                        {'message': MESSAGE, 'clientUserMessageId': ATTEMPT, 'retry': True})
        if response.get('clientUserMessageId') != ATTEMPT:
            raise RuntimeError('portal retry returned a different attempt')
        report['retryReceipt'] = response
    accepted = ledger()
    if accepted['state'] != 'accepted':
        raise RuntimeError('original message delivery is not confirmed')
    report['originalMessage'] = {'attempt': ATTEMPT, 'state': 'accepted',
                                 'turnId': accepted.get('turnId'),
                                 'queuedSubmissionId': accepted.get('queuedSubmissionId')}
    report['completedAt'] = time.time()
    cutover.save(root / 'acceptance.json', report)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--root', type=Path, required=True)
    accept(parser.parse_args().root)
```

## migration-test.py

SHA-256: `95b1039676bd265e226d83e8be78359dd61d24d32255f505a4b836a0dbc1adb6`

```python
#!/usr/bin/env python3
"""Disposable synthetic fixtures; never opens live conversation databases."""
import importlib.util
import contextlib
import json
import os
import sqlite3
import subprocess
import sys
import tempfile
import unittest
from types import SimpleNamespace
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).parent
spec = importlib.util.spec_from_file_location('partition', ROOT / 'migration-partition.py')
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)
spec = importlib.util.spec_from_file_location('cutover', ROOT / 'migration-cutover.py')
c = importlib.util.module_from_spec(spec)
spec.loader.exec_module(c)


class PartitionTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(prefix='portal-migration-test-')
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.source = self.root / 'original'
        self.source.mkdir()
        self.prepared = self.root / 'prepared'
        self.prepared.mkdir()
        for name in ('auth.json', 'config.toml'):
            (self.prepared / name).write_text('{}' if name.endswith('.json') else '')
        self.definitions = json.loads((ROOT / 'migration-schemas.json').read_text())
        for name, definitions in self.definitions.items():
            with contextlib.closing(sqlite3.connect(self.source / name)) as db, db:
                for kind, table, _, ddl in definitions:
                    if kind == 'table' and not table.startswith('sqlite_'):
                        db.execute(ddl)
                for kind, _, _, ddl in definitions:
                    if ddl and kind in ('index', 'trigger', 'view'):
                        db.execute(ddl)
        self.ids = ['00000000-0000-0000-0000-000000000001',
                    '00000000-0000-0000-0000-000000000002']
        self.threads = {}
        for index, thread in enumerate(self.ids):
            path = self.source / 'sessions' / f'rollout-{thread}.jsonl'
            path.parent.mkdir(exist_ok=True)
            path.write_text(json.dumps({'type': 'session_meta', 'payload': {'id': thread}}) + '\n')
            self.threads[thread] = {'id': thread, 'rollout_path': str(path)}
            with contextlib.closing(sqlite3.connect(self.source / 'state_5.sqlite')) as db, db:
                db.execute('insert into threads(id, rollout_path, created_at, updated_at, source, '
                           'model_provider, cwd, title, sandbox_policy, approval_mode) '
                           'values (?, ?, 1, 2, ?, ?, ?, ?, ?, ?)',
                           (thread, str(path), 'cli', 'openai', '/fixture', 'name', '{}', 'never'))
            with contextlib.closing(sqlite3.connect(self.source / 'thread_history_1.sqlite')) as db, db:
                db.execute('insert into thread_items(thread_id,turn_id,item_id,rollout_ordinal,created_at_ms,item_json) '
                           'values (?, ?, ?, ?, ?, ?)', (thread, 'turn', 'item', index, 1, '{"opaque":"preserved"}'))
        with contextlib.closing(sqlite3.connect(self.source / 'thread_history_1.sqlite')) as db, db:
            db.execute("insert into thread_history_projection_state values ('unknown-stock', 7, 9)")
        self.inventory = {'source': str(self.source), 'portal': [self.ids[0]], 'stock': [self.ids[1]],
                          'threads': self.threads, 'missingRows': [], 'missingPortalRollouts': [],
                          'externalPortalRollouts': []}

    def run_partition(self):
        return m.partition(self.inventory, self.root / 'stage', self.root / 'final-portal', self.prepared)

    def test_partition_preserves_schema_history_and_original(self):
        self.run_partition()
        for label, expected in [('portal', self.ids[0]), ('stock', self.ids[1])]:
            for name in m.SCHEMAS:
                with contextlib.closing(sqlite3.connect(self.root / 'stage' / label / name)) as db:
                    self.assertEqual(m.schema_hash(m.schema(db)), m.SCHEMAS[name])
            with contextlib.closing(sqlite3.connect(self.root / 'stage' / label / 'state_5.sqlite')) as db:
                rows = list(db.execute('select id,rollout_path from threads'))
                self.assertEqual([x[0] for x in rows], [expected])
                prefix = self.root / 'final-portal' if label == 'portal' else self.source
                self.assertTrue(rows[0][1].startswith(str(prefix) + '/'))
            with contextlib.closing(sqlite3.connect(self.root / 'stage' / label / 'thread_history_1.sqlite')) as db:
                self.assertEqual(db.execute('select thread_id,item_json from thread_items').fetchall(),
                                 [(expected, '{"opaque":"preserved"}')])
                self.assertEqual(db.execute('select count(*) from thread_history_projection_state').fetchone()[0],
                                 1 if label == 'stock' else 0)
        with contextlib.closing(sqlite3.connect(self.source / 'state_5.sqlite')) as db:
            self.assertEqual(db.execute('select count(*) from threads').fetchone()[0], 2)

    def test_refuses_missing_portal_history_before_copy(self):
        self.inventory['missingPortalRollouts'] = [self.ids[0]]
        with self.assertRaisesRegex(ValueError, 'missing or external'):
            self.run_partition()
        self.assertFalse((self.root / 'stage').exists())

    def test_refuses_low_space_before_copy(self):
        with patch.object(m.shutil, 'disk_usage', return_value=type('Disk', (), {'free': 1})()):
            with self.assertRaisesRegex(ValueError, 'insufficient space'):
                self.run_partition()
        self.assertFalse((self.root / 'stage').exists())

    def test_refuses_unknown_schema(self):
        with contextlib.closing(sqlite3.connect(self.source / 'state_5.sqlite')) as db, db:
            db.execute('create table unknown(value text)')
        with self.assertRaisesRegex(ValueError, 'unsupported native schema'):
            self.run_partition()


    @contextlib.contextmanager
    def publication_fixture(self):
        operation = self.root / 'operation'
        operation.mkdir()
        candidate = self.root / 'candidate'
        candidate.mkdir()
        profile = self.root / 'profile'
        profile.symlink_to(candidate)
        start = Path('/proc/self/stat').read_text().rsplit(')', 1)[1].split()[19]
        c.save(operation / 'journal.json', {'outer': {'pid': os.getpid(), 'start': start}})
        modules = {'migration-inventory': SimpleNamespace(inventory=lambda: self.inventory),
                   'migration-partition': m}
        with patch.object(c, 'SOURCE', self.source), patch.object(c, 'PORTAL', self.prepared), \
                patch.object(c, 'PROFILE', profile), patch.object(c, 'native_processes', return_value=[]), \
                patch.object(c, 'assert_no_open_source_files'), patch.object(c, 'module', side_effect=modules.__getitem__):
            yield operation, {'candidatePackage': str(candidate), 'previousPackage': '/old-package'}

    def test_short_lived_writer_during_copy_refuses_publication(self):
        partition = m.partition
        def copy_with_writer(*args):
            result = partition(*args)
            subprocess.run([sys.executable, '-c',
                            'import pathlib,sys; pathlib.Path(sys.argv[1]).write_text("new turn")',
                            str(self.source / 'sessions' / 'new-turn.jsonl')], check=True)
            return result
        with self.publication_fixture() as (operation, config), patch.object(m, 'partition', side_effect=copy_with_writer):
            with self.assertRaises(c.SourceChanged):
                c.publish(operation, config)
            journal = json.loads((operation / 'journal.json').read_text())
            self.assertNotIn('publication', journal)
            self.assertTrue((self.source / 'sessions' / 'new-turn.jsonl').exists())
            self.assertFalse((self.prepared / 'state_5.sqlite').exists())

    def test_wal_source_reads_preserve_observed_content(self):
        for name in self.definitions:
            with contextlib.closing(sqlite3.connect(self.source / name)) as db:
                db.execute('pragma journal_mode=WAL')
        with self.publication_fixture() as (operation, config):
            c.publish(operation, config)
            self.assertTrue(json.loads((operation / 'journal.json').read_text())['published'])

    def test_short_lived_wal_writer_refuses_publication(self):
        with contextlib.closing(sqlite3.connect(self.source / 'state_5.sqlite')) as db:
            db.execute('pragma journal_mode=WAL')
        partition = m.partition
        def copy_with_writer(*args):
            result = partition(*args)
            subprocess.run([sys.executable, '-c',
                'import sqlite3,sys; c=sqlite3.connect(sys.argv[1]); '
                'c.execute("update threads set title=?", ("new title",)); c.commit(); c.close()',
                str(self.source / 'state_5.sqlite')], check=True)
            return result
        with self.publication_fixture() as (operation, config), patch.object(m, 'partition', side_effect=copy_with_writer):
            with self.assertRaises(c.SourceChanged):
                c.publish(operation, config)
            self.assertNotIn('publication', json.loads((operation / 'journal.json').read_text()))

    def test_interrupted_exchange_resumes_without_losing_new_stock_writes(self):
        exchange = c.exchange
        def interrupt_after_exchange(*args):
            exchange(*args)
            raise InterruptedError('simulated process loss')
        with self.publication_fixture() as (operation, config):
            with patch.object(c, 'exchange', side_effect=interrupt_after_exchange):
                with self.assertRaises(InterruptedError):
                    c.publish(operation, config)
            (self.source / 'new-stock-turn').write_text('accepted after exchange')
            c.publish(operation, config)
            self.assertTrue(json.loads((operation / 'journal.json').read_text())['published'])
            self.assertEqual((self.source / 'new-stock-turn').read_text(), 'accepted after exchange')
            with contextlib.closing(sqlite3.connect(self.prepared / 'state_5.sqlite')) as db:
                self.assertEqual(db.execute('select id from threads').fetchall(), [(self.ids[0],)])

    def test_source_write_after_interruption_refuses_resume(self):
        with self.publication_fixture() as (operation, config):
            with patch.object(c, 'exchange', side_effect=InterruptedError('before first exchange')):
                with self.assertRaises(InterruptedError):
                    c.publish(operation, config)
            (self.source / 'sessions' / 'late-turn.jsonl').write_text('not in staged copy')
            with self.assertRaisesRegex(c.SourceChanged, 'after publication intent'):
                c.publish(operation, config)
            self.assertTrue(json.loads((operation / 'journal.json').read_text())['sourceChangedAfterIntent'])
            self.assertTrue((self.source / 'sessions' / 'late-turn.jsonl').exists())

    def test_outer_retry_after_intent_starts_selected_hook_before_switch(self):
        with self.publication_fixture() as (operation, config):
            config.update(source='/fixture', sourceRevision='expected', claimId='fixture')
            current = self.root / 'codex'; current.touch()
            pending = self.root / 'pending'
            pending.write_text(json.dumps({'package_root': config['candidatePackage'], 'codex_path': str(current)}))
            c.update(operation, hookEntered=True)
            commands = []
            def run_command(args, **kwargs):
                commands.append(args)
                if args[:3] == ['systemctl', '--user', 'start']:
                    c.publish(operation, config)
            def switch(args, **kwargs):
                self.assertTrue(json.loads((operation / 'journal.json').read_text())['published'])
                commands.append(args)
                return SimpleNamespace(returncode=0)
            with patch.object(c, 'require_claim'), patch.object(c, 'wait_for_idle') as idle, \
                    patch.object(c, 'CODEX_CURRENT', current), patch.object(c, 'PENDING', pending), \
                    patch.object(c, 'DROPIN', self.root / 'dropin' / 'migration.conf'), \
                    patch.object(c, 'command', side_effect=run_command), \
                    patch.object(c.subprocess, 'check_output', return_value='expected\n'), \
                    patch.object(c.subprocess, 'run', side_effect=switch):
                with patch.object(c, 'exchange', side_effect=InterruptedError('after intent, before exchange')):
                    with self.assertRaises(InterruptedError):
                        c.run(operation, config)
                before = c.source_fingerprint(self.source)
                c.run(operation, config)
                self.assertEqual(c.source_fingerprint(operation / 'partition' / 'stock'), before)
                idle.assert_not_called()
            self.assertEqual(json.loads((operation / 'journal.json').read_text())['phase'], 'accepted')
            start = next(i for i, args in enumerate(commands) if args[:3] == ['systemctl', '--user', 'start'])
            switch_index = next(i for i, args in enumerate(commands) if 'switch' in args)
            self.assertLess(start, switch_index)


class PublicationTest(unittest.TestCase):
    def test_inotify_detects_completed_writer_and_accepts_own_exchange(self):
        with tempfile.TemporaryDirectory(prefix='portal-watch-test-') as directory:
            root = Path(directory)
            live, staged = root / 'live', root / 'staged'
            live.mkdir(); staged.mkdir()
            (live / 'history').write_text('before')
            observer = c.SourceWatch(live)
            try:
                subprocess.run([sys.executable, '-c',
                    'import pathlib,sys; pathlib.Path(sys.argv[1]).write_text("after")',
                    str(live / 'history')], check=True)
                with self.assertRaises(c.SourceChanged):
                    observer.assert_stable()
            finally:
                observer.close()
            observer = c.SourceWatch(live)
            try:
                before = c.source_fingerprint(live)
                c.exchange(live, staged, c.identity(live), c.identity(staged))
                observer.assert_stable(allow_exchange=True)
                self.assertEqual(c.source_fingerprint(staged), before)
            finally:
                observer.close()

    def test_selected_failed_hook_recovers_native_before_switch(self):
        with tempfile.TemporaryDirectory(prefix='portal-recover-test-') as directory:
            root = Path(directory)
            profile = root / 'profile'
            candidate = root / 'candidate'
            candidate.mkdir(); profile.symlink_to(candidate)
            current = root / 'codex'
            current.touch()
            pending = root / 'pending'
            pending.write_text(json.dumps({'package_root': str(candidate), 'codex_path': str(current)}))
            c.save(root / 'journal.json', {'hookEntered': True})
            with patch.object(c, 'PROFILE', profile), patch.object(c, 'CODEX_CURRENT', current), \
                    patch.object(c, 'PENDING', pending), patch.object(c, 'command') as run:
                c.recover_selected_native(root, {'candidatePackage': str(candidate)})
                run.assert_called_once_with(['systemctl', '--user', 'start', c.UNIT])
                pending.write_text(json.dumps({'package_root': 'wrong', 'codex_path': str(current)}))
                run.reset_mock()
                with self.assertRaisesRegex(RuntimeError, 'pending target'):
                    c.recover_selected_native(root, {'candidatePackage': str(candidate)})
                run.assert_not_called()

    def test_exchange_recovers_after_lost_journal_write_and_preserves_new_writes(self):
        with tempfile.TemporaryDirectory(prefix='portal-exchange-test-') as directory:
            root = Path(directory)
            live, staged = root / 'live', root / 'staged'
            live.mkdir(); staged.mkdir()
            (live / 'original').write_text('original history')
            (staged / 'partition').write_text('partitioned history')
            before = c.identity(live), c.identity(staged)
            # The journal still contains the pre-exchange identities after a
            # hypothetical kill immediately after renameat2.
            c.exchange(live, staged, *before)
            (live / 'new-turn').write_text('accepted after publication')
            c.exchange(live, staged, *before)
            self.assertEqual((live / 'new-turn').read_text(), 'accepted after publication')
            self.assertEqual((staged / 'original').read_text(), 'original history')
            self.assertFalse((live / 'original').exists())

    def test_exchange_rejects_unexpected_directories(self):
        with tempfile.TemporaryDirectory(prefix='portal-exchange-test-') as directory:
            root = Path(directory)
            live, staged = root / 'live', root / 'staged'
            live.mkdir(); staged.mkdir()
            with self.assertRaisesRegex(RuntimeError, 'identity changed'):
                c.exchange(live, staged, [0, 0], c.identity(staged))

    def test_source_open_file_refuses_copy(self):
        import subprocess
        import sys
        with tempfile.TemporaryDirectory(prefix='portal-writer-test-') as directory:
            root = Path(directory)
            (root / 'state_5.sqlite').touch()
            child = subprocess.Popen([sys.executable, '-c',
                'import sys,time; f=open(sys.argv[1]); print("ready",flush=True); time.sleep(30)',
                str(root / 'state_5.sqlite')], stdout=subprocess.PIPE, text=True)
            try:
                self.assertEqual(child.stdout.readline().strip(), 'ready')
                with self.assertRaises(subprocess.CalledProcessError) as raised:
                    c.assert_no_open_source_files(root)
                self.assertIn('still open', raised.exception.stderr)
            finally:
                child.terminate(); child.wait(); child.stdout.close()


if __name__ == '__main__':
    unittest.main()
```

## migration-schemas.json

SHA-256: `9292c98a68c73fd288e7c0ab8bdbcad2d9116832bfa86d63bb949732a2285c89`

```json
{
  "state_5.sqlite": [
    [
      "index",
      "idx_projects_position",
      "projects",
      "CREATE INDEX idx_projects_position\n    ON projects(position ASC, id ASC)"
    ],
    [
      "index",
      "idx_thread_attachments_identity_thread",
      "thread_attachments",
      "CREATE INDEX idx_thread_attachments_identity_thread\n    ON thread_attachments(attachment_type, identity_key, thread_id)"
    ],
    [
      "index",
      "idx_thread_attachments_thread_created_id",
      "thread_attachments",
      "CREATE INDEX idx_thread_attachments_thread_created_id\n    ON thread_attachments(thread_id, created_at, id)"
    ],
    [
      "index",
      "idx_thread_dynamic_tools_thread",
      "thread_dynamic_tools",
      "CREATE INDEX idx_thread_dynamic_tools_thread ON thread_dynamic_tools(thread_id)"
    ],
    [
      "index",
      "idx_thread_spawn_edges_parent_status",
      "thread_spawn_edges",
      "CREATE INDEX idx_thread_spawn_edges_parent_status\n    ON thread_spawn_edges(parent_thread_id, status)"
    ],
    [
      "index",
      "idx_threads_archive_created_at_ms",
      "threads",
      "CREATE INDEX idx_threads_archive_created_at_ms\n    ON threads(archived, created_at_ms DESC, id DESC)\n    WHERE archived = 1"
    ],
    [
      "index",
      "idx_threads_archive_recency_at_ms",
      "threads",
      "CREATE INDEX idx_threads_archive_recency_at_ms\n    ON threads(archived, recency_at_ms DESC, id DESC)\n    WHERE archived = 1"
    ],
    [
      "index",
      "idx_threads_archive_updated_at_ms",
      "threads",
      "CREATE INDEX idx_threads_archive_updated_at_ms\n    ON threads(archived, updated_at_ms DESC, id DESC)\n    WHERE archived = 1"
    ],
    [
      "index",
      "idx_threads_archived",
      "threads",
      "CREATE INDEX idx_threads_archived ON threads(archived)"
    ],
    [
      "index",
      "idx_threads_archived_cwd_created_at_ms",
      "threads",
      "CREATE INDEX idx_threads_archived_cwd_created_at_ms ON threads(archived, cwd, created_at_ms DESC, id DESC)"
    ],
    [
      "index",
      "idx_threads_archived_cwd_recency_at_ms",
      "threads",
      "CREATE INDEX idx_threads_archived_cwd_recency_at_ms\n    ON threads(archived, cwd, recency_at_ms DESC, id DESC)"
    ],
    [
      "index",
      "idx_threads_archived_cwd_updated_at_ms",
      "threads",
      "CREATE INDEX idx_threads_archived_cwd_updated_at_ms ON threads(archived, cwd, updated_at_ms DESC, id DESC)"
    ],
    [
      "index",
      "idx_threads_attached_parent",
      "threads",
      "CREATE INDEX idx_threads_attached_parent ON threads(attached_thread_parent_id)\n    WHERE attached_thread_parent_id IS NOT NULL"
    ],
    [
      "index",
      "idx_threads_created_at",
      "threads",
      "CREATE INDEX idx_threads_created_at ON threads(created_at DESC, id DESC)"
    ],
    [
      "index",
      "idx_threads_created_at_ms",
      "threads",
      "CREATE INDEX idx_threads_created_at_ms ON threads(created_at_ms DESC, id DESC)"
    ],
    [
      "index",
      "idx_threads_pinned_recency_at_ms",
      "threads",
      "CREATE INDEX idx_threads_pinned_recency_at_ms\n    ON threads(archived, recency_at_ms DESC, id DESC)\n    WHERE is_pinned = 1 AND preview <> ''"
    ],
    [
      "index",
      "idx_threads_project_id",
      "threads",
      "CREATE INDEX idx_threads_project_id\n    ON threads(project_id, archived, created_at_ms DESC, id DESC)\n    WHERE project_id IS NOT NULL"
    ],
    [
      "index",
      "idx_threads_project_recency",
      "threads",
      "CREATE INDEX idx_threads_project_recency\n    ON threads(project_id, recency_at_ms DESC)\n    WHERE archived = 0 AND project_id IS NOT NULL"
    ],
    [
      "index",
      "idx_threads_provider",
      "threads",
      "CREATE INDEX idx_threads_provider ON threads(model_provider)"
    ],
    [
      "index",
      "idx_threads_recency_at_ms",
      "threads",
      "CREATE INDEX idx_threads_recency_at_ms\n    ON threads(recency_at_ms DESC, id DESC)"
    ],
    [
      "index",
      "idx_threads_section_position",
      "threads",
      "CREATE INDEX idx_threads_section_position\n    ON threads(archived, thread_section_id, section_position ASC, id ASC)\n    WHERE thread_section_id IS NOT NULL"
    ],
    [
      "index",
      "idx_threads_section_recency_at_ms",
      "threads",
      "CREATE INDEX idx_threads_section_recency_at_ms\n    ON threads(archived, thread_section_id, recency_at_ms DESC, id DESC)\n    WHERE thread_section_id IS NOT NULL"
    ],
    [
      "index",
      "idx_threads_source",
      "threads",
      "CREATE INDEX idx_threads_source ON threads(source)"
    ],
    [
      "index",
      "idx_threads_updated_at",
      "threads",
      "CREATE INDEX idx_threads_updated_at ON threads(updated_at DESC, id DESC)"
    ],
    [
      "index",
      "idx_threads_updated_at_ms",
      "threads",
      "CREATE INDEX idx_threads_updated_at_ms ON threads(updated_at_ms DESC, id DESC)"
    ],
    [
      "index",
      "idx_threads_visible_created_at_ms",
      "threads",
      "CREATE INDEX idx_threads_visible_created_at_ms\n    ON threads(archived, created_at_ms DESC)\n    WHERE preview <> ''"
    ],
    [
      "index",
      "idx_threads_visible_recency_at_ms",
      "threads",
      "CREATE INDEX idx_threads_visible_recency_at_ms\n    ON threads(archived, recency_at_ms DESC, id DESC)\n    WHERE preview <> ''"
    ],
    [
      "index",
      "idx_threads_visible_updated_at_ms",
      "threads",
      "CREATE INDEX idx_threads_visible_updated_at_ms\n    ON threads(archived, updated_at_ms DESC)\n    WHERE preview <> ''"
    ],
    [
      "index",
      "sqlite_autoindex__sqlx_migrations_1",
      "_sqlx_migrations",
      null
    ],
    [
      "index",
      "sqlite_autoindex_external_agent_config_imports_1",
      "external_agent_config_imports",
      null
    ],
    [
      "index",
      "sqlite_autoindex_guardian_review_feedback_1",
      "guardian_review_feedback",
      null
    ],
    [
      "index",
      "sqlite_autoindex_project_idempotency_keys_1",
      "project_idempotency_keys",
      null
    ],
    [
      "index",
      "sqlite_autoindex_project_roots_1",
      "project_roots",
      null
    ],
    [
      "index",
      "sqlite_autoindex_projects_1",
      "projects",
      null
    ],
    [
      "index",
      "sqlite_autoindex_remote_control_enrollments_1",
      "remote_control_enrollments",
      null
    ],
    [
      "index",
      "sqlite_autoindex_rollout_migration_skipped_rollouts_1",
      "rollout_migration_skipped_rollouts",
      null
    ],
    [
      "index",
      "sqlite_autoindex_rollout_migration_state_1",
      "rollout_migration_state",
      null
    ],
    [
      "index",
      "sqlite_autoindex_thread_attachments_1",
      "thread_attachments",
      null
    ],
    [
      "index",
      "sqlite_autoindex_thread_attachments_2",
      "thread_attachments",
      null
    ],
    [
      "index",
      "sqlite_autoindex_thread_dynamic_tools_1",
      "thread_dynamic_tools",
      null
    ],
    [
      "index",
      "sqlite_autoindex_thread_read_receipts_1",
      "thread_read_receipts",
      null
    ],
    [
      "index",
      "sqlite_autoindex_thread_sections_1",
      "thread_sections",
      null
    ],
    [
      "index",
      "sqlite_autoindex_thread_spawn_edges_1",
      "thread_spawn_edges",
      null
    ],
    [
      "index",
      "sqlite_autoindex_threads_1",
      "threads",
      null
    ],
    [
      "table",
      "_sqlx_migrations",
      "_sqlx_migrations",
      "CREATE TABLE _sqlx_migrations (\n    version BIGINT PRIMARY KEY,\n    description TEXT NOT NULL,\n    installed_on TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,\n    success BOOLEAN NOT NULL,\n    checksum BLOB NOT NULL,\n    execution_time BIGINT NOT NULL\n)"
    ],
    [
      "table",
      "backfill_state",
      "backfill_state",
      "CREATE TABLE backfill_state (\n    id INTEGER PRIMARY KEY CHECK (id = 1),\n    status TEXT NOT NULL,\n    last_watermark TEXT,\n    last_success_at INTEGER,\n    updated_at INTEGER NOT NULL\n)"
    ],
    [
      "table",
      "external_agent_config_imports",
      "external_agent_config_imports",
      "CREATE TABLE external_agent_config_imports (\n    import_id TEXT PRIMARY KEY,\n    completed_at_ms INTEGER NOT NULL,\n    successes TEXT NOT NULL,\n    failures TEXT NOT NULL\n, provider_id TEXT)"
    ],
    [
      "table",
      "guardian_review_feedback",
      "guardian_review_feedback",
      "CREATE TABLE guardian_review_feedback (\n    id TEXT PRIMARY KEY NOT NULL,\n    thread_id TEXT NOT NULL REFERENCES threads(id) ON DELETE CASCADE,\n    record BLOB NOT NULL\n)"
    ],
    [
      "table",
      "project_idempotency_keys",
      "project_idempotency_keys",
      "CREATE TABLE project_idempotency_keys (\n    key TEXT PRIMARY KEY,\n    project_id TEXT NOT NULL,\n    created_at_ms INTEGER NOT NULL\n)"
    ],
    [
      "table",
      "project_roots",
      "project_roots",
      "CREATE TABLE project_roots (\n    project_id TEXT NOT NULL REFERENCES projects(id) ON DELETE CASCADE,\n    position INTEGER NOT NULL,\n    path TEXT NOT NULL,\n    PRIMARY KEY (project_id, position)\n)"
    ],
    [
      "table",
      "projects",
      "projects",
      "CREATE TABLE projects (\n    id TEXT PRIMARY KEY,\n    name TEXT NOT NULL,\n    metadata TEXT NOT NULL DEFAULT '{}',\n    position INTEGER NOT NULL,\n    created_at_ms INTEGER NOT NULL,\n    updated_at_ms INTEGER NOT NULL\n)"
    ],
    [
      "table",
      "remote_control_enrollments",
      "remote_control_enrollments",
      "CREATE TABLE remote_control_enrollments (\n    websocket_url TEXT NOT NULL,\n    account_id TEXT NOT NULL,\n    app_server_client_name TEXT NOT NULL,\n    server_id TEXT NOT NULL,\n    environment_id TEXT NOT NULL,\n    server_name TEXT NOT NULL,\n    updated_at INTEGER NOT NULL, remote_control_enabled INTEGER,\n    PRIMARY KEY (websocket_url, account_id, app_server_client_name)\n)"
    ],
    [
      "table",
      "rollout_migration_skipped_rollouts",
      "rollout_migration_skipped_rollouts",
      "CREATE TABLE rollout_migration_skipped_rollouts (\n    migration_id TEXT NOT NULL,\n    rollout_path TEXT NOT NULL,\n    rollout_size_bytes INTEGER NOT NULL,\n    rollout_modified_at_ns INTEGER NOT NULL,\n    skip_reason TEXT NOT NULL,\n    skipped_at INTEGER NOT NULL,\n    PRIMARY KEY (migration_id, rollout_path)\n)"
    ],
    [
      "table",
      "rollout_migration_state",
      "rollout_migration_state",
      "CREATE TABLE rollout_migration_state (\n    migration_id TEXT PRIMARY KEY,\n    last_checked_thread_created_at INTEGER,\n    last_checked_thread_id TEXT,\n    updated_at INTEGER NOT NULL\n)"
    ],
    [
      "table",
      "thread_attachments",
      "thread_attachments",
      "CREATE TABLE \"thread_attachments\" (\n    id TEXT PRIMARY KEY,\n    thread_id TEXT NOT NULL REFERENCES threads(id) ON DELETE CASCADE,\n    attachment_type TEXT NOT NULL,\n    identity_key TEXT NOT NULL,\n    payload TEXT NOT NULL,\n    created_at INTEGER NOT NULL,\n    UNIQUE (thread_id, attachment_type, identity_key)\n)"
    ],
    [
      "table",
      "thread_dynamic_tools",
      "thread_dynamic_tools",
      "CREATE TABLE thread_dynamic_tools (\n    thread_id TEXT NOT NULL,\n    position INTEGER NOT NULL,\n    name TEXT NOT NULL,\n    description TEXT NOT NULL,\n    input_schema TEXT NOT NULL, defer_loading INTEGER NOT NULL DEFAULT 0, namespace TEXT,\n    PRIMARY KEY(thread_id, position),\n    FOREIGN KEY(thread_id) REFERENCES threads(id) ON DELETE CASCADE\n)"
    ],
    [
      "table",
      "thread_read_receipts",
      "thread_read_receipts",
      "CREATE TABLE thread_read_receipts (\n    thread_id TEXT PRIMARY KEY NOT NULL,\n    first_unread_turn TEXT,\n    revision TEXT NOT NULL,\n    last_published_turn TEXT\n)"
    ],
    [
      "table",
      "thread_sections",
      "thread_sections",
      "CREATE TABLE thread_sections (\n    id TEXT PRIMARY KEY,\n    name TEXT NOT NULL\n, appearance TEXT)"
    ],
    [
      "table",
      "thread_spawn_edges",
      "thread_spawn_edges",
      "CREATE TABLE thread_spawn_edges (\n    parent_thread_id TEXT NOT NULL,\n    child_thread_id TEXT NOT NULL PRIMARY KEY,\n    status TEXT NOT NULL\n)"
    ],
    [
      "table",
      "threads",
      "threads",
      "CREATE TABLE threads (\n    id TEXT PRIMARY KEY,\n    rollout_path TEXT NOT NULL,\n    created_at INTEGER NOT NULL,\n    updated_at INTEGER NOT NULL,\n    source TEXT NOT NULL,\n    model_provider TEXT NOT NULL,\n    cwd TEXT NOT NULL,\n    title TEXT NOT NULL,\n    sandbox_policy TEXT NOT NULL,\n    approval_mode TEXT NOT NULL,\n    tokens_used INTEGER NOT NULL DEFAULT 0,\n    has_user_event INTEGER NOT NULL DEFAULT 0,\n    archived INTEGER NOT NULL DEFAULT 0,\n    archived_at INTEGER,\n    git_sha TEXT,\n    git_branch TEXT,\n    git_origin_url TEXT\n, cli_version TEXT NOT NULL DEFAULT '', first_user_message TEXT NOT NULL DEFAULT '', agent_nickname TEXT, agent_role TEXT, memory_mode TEXT NOT NULL DEFAULT 'enabled', model TEXT, reasoning_effort TEXT, agent_path TEXT, created_at_ms INTEGER, updated_at_ms INTEGER, thread_source TEXT, preview TEXT NOT NULL DEFAULT '', recency_at INTEGER NOT NULL DEFAULT 0, recency_at_ms INTEGER NOT NULL DEFAULT 0, history_mode TEXT NOT NULL DEFAULT 'legacy', name TEXT, is_pinned INTEGER NOT NULL DEFAULT 0, thread_section_id TEXT\n    REFERENCES thread_sections(id) ON DELETE SET NULL, section_position INTEGER, section_entered_at_ms INTEGER, project_id TEXT\n    REFERENCES projects(id) ON DELETE SET NULL, originator TEXT, daybreak_enabled BOOLEAN, creator_user_id TEXT, creator_account_id TEXT, attached_thread_parent_id TEXT)"
    ],
    [
      "trigger",
      "threads_created_at_ms_after_insert",
      "threads",
      "CREATE TRIGGER threads_created_at_ms_after_insert\nAFTER INSERT ON threads\nWHEN NEW.created_at_ms IS NULL\nBEGIN\n    UPDATE threads\n    SET created_at_ms = NEW.created_at * 1000\n    WHERE id = NEW.id;\nEND"
    ],
    [
      "trigger",
      "threads_created_at_ms_after_update",
      "threads",
      "CREATE TRIGGER threads_created_at_ms_after_update\nAFTER UPDATE OF created_at ON threads\nWHEN NEW.created_at != OLD.created_at\n AND NEW.created_at_ms IS OLD.created_at_ms\nBEGIN\n    UPDATE threads\n    SET created_at_ms = NEW.created_at * 1000\n    WHERE id = NEW.id;\nEND"
    ],
    [
      "trigger",
      "threads_recency_at_after_insert",
      "threads",
      "CREATE TRIGGER threads_recency_at_after_insert\nAFTER INSERT ON threads\nWHEN NEW.recency_at_ms = 0\nBEGIN\n    UPDATE threads\n    SET recency_at = NEW.updated_at,\n        recency_at_ms = COALESCE(NEW.updated_at_ms, NEW.updated_at * 1000)\n    WHERE id = NEW.id;\nEND"
    ],
    [
      "trigger",
      "threads_updated_at_ms_after_insert",
      "threads",
      "CREATE TRIGGER threads_updated_at_ms_after_insert\nAFTER INSERT ON threads\nWHEN NEW.updated_at_ms IS NULL\nBEGIN\n    UPDATE threads\n    SET updated_at_ms = NEW.updated_at * 1000\n    WHERE id = NEW.id;\nEND"
    ],
    [
      "trigger",
      "threads_updated_at_ms_after_update",
      "threads",
      "CREATE TRIGGER threads_updated_at_ms_after_update\nAFTER UPDATE OF updated_at ON threads\nWHEN NEW.updated_at != OLD.updated_at\n AND NEW.updated_at_ms IS OLD.updated_at_ms\nBEGIN\n    UPDATE threads\n    SET updated_at_ms = NEW.updated_at * 1000\n    WHERE id = NEW.id;\nEND"
    ]
  ],
  "thread_history_1.sqlite": [
    [
      "index",
      "idx_thread_items_by_turn_page",
      "thread_items",
      "CREATE INDEX idx_thread_items_by_turn_page\n    ON thread_items(thread_id, turn_id, rollout_ordinal)"
    ],
    [
      "index",
      "idx_thread_items_by_turn_updated_page",
      "thread_items",
      "CREATE INDEX idx_thread_items_by_turn_updated_page\n    ON thread_items(thread_id, turn_id, updated_at_ordinal)"
    ],
    [
      "index",
      "idx_thread_items_page",
      "thread_items",
      "CREATE UNIQUE INDEX idx_thread_items_page\n    ON thread_items(thread_id, rollout_ordinal)"
    ],
    [
      "index",
      "idx_thread_items_updated_page",
      "thread_items",
      "CREATE INDEX idx_thread_items_updated_page\n    ON thread_items(thread_id, updated_at_ordinal)"
    ],
    [
      "index",
      "idx_thread_items_user_messages",
      "thread_items",
      "CREATE INDEX idx_thread_items_user_messages\n    ON thread_items(thread_id, rollout_ordinal)\n    WHERE item_type = 'userMessage'"
    ],
    [
      "index",
      "idx_thread_realtime_items_boundary",
      "thread_realtime_items",
      "CREATE INDEX idx_thread_realtime_items_boundary\n    ON thread_realtime_items(thread_id, rollout_ordinal)\n    WHERE item_type IN ('realtime_session_started', 'realtime_session_closed')"
    ],
    [
      "index",
      "idx_thread_realtime_items_page",
      "thread_realtime_items",
      "CREATE UNIQUE INDEX idx_thread_realtime_items_page\n    ON thread_realtime_items(thread_id, rollout_ordinal)"
    ],
    [
      "index",
      "idx_thread_turns_end_page",
      "thread_turns",
      "CREATE INDEX idx_thread_turns_end_page\n    ON thread_turns(thread_id, rollout_end_ordinal, turn_id)\n    WHERE rollout_end_ordinal IS NOT NULL"
    ],
    [
      "index",
      "idx_thread_turns_page",
      "thread_turns",
      "CREATE UNIQUE INDEX idx_thread_turns_page\n    ON thread_turns(thread_id, rollout_ordinal)"
    ],
    [
      "index",
      "sqlite_autoindex__sqlx_migrations_1",
      "_sqlx_migrations",
      null
    ],
    [
      "index",
      "sqlite_autoindex_thread_history_projection_state_1",
      "thread_history_projection_state",
      null
    ],
    [
      "index",
      "sqlite_autoindex_thread_items_1",
      "thread_items",
      null
    ],
    [
      "index",
      "sqlite_autoindex_thread_realtime_items_1",
      "thread_realtime_items",
      null
    ],
    [
      "index",
      "sqlite_autoindex_thread_turns_1",
      "thread_turns",
      null
    ],
    [
      "table",
      "_sqlx_migrations",
      "_sqlx_migrations",
      "CREATE TABLE _sqlx_migrations (\n    version BIGINT PRIMARY KEY,\n    description TEXT NOT NULL,\n    installed_on TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,\n    success BOOLEAN NOT NULL,\n    checksum BLOB NOT NULL,\n    execution_time BIGINT NOT NULL\n)"
    ],
    [
      "table",
      "thread_history_projection_state",
      "thread_history_projection_state",
      "CREATE TABLE thread_history_projection_state (\n    thread_id TEXT PRIMARY KEY,\n    next_rollout_byte_offset INTEGER NOT NULL,\n    next_rollout_ordinal INTEGER NOT NULL\n)"
    ],
    [
      "table",
      "thread_items",
      "thread_items",
      "CREATE TABLE thread_items (\n    thread_id TEXT NOT NULL,\n    turn_id TEXT NOT NULL,\n    item_id TEXT NOT NULL,\n    rollout_ordinal INTEGER NOT NULL,\n    created_at_ms INTEGER NOT NULL,\n    item_json TEXT NOT NULL, item_type TEXT NOT NULL DEFAULT '', updated_at_ordinal INTEGER NOT NULL DEFAULT 0, started_at_ms INTEGER, completed_at_ms INTEGER,\n    PRIMARY KEY (thread_id, turn_id, item_id)\n)"
    ],
    [
      "table",
      "thread_realtime_items",
      "thread_realtime_items",
      "CREATE TABLE thread_realtime_items (\n    thread_id TEXT NOT NULL,\n    item_id TEXT NOT NULL,\n    rollout_ordinal INTEGER NOT NULL,\n    created_at_ms INTEGER NOT NULL,\n    item_type TEXT NOT NULL,\n    item_json TEXT NOT NULL,\n    PRIMARY KEY (thread_id, item_id)\n)"
    ],
    [
      "table",
      "thread_turns",
      "thread_turns",
      "CREATE TABLE thread_turns (\n    thread_id TEXT NOT NULL,\n    turn_id TEXT NOT NULL,\n    rollout_ordinal INTEGER NOT NULL,\n    status TEXT NOT NULL,\n    error_json TEXT,\n    started_at INTEGER,\n    completed_at INTEGER,\n    duration_ms INTEGER,\n    first_user_item_id TEXT,\n    final_agent_item_id TEXT, rollout_byte_offset INTEGER, rollout_end_ordinal INTEGER, rollout_end_byte_offset INTEGER, root_turn_id TEXT,\n    PRIMARY KEY (thread_id, turn_id)\n)"
    ],
    [
      "trigger",
      "thread_realtime_items_projection_cleanup",
      "thread_history_projection_state",
      "CREATE TRIGGER thread_realtime_items_projection_cleanup\n    AFTER DELETE ON thread_history_projection_state\nBEGIN\n    DELETE FROM thread_realtime_items WHERE thread_id = OLD.thread_id;\nEND"
    ]
  ],
  "queue_1.sqlite": [
    [
      "index",
      "queued_items_thread_order_idx",
      "queued_items",
      "CREATE UNIQUE INDEX queued_items_thread_order_idx\n    ON queued_items(thread_id, queue_order)"
    ],
    [
      "index",
      "sqlite_autoindex__sqlx_migrations_1",
      "_sqlx_migrations",
      null
    ],
    [
      "index",
      "sqlite_autoindex_queued_items_1",
      "queued_items",
      null
    ],
    [
      "index",
      "sqlite_autoindex_queued_thread_revisions_1",
      "queued_thread_revisions",
      null
    ],
    [
      "table",
      "_sqlx_migrations",
      "_sqlx_migrations",
      "CREATE TABLE _sqlx_migrations (\n    version BIGINT PRIMARY KEY,\n    description TEXT NOT NULL,\n    installed_on TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,\n    success BOOLEAN NOT NULL,\n    checksum BLOB NOT NULL,\n    execution_time BIGINT NOT NULL\n)"
    ],
    [
      "table",
      "queued_items",
      "queued_items",
      "CREATE TABLE queued_items (\n    id TEXT PRIMARY KEY NOT NULL,\n    thread_id TEXT NOT NULL,\n    payload_json TEXT NOT NULL,\n    queue_order INTEGER NOT NULL,\n    created_at_ms INTEGER NOT NULL,\n    updated_at_ms INTEGER NOT NULL\n)"
    ],
    [
      "table",
      "queued_thread_revisions",
      "queued_thread_revisions",
      "CREATE TABLE queued_thread_revisions (\n    revision INTEGER PRIMARY KEY AUTOINCREMENT,\n    thread_id TEXT NOT NULL UNIQUE\n)"
    ],
    [
      "table",
      "sqlite_sequence",
      "sqlite_sequence",
      "CREATE TABLE sqlite_sequence(name,seq)"
    ],
    [
      "trigger",
      "queued_items_revision_after_delete",
      "queued_items",
      "CREATE TRIGGER queued_items_revision_after_delete\nAFTER DELETE ON queued_items\nBEGIN\n    INSERT INTO queued_thread_revisions (thread_id)\n    VALUES (OLD.thread_id)\n    ON CONFLICT(thread_id) DO UPDATE\n    SET revision = (SELECT COALESCE(MAX(revision), 0) + 1 FROM queued_thread_revisions);\nEND"
    ],
    [
      "trigger",
      "queued_items_revision_after_insert",
      "queued_items",
      "CREATE TRIGGER queued_items_revision_after_insert\nAFTER INSERT ON queued_items\nBEGIN\n    INSERT INTO queued_thread_revisions (thread_id)\n    VALUES (NEW.thread_id)\n    ON CONFLICT(thread_id) DO UPDATE\n    SET revision = (SELECT COALESCE(MAX(revision), 0) + 1 FROM queued_thread_revisions);\nEND"
    ],
    [
      "trigger",
      "queued_items_revision_after_update",
      "queued_items",
      "CREATE TRIGGER queued_items_revision_after_update\nAFTER UPDATE ON queued_items\nBEGIN\n    INSERT INTO queued_thread_revisions (thread_id)\n    VALUES (NEW.thread_id)\n    ON CONFLICT(thread_id) DO UPDATE\n    SET revision = (SELECT COALESCE(MAX(revision), 0) + 1 FROM queued_thread_revisions);\nEND"
    ]
  ],
  "goals_1.sqlite": [
    [
      "index",
      "sqlite_autoindex__sqlx_migrations_1",
      "_sqlx_migrations",
      null
    ],
    [
      "index",
      "sqlite_autoindex_thread_goal_continuation_deferrals_1",
      "thread_goal_continuation_deferrals",
      null
    ],
    [
      "index",
      "sqlite_autoindex_thread_goals_1",
      "thread_goals",
      null
    ],
    [
      "table",
      "_sqlx_migrations",
      "_sqlx_migrations",
      "CREATE TABLE _sqlx_migrations (\n    version BIGINT PRIMARY KEY,\n    description TEXT NOT NULL,\n    installed_on TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,\n    success BOOLEAN NOT NULL,\n    checksum BLOB NOT NULL,\n    execution_time BIGINT NOT NULL\n)"
    ],
    [
      "table",
      "thread_goal_continuation_deferrals",
      "thread_goal_continuation_deferrals",
      "CREATE TABLE thread_goal_continuation_deferrals (\n    thread_id TEXT PRIMARY KEY NOT NULL REFERENCES thread_goals(thread_id) ON DELETE CASCADE\n)"
    ],
    [
      "table",
      "thread_goals",
      "thread_goals",
      "CREATE TABLE thread_goals (\n    thread_id TEXT PRIMARY KEY NOT NULL,\n    goal_id TEXT NOT NULL,\n    objective TEXT NOT NULL,\n    status TEXT NOT NULL CHECK(status IN (\n        'active',\n        'paused',\n        'blocked',\n        'usage_limited',\n        'budget_limited',\n        'complete'\n    )),\n    token_budget INTEGER,\n    tokens_used INTEGER NOT NULL DEFAULT 0,\n    time_used_seconds INTEGER NOT NULL DEFAULT 0,\n    created_at_ms INTEGER NOT NULL,\n    updated_at_ms INTEGER NOT NULL\n)"
    ]
  ],
  "memories_1.sqlite": [
    [
      "index",
      "idx_jobs_kind_status_retry_lease",
      "jobs",
      "CREATE INDEX idx_jobs_kind_status_retry_lease\n    ON jobs(kind, status, retry_at, lease_until)"
    ],
    [
      "index",
      "idx_stage1_outputs_source_updated_at",
      "stage1_outputs",
      "CREATE INDEX idx_stage1_outputs_source_updated_at\n    ON stage1_outputs(source_updated_at DESC, thread_id DESC)"
    ],
    [
      "index",
      "sqlite_autoindex__sqlx_migrations_1",
      "_sqlx_migrations",
      null
    ],
    [
      "index",
      "sqlite_autoindex_jobs_1",
      "jobs",
      null
    ],
    [
      "index",
      "sqlite_autoindex_stage1_outputs_1",
      "stage1_outputs",
      null
    ],
    [
      "table",
      "_sqlx_migrations",
      "_sqlx_migrations",
      "CREATE TABLE _sqlx_migrations (\n    version BIGINT PRIMARY KEY,\n    description TEXT NOT NULL,\n    installed_on TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,\n    success BOOLEAN NOT NULL,\n    checksum BLOB NOT NULL,\n    execution_time BIGINT NOT NULL\n)"
    ],
    [
      "table",
      "consolidation_progress",
      "consolidation_progress",
      "CREATE TABLE consolidation_progress (\n    singleton INTEGER PRIMARY KEY CHECK (singleton = 1),\n    max_thread_count INTEGER NOT NULL DEFAULT 0\n)"
    ],
    [
      "table",
      "jobs",
      "jobs",
      "CREATE TABLE jobs (\n    kind TEXT NOT NULL,\n    job_key TEXT NOT NULL,\n    status TEXT NOT NULL,\n    worker_id TEXT,\n    ownership_token TEXT,\n    started_at INTEGER,\n    finished_at INTEGER,\n    lease_until INTEGER,\n    retry_at INTEGER,\n    retry_remaining INTEGER NOT NULL,\n    last_error TEXT,\n    input_watermark INTEGER,\n    last_success_watermark INTEGER,\n    PRIMARY KEY (kind, job_key)\n)"
    ],
    [
      "table",
      "stage1_outputs",
      "stage1_outputs",
      "CREATE TABLE stage1_outputs (\n    thread_id TEXT PRIMARY KEY,\n    source_updated_at INTEGER NOT NULL,\n    raw_memory TEXT NOT NULL,\n    rollout_summary TEXT NOT NULL,\n    rollout_slug TEXT,\n    generated_at INTEGER NOT NULL,\n    usage_count INTEGER,\n    last_usage INTEGER,\n    selected_for_phase2 INTEGER NOT NULL DEFAULT 0,\n    selected_for_phase2_source_updated_at INTEGER\n)"
    ]
  ]
}
```


#!/usr/bin/env python3
"""Parse only fixed diagnostic projections; never relay untrusted log text."""
import json
from pathlib import Path
import sys

REVISION = '110d1f71a6fd8671cc9316f509d61ed56cf740b3'
MARKER = '{"notificationFixtureDiagnostic":'

def summarize(content, result):
    installed = guard = invalid = False
    errors = []
    records = 0
    for line in content.splitlines():
        start = line.find(MARKER)
        if start < 0:
            continue
        try:
            value = json.loads(line[start:])
            assert set(value) == {'notificationFixtureDiagnostic'}
            row = value['notificationFixtureDiagnostic']
            records += 1
            assert records <= 8
            if row == {'event': 'installed'}:
                installed = True
            elif row == {'event': 'guard_failed'}:
                guard = True
            else:
                assert set(row) == {'event', 'line', 'column', 'category'}
                assert row['event'] == 'error' and row['category'] in ('checkbox_state_unchanged', 'other')
                a, b = row['line'], row['column']
                assert (a is None and b is None) or (type(a) is int and 1 <= a <= 382 and type(b) is int and 1 <= b <= 4096)
                errors.append({'line': a, 'column': b, 'category': row['category']})
        except Exception:
            invalid = True
    located = [row for row in errors if row['line'] is not None]
    coverage = 'guard_failed' if guard else 'invalid_projection' if invalid else 'missing_active_marker' if not installed else \
        'active_with_fixture_location' if located else 'active_without_fixture_location' if errors else 'active_no_projected_errors'
    outcome = 'inconclusive'
    if installed and not guard and not invalid:
        outcome = 'checkbox_exception_located' if any(row['category'] == 'checkbox_state_unchanged' for row in located) else \
            'exception_located' if located else 'no_failure_reproduced' if result == 0 and not errors else 'inconclusive'
    return {'revision': REVISION, 'exitStatus': result, 'observerCoverage': coverage, 'diagnosticOutcome': outcome,
            'knownCheckboxObserved': any(row['category'] == 'checkbox_state_unchanged' for row in errors),
            'positions': errors[:7], 'productSourceChanged': False, 'physicalDisplayOrFocusClaim': False}

if __name__ == '__main__':
    try:
        result = int(sys.argv[2])
        assert 0 <= result <= 255
        with Path(sys.argv[1]).open() as log:
            content = log.read(2 * 1024 * 1024)
            assert not log.read(1)
        print(json.dumps(summarize(content, result), separators=(',', ':')))
    except Exception:
        print('{"observerCoverage":"parser_unavailable","diagnosticOutcome":"inconclusive"}')

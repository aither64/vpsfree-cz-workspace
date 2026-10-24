#!/usr/bin/env python3
"""One normal index GET, then published-progress reads; parent utility executes."""
import base64, datetime, json, os, pathlib, ssl, subprocess, sys, time, urllib.error, urllib.request
SLUG = '2026-10-20-dev-workspace-portal-improvements'
WORKSPACE = '/home/aither/workspace/ai/vpsfree.cz'
SESSION = pathlib.Path(WORKSPACE) / 'work' / SLUG
OUT = SESSION / 'verification/deployment-index-publication'
URL = 'https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/api/index-status'
WARNINGS = {'Some session status is unavailable.', 'Some repository status is unavailable.',
            'Some recent Codex activity is unavailable.',
            'Session status is temporarily unavailable; showing the last known state.'}
class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, *args, **kwargs): return None

def main():
    os.umask(0o077)
    assert ('DEV_SESSION_SLUG' in os.environ) == ('DEV_SESSION_WORKSPACE' in os.environ)
    assert os.environ.get('DEV_SESSION_SLUG', SLUG) == SLUG
    assert os.environ.get('DEV_SESSION_WORKSPACE', WORKSPACE) == WORKSPACE
    assert subprocess.check_output(['dev-session', 'current'], cwd=SESSION, text=True).strip() == SLUG
    OUT.mkdir(mode=0o700)  # Refuse existing attempt before credentials/demand; no retry.
    started = time.monotonic()
    result = {'state':'running', 'pid':os.getpid(), 'normalDemandCount':0, 'progressReadCount':0}
    def save(name):
        temporary = OUT / (name + '.tmp')
        temporary.write_text(json.dumps(result, indent=2) + '\n'); temporary.replace(OUT / name)
    save('status.json')
    stage = 'credential'
    try:
        try:
            password = subprocess.check_output(['ssh','-o','BatchMode=yes','-o','StrictHostKeyChecking=yes',
                '-o','IdentitiesOnly=yes','-o','ConnectTimeout=10','-i','/home/aither/.ssh/id_ed25519',
                'root@172.16.106.40','cat -- /var/lib/dev-workspaces/password/password'],
                text=True, stdin=subprocess.DEVNULL, stderr=subprocess.PIPE, timeout=15).strip()
        except Exception: raise RuntimeError('configured_credential_unavailable_via_explicit_ssh') from None
        stage = 'ca_trust'
        opener = urllib.request.build_opener(urllib.request.HTTPSHandler(context=ssl.create_default_context(
            cafile='/var/lib/dev-workspaces/public/ca.pem')), NoRedirect)
        auth = 'Basic ' + base64.b64encode(('aither:'+password).encode()).decode()
        demanded_at = datetime.datetime.now(datetime.timezone.utc)
        previous = None
        with (OUT / 'observations.jsonl').open('w', buffering=1) as log:
            for sample in range(32):  # One demand + at most31 progress reads.
                progress = sample > 0
                if sample > 1: time.sleep(1)
                stage = 'progress' if progress else 'normal_demand'
                result['progressReadCount' if progress else 'normalDemandCount'] += 1
                save('status.json')
                req = urllib.request.Request(URL + ('?progress=1' if progress else ''), headers={'Authorization':auth})
                with opener.open(req, timeout=10) as response:
                    body = response.read(2*1024*1024+1)
                    if len(body)>2*1024*1024: raise RuntimeError('response_exceeds_2_mib')
                    data = json.loads(body); rows = data.get('sessions') or []; warning = data.get('warning') or ''
                    item = {'observedAt':datetime.datetime.now(datetime.timezone.utc).isoformat(),
                        'elapsedSeconds':round(time.monotonic()-started,3), 'read':stage, 'httpStatus':response.status,
                        'loading':data.get('loading'), 'authoritative':data.get('authoritative'),
                        'generatedAt':data.get('generatedAt'), 'sessionCount':len(rows),
                        'operationCount':len(data.get('operations') or []), 'warningPresent':bool(warning),
                        'warning':warning if warning in WARNINGS or not warning else 'Unrecognized warning; raw text withheld',
                        'clusterNoticeCount':sum(bool(row.get('clusterNotice')) for row in rows),
                        'unknownWithoutNoticeCount':sum(row.get('runningClustersKnown') is not True and not row.get('clusterNotice') for row in rows)}
                log.write(json.dumps(item)+'\n'); result['lastObservation'] = item; save('status.json')
                generated = datetime.datetime.fromisoformat(item['generatedAt'].replace('Z','+00:00'))
                fresh = generated >= demanded_at
                if progress and fresh and warning:
                    result.update(state='warning', outcome='fresh_publication_has_warning', exitCode=2); break
                ready = progress and fresh and item['loading'] is False and item['authoritative'] is True and len(rows)>0 and not warning and item['unknownWithoutNoticeCount']==0
                if ready and previous == item['generatedAt']:
                    result.update(state='warning' if item['clusterNoticeCount'] else 'passed',
                        outcome='fresh_stable_publication_has_notices' if item['clusterNoticeCount'] else 'fresh_authoritative_publication_settled',
                        stableProgressSamples=2, exitCode=2 if item['clusterNoticeCount'] else 0); break
                previous = item['generatedAt'] if ready else None
            else: result.update(state='incomplete', outcome='31_progress_observations_exhausted_with_recorded_status', exitCode=3)
    except Exception as error:
        detail = {'stage':stage,'type':type(error).__name__}
        if isinstance(error, urllib.error.HTTPError): detail['httpStatus'] = error.code
        elif isinstance(error, urllib.error.URLError): detail['reasonType'] = type(error.reason).__name__
        elif isinstance(error, RuntimeError): detail['reason'] = str(error)
        result.update(state='failed', error=detail, exitCode=1)
    result.update(elapsedSeconds=round(time.monotonic()-started,3), finishedAt=datetime.datetime.now(datetime.timezone.utc).isoformat())
    save('status.json'); save('result.json'); print(json.dumps(result)); return result['exitCode']
if __name__ == '__main__': sys.exit(main())

import hashlib
import json
import pathlib
import subprocess

W = pathlib.Path('/home/aither/workspace/ai/vpsfree.cz')
S = W / 'work/2026-10-20-dev-workspace-portal-improvements'
T = W / 'worktrees/2026-10-20-dev-workspace-portal-improvements'
B = T / 'dev-workspace'
OLD = '0c0dd2d22ce4e03c22a7bd0c471267deb6ee3a2a'
BASE = 'bc40cdda2d28c9732396db4163daa244bba79acb'
FINAL = '483d4e7eafeda974dfe19de45687795562072d7d'
HOST = 'f8f2938b4e2cfd6e5b82657d08f014357817808f'
A = 'ea64ef57fdd2ff5fd60715b62f2d1696bc0133e5'


def git(*args, repo=B):
    return subprocess.check_output(['git', '-C', str(repo), *args])


def source(rev, path, repo=B):
    return git('show', rev + ':' + path, repo=repo)


def digest(data):
    return hashlib.sha256(data).hexdigest()


def receipt(path):
    return {'path': path, 'sha256': digest((S / path).read_bytes())}


def exact(path, revisions=(BASE, FINAL), repo=B):
    values = [source(rev, path, repo) for rev in revisions]
    modes = [git('ls-tree', rev, '--', path, repo=repo).decode().split('\t')[0]
             for rev in revisions]
    assert len(set(values)) == len(set(modes)) == 1, path
    return {'path': path, 'revisions': list(revisions), 'modeBlob': modes[-1],
            'sha256': digest(values[-1]), 'equal': True}


blocks = []


def block(name, path, before, after, extraction, transformations=()):
    assert before == after, name
    blocks.append({'name': name, 'path': path, 'sha256': digest(before),
                   'bytes': len(before), 'equal': True, 'extraction': extraction,
                   'explicitTransformations': list(transformations)})


path = 'portal/internal/web/static/app.js'
a, b = (source(rev, path).decode() for rev in (BASE, FINAL))
extra = '    file: (path, options) => request(`${apiPath(slug, "file")}?artifact=${encodeURIComponent(path)}`, options),\n'
assert b.count(extra) == 1 and extra not in a
start = '  const artifactList ='
block('request_client_helpers_and_read_scope_before_Files', path,
      a[:a.index(start)].encode(), b[:b.index(start)].replace(extra, '').encode(),
      'BOF to const artifactList (excluded)', [{'finalOnlyRemove': extra}])
start = '  const pageReads ='
x, y = a[a.index(start):], b[b.index(start):]
old_pause = 'pageReads.pause(); filesReads.pause(); clearTimeout(detailsTimer); detailsTimer = null;'
new_pause = 'pageReads.pause(); pauseFiles(); clearTimeout(detailsTimer); detailsTimer = null;'
common_pause = 'pageReads.pause(); clearTimeout(detailsTimer); detailsTimer = null;'
old_resume = 'pageReads.resume(); filesReads.resume();\n    if (!filesLoaded && document.getElementById("files")?.classList.contains("active")) void refreshFiles();'
new_resume = 'pageReads.resume(); resumeFiles();'
for text, match in ((x, old_pause), (y, new_pause), (x, old_resume), (y, new_resume)):
    assert text.count(match) == 1
block('page_conversation_pending_history_send_scheduler_outside_Files', path,
      x.replace(old_pause, common_pause).replace(old_resume, 'pageReads.resume();').encode(),
      y.replace(new_pause, common_pause).replace(new_resume, 'pageReads.resume();').encode(),
      'const pageReads through EOF',
      [{'base': old_pause, 'final': new_pause, 'compareAs': common_pause},
       {'base': old_resume, 'final': new_resume, 'compareAs': 'pageReads.resume();'}])
for name, start, end in (
        ('createReadScope', '  const createReadScope =', '\n  const '),
        ('refreshPending_and_later_conversation_pause_resume', '  const refreshPending =', None)):
    def extract(text):
        i = text.index(start)
        return text[i:text.index(end, i + len(start))] if end else text[i:]
    block(name, path, extract(a).encode(), extract(b).encode(), {'start': start, 'end': end or 'EOF'})

path = 'portal/internal/web/server.go'
a, b = (source(rev, path).decode() for rev in (BASE, FINAL))
extra = '\t"mime"\n'
assert b.count(extra) == 1 and extra not in a
block('server_before_Files_adapters_including_notification_routes', path,
      a[:a.index('func artifactContentType(')].encode(),
      b[:b.index('func (s *Server) serveArtifactFile(')].replace(extra, '').encode(),
      {'baseEnd': 'func artifactContentType(', 'finalEnd': 'func (s *Server) serveArtifactFile('},
      [{'finalOnlyRemove': extra}])
start = 'func (s *Server) sessionAPI('
block('server_session_API_resolver_native_pending_settings', path,
      a[a.index(start):].encode(), b[b.index(start):].encode(), {'start': start, 'end': 'EOF'})
path = 'portal/internal/web/server_test.go'
a, b = (source(rev, path) for rev in (BASE, FINAL))
start = b'func writeWebRuntimeAuthority('
block('shared_native_notification_fixture_helpers', path, a[a.index(start):], b[b.index(start):],
      'writeWebRuntimeAuthority through EOF; includes browserContractCodex, prepareInteractiveConversation, newTestServer')
path = 'portal/internal/web/templates/session.html'
a, b = (source(rev, path).decode() for rev in (BASE, FINAL))
start = '      <section id="files"'
end = '    </section>\n    {{end}}\n  </main>'
def nonfiles(text):
    i = text.index(start)
    return text[:i] + text[text.index(end, i):]
x = nonfiles(a).replace('/static/style.css?v=21', '/static/style.css?v=CACHE').replace('/static/app.js?v=55', '/static/app.js?v=CACHE')
y = nonfiles(b).replace('/static/style.css?v=22', '/static/style.css?v=CACHE').replace('/static/app.js?v=56', '/static/app.js?v=CACHE')
block('session_non_Files_template_composer_notification_script_refs', path, x.encode(), y.encode(),
      {'excludeFrom': start, 'excludeUntil': end}, ['style v21/v22 and app v55/v56 normalized to CACHE'])
path = 'portal/internal/web/templates/index.html'
a = source(BASE, path).replace(b'/static/app.js?v=55', b'/static/app.js?v=CACHE')
b = source(FINAL, path).replace(b'/static/app.js?v=56', b'/static/app.js?v=CACHE')
block('index_template_notification_hooks', path, a, b, 'whole file', ['app v55/v56 normalized to CACHE'])

notification_paths = [
    'notifications.go', 'notifications_store.go', 'notifications_transport.go',
    'notifications_test.go', 'notifications_browser_test.go', 'notifications_browser_test.cjs',
    'static/browser-notifications.js', 'static/notification-worker.js',
    'static/session-attention-store.js', 'static/session-attention.js',
    'templates/notifications.html', 'attention.go']
notification = [exact('portal/internal/web/' + p, (OLD, BASE, FINAL)) for p in notification_paths]
native_paths = [p for p in git('ls-tree', '-r', '--name-only', FINAL, 'portal/internal/web').decode().splitlines()
                if pathlib.PurePosixPath(p).name.startswith('firefox_tabs')]
native = [exact(p) for p in native_paths]
dependencies = [exact(p) for p in [
    'flake.nix', 'flake.lock', 'portal/go.mod', 'portal/go.sum', 'nix/workspace-portal.nix',
    'nix/codex-package.nix', 'nix/tests/codex-package.nix', 'portal/internal/session/runtime-contract.json',
    'test/fixtures/runtime-authority-corpus.json', 'portal/internal/web/pending_revision.go',
    'portal/internal/web/member_conversation.go', 'portal/internal/web/read_diagnostics.go',
    'portal/internal/web/codex_providers.go', 'portal/internal/web/codex_limits.go',
    'portal/internal/web/coordination.go', 'portal/internal/web/static/codex-providers.js',
    'portal/internal/web/static/coordination.js']]
subtrees = []
for path in ['portal/internal/workspacecodex', 'portal/internal/codexproviders',
             'portal/internal/teamruntime', 'portal/internal/agentteams', 'portal/internal/userstate']:
    trees = [git('rev-parse', rev + ':' + path).decode().strip() for rev in (BASE, FINAL)]
    assert trees[0] == trees[1]
    subtrees.append({'path': path, 'tree': trees[0], 'equal': True})
host_original = json.loads((S / 'verification/final-coordinated-ea64ef57/final-host-contract-proof.json').read_text())
host = []
for path in host_original['runtimeHostBlobTreesEqual']:
    if path == 'nix/systemd':
        revisions = [HOST, OLD, BASE, FINAL]
        trees = [git('rev-parse', rev + ':' + path).decode().strip() for rev in revisions]
        assert len(set(trees)) == 1
        host.append({'path': path, 'revisions': revisions, 'tree': trees[0], 'equal': True})
    else:
        host.append(exact(path, (HOST, OLD, BASE, FINAL)))
configuration = [exact(path, ('450e1ff538c1e94c1ec74f57b50fbe2efb31502b',
                            '354e944f9dcf071e4878f0a0bbf2e71f52693801'), T / 'vpsfree-cz-configuration')
                 for path in host_original['configurationHostFilesEqual']]
assert git('rev-parse', 'HEAD', repo=T / 'codex-web').decode().strip() == A
lockedA = [v['locked'] for v in json.loads(source(FINAL, 'flake.lock'))['nodes'].values()
           if v.get('locked', {}).get('repo') == 'codex-web']
assert len(lockedA) == 1 and lockedA[0]['rev'] == A
catalog = exact('codex/ephemeral_luna_models.json', (A, A), T / 'codex-web')
old_candidate = json.loads((S / 'verification/targeted-read-budget-successor/activation/candidate.json').read_text())
candidate = json.loads((S / 'verification/files-final-composition/activation/candidate.json').read_text())
tools = {k: old_candidate[k] for k in ['system', 'systemConfiguration', 'systemRuntime', 'native', 'node', 'nodePath', 'browsers']}
assert all(candidate[k] == v for k, v in tools.items())
historical = [receipt(p) for p in [
    'verification/targeted-read-budget-successor/B-exercised-source-reuse-proof.json',
    'verification/targeted-read-budget-successor/actual-read-budget-evidence.json',
    'verification/targeted-read-budget-successor/component-evidence.json',
    'verification/targeted-read-budget-successor/retained-evidence.json',
    'verification/final-coordinated-ea64ef57/final-host-contract-proof.json',
    'verification/final-coordinated-ea64ef57/verification-watcher/notifications.log',
    'verification/final-coordinated-ea64ef57/verification-watcher/operation-result.json',
    'verification/two-tab-parent/watcher/operation-result.json',
    'verification/two-tab-parent/watcher/read-budget.log', 'verification/two-tab-parent/review.md']]
runtime = json.loads((S / 'verification/files-runtime/operation-result.json').read_text())
assert runtime['testedHead'] == FINAL and runtime['exitCode'] == 0
ci = json.loads((S / 'verification/files-parent-inventory/B-final-ci.json').read_text())
assert ci['headSha'] == FINAL and ci['conclusion'] == 'success'
frontend = json.loads((S / 'verification/files-inline-frontend/commit-proof.json').read_text())
tree = git('rev-parse', FINAL + '^{tree}').decode().strip()
assert frontend['tree'] == tree
changed = git('diff', '--name-only', BASE, FINAL).decode().splitlines()
assert len(changed) == 31
result = {
    'schema': 1, 'scope': 'finite source provenance; no tests/probes/network/build or source/Git mutations',
    'originalB': OLD, 'deployedB': BASE, 'finalB': FINAL, 'finalTree': tree,
    'changedPathCount': 31, 'changedPaths': changed, 'wholeApplicationEquivalent': False,
    'retainedHistoricalReceipts': historical,
    'notifications': {'state': 'original 0c0 disposable actual-browser PASS retained, exact exercised implementation/fixture/dependency source reused',
                      'files': notification, 'notClaimed': ['new final-B run', 'live provider or OS display performance']},
    'nativeTwoTab': {'state': 'original bc40 TestFirefoxReadBudget PASS retained with finite source/dependency binding',
                     'fixtureFiles': native, 'scope': 'two Firefox tabs, native visibility/read counts, one SSE, pending freshness/question/retry; zero sends/dispatches/journal entries',
                     'notClaimed': ['new final-B execution', '50-tab acceptance', 'durable send/lost-response receipt acceptance']},
    'unchangedExtractedBlocks': blocks, 'unchangedDependencies': dependencies, 'unchangedSubtrees': subtrees,
    'A': {'head': A, 'tree': git('rev-parse', A + '^{tree}', repo=T / 'codex-web').decode().strip(),
          'lockedByB': lockedA[0], 'catalog': catalog, 'priorResultsRetained': True},
    'hostProfileOnly': {'scope': 'source prerequisites only, no live-state or activation assertion',
                        'BContracts': host, 'configurationContracts': configuration, 'retainedSystemAndToolPaths': tools,
                        'provenance': 'Extend retained jwnd/config450/Bf8 source proof through 0c0/bc40/final; profile change is separate from system activation.',
                        'operationalHelperBinding': 'imp1 separately owns; not certified here'},
    'currentPassedEvidence': {
        'FilesRuntime': {'sourceB': FINAL, 'exitCode': 0, 'browser': 'PASS10.92s', 'archiveRevive': 'PASS3.22s active/archived/revived',
                         'receipts': [receipt('verification/files-runtime/' + p) for p in ['operation-result.json', 'browser.log', 'lifecycle.log']],
                         'preservedLauncherFailureNote': receipt('verification/files-runtime/result.md'),
                         'caveat': 'result.md describes initial launcher failure, not subsequent exit0 result; retained unchanged'},
        'Files18Cases': {'sourceB': frontend['head'], 'tree': frontend['tree'], 'finalTreeEqual': True,
                         'result': '18 cases PASS before history projection; original identity retained',
                         'receipts': [receipt('verification/files-inline-frontend/' + p) for p in ['quick-final.log', 'commit-proof.json']]},
        'CI': {'sourceB': FINAL, 'result': ci['conclusion'], 'jobs': {j['name']: j['conclusion'] for j in ci['jobs']},
               'receipt': receipt('verification/files-parent-inventory/B-final-ci.json')}},
    'limitations': [
        'No whole-app or derivation equivalence: Files readers/rendering/templates/style and CLI behavior changed.',
        'Non-Files comparisons explicitly exclude Files body/client method and normalize only named Files lifecycle hooks/cache refs; changed behavior relies on current Files evidence.',
        'style.css diff changes only Files/tree/source-preview selectors; no claim whole stylesheet bytes equal.',
        'Question shared fixture adds passive Files inputs; no unchanged whole TestQuestionBrowser setup claim.',
        'Read-cycle CJS adds pauseFiles/resumeFiles stubs; historical107cases remain historical, not a final-head rerun.',
        'Native50 withdrawn/unverified; retained lost-response durable-receipt failure is not cured or relabeled.',
        'No live health/activation/system links/roots/provider permission/subscription observation performed.']}
out = S / 'verification/files-final-composition/final-evidence-reuse.json'
assert not out.exists()
out.write_text(json.dumps(result, indent=2) + '\n')
print('Wrote', out, 'bytes', out.stat().st_size, 'exact blocks', len(blocks))

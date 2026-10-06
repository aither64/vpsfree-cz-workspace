from pathlib import Path
import urllib.request, ssl, base64, hashlib
root=Path('/home/aither/workspace/ai/vpsfree.cz')
slug='2026-10-04-upload-display-limits'
base='https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz'
context=ssl.create_default_context(cafile='/var/lib/dev-workspaces/public/ca.pem')
opener=urllib.request.build_opener(urllib.request.ProxyHandler({}),urllib.request.HTTPSHandler(context=context))
password=Path('/var/lib/dev-workspaces/password/password').read_text().strip()
auth='Basic '+base64.b64encode(('aither:'+password).encode()).decode()
def read(path):
    request=urllib.request.Request(base+path,headers={'Authorization':auth,'Cache-Control':'no-cache'})
    with opener.open(request,timeout=30) as response:
        assert response.status==200
        assert response.url==base+path
        return response.read()
runtime=root/'worktrees'/slug/'dev-workspace/portal/internal/web/static'
provider=root/'worktrees'/slug/'codex-web/conversation/assets'
for url,expected in [('/static/style.css?v=4',runtime/'style.css'),('/static/app.js?v=22',runtime/'app.js'),('/static/preparation.js?v=3',runtime/'preparation.js'),('/codex/assets/conversation.js?v=12',provider/'conversation.js'),('/codex/assets/uploads.js?v=4',provider/'uploads.js'),('/codex/assets/uploads.css?v=3',provider/'uploads.css')]:
    data=read(url)
    assert data==expected.read_bytes(), f'asset mismatch: {url}'
    print(url,hashlib.sha256(data).hexdigest(),'matches reviewed source')
html=read('/')
for url in [b'/static/style.css?v=4',b'/static/app.js?v=22',b'/codex/assets/uploads.css?v=3']:
    assert url in html
print('Authenticated TLS and current index cache versions passed; no page scripts or upload API executed.')

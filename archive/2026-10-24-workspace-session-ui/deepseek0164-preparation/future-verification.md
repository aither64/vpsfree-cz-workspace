# Prepared verification; not executed

Run only after the parent supplies reviewed final system, assembled Codex and
Home Manager wrapper identities and authorizes the real provider check. The
system's assembly/helper/copy/closure checks and normal rollout prerequisites
are separate parent gates. No placeholder below is an accepted output path.

## Final output and installed wrapper identity

Parent supplies these exact absolute paths from retained build/deployment
receipts, without discovering or evaluating another candidate here:

```sh
: "${DEEPSEEK_REVIEWED_SYSTEM:?exact final system output required}"
: "${DEEPSEEK_REVIEWED_ASSEMBLED_CODEX:?exact assembled Codex output required}"
: "${DEEPSEEK_REVIEWED_WRAPPER:?exact store wrapper /bin/codex-ds required}"
: "${DEEPSEEK_INSTALLED_WRAPPER:?Home Manager installed wrapper path required}"

test "$(readlink -f /run/current-system)" = "$DEEPSEEK_REVIEWED_SYSTEM"
test "$(readlink -f "$DEEPSEEK_INSTALLED_WRAPPER")" = "$DEEPSEEK_REVIEWED_WRAPPER"
test "$(readlink -f "$DEEPSEEK_REVIEWED_SYSTEM/sw/bin/codex")" = \
  "$(readlink -f "$DEEPSEEK_REVIEWED_ASSEMBLED_CODEX/bin/codex")"
rg -n -F -- "exec $DEEPSEEK_REVIEWED_ASSEMBLED_CODEX/bin/codex -p ds \"\$@\"" \
  "$DEEPSEEK_REVIEWED_WRAPPER"
printf '%s  %s\n' \
  d2af1cd0ea4187d413c237e80204e94ffcd5c7d8142840a662156b89750f54ae \
  "$DEEPSEEK_REVIEWED_ASSEMBLED_CODEX/libexec/codex/bin/codex" | sha256sum -c -
printf '%s  %s\n' \
  bce20f679495809f4fa6e48672b6dcbab84b6adff5251890b6e6a21eddb9c12f \
  /etc/codex/deepseek-models.json | sha256sum -c -
```

Retain resolved paths, wrapper hash/content and native/manifest/helper/closure
receipts. Inspect the wrapper's complete public text to confirm it still has
the reviewed key handling and exec target. Do not execute it during identity
checking: its hardcoded key-file read overrides an injected environment key.
The separate final package/actual-daemon proof remains required. Neither this
identity check nor `--help` establishes profile compatibility.

## One isolated real provider request

Use a fresh parent-owned watcher when the real request is authorized. The
parent supplies `DEEPSEEK_PROBE_EVIDENCE` as a private directory for this one
attempt and securely injects `DEEPSEEK_API_KEY`; secret acquisition is outside
this recipe. Never place its value in arguments, source, logs or receipts.
Do not read/copy production OpenAI auth or the production DeepSeek key file.
Do not force an OpenAI login method.

Run from the frozen evidence directory. This copies only the public source
profile already validated here, preserves all nine values, and uses the
catalog at its unchanged managed absolute path after the hash gate above.
The selected profile has no per-user base config or auth file in this home.
Codex may still load system/package configuration layers; strict-config
runtime failure must be reported, not bypassed.

```sh
/nix/store/5a0h3d6488628sh6w1ccqk8dizvmp8ji-python3-3.13.15-env/bin/python3 - <<'PY'
import hashlib
import os
from pathlib import Path
import subprocess
import tempfile

os.umask(0o077)
system = Path(os.environ['DEEPSEEK_REVIEWED_SYSTEM'])
assembled = Path(os.environ['DEEPSEEK_REVIEWED_ASSEMBLED_CODEX'])
output_parent = Path(os.environ['DEEPSEEK_PROBE_EVIDENCE'])
assert str(system).startswith('/nix/store/') and system.is_dir()
assert str(assembled).startswith('/nix/store/') and assembled.is_dir()
assert output_parent.is_absolute() and output_parent.is_dir()
assert output_parent.stat().st_mode & 0o077 == 0
assert Path('/run/current-system').resolve() == system
native = assembled / 'libexec/codex/bin/codex'
assert hashlib.sha256(native.read_bytes()).hexdigest() == 'd2af1cd0ea4187d413c237e80204e94ffcd5c7d8142840a662156b89750f54ae'
catalog = Path('/etc/codex/deepseek-models.json')
assert hashlib.sha256(catalog.read_bytes()).hexdigest() == 'bce20f679495809f4fa6e48672b6dcbab84b6adff5251890b6e6a21eddb9c12f'
profile = Path('ds.config.toml').read_bytes()
assert hashlib.sha256(profile).hexdigest() == '2f56fd540dd93ccef16c7963dba59fb2e452af5a9ec4f78c2510e743d70374e3'
key = os.environ['DEEPSEEK_API_KEY']  # Supplied securely for this later authorized run.
assert key
probe = Path(tempfile.mkdtemp(prefix='isolated-deepseek-', dir=output_parent))
for name in ('home', 'codex-home', 'work', 'tmp', 'config', 'cache', 'state'):
    (probe / name).mkdir(mode=0o700)
(probe / 'codex-home/ds.config.toml').write_bytes(profile)
env = {
    'HOME': str(probe / 'home'),
    'CODEX_HOME': str(probe / 'codex-home'),
    'XDG_CONFIG_HOME': str(probe / 'config'),
    'XDG_CACHE_HOME': str(probe / 'cache'),
    'XDG_STATE_HOME': str(probe / 'state'),
    'TMPDIR': str(probe / 'tmp'),
    'PATH': f'{assembled}/bin:{system}/sw/bin',
    'LANG': 'C.UTF-8',
    'DEEPSEEK_API_KEY': key,
}
command = [str(assembled / 'bin/codex'), '-p', 'ds', '--strict-config',
           '--ask-for-approval', 'never', 'exec', '--ephemeral',
           '--sandbox', 'read-only', '--skip-git-repo-check',
           '--output-last-message', str(probe / 'last-message.txt'),
           'Reply only CODEX_UPDATE_OK. Do not call tools.']
print(f'Private attempt evidence: {probe}', flush=True)
with (probe / 'provider.log').open('xb') as log:
    result = subprocess.run(command, cwd=probe / 'work', env=env,
                            stdin=subprocess.DEVNULL, stdout=log,
                            stderr=subprocess.STDOUT, check=False)
(probe / 'provider.exit').write_text(str(result.returncode) + '\n')
assert result.returncode == 0, 'Provider execution failed; retain evidence and report.'
assert (probe / 'last-message.txt').read_text().strip() == 'CODEX_UPDATE_OK'
print('PASS: one isolated ds strict-config provider request.')
PY
```

This request consumes provider usage. It executes the same assembled launcher
selected by the separately verified wrapper and exercises the complete profile;
it does not execute the wrapper's production secret reader. The no-tools prompt
is model guidance, not a tool-isolation guarantee. Parent watcher owns bounded
monitoring and any process/daemon reconciliation; a failure or timeout is not
permission to retry, deploy, downgrade or use a production home. Retain private
attempt state/logs for the parent and summarize without secret values.

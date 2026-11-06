# Fresh verification utility operation — batch 1

Read dev-session-monitor SKILL.md at
/home/aither/.local/state/dev-workspaces/codex-homes/vpsfree-cz/skills/dev-session-monitor/SKILL.md.
You only execute/monitor this exact batch; no edits, diagnosis, retries, dependency
changes, deployment, acceptance decisions or nested agents. Local logs/result
artifacts below are allowed. Keep ownership of your operation/tool handle until
all command/VM effects are accounted for. Never run lifecycle/cleanup/claims.

Policy: pinned/selected catalog digest
495ef6620926420612ee4988e69d03a4e975e41734a1a5e3208db65fcd731db7,
utilities.verification_watcher gpt-6-luna/low, operation lifetime, full_access.
Native config is
/nix/store/0q7rc75dh4mjrxpb37m1hchfwcbmpa7a-dev-workspace-0.2.0/share/dev-workspace/agent-teams/utilities/verification_watcher-low.toml.
Runtime policy danger-full-access, approval never (inherited full-access executor
or explicit equivalent). Verify these settings before treating launch as ready.

Working directory for every command:
/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-01-mx2-nixos-migration/vpsfree-cz-configuration
Session identity: 2026-11-01-mx2-nixos-migration,
workspace /home/aither/workspace/ai/vpsfree.cz.
First verify dev-session current/env binding, clean source HEAD exactly
53d1310dd1be1c35ea83317a620ce9f6a7fae227 and flake.lock SHA256
505f6c89e18972827beecc29a0c7c85e1df2576ed4074205501167a3dd6f326a.
If identity/source differs, report incomplete without repair or execution.
Independent final review completed, Important R1 and Advisory R2 narrowly fixed
and directly accepted by lead. Long execution is now authorized; no production
machine or default integration action is authorized.

Run the following command argv arrays in order, once each. Do NOT include any
punctuation beyond the literal arguments. Stop on the first nonzero result.

1. ["nix", "build", "--no-link", "-L", ".#checks.x86_64-linux.mx2"]
2. ["nix", "develop", "--no-write-lock-file", "-c", "confctl", "build", "--yes", "cz.vpsfree/containers/mx2"]
3. ["nix", "develop", "--no-write-lock-file", "-c", "confctl", "build", "--yes", "cz.vpsfree/containers/brq/int.ns1"]
4. ["nix", "develop", "--no-write-lock-file", "-c", "confctl", "build", "--yes", "cz.vpsfree/containers/prg/int.ns1"]
5. ["nix", "develop", "--no-write-lock-file", "-c", "confctl", "build", "--yes", "cz.vpsfree/containers/prg/int.mon1"]
6. ["nix", "develop", "--no-write-lock-file", "-c", "confctl", "build", "--yes", "cz.vpsfree/containers/prg/int.mon2"]

Complete stdout/stderr per command under absolute session directory
/home/aither/workspace/ai/vpsfree.cz/work/2026-11-01-mx2-nixos-migration:
verification-1-vm.log, verification-1-build-mx2.log,
verification-1-build-brq-int-ns1.log, verification-1-build-prg-int-ns1.log,
verification-1-build-prg-int-mon1.log, verification-1-build-prg-int-mon2.log.
Preserve exact exit status and duration. Result summary verification-run-1.md.
Use a cancellable owned command/process handle (TTY if needed); bounded log
reads/normal blocking waits <=60s, no busy polling. Parent will not poll your logs.
Send progress when substitution/build preparation becomes VM runtime and at
stage completion, and immediately on failure/escalation.

Expected check drv:
/nix/store/4xlkdsfhvjgm07za5gdyyn0ialfc6np4-vm-test-run-mx2.drv
Expected check output:
/nix/store/fd5wgwclsmlpkxwailkbwnyx68m08j8d-vm-test-run-mx2
Expected mx2 system drv:
/nix/store/40sp2bas7rr2609lccpw3iq3b9kdyc7d-nixos-system-mx2-26.05.20261026.718f670.drv
Expected mx2 system output:
/nix/store/rq91giv8lrlgsj26h7dv7cv9c5sr5w5l-nixos-system-mx2-26.05.20261026.718f670
Verify expected outputs exist after the corresponding successful command. Retain
native confctl generation/result identities for exact built names where its
normal metadata/log supplies them; don't invent output paths or investigate.

The check uses at most three isolated VMs. Test runtime has a 30-minute ceiling,
separate from substitution/build preparation (target runtime under15min). Do not
invent a silence timeout for preparation; report a concrete overrun/stall signal.
Authorized cancellation: this exact owned batch only if test runtime exceeds its
30-minute ceiling, unexpected local Linux kernel compilation begins, evidence of
external-network escape appears, or native test reports repeated boot failure.
Stop/cancel only your owned command via its native handle, preserve evidence and
reconcile remaining builder/VM effects before returning; don't kill unrelated Nix
builds or processes. Downloading a substituted kernel is fine; local kernel
compilation is an escalation. First assertion/command failure stops the batch;
let the native driver finish/shut down its VMs and report raw evidence, no retry.
A derivation called dry-activate being built is not deployment; never invoke it.
If a failed build needs its native log, one read-only nix log of the exact failed
derivation may be saved; don't rerun the build. Include bounded failure excerpt,
log/artifact paths and still-running-operation status. Return to parent promptly.

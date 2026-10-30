# Provider-independent retained recovery

Both reported sessions positively verify all eight retained subjects, then fail
with `a retained active conversation is absent from archive discovery`.
Read-only native probes return zero rows with the ordinary query and all eight
rows with `modelProviders: []`. The native database records `codex-lb` for these
threads. Loaded discovery is empty after reboot. The project-filter hypothesis
was disproved: the all-provider query includes project members without separate
project selectors.

Add an optional ModelProviders slice to codex-web's ThreadListOptions. Nil keeps
the existing native default; an explicit empty slice requests all providers.
Retained active discovery in dev-workspace opts into all providers. Its exact
root/member/project/CWD checks, pagination, loaded-thread union and submission
proofs remain unchanged. No thread loading, history rewrite, submission replay,
state schema or migration is needed. The generic library owns request encoding;
the runtime owns the policy of provider-independent retained identity.

Add wire-level option coverage and a recovery-discovery regression in which
saved threads from another provider are visible only with the explicit filter
and no threads are loaded. Verify unknown extra identities still refuse. Keep
the change bounded; do not change default listing behavior for other consumers.
Update the runtime recovery guide with the provider-independence invariant.

Publish codex-web, pin it once in dev-workspace including Go module metadata,
publish the runtime, and select it once in the workspace and configuration.
Independent review covers the complete four-repository series and no-migration
conclusion. Run focused checks before review, relevant packaged checks and a
native restart fixture after review, then system/profile deployment under one
aitherdev machine claim. Preserve all unrelated composition inputs. No reboot
is required. Recover forward on activation failure.

After deployed health and retained observation pass, restore and explicitly
continue 2026-10-24-vpsadmin-haveapi-upgrade, 2026-10-30-linux-cve-review and
2026-10-30-oomd-abuse-policy as requested. Preserve their existing queues, goals,
teams and settings. Integrate verified feature heads into each affected master
under short repository claims, then release the machine claim.

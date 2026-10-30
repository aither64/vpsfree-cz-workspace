# Stage1 retained outcome and effects assessment

Read-only owner assessment after lead delivery. No CAS, retry, source edit,
cleanup, rollback, lock removal or automatic Git-window release performed.
Original raw utility events/logs/receipts remain unchanged.

## Result

Native reconstruction passed: isolated final `19562b6449f01ca4939d57f70ee59de8af13880f`,
tree `3e04ce2bd85f871c3f40f86db5668f30684100a4`. Shared feature/ref stays
`9bea27c93beb22d08c3be2eb481bce4ef57300a6`, index byte-exact/empty. CAS is NOT selected.
All eight message-only trees/patches/author records/messages independently
match, before the intentionally changed final owner. Nine ordinary pre-commit
and commit-msg runs passed, with width warnings described below.

## Exact owner mapping

| Owner | Original | Pure message-only successor | Same tree | Stable patch ID | Max message width |
| --- | --- | --- | --- | --- | --- |
| 1 | `274e826dae6d5b7230857174a25afa1f91ab4ffb` | `ae33b06b0264b2aabcb5af21bb47c029a6a3f091` | `9f11aceece3a979778ebfdf0e61421504d3898af` | `31aab0a785e9bbff6e9de7632a10c9bc6c21d3b7` | 74 |
| 2 | `c2c5a006b49730d8b72d103ff063a1e89bba1ee2` | `be4ec430d49395513a0c7188bffcd78f17cd4ae9` | `1b4af65d1134e32a4fe681245af560b920289bf9` | `2629ea932e8b3407095b9b446e822f20241273b9` | 72 |
| 3 | `405a802857093176883e0f173589b433756a9647` | `50a796f2824424252be177aedafb277b6f149073` | `29b00319a5aedaa44a56d60bc6d0b70083a8ac16` | `210e424eb5693b95f7088536f4e42a1b6374511e` | 78 |
| 4 | `87e6bd4a5f5a117be5885d7a1a15ab602dde91e0` | `247c091e6a48083099395e5e1f4847ef5a585be6` | `274e2524effff73896b1fb972c592954b01b31c2` | `9a828785d93261f1855cc0b29efbcddea05a59d6` | 76 |
| 5 | `595bafea97f31aab3c34438db3f64fca78a9e94b` | `a1c4dc932b953cc21fde47a2fc2e6f85bb03e8f8` | `ed46a15a29f43e50998d5e0cb781cf667d726783` | `e42c603f613a352430e00eab45ff9a1145b32eb6` | 76 |
| 6 | `4de50f0046052d377780a3be3a9aeec37ad86f6e` | `a2e4c097103eeeba8ae016571ffbe25316ceb10f` | `e5e074bad8c74a27eb3dc422e44cb8e08389a245` | `7396df143786ea41dcf2413c334229659c39be11` | 77 |
| 7 | `81235fe742c5e8382997a1cb0b09f983f22a0456` | `39b6f68f245d6ebddf40a5ffc8e2e9485a9a8a17` | `f2c5065769c36058fe6605993e39f598d9f721ff` | `4edf384c67746d71106b0fc896eb766beba8a643` | 75 |
| 8 | `9bea27c93beb22d08c3be2eb481bce4ef57300a6` | `db42571928c08debf2485485bec4c7e5ac92d641` | `04b33b688828b55c8d91deef51c49392de78495c` | `85d152089d4983e60ce3337a989c7edcb3ab00f4` | 76 |

Pure eight-owner checkpoint `db42571928c08debf2485485bec4c7e5ac92d641`,
tree `04b33b688828b55c8d91deef51c49392de78495c`, complete tree diff empty
against old9bea. All eight full-index binary patches equal retained old/new
patches byte-for-byte. Every original author/name/email/date is unchanged;
subjects/body prefixes preserved and exact selected files equal stored commit
bodies. All selected messages remain <=80columns.

Final `19562b6449f01ca4939d57f70ee59de8af13880f` replaces only pure owner8 and has
parent `39b6f68f245d6ebddf40a5ffc8e2e9485a9a8a17`. Exactly docs/os/testing.md
and hotplug-recorder.c differ from pure8;128insertions/34deletions, diffSHA256
`56f36d35c469b57480b10c704af89a40b47571510033ac270d62d5fec6c613dd`.
C SHA256 `4bf11e25f04d444b5af5ac4cc506ab566c13ba50d96e67bf2c72c5b774005b00`;
docs SHA256 `a5fddc497e44614a04478752b1b042e8c3848ef5c13506d77ced36798b8280bb`.
Both isolated/shared frozen file bytes match. Final series contains eight
logical commits, no extra repair/fixup owner.

## Exact Git effects and preservation

Dated local backup `refs/heads/backup/2026-10-23-ci-failure-analysis-pre-message-remediation-9bea27c93`
points exactly to old9bea. New detached worktree admin is `/home/aither/workspace/ai/vpsfree.cz/repos/vpsadminos.git/worktrees/vpsadminos-validation-messages`;
isolated tracked/untracked status clean. No shared branch/ref update occurred.
Shared original index equals the retained byte backup; its staged diff is
empty. Retained before/after shared byte/mode/link manifests are equal, and
current rehash of all 7643 preflight regular files plus complete
path/type/mode/link snapshot matches again. Source dirty paths remain only
the frozen C/docs; no peer byte restoration/mutation was needed.

## Hooks and warnings

All9 pre-commit and all9 commit-msg hook runs pass. TextWidth warns for
existing body lines over72 and the retained long subjects over60; independent
exact commit body checks remain <=80, as workspace/local repository requires.
These warnings were not bypassed or suppressed. No hook failure or source
rewrite is present; byte/patch/message equivalence confirms intended output.
Exact non-trace warning lines from immutable stream:

```text
Check text width..........................................[TextWidth] WARNING
Line 5 of commit message has > 72 characters
Line 9 of commit message has > 72 characters
Line 10 of commit message has > 72 characters
Check text width..........................................[TextWidth] WARNING
Line 3 of commit message has > 72 characters
Line 4 of commit message has > 72 characters
Line 5 of commit message has > 72 characters
Line 9 of commit message has > 72 characters
Line 10 of commit message has > 72 characters
Line 11 of commit message has > 72 characters
Line 14 of commit message has > 72 characters
Line 15 of commit message has > 72 characters
Check text width..........................................[TextWidth] WARNING
Line 6 of commit message has > 72 characters
Line 7 of commit message has > 72 characters
Line 11 of commit message has > 72 characters
Line 12 of commit message has > 72 characters
Line 13 of commit message has > 72 characters
Line 17 of commit message has > 72 characters
Line 19 of commit message has > 72 characters
Check text width..........................................[TextWidth] WARNING
Line 4 of commit message has > 72 characters
Line 5 of commit message has > 72 characters
Line 6 of commit message has > 72 characters
Check text width..........................................[TextWidth] WARNING
Line 3 of commit message has > 72 characters
Line 4 of commit message has > 72 characters
Line 7 of commit message has > 72 characters
Line 8 of commit message has > 72 characters
Line 9 of commit message has > 72 characters
Line 10 of commit message has > 72 characters
Line 14 of commit message has > 72 characters
Line 15 of commit message has > 72 characters
Check text width..........................................[TextWidth] WARNING
Commit message subject must be <= 60 characters
Line 3 of commit message has > 72 characters
Line 5 of commit message has > 72 characters
Check text width..........................................[TextWidth] WARNING
Commit message subject must be <= 60 characters
Line 3 of commit message has > 72 characters
Line 8 of commit message has > 72 characters
Line 9 of commit message has > 72 characters
Line 10 of commit message has > 72 characters
Line 13 of commit message has > 72 characters
Line 14 of commit message has > 72 characters
Check text width..........................................[TextWidth] WARNING
Commit message subject must be <= 60 characters
Line 3 of commit message has > 72 characters
Line 8 of commit message has > 72 characters
Line 9 of commit message has > 72 characters
Line 10 of commit message has > 72 characters
Line 13 of commit message has > 72 characters
Line 14 of commit message has > 72 characters
```

## Timing, stream and physical evidence

Native scope-command0/log-reader0; stream67201B. First-to-last batch xtrace
interval 44.139386s, largest adjacent trace gap 8.013136s. These are
retained wall-clock xtrace observations, not reconstructed monotonic timings
or proof of the promised5s watcher cadence. No cancellation is recorded.
Native timeout600s was not reached; no stream/observed-space tripwire fired.
Endpoint positive-root allocation charge 351571968B; accumulated
positive deltas over retained du samples 351571968B. Both are sampled
conservative shared-root charges, not exclusive ownership, peak or hard quota
proof. Full isolated checkout347021312B, scratch3981312B. Shared bare Git grew
446464B; evidence20480B; watch102400B; shared feature endpoint unchanged.
Retained observation minimum free 131523407872B, above40GiB.
Global df deltas are not attributed to this operation. Sources/objects plus
scratch/evidence are included as in the accepted launch contract; omitted
short-lived allocation/deletion and intermittent observations remain unknown.

## One selected independent owner reconciliation

Effect receipt [message-reconstruction-owner-effects.json](message-reconstruction-owner-effects.json),
`72a30b4a78b5e9b2545287060d432a1049a183a3f57d6cdab95dff6c148622ad`;
242397B, native0/
0.625995s. ALL 1520 enumerated processes were
inspected independently of prior membership, within target10s/outer30s,
20000procs/128FD-perPID/32768FDtotal/8192argv/1MiB receipt bounds.
Actual 4893 FD targets attempted; no process/deadline/totalFD/
argv truncation. Four FD directories reached128 and protected views/errors
are recorded. No positive readable canonical owned reference. One observer
ancestor selfmatch is explicitly excluded only by recorded observer birth.
No signal, path/name ownership inference or cleanup occurred.

The only retained fullstat row is watcher bootstrap parent PID1861399 birth
1209886701 (event6), now absent. It is not a historical Git-batch birth record;
missing operation births were not invented from ps lstart. Current exact
named scope is not-found/inactive, ControlGroup empty and its originally
named canonical cgroup absent. This supplements current effects closure;
it cannot recover the missing historical process observations.

Remaining qualification: protected cwd/root/exe views,684 FD-directory permission
denials,256 FD-target denials, four128FD caps, disappearing process paths and
non-atomic proc observations prevent complete privileged/all-FD/historical/
escaped-process absence proof. Current no-positive-readable-refs + named
scope/cgroup absence is bounded evidence, not a guard PASS. Lead decides
whether this closes the omission sufficiently and whether to select CAS.
Window is not automatically released.

## Retention

Original watch/scratch/isolated checkout, dated backup ref, pure checkpoint
objects/maps/patches, output roots and raw utility evidence remain intact.
No further scan/rebuild/rerun is needed or authorized by this assessment.
Portal: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-22-ci-failure-analysis/


# Three existing-draft updates completed

All three released updates completed in order, with exact remote readback and
a normal-hook one-file submission checkpoint before each subsequent write.

| CVE | Draft | Revision | Checkpoint |
| --- | --- | --- | --- |
| CVE-2026-74753 | 85 | 25 | `fb6575f8be054b0be86458304ecdc122b78c9c21` |
| CVE-2026-53260 | 112 | 14 | `8bdc4f87f3764059c7ad1c629d5de9fbf7a34f78` |
| CVE-2026-72069 | 113 | 14 | `cfef162049f632016c9e67bca0e400c58c8618d2` |

Released source: `0b2f060e61c5480ccd09e93d2ecbace39bcb27a1`.
Final HEAD: `cfef162049f632016c9e67bca0e400c58c8618d2`.
All 39 node rows match the reviewed states, times and localized notes: 36
mitigated, one not affected and two unknown. The RT storage results remain
unknown. Perf now records its reviewed corrective boots while retaining earlier
exposure uncertainty. Public advisory text and all child identities are
unchanged. CIFS received no update.

The final range contains only three commits modifying the three intended
submission baselines. All other source and evaluations match the released
source byte for byte. The other 57 approved baselines and all unrelated
baselines are unchanged. Every original recovery checkpoint remains in the
consumed ancestry. The project worktree and index are clean; frozen evidence
remains SHA-256
`61904e984266df2f6c53435b2b026b0d0980b35a23ed843eebf95b23c27c9274`.

The first update stopped after a successful remote write because the local
operator checker stripped a leading porcelain status space before parsing its
path. Read-only inspection found only the expected submission path. Following
lead acceptance, only that local assertion changed to preserve whitespace;
known-input checks and the complete saved readback passed. The already-written
baseline was committed normally without repeating the perf API write. The
[update ledger](updates-ledger.json) records the cause, actual returned revision,
digest, source and recovery checkpoint. No application source changed to fix
this operator error.

The [completion receipt](updates-completion.json) records the aggregate local
proof and ledger hash. Raw outputs remain restricted under ignored project
`.state/draft-sync-followup/`. No API call followed the third update. The
exclusive Git and remote-write slot was returned to the lead; Nix shell 94281
is idle. No publication, email, push, integration or lifecycle action occurred.

[Session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-19-vpsadmin-kernel-cves/)

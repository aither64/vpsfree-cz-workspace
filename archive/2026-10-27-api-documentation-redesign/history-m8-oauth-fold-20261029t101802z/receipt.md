# Final OAuth correction folded into Optional

Checked owner4 sidecar `6f7aa4449759260e6095870ffccb2fd0870284d6`, tree
`e526e62753d6c18218074995761a944e6e61bdd5`, parent old published/reviewed
`fb07c1378e4267bdfd54fa8fbfcfc57b6ec53413`. Its actual checked-commit receipt
and explicit SOURCE/Git/hooks release were read before any mutation:
[owner receipt](../verification/oauth-origin-correction-fb07/receipt.md).
Exact module/spec/guide correction:3 paths,+105/-7. Documentation uses
strict-origin; OAuth endpoints retain default no-referrer, with exact Origin,
cookie/session CSRF, parser and revocation semantics preserved. No source edit
was made during this mechanical fold.

Base `f6e5c3750c747b33ec869c54ca220bf6f1d9d2d0`. Actual final series:

| Group | Old SHA | Final SHA | Final tree |
| --- | --- | --- | --- |
| Core | `51073383f063abbc24bf19ca669b9b6e46bb9555` | `51073383f063abbc24bf19ca669b9b6e46bb9555` | `df0fd318b400a64e7cd6be784c93e565432aaff2` |
| Optional | `2462dfbac4921e15619ce17736bde9931f6d3fac` | `78ab264add97495aa38ffb33800f16cc9870838d` | `6329fa36a7e730bb785d1cc64bcde1ffb2c7da04` |
| Performance/HEAD | `fb07c1378e4267bdfd54fa8fbfcfc57b6ec53413` | `2f6c18a80f3a5f8ce46449ff81183b100b60f34c` | `e526e62753d6c18218074995761a944e6e61bdd5` |

Core stayed EXACT, with no recommit or Core hooks. Trusted same-session clean
scratch was reused via ordinary new-branch switch at old Optional. Exact checked
OAuth binary/full-index patch was checked/applied with --index to that Optional,
then ordinarily amended. Original Performance patch was checked/applied with
--index and ordinarily committed. All three complete original messages are
verbatim (Core.message/Optional.message/Performance.message). Staged and committed
complete mode/blob/physical inventories match each old group plus exactly the
checked OAuth correction;905 entries at Optional,908 at final.

Each corresponding old Optional→new Optional and old Performance→new Performance
diff is the BYTEIDENTICAL accepted three-path OAuth patch, SHA256
`9ddbb27e0d6c4be48d24de239834e194eb96d863f5be1b5c4a7d420c1e9b5a82`.
Original Performance full-index/binary parent patch is unchanged. Final tree and
empty accepted-sidecar→final diff agree; base-to-final aggregate is BYTEEXACT
the checked sidecar aggregate, SHA256
`9f9231d0dbdb3066d44f87f61e9a3ee6a9634b07c6acfbb2adcf4a8bd258eeb7`.
Exactly three groups remain; final-series.txt/range-diff.txt and aggregate patches
retain exact lineage/equivalence. Full inventory is148 paths,+11565/-1282.
Actual full path-set equals old148 union the exact three owning paths, which
were already present; no guessed count/tolerance, unrelated paths, migrations,
schema/persisted-state changes or dependency/channel/input update streams.

Before feature movement, full tree/aggregate/group/message/source/index/input/
flags/ref proofs passed. Guarded expected-old sidecar6f7aa444→final2f6c18a8
update-ref exited0; actual readback proves current final HEAD/tree. Original and
scratch sources/indexes are clean and empty; all908 accepted physical bytes/modes
match both, all905 unaffected files preserved, logical entries/flags unchanged.
All2148 protected files,23 exact session roots, frozen root/server locks and hook
bytes remain exact. No tool setup, install, Nix realization, hook config/signature
bypass or environment replacement. Existing immutable Ruby/Git/Bash/root frozen
bundle and normal OS utilities were used (environment.json).

Ordinary mandatory HaveapiI18n/RuboCop and all commit-message hooks passed:
Optional exit0/7.965s; Performance exit0/4.359s. No actual failure or retry.
Owner4 OAuth80/0 seed16029, lint2files and whitespace proof retain their actual
checked-sidecar labels, with final bytes identical. No duplicate quick/spec/
package/runtime/compiler/browser/performance checks were run for this fold.

Owner4's make doc ran exactly once. The intentional source guide and existing
ignored servers/ruby/doc/documentation-oauth.md copy are byte-identical, SHA256
`cd890eb49bcb371d3e484d95ecc1341ecbfccbecbe70e1b6088edbcf1971768d`.
This replaces prior guide-copy SHA256
`00bfb50e73d6357e43861a4c7df7a481333cb0d55d2f0122e95e7edeab889659`;
other ten packaged documentation copies remain exact. No additional make doc or
ignored copy mutation occurred. Application guide changes stay owned by owner4;
this operation adds only session evidence, with no useful extra project prose.

Every prior local/remote-tracking recovery ref remains unchanged, including
externally deployed511, reviewed/publishedfb07, d67 and all prior accepted/reviewed
sidecars. Unique new local refs preserve exact oldfb07 and accepted6f7:

- `refs/heads/recovery/2026-10-27-api-documentation-redesign-m8-oauth-reviewed-20261029t101802z` → `fb07c1378e4267bdfd54fa8fbfcfc57b6ec53413`
- `refs/heads/recovery/2026-10-27-api-documentation-redesign-m8-oauth-accepted-20261029t101802z` → `6f7aa4449759260e6095870ffccb2fd0870284d6`

refs.before/after and completion.json retain proof. No remote action occurred;
remote feature/recovery state was neither changed nor freshly queried here.

All owned commands ended, with no active utility/process or uncertain effect.
SOURCE/Git/hooks explicitly RELEASED immediately after final readback/preservation;
prompt lead report ea099ee4-b8ae-4206-9104-9cd987627929 delivered before this receipt.
Affected HIGH auth/security/history review remains for reviewer0 on this actual
final range. Prior product/R3/CI/Python reviews keep their recorded scopes.
Rack headers/forms do not prove native browser-generated Origin; later peer
native Chromium acceptance and publication require main's separate relay.
No readiness, deployment or integration claim; no push/CI/default/tag/release,
preview/service/provider/TLS/peer/session lifecycle operation. Session stays open.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-27-api-documentation-redesign/

# Guide commands: affected final review packet

User requested concrete vpsFree.cz `vpsfreectl` client-creation commands,
client/JSON/session-key generation commands and intentional private JSON output.
Architect appendix in existing design.md,2026-10-30 vpsFree.cz operator commands
for documentation OAuth, accepted by lead; lead applied the context-owner writing
pass directly. No factual correction or rewrite of that settled prose was needed.

Session `2026-10-24-vpsadmin-haveapi-upgrade`; existing plan/state/design remain
lead/architect-owned. Repository canonical SSH
`git@github.com:vpsfreecz/vpsfree-cz-configuration.git`, own registered worktree
`/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-24-vpsadmin-haveapi-upgrade/vpsfree-cz-configuration`,
branch `2026-10-24-vpsadmin-haveapi-upgrade-docs-deployment`.

## Exact old/new ranges and full history

Original accepted/published range `fcc7fc97be79df92ed39b4a7bfcc8ba21dc6c627..d0024528e93da895deeb4b7efc2b68c1461c94ec`,
tree `18448041543e983a6c5932277bcc0e5cc829dddf`. Original source/review packet
snapshot [original-d002](original-d002/review-packet.md), existing
[postreview/builds](../postreview/receipt.md), [publication](../publication/receipt.md)
and original E1-R1 records remain unchanged. Recovery ref
`refs/heads/2026-10-24-vpsadmin-haveapi-upgrade-docs-deployment-published-d002`
was established at exactd002 before the local history rewrite. No remote push
or source integration was performed by this milestone.

Final range `fcc7fc97be79df92ed39b4a7bfcc8ba21dc6c627..249f2eb5896b0a2697ed94e44657294847b3e606`, tree `9ed17cb32d860332bd347d2aa1b6807ecd8462ae`; clean owned worktree.
Exactly TWO coherent commits: owning functional `02121132a4bafcaa061072e995290f2e17b8ede3` (the new
operator instructions folded into the existing guide stream) and replayed normal
generated pin `249f2eb5896b0a2697ed94e44657294847b3e606`. The generated pin patch and complete message are
byte-identical to d002. One final33d6 services-input stream, no repeated pin,
fixup, intermediate application update or obsolete approach in final history.
[Full commit series](commit-series.txt), [full final diff](final.diff),
[old/new range-diff](old-new-range-diff.txt), [guide-only delta](old-new-guide-only.diff),
[complete outside equality](final-source-proof.json).

Only `docs/operations/vpsadmin-documentation-oauth.md` differs from d002
(+97/-52 before consolidation). Every other path/mode/type/Git OID is identical,
including all code/config/lock inputs. The final guide is exactly the settled
lead wording, SHA256 `d60238e39c8b755f51e4785394fd4041a91eb31e04798eeb878a8bab9ef47457`.
**NO MIGRATIONS** introduced; the accepted348inventory entries (315 actual core/
plugin migrations+33specs) remain byte/object equal, with no new migration or
merged/released/deployed/externally-consumed migration lineage.

Original E1 reviewer0 all4/HIGH report remains ONE BlockingE1-R1 at aead resolved
under lead-accepted step9 atd002; no additional source findings. This is retained
as original+resolved review, never relabeled an original no-findings review.
The new requested command documentation needs affected final review now.

## Concrete command contract

Guide only: first-setup Ruby SecureRandom generation in fresh private directory
under umask077, separate client-id/64ASCII-secret files without newline,
JSON with exact callback and switchfalse, separate raw64byte stable key shared
by API hosts. Intentional secret-bearing JSON print and cat reprint are labeled
private. Existing directory refusal/reuse/partial/uncertain-client reconciliation
are explicit; an ordinary upgrade does not rotate or recreate inputs.

Documented command uses vpsfreectl explicit `--api` BEFORE `--auth token`,
header transport, `--no-raw-values`, `oauth2_client create --`, protected@file
values, nondefault/fixed3600/no-refresh/SSOoff. No invented scope/client_type
Create fields or JSON/stdin-import flag. Normal authentication retains stdin and
keeps passwords/tokens/client-secret values out of argv. Existing provider,
proxy-first activation, API file modes, stable key, acceptance and rollback body
is retained. No product helper, provisioning framework or repository test source.

## Offline quick verification and exact scope

[Offline result](offline-result.json), [literal generation](literal-generation.bash),
[literal CLI block](literal-cli.bash), [fixture correction](fixture-correction.json).
All literal bash/shell blocks pass bash-n; whitespace and local links pass.
Only the documented `$HOME/vpsadmin-documentation-oauth` output directory was
substituted into an owned fixture path; HOME/CODEX_HOME were never overridden.
RUBYOPT loaded a fixture-only fixed SecureRandom provider, so no real credential
was generated. Synthetic ID/secret/key bytes are constant public test data.

Generation PASS:0700directory/all0600regular files; correct fields,32ASCIIid,
64ASCIIsecret/no newline, raw64bytekey, printedJSON and cat bytes equal retained
JSON, exact callback/switchfalse. Repeat existing-directory run refuses1 before
Ruby and preserves ALL file bytes/modes. No regeneration after successful setup.

[Actual released parser result](cli-parser.stdout) PASS using installed
HaveAPI client0.32.0 CLI under a communicator/action stub and user/network
namespace. Its full CLI parser source is byte-identical to release
`0e7166a0f8f15827bfac051666a53bf449e999ec`, SHA256
`bd10e79f2230a921905ea18bf52690b52a79c67ada157fb6fbbbc7c13a13a9e8`.
VpsFree thin subclass source56357098 was inspected; vpsAdmin subclass adds only
version display/custom unrelated commands, leaving this action parser intact.
The fixture retains actual global options, actual token-option parsing,
param-name dasherizing/Boolean handling and@file reading. Config read is stubbed
to avoid reading real saved credentials; sockets are blocked; communicator and
action execute are stubs. Auth stub sees a stdin marker (no redirection/EOF),
URL is correct at auth-option connection time, header transport selected,
all3false options are actual false, exact callback/fixed3600 values parsed,
file bytes no newline, no scope/client_type or secret bytes in argv.
This is parser-boundary proof, NOT real authentication, HTTP serialization,
server-side client creation or production acceptance.

Initial parser fixture failed because synthetic auth metadata used string
`token` while actual choices/description expect symbol :token. Original full
stderr/result preserved in first-*; corrected ONLY stub metadata and reran ONLY
the parser. The guide/source never changed; successful generation was not rerun.
No actual vpsfreectl executable/help/network/auth/client call occurred.

Normal declared-shell amend hooks Nixfmt/RuboCop and commit-msg PASS, no bypass;
normal identity and message file used. Same native72column advisory only;
authored message lines<=80. Rebase edit63701 and amend/replay75335 exit0,
all own handles complete. Guide bytes unchanged after these checks.

## Review and runtime limits

Request retained affected documentation/security/history review, with complete
base-to-head history/consolidation/NO MIGRATIONS. Suggested HIGH risk for secret-
handling operator instructions: general, risk/compatibility and scope lanes;
lead selects final applicable lanes and retained reviewer settings. No new
runtime design/API boundary was introduced and no production operation occurs.

The existing3target runtime builds/generatedconfig/source/input/closure/NAR/root
proof remains at exactd002 ONLY. New documentation head249f has NOT been built;
no final-docs-head output/derivation or binary-equivalence claim is made. Outside
file equality supports reuse for unchanged behavior scope, not relabeling old
artifacts. No automatic3system/A0/client/browser/SDK/fullcampaign was run.

STOP for final affected review BEFORE feature publication. Because same local
feature history was rewritten, later same-ref publication uses ordinary exact
`--force-with-lease` against originald002 after fresh guards, not --force/default
push; no extra user gate is invented and no push runs now. Existing original
published ref/recovery/evidence and all roots remain retained. No default merge,
production client/key/private-file provisioning, staging, runtime/lifecycle or
parent dev-update3922 action. Own source clean/no active writer or operation.

Portal: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-24-vpsadmin-haveapi-upgrade/

## Final publication

Lead accepted retained reviewer0 affected final report NO NEW FINDINGS at exact249f.
[Publication/effects receipt](publication/receipt.md) records the released exact
lease push0, independent SSH readback/default unchanged and no active writer.
Original review/build/recovery scope and D002-only runtime limitation stand.

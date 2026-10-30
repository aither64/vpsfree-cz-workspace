# Final affected review: CLI/curl generated-shell security fixes

User requests independent security audit, appropriate fixes including pre-existing
bugs, then independent audit again. Daybreak subscription/xhigh first audit of
exactf6→ae46 confirmed two pre-existing MEDIUM copy/run shell-injection defects;
no introduced regression confirmed. Main accepts both for correction. See own
security-audit-findings.md and deliberately shared security-audit-shared-fixtures.md;
no peer file access. Peer PoCs4/0 were independently reproduced by owner1 as four
new negative regressions failing on exactbaseline before source corrections.

HaveAPI git@github.com:vpsfreecz/haveapi.git, targetmaster (no merge approval).
Worktree /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-27-api-documentation-redesign/haveapi-shell-safety;
branch2026-10-27-api-documentation-redesign-shell-safety.
New reviewed rangeae46cf27a9afb6558d386c293cec7231dd6c423d→
ddf836fbb33ec6f920c3edfd9a4a53c2c2eb494b,
tree30efb19e02a756036771767745a9858fe968f95b. Exactly4paths/+207/-22:
servers/ruby/lib/haveapi/client_examples/ruby_cli.rb;
servers/ruby/lib/haveapi/client_examples/curl.rb;
servers/ruby/spec/client_examples/shell_spec.rb (new182lines);
doc/client-examples.md (+shell rules, main-authored prose).
Candidate/index clean, checked/staged/committed/current identities match proof.

Accepted design is final design.md section “Security remediation — CLI and curl
shell arguments”. Two renderer sinks only: stdlib Shellwords escaping once per
complete dynamic token after existingto_s orJSON.generate; curlPP shell-body
construction removed. Cover init/auth/action URLs/version/resource/action/path/
optionnames/values/method/header/data. Preserve authored prompt/continuations,
public placeholders, CLI Boolean flagchoice (including existing falseunderscore),
delimiter/order/to_s/OptionParser/@file/@@ and curlGETquery/body/method behavior.
No Host/proxy/auth/clientruntime/input/schema/dependency/framework/base-transform
change. No new binary/NULargv capability. Do not call old unsafe rollback secure.

Threat: attacker influence over example data or deployment-accepted Host plus
victimcopy/run required; developer-local command execution. Fix at shellsource
boundary, no server/browser execution merely from rendering. New tests invoke
actual declaredsh and tempfakeexecutables, require successful exit AND exact
NUL-delimitedargv/count/order AND no markers; JSON parsed complete values. All4
reported paths plus bounded token/literal families and authcommandspans covered.
No realclient/network/userconfig. Do not relax semantic or exactargument checks.
Main inspected actual committedtwo-production/docdiff, new182line spec and logs.

Fullf6e5c3750c747b33ec869c54ca220bf6f1d9d2d0→ddf sixcommit series:
51073383f063abbc24bf19ca669b9b6e46bb9555 Core;
78ab264add97495aa38ffb33800f16cc9870838d OptionalOAuth;
2f6c18a80f3a5f8ce46449ff81183b100b60f34c Performance;
1b264e25a73a0ab9bca5f847bd52254f74e0931c Style;
ae46cf27a9afb6558d386c293cec7231dd6c423d Instructions;
ddf836fbb33ec6f920c3edfd9a4a53c2c2eb494b Security.
Full finaldiff150paths/+11962/-1333. Priorfive commits exactreviewed/consumed
boundaries, this independently meaningful user security milestone is one coherent
fixcommit. No obsolete securityattempts/fixups, NO MIGRATIONS/schema/seed/format
lineage; NO repeated dependency/input/channel/version/generatedupdate streams.
Independent fullhistory/consolidation conclusions required; reuse prior source
review at unchanged scope instead of redoing auth/UI audit. All original2f6/1b/
ae46 refs and review/deployedsource preserved. One unrelated concurrently created
local auditref→ae46 was observed and preserved, no existingref moved/deleted.

Quicks: exactbaselineae46two-production bytes,4reportedcorrected-security
regressions allfailed expected(shellsuccess+unexpectedmarker),0.1636s+1.1sload.
Corrected shell/syntax/detail/presentation43/0 seed81106,1.16s+1.39sload. Changed3Ruby
lint clean; whitespace/make doc/guidecopyequal; mandatory i18n/RuboCop+commitmessage
hooksPASS6.710562s. Initial newRSpecmetadata/indentlint failures preserved and
fixed only metadata/layout, no assertionweakening. No speculative third issue,
broadtoolchain/runtime/compiler/browser/OAuth/performance/installed/wire gates.
Proofs verification/shell-safety/{result.json,complete-history.txt,
baseline-regression.log,focused-final.log,lint-final2.log,commit.log,loaded-source.log}.
All ownedhandles complete/sourceGitcheckreleased, no utility/uncertain effect.

HIGH risk because generatedshell boundary/localcommand execution; all4lanes:
general, architecture/repetition, scope/proportionality, risk/compatibility.
Retained reviewer0 eligible independent Sol/xhigh/read_only,
thread01a18193-44f5-7741-8b6e-6893a0e7f14d, actual identity/settings must be verified.
Read current mandatory review skill and all4full lane references/required owning
instructions. Assess fixes and value preservation plus tests/style/docs scope.
No tests/build/network/Git/source mutation or nested reviewer needed for review.

Consuming devvpsAdmin still pins1b, publishedreviewcandidateae46 preserved. No
publicrenderer/Context/custom-output interface change, persisted state or update
order requirement; oldrenderers remain vulnerable. No new deployment/release/
defaultmerge/production/lifecycle authority. Only after accepted finalreview main
will delegate ordinaryexactbranchpublication, then request independent Daybreak
re-audit. Architect's separate clients/ruby/lib/haveapi/cli/example_formatter.rb
interpolation lead is UNCONFIRMED and outside this twofinding package; route to
independent re-audit for evidence, do not claim thirdbug or speculative fix here.
Report findings severity/path first ornone, history/migration/update conclusions,
residualscope and completedread-only effects. Main reconciles, originalowner1 fixes.

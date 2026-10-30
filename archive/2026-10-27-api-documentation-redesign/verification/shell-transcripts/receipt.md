# Security remediation cycle 2 — committed, awaiting review

Isolated registered worktree:
`/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-27-api-documentation-redesign/haveapi-shell-transcripts`.
Branch: `2026-10-27-api-documentation-redesign-shell-transcripts`.

| Commit | Tree | Direct parent | Scope |
| --- | --- | --- | --- |
| `a3f522e509faaf9da34d9e87c7f7e9246c76bd6c` | `98467ac10c6e3d79e95dad1ba2d25a7b3b5556c6` | `ddf836fbb33ec6f920c3edfd9a4a53c2c2eb494b` | CLI help, 2 paths, +92/-4 |
| `aee093cd3387c261570067e58b7f1e16029e3619` | `295f884f0b2a8257883e82197fad3d8821c251ca` | `a3f522e509faaf9da34d9e87c7f7e9246c76bd6c` | Server transcripts, 6 paths, +176/-19 |

The eight-path cycle is +268/-23; exact inventory is in
[cycle2-paths.txt](cycle2-paths.txt). CLI help now shell-encodes complete dynamic
tokens once after existing conversion, preserving Boolean flags, filtering,
delimiter/order, values and response/title routing. Server CLI success tables
and failure diagnostics are displayed as comments. curl owns composed shell
examples with commented responses; its direct request and raw JSON response
remain intact. CRLF and bare CR become LF only within response display fragments,
then every physical line receives `# ` and a terminal newline. Static Password
display lines are comments. Request source, common result shapes, templates,
production JS/CSS, raw HTTP and custom output are unchanged. The guide contains
the exact main-supplied paragraph.

## Executed checks

- Before production edits, exact ddf production reproduced all three new marker
  exploits: CLI help 1 expected failing example; server transcripts 2 expected
  failing examples, alongside 4 passing first-cycle regressions. Retained
  [CLI baseline](baseline-cli.log) and [transcript baseline](baseline-transcripts.log)
  show execution and request corruption, not just source spelling.
- Isolated CLI-help spec: **3/0**, seed 81107, 0.06405s + 0.6952s load.
  Requires the ordinary CLI library directly, without client `spec_helper` or a
  live fixture. Hostile executable/resource/action/option/value tokens execute
  only the temporary fake executable; NUL-delimited argv/order/value and absent
  marker assertions pass. Absent/filtered inputs, Boolean flags, existing
  serialization, @/@@, title and `cli.format_output` routing remain covered.
- Server shell/syntax/detail/presentation/actual HTML: **54/0**, seed 81107,
  1.91s + 1.34s load. Both direct details, success rows/tables and failure
  diagnostics execute the whole displayed transcript after removing only the
  leading `$ `. Exact argv and parsed curl JSON remain unchanged; hostile
  multiline labels/data/messages/error keys, LF/CRLF/CR, substitutions, quotes,
  leading syntax and trailing backslashes stay visible and inert. Inherited
  shell composition, direct curl JSON, raw HTTP and custom output are covered.
- Existing documentation asset command: **PASS**. The real Copy handler writes
  the exact full selected transcript, comments and continuations included,
  through secure and native fallback paths. Existing focus/selection/scroll,
  failed-copy and selected-panel assertions remain. The first extension failed
  because its former copyText-only fixture lacked `createElementNS`; lead
  accepted reuse of the existing SVG factory. Both failed and corrected logs
  are retained; production JavaScript was unchanged.
- Changed Ruby lint: 2 client files and 4 server files clean. Earlier new-spec
  Ruby-3.0 shorthand/parser and layout offenses, plus server layout/chomp
  diagnostics, remain recorded. Only owning syntax/layout was corrected.
- One `make doc` exited 0; source guide equals its ignored packaged copy.
  `git diff --check` passed. Both ordinary `commit -F` operations passed mandatory
  HaveapiI18n/RuboCop and message hooks. The first message had a non-failing
  72-column width warning; all lines meet the mandatory 80-column limit.

Exact commands, durations and logs are in the adjacent JSON/log files:
[CLI](cli-final.json), [server](server-focused-final.json),
[asset](documentation-assets-fixed.json), [documentation copy](make-doc.json),
[first commit](commit-cli.json), [second commit](commit-server.json).

## Source, environment and history

Session current and both markers matched the bound session. Saved implementer1
Sol/xhigh/workspace_write settings were retained. Ordinary worktree creation
completed checkout/ref/registration but refused its configuration signature;
effects were inspected, identical configuration reviewed and normally signed.
Creation was not retried. No bypass, dependency install/resolution or graph repair.

[environment.json](environment.json) retains the candidate-local frozen root and
server bundle selection, existing shared gem store, declared Ruby 3.4.11, Git
2.56.0, Bash 5.3p20 and Node 24.21.0 paths with the normal OS PATH tail.
[loaded-source.log](loaded-source.log) proves loaded server renderer, CLI formatter
and HaveAPI client gem paths point into this candidate. All checks were quick
inline operations; no utility, actual client, network target or listener ran.

[result.json](result.json) binds checked/staged/committed/index/current hashes for
all eight paths, clean source/index, unchanged local locks and copied-guide
identity. All **312** pre-existing heads/remote-tracking/tag values remained
unchanged, including original 2f6, style 1b, instructions ae46, published ddf and
unrelated audit refs. Only this new candidate branch was added. No peer files,
worktree, team or transcript were accessed.

[complete-history.txt](complete-history.txt) inventories all eight f6-to-final
commits; [complete-diffstat.txt](complete-diffstat.txt) records the aggregate
152 paths/+12223/-1349. The six accepted ancestor boundaries are unchanged.
The two new coherent commits contain no obsolete fixups, migrations, dependency,
version, input or lock updates. No repeated update stream is introduced; the
inherited accepted history is preserved for independent whole-branch assessment.
Rollback needs no state migration but restores unsafe example behavior.

All owned setup/check/commit handles completed; no active or uncertain owned
effects remain. **SOURCE/Git/CHECK/utility ownership RELEASED** before this receipt.
Main was notified immediately. Mandatory HIGH/all-four-lane review, publication
and independent security re-audit remain pending and lead-owned. No publication,
long checks, merge/default change, consumer update, deployment, preview, peer or
lifecycle action was performed.

[Session](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-27-api-documentation-redesign/)

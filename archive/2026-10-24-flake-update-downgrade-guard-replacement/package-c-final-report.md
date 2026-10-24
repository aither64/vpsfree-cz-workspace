# Package C final local deliverable

All five local consumer branches now select
`github:vpsfreecz/confctl/bdaed19e901237e05bd0a779f368e76cb311143f#confctl`.
Publication is held for the lead's affected final review. No final-P live,
package, Git-race or VM verification has been launched by implementer0.

[Final branch inventory](package-c-final-branches.json) contains exact bases,
heads, targets, complete commit series, final path inventories, old/new ranges,
range-diffs, original publication provenance and fresh feature lease heads.
[Review source files](review-final-c/) contain full commit descriptions, diffs
and range-diffs. [Pre-final inventory](package-c-pre-final-provider.json)
records the original heads and retained local backup refs.

The four ordinary adoptions each contain one commit. Status contains its
consolidated adoption plus the independent baseline vendor-hash fix. The status
fix's patch is identical to local predecessor `521c5b6`; its final head is
`c8869b8f274dd840539a94da30d19d355cd623c1`, after adoption `13830fc...`.
Each final tree differs from its pre-final tree only by two exact provider-SHA
substitutions in the workflow pin and shared-guide link. There are no obsolete
pin/fixup commits, migrations, runtime inputs, lockfile changes, persistent
format changes or deployment/state boundaries to preserve.

## Quick checks and hooks

The final-P copy [package-c-final-fixtures.py](package-c-final-fixtures.py)
changes only the expected tool reference from the original offline fixture.
It passed in each declared environment:

```sh
nix develop --no-write-lock-file -c python3 /home/aither/workspace/ai/vpsfree.cz/work/2026-10-24-flake-update-downgrade-guard-replacement/package-c-final-fixtures.py <project>
```

Results were HaveAPI 9, Terraform 9, vpsAdminOS 6, status 7, IRC 9: all 40
scenarios returned 0. Four raw logs are named
`package-c-final-provider-quick-<project>.log`; status's final command also
checked gofmt, i18n and the setter regressions:

```sh
nix develop --no-write-lock-file -c bash -c 'test -z "$(gofmt -l tools/vendor_hash_test.go)" && make i18n-health && go test -count=1 ./tools && python3 /home/aither/workspace/ai/vpsfree.cz/work/2026-10-24-flake-update-downgrade-guard-replacement/package-c-final-fixtures.py vpsf-status'
```

That command returned 0; fresh setter tests took 0.193 seconds. The complete
Go suite had already passed on the identical independent-fix patch before
consolidation; its exact commands/results are in
[the status follow-up](package-c-status-followup.md). Actionlint 1.7.12 with
ShellCheck 0.11.0 passed all five final workflow files. `git diff --check` passed.
The original action compatibility evidence and fresh tag checks remain valid;
this consolidation changes no `uses:` ref.

Ordinary Overcommit amendments passed in HaveAPI, vpsAdminOS and IRC, with
only existing >72-character commit-message warnings within the 80-character
limit. Terraform declares no hook framework. Status's adoption amendment
passed Lefthook/i18n. Replaying its existing fix outside the declared shell
printed `Can't find lefthook in PATH`; effects were reconciled, and the final
fix was amended normally inside `nix develop` with active Lefthook. Explicit
final gofmt/i18n and helper checks passed as above. No hook-disable option or
custom index/stash workaround was used. Four raw amendment logs are named
`package-c-final-provider-commit-<project>.log`.

## Review and next verification

The lead accepted all five clean source heads and independently inventoried
all eight repositories before assigning reviewer0. Application source remains
fixed during review. Fresh default and feature lease checks are still required
immediately before post-review publication; target movement must be reported
before changing the reviewed patch. Provider P publishes first, then consumers.
No current-head CI is skipped or cancelled.

[Final verification packet](package-c-final-verification-brief.md) binds the new
manifest, driver and real race fixture to final P/all five C heads, with an
owned startup package out-link and new root. Static JSON/AST/Bash/content-hash
preflight passed. The lead supplies the completed affected-review report and
owns all runtime launch, serialized with B's two D patterns and real caller/hook
probes. All seven complete patterns rerun on P; the first three successful 7ba
runs remain historical evidence only. The real Git race and singleton
Terraform `workflows` VM with eight ordered examples remain required.

Original driver/manifest/review hashes `158cfaed...`, `31d8445...`, `c0dd0bf...`
and all first-attempt receipts remain unchanged. The failed status checkout is
retained with reconciled effects; no cleanup or blind retry was performed.
There is no running C command, watcher, repository claim or machine claim.
No merge, deployment or session lifecycle action was taken.

[Session](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-24-flake-update-downgrade-guard-replacement/)

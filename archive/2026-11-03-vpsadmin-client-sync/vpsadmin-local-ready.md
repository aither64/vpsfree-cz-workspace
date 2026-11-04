# vpsAdmin local integration readiness

## Actual integration result

The lead reported that canonical API documentation was integrated at exact head
`4ac49f49e63545200df8afa920c6eafda8722523` using normal hooks, SSH push and remote
proof; the lead's claim was released and its release verified. The preparation
steps and transport limits retained below are historical.

One metadata collection after the master push found these automatic runs, all at
that exact head and created at 2026-11-04 11:37:02 UTC:

| Workflow | Run | Observed state |
| --- | --- | --- |
| API Specs (topic parallel) | [41822368583](https://github.com/vpsfreecz/vpsadmin/actions/runs/41822368583) | queued |
| API Migration Specs | [41822368910](https://github.com/vpsfreecz/vpsadmin/actions/runs/41822368910) | completed, success |
| i18n health | [41822368892](https://github.com/vpsfreecz/vpsadmin/actions/runs/41822368892) | completed, success |

The prior feature-branch runs `41679570284`, `41679570579` and `41679570125` all
passed on the identical feature head; retain that evidence. The lead owns any
later related default-CI observation. This package performed no run/log polling,
rerun, dispatch or new utility operation.

### Unresolved default-CI residual

Run `41822368583` subsequently failed on master at the same integrated head.
The lead accepts the documentation delivery with this explicit unresolved
baseline CI residual; the result must not be presented as all green.

The failing job is `API specs (full) - platform-operations`, ID `126548402180`.
Seed `13353` ran 239 examples with one failure:
`./spec/api/resources/security_advisory_spec.rb[1:3:2]`, defined at line 487,
"scopes CVE, node and update reads and included parents without changing retained
history". The assertion at line 522 expected the response envelope's `status` to
be true. For an anonymous GET `/v7.0/security_advisory_cves`, filtering by a draft
advisory and requesting count plus included `security_advisory`, the actual HTTP
status was 200 but envelope status was false, with an errors Hash keyed by
`security_advisory` and no returned metadata. Expected behavior was a successful
empty list and count zero. No request-exception marker, timeout or runner failure
explains this assertion.

The source declares that filter as a resource parameter in
`api/lib/vpsadmin/api/resources/security_advisory_cve.rb`; its query separately
filters advisories through `visible_to(current_user)`. HaveAPI 0.32.2's resource
parameter cleaner converts the ID through its model adapter and checks referenced
record authorization. Saved diagnostics identify the rejected parameter but omit
the validation message, so they cannot establish which conversion/lookup or
authorization branch rejected it. No claim about a specific underlying defect
or a Rails regression is established.

The aggregate job `126562400379` correctly failed because the full matrix failed.
Its logs show both modes had 13 manifests covering all 417 eligible spec paths;
there is no missing/duplicate topic-coverage finding.

The same example passed in feature run `41679570284`, job `126069310937`, on the
identical source head with seed `56402` (239 examples, zero failures). Its resolved
dependencies differ, so that success is not equivalent-input validation:

| Evidence | Failed master run | Passing feature run |
| --- | --- | --- |
| ActiveModel / ActiveRecord / ActiveSupport | 8.1.4.1 | 8.1.4 |
| mime-types-data | 3.2026.1103 | 3.2026.1027 |
| Effective API lock SHA-256 | `aa49ff9efa5e9beaa4ea278eabfc17fd40ed032d99d0705ee9f18a880d60cd21` | `cc8bafa0ce1ba177ee4eb86bf29b7b644a5ad90a14dcef36aad1022ad62a1b47` |

Both environments report Ruby 3.4.12, Bundler 2.6.9 and RSpec core 3.13.6;
both locks select HaveAPI and its generators at 0.32.2, mysql2 0.5.7, Rack 3.2.8
and Sinatra 4.2.1. Both database logs report MariaDB 11.8.6, REPEATABLE-READ and
`innodb_snapshot_isolation=0`. Dependency resolution and random order both changed;
neither is proven causal. This is an application-validation failure, not evidence
of a runner outage or an established timing-only flake.

The failing example predates this work (last touched by `8225229aa` and present
in base `942c6eae`). Commit `4ac49f49` changes only two Markdown files, with no
runtime, spec, dependency or workflow edits. The docs triggered existing CI but
provide no runtime change explaining this assertion.

Failure logs, terminal metadata, artifact IDs and full evidence remain under
`phase2-integration/default-ci/01-vpsadmin-41822368583*`. Retained failed result/env
artifact `13318816860` is
[01-vpsadmin-41822368583-full-platform-operations.zip](phase2-integration/default-ci/01-vpsadmin-41822368583-full-platform-operations.zip);
passing artifact `13254476736` is
[01-vpsadmin-feature-41679570284-full-platform-operations.zip](phase2-integration/default-ci/01-vpsadmin-feature-41679570284-full-platform-operations.zip).
The separate feature job log and both extracted dependency locks are alongside
them. These are exact terminal-run artifacts, not active-run polling.
The `.lock` text reconstructed from stdout supports the dependency-version
comparison but is not a byte-identical copy of either original lock; the saved
environment JSON is authoritative for the original SHA-256 values above. No
installation or reproduction used those reconstructed text files.

Follow-up remains with the lead as a separate API product/dependency diagnostic
issue. A scoped comparison of the rejected resource parameter under the retained
graphs and matching example order could distinguish dependency behavior from
order-dependent state. That investigation has not been started. No blind rerun,
graph freeze, product/test patch, new experiment, utility, claim or default
mutation was performed for this diagnosis.

The canonical public raw document returned HTTP 200 at 2026-11-04 11:43:30 UTC.
Its SHA-256 is still
`109f3830f889d61785c17831b795ee3a611f624c3a4a25c0707eada31b3c53c2`, matching
the reviewed document. The exact heading `## Generated client synchronization`
appears once and produces the fixed `#generated-client-synchronization` anchor.
The [public check receipt](vpsadmin-canonical-public.json) retains the URL, time,
response date, digest and anchor result. The canonical link is now public:

https://github.com/vpsfreecz/vpsadmin/blob/master/docs/api-schema-export.md#generated-client-synchronization

## Historical local readiness

Update after the lead resumed read-only network verification on 2026-11-04:
ordinary SSH fetch and independent `ls-remote` both succeeded. Remote master is
still `942c6eaed41331f823d8e0f670ed239e2b308440`; the remote feature and clean
local source both remain `4ac49f49e63545200df8afa920c6eafda8722523`. The detached
target remains clean at the reviewed base. The accepted range, comparison,
independent review and CI evidence are unchanged. The earlier SSH freshness gap
below is resolved. No setup, optional checks, source edits or owner merges were
performed; the existing frozen launcher is ready for the lead's short claim.

Local preparation is complete as of 2026-11-04. The lead owns the later sequential
merge. All network work is held under the user's instruction to prepare locally
and wait for GitHub recovery. No further remote probes, pushes, CI calls, claims
or default-branch mutations are part of this handoff.

- Reviewed base: `942c6eaed41331f823d8e0f670ed239e2b308440`.
- Reviewed feature: `4ac49f49e63545200df8afa920c6eafda8722523`, branch
  `2026-11-03-vpsadmin-client-sync`, clean at the last local check.
- Detached target:
  `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-03-vpsadmin-client-sync/vpsadmin-integration`,
  clean at the same base, with the feature proven to descend from it.
- Complete range: one commit, `docs: require generated client synchronization`.
  Only `AGENTS.md` and `docs/api-schema-export.md` change. No migrations,
  dependencies, versions, generated content, runtime changes or repeated streams.
- The lead reported final independent documentation/history review with no
  findings. Required commit hooks and local links/anchor/whitespace checks passed.
  The accepted base/head comparison was already captured; the range is unchanged.

## Prepared command and environment

Use the existing [launcher](vpsadmin-merge-env.sh) after the lead resumes remote
verification and performs the ordinary fresh checks under the exact merge claim:

```sh
/home/aither/workspace/ai/vpsfree.cz/work/2026-11-03-vpsadmin-client-sync/vpsadmin-merge-env.sh git -C /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-03-vpsadmin-client-sync/vpsadmin-integration merge --ff-only 4ac49f49e63545200df8afa920c6eafda8722523
```

The [environment receipt](vpsadmin-merge-environment.json) retains exact store
paths, PATH, gem locations and frozen Bundler settings. The launcher exports the
prepared environment and executes its arguments; it runs no Nix shell hook,
installation or build. `BUNDLE_FROZEN=true`, `BUNDLE_IGNORE_CONFIG=1` and
`BUNDLE_AUTO_INSTALL=false` are explicit. Ruby is the existing store output
`/nix/store/nin40kn7prvsn7pmbl7k576hhwcpp9x1-ruby-3.4.9`; Git is
`/nix/store/nly4cml071i82515r89rpdw38z55wjqd-git-2.54.0`.

Root gems remain in this session's source `vpsadmin/.gems`; ignored target aliases
reuse those owned root/API bundles, with matching local locks. No other owner's
bundle was copied or changed. Under the explicit frozen/no-auto-install settings,
both bundle checks and the normal post-merge hook probe passed. Hook configuration
and trust were prepared outside claims. Preserve these owned paths until the lead
has completed and verified integration.

## Limits of the retained remote evidence

The feature was previously published and SSH-verified at the exact head above.
Its automatic CI identities were sent to the lead: API specs `41679570284`,
migration specs `41679570579`, i18n health `41679570125`. Their observation and
acceptance remain with the lead; this handoff performs no further CI calls.

The 2026-11-04 SSH fetch and ls-remote failed with `Permission denied (publickey)`.
Both commands exited; there is no active fetch or uncertain mutation. The shell
lacked `SSH_AUTH_SOCK`; transport diagnosis was transferred to owner0, and all
further probes are now held. A prior unauthenticated public GitHub API response
at 09:40:25 UTC reported master still at the reviewed base, retained in
[vpsadmin-public-default.json](vpsadmin-public-default.json). That public response
does not replace a fresh successful Git fetch and remote proof.

Conditional integration approval for the unchanged six-target scope remains with
the lead. After the lead resumes remote work, verify the current target before
claiming full integration readiness; refresh outside claims if it moved. No
additional local checks or utility operation are currently needed.

# Advisory visibility CI findings

Status: **bounded investigation complete; root cause unresolved; matched local topic passed**.
Architect0 synthesis of accepted evidence, 2026-11-04. Diagnosis/proposal only;
no production fix, project commit, merge, publication or deployment. Session open.

## Failure and intended behavior

[Failed run 41822368583](https://github.com/vpsfreecz/vpsadmin/actions/runs/41822368583)
ran source `4ac49f49e63545200df8afa920c6eafda8722523`, full/platform-operations,
seed 13353. Of 239 examples, only
`security_advisory_spec.rb[1:3:2]` failed. Its anonymous CVE index request filtered
by an existing draft advisory returned HTTP 200 but API status false, with an
error under `security_advisory` and no count metadata. The native artifacts omit
the error value, record ID and rejecting branch. See [CI evidence](ci-evidence.md).

The intended response is API success with no rows and count zero. Public and
non-admin readers see only published advisories and related records; admins
retain all states. Hidden child Show requests return 404. Counts, includes and
affected-user/VPS ownership restrictions must preserve these visibility rules,
and reads must not alter retained history.

## Demonstrated mechanism and counterevidence

HaveAPI 0.32.2 validates a Resource input before executing the list action:
strict ID conversion → ActiveRecord lookup → referenced Show authorization.
Field validation errors are collected into the API error envelope. This explains
how the observed response shape can arise; the exact original rejection is
still unknown. The adapter can also translate a lookup/callback `ArgumentError`
or `TypeError` into “invalid ID,” so that message alone would not prove malformed
input. [Validation trace and reproduction receipt](validation-reproduction.md).

Resource input authorization calls `SecurityAdvisory::Show#authorized?`, which
permits anonymous readers; it does **not** call the visibility-filtered
`Show#prepare`. After validation, the child list query joins its parent and
applies `SecurityAdvisory.visible_to`. Included-parent output separately invokes
Show preparation. Therefore hidden draft state alone does not explain the input
rejection or justify weakening authorization/changing filter types.

The exact isolated example passed at seed 13353 with the failed CI lock retained
after setup, full plugins, and loaded Rails 8.1.4.1, mime-types-data 3.2026.1103
and HaveAPI 0.32.2. The trace showed anonymous String `"1"` resolving to the draft
parent, successful Show authorization and execution of the CVE/Update queries.
All role/state assertions passed; no Resource cleaner error occurred.

The complete eight-file topic also passed: **239 examples, zero failures/pending**,
seed 13353, 2932.288 seconds. Independent comparison confirms every scoped ID
and the complete execution order match the failed native run; the target is
position 237 in both and is the only status difference. Its first anonymous draft
input was String `"55"`, resolved to draft ID 55, authorized and queried normally.
There were 168 target diagnostic events and no Resource cleaner errors.
[Order/result receipt](evidence/reproduction/topic-vs-native.json).

Together these observations rule out a deterministic failure caused solely by
hidden state, the failed dependency graph, or the recorded example sequence
**in the local instrumented runtime**. They do not rule out transient state or
dependency/runtime/order interactions. Local Ruby 3.4.9
and MariaDB 11.4.12 differ from native CI's 3.4.12 and 11.8.6; both use
REPEATABLE-READ with snapshot isolation OFF.

## Remaining causal uncertainty

The earlier [passing run 41679570284](https://github.com/vpsfreecz/vpsadmin/actions/runs/41679570284)
has identical source, manifest and all 239 scoped example IDs. Its Rails trio
was 8.1.4 and mime-types-data 3.2026.1027; seed/order and runner image also differ.
The full lockfiles were recovered from logs and hash-match native metadata.
Neither the historical comparison nor the isolated pass identifies Rails,
random order or timing as the cause.

Open explanations include prior-example/shared state, lookup/callback failure,
unexpected raw input, and Ruby/DB/runner effects or their interactions. Native
process/DB state and installed binary checksums are unavailable. A passing local
run also cannot exclude effects of diagnostic instrumentation. The loaded local
HaveAPI boundary files byte-match the source used for the static trace.

## Smallest justified proposal and bounded follow-up

The smallest justified proposal is **vpsAdmin test-only diagnostics that preserve
the original Resource validation cause**, with production behavior unchanged.
The disposable prototype already records Resource input, validation error/original
cause, authorization and whether the query was reached. A durable test-support
change should retain the structured error for this synthetic failing example and
capture the original cause before `Params#validate` aggregates field messages.
The current field-name diagnostic cannot distinguish these branches, and the
ordinary request-exception hook cannot recover a handled field-validation cause.
This proposal is not an implemented or committed project patch.

The isolated and exact-topic checks are complete, with no operation remaining.
The read-only [runtime availability assessment](evidence/reproduction/native-runtime-availability.json)
is also complete. Official [Ruby builder](https://github.com/ruby/ruby-builder/releases/tag/ruby-3.4.12)
offers the Ubuntu 26.04 x64 Ruby 3.4.12 binary (42,575,614 bytes, SHA256
`b4943e5d36b82f38c3f3c9f979a1d1b5dfb9769dcada5e70945e0fe63b6b8586`).
Official Ubuntu [main](https://archive.ubuntu.com/ubuntu/pool/main/m/mariadb/) and
[universe](https://archive.ubuntu.com/ubuntu/pool/universe/m/mariadb/) indexes list
the matching MariaDB `1:11.8.6-5ubuntu0.1` server/client/library/header/compatibility
packages. Exact Nix outputs and a cached Ubuntu 26.04 image are absent; Podman is
available. A source build is not inherently required, but a new image, exact apt
setup, Ruby revision check and separate 104-gem bundle/mysql2 build are needed.
Preparation cost is unmeasured. No runtime artifacts were installed or new run
launched; the lead ended the first batch at this explicit uncertainty boundary.

- If investigation resumes, the next experiment is
  **one full topic** with unchanged source/graph/seed in a disposable runtime
  aligned to native Ruby 3.4.12 and MariaDB 11.8.6, including matching client
  headers/library and a fresh mysql2 extension. Retain the prior-example history.
  Verify the available artifact digests/package inputs, Ruby revision and setup
  cost before launching; do not silently substitute versions or expand into a
  source-build/image project. The native runner's preinstalled Ruby archive
  checksum is unavailable, so matching versions does not establish binary identity.
- If the same failure recurs, use the captured branch/cause to select a minimal
  mechanism-specific reproduction and owning-component remedy. If evidence is
  incomplete or order differs, resolve that discrepancy before adding runs.
  Stop after the selected topic result and input/order receipt;
  do not automatically expand into a seed/dependency matrix. If the aligned run
  also passes, report the unreproduced native rejection and remaining environment
  gaps instead of inventing a fix. Runner/kernel/cache/process state and diagnostic
  instrumentation remain caveats even after matching Ruby/DB versions. Detailed
  conditions are in [design](design.md).

## Security, compatibility and focused checks

No API/schema/client, persisted-state, migration, protocol or deployment contract
has changed. No rollout or software rollback is required. A later demonstrated
fix must preserve anonymous/user/support/admin behavior across all advisory
states, counts and included parents, plus affected-user/VPS ownership. Its focused
regression should cover the actual rejecting branch, valid/missing/malformed
filter IDs, and retained history. Resource-to-integer conversion is not currently
justified: it could change existence checks, authorization and generated metadata.
Retries, skips, weaker assertions and permanent dependency freezes would conceal
the unresolved cause.

This is investigation evidence, not a reviewed production patch. No automatic
change review is required for these findings. No new test or environment was
started to prepare this synthesis.

[Session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-04-vpsadmin-advisory-visibility-ci/).

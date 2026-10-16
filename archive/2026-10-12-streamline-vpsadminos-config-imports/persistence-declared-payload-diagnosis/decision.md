# Declared payload fixture initialization

Architect0 (retained Astra/xhigh, roster revision18) traced the old-baseline
failure to preboot fixture scaffolding, not the candidate mount adapter.
The full report arrived in the lead conversation on 2026-10-15.

The suite creates backing/var/lib/preservation-test as root0755 before boot.
Old activation creates a temporary account-owned0750 source before the
/guest-backing bind; mounting the prepared backing hides it. The next old live
switch preserves the already-existing root0755 source under impermanence’s
missing-only metadata rule. Original logs show matching997:997 account/maps,
custom state42:43:0710, file owner997:997, but payload directory0:0:755.
The assertion fails before oldChallenge or candidate adoption.

Accepted bounded correction, after the immutable run terminates: only in the
declared layout, after the oldInitial live switch and before first payload,
verify backing bind identity and exact mounted payload identity, require the
payload directory empty (including hidden entries, fail on find error), then
install -d -m0750 -o preservation-test -g preservation-test on that one empty
fixture placeholder. Resolve the real allocated account; no hard-coded ID,
recursive ownership change, state/map/data repair or assertion relaxation.
Preserve scaffolding needed for old boot. All other script/fixture/module
behavior stays unchanged.

Implementer0 owns application edits after parent authorization. Parent owns
focused generated-script and exact-input comparison, hooks/fold/review,
publication and a new declared-backing runtime. Reuse other successful rows
only with exact execution input identities; account for provenance-only source
path diagnostics separately. Do not modify or resume the failed old guest.

Evidence: runner-declared-excerpt.txt, machine-declared-excerpt.txt and original
/tmp/ni.p5mnmdxx/os-test-dist-config__nixos-persistence-upgrade-8c45b496 logs.
See suite167–173/203–214, fixture12–13/69–77/100–105/120–129 and actual old
/nix/store/pqmh1r9qwczn3rqfy27izmvx8alljcma-nixos-system-persistence-fixture-26.05pre-git/activate.

Proposal inspection: accepted the guarded layout-only block. Both emptiness
checks use find -printf x -quit, so command substitution cannot strip an entry
name consisting only of newlines into false emptiness. Find errors explicitly
exit; device/inode and source identity survive install. Actual old system
sw/bin/find and sw/bin/install are present. Proposal preparation is static only.

Input-reuse verification plan: evaluate the complete existing suite config
using the original host metadata intentionally, then compare the actual host
outputs, runner/machine configuration, all12rendered bodies, generation paths
and registration paths to the native first-run config. Only one candidate-source
stdout diagnostic may differ in the11unaffected bodies. This preserves an exact
already-tested host rather than silently treating different toplevel revisions
as equivalent. The new run will record the final TEST SOURCE head separately
from the reused host image's original edb90d2fe build revision. If outputs differ
outside the accepted executable block/provenance diagnostic, resolve it before
claiming reuse. The unchanged normal persistence check derivation should match
CI6218pz068gff57gp72fjhw2b0ylh5msd; compare it explicitly. No baseline evaluation
or broad12case retry is needed merely to produce this comparison.

# API platform-config failure: cold VPS attribute fixture

The final narrow candidate is 024ab881be181fad839751de9efe60a44fecbe39, tree
dbfbe6b5313150ca5a1135f295e36e4f2d4ed1a5, clean and unpublished. Against reviewed/published
cb8c214dba62731c93dafb102072444bcc77cc4e its only content delta is
api/spec/lib/vpsadmin/api/incident_reports_spec.rb, five additions/one deletion.
It defines the actual Vps column readers before constructing the unchanged
verifying instance double. All five original assertions remain unchanged.
No production/API, migration, schema, dependency, flake/package, SDK or workflow
change is justified or included. Root owns final narrow-fix inspection and later
publication; Owner3 has the exact candidate and continuing publication dependency.
Main state/plan and previous evidence homes remain untouched.

## Exact failed attempt evidence

Run43911462363/workflow234996228/attempt1/headcb8 is lead-observed. This package
collected only required coreplatform-config job133454171654 log/result/manifest
and subsequently necessary fullplatform-config job133454172226 metadata/log.
No run observer, aggregate download, unrelated job result or broad second
artifact listing was started. Root separately reported both platform-operations
jobs successful; this package did not independently fetch or relabel them.

Native collector41114 completed0, all owned cells/sessions joined per root.
collection-result.json SHAa3e8e46fa9b5d269ab21abc95c2abcca3bc24a6696a76105babe44602bbe7982
binds three successful downloads and matching providerZIPdigests. Utility elapsed
reports1.4s/1.20s are different collection scopes, neither a test duration.
Archives were inspected for bounded flat regular members before extraction;
raw logs/ZIPs remain unchanged. Sanitized excerpts omit terminal escapes.

Core actual native JSON:482examples/5failures/16pending/0outsideerrors,
seed8635,554.417229797s. The first five executed examples all fail in the same
.oomd_event_message group:

| Original ID suffix | Original source line | Assertion scope |
| --- | --- | --- |
| [1:1:3] |30| unsupported-language fallback and ambient locale restoration |
| [1:1:5] |55| separate report/ambient languages across threads |
| [1:1:2] |30| empty-language fallback and locale restoration |
| [1:1:1] |30| nil-language fallback and locale restoration |
| [1:1:4] |45| ambient locale restoration after rendering failure |

All raise RSpec::Mocks::MockExpectationError at the old letline27: Vps does not
implement the instance method hostname. The exception-restoration expectation
is masked by that fixture error; the thread case records both thread errors.
Production rendering is not reached by these failures. The pending16 reasons
are existing plugin requirements; no filters/skips were changed.

The retained47artifact listing did not yet contain the fullplatform-config result.
The root-authorized known-small same-service route retrieved only exact fulljob
metadata and log (native76347 terminal0), not another artifact inventory. Its raw
233718B log SHA4ada05265df857f324c372ae7334a08bd272ab9345b00da666632703284d38da
explicitly records the same five cases and same hostname-verifying-double errors,
482examples/5failures/3pending, seed48559, printed duration12minutes56seconds.
No native full-mode result JSON is claimed. There is no distinct additional
product/test failure requiring broader correction.

Root's terminal exact-attempt read at17:25:01Z separately reports cb8 API run
43911462363 completed/failure (24of27jobs passed; both platform-config and
aggregate failed). It reports integrationCI228803702/run43911462168/attempt1
completed/success, provider updated17:23:21Z, and i18n/RuboCop successful. These
are root observations, not another provider collection or new coverage claim by
this package. All four cb8 workflows are terminal; no cancellation was initiated.

## Dependencies and proved mechanism

The timestamped core log printed a lock recovered byte-exactly and hash-matched
to native environment1f5cc5b41540300c820d12b2b41cf318ded1345548c674336d1395b508b9974b.
Its entire diff against retained1b68 is connection_pool3.0.2->3.0.3. Relevant
interfaces are identical: RSpecCore3.13.7, Mocks3.13.9, AR/AS8.1.4.1,
HaveAPI0.32.2. Full log's printed lock was separately recovered/hash-matched
1e038e10a75bd7fd9cf9beb00ec004a18073fd21f396991c95a1baa7900e8457;
these same relevant versions and connection_pool3.0.3 appear there. CI uses
Ruby3.4.12/Bundler2.6.9/MariaDB11.8.6, REPEATABLE-READ, snapshot_isolation0.

AR generates column readers lazily. RSpec's instance-method verification checks
class-defined methods without invoking an instance's method_missing, so a cold
Vps class can reject a real database attribute. Other example orders can hide
this by first instantiating a Vps. The actual core failures occur at the beginning
of the process; no precursor bisect is needed to establish this cold interface.

The existing installed frozen1b68 bundle was sufficient for the interface proof:
its RSpec/AR versions exactly match both CI failures, with only the separate
connection_pool gem at3.0.2 versus3.0.3. No API bundle install, resolution,
dependency source change or environment expansion was performed. Local Ruby3.4.9
and MariaDB11.4 remain recorded differences; this focused proof is not a claim
that the entire failed CI environment was recreated. The ordinary declared root
Nix shell still performs its existing Bundler bootstrap, separately from the
private leaf API bundle. Do not label the whole command no-reinstall.

## Focused reproduction and correction

focused-leaf.sh runs exactly original group[1:1] plus two private native RSpec
controls under seed8635, using the existing frozen bundle. The controls force
Vps.undefine_attribute_methods only for these cases to represent legitimate cold
model state, and restore generated methods afterward. They verify that:

- cold hostname verification fails, explicit real column generation permits it,
  and an unsupported method still raises the strict verifying-double error;
- actual unsaved Vps.new accepts id/hostname unchanged without persisting a row.

Original-source native41979 terminated1:7examples/5failures/0pending/0outsideerrors,
15.301057857s. Its five failing IDs exactly match the original core CI five;
both focused interface controls pass. original-cold.json/log/exit and the original
tracked source copy preserve this baseline.

The sole source correction calls Vps.define_attribute_methods inside the existing
let, then constructs the exact original instance_double with the same id/hostname.
This uses AR's thread-safe generator and actual schema interface. It keeps strict
verification, hostile-placeholder interpolation input, all fallback/locale values,
render-exception restoration and thread assertions. No unchecked double or
mock-verification setting was introduced. The inline comment is the durable
explanation of this test invariant; product docs need no behavior update.

Corrected native86497 terminated0:7examples/0failures/0pending/0outsideerrors,
15.841389942s. The same five native IDs pass and both controls pass. Relevant
runtime versions/lock are recorded in the two environment JSONs. The exact final
file SHAcd87dc2f5e43c4a5c4d78e34add6406aaa7959a0a4eaa1946ffc7b2d9cdfd757 equals tested bytes.
Syntax and scoped RuboCop passed; normal trusted pre-commit/commit-msg hooks
passed on both the fixup and owning localization commit. Consolidation commit-msg
had four inherited body-line >72 warnings; every line stays within required80.
No suite/topic rerun, blind CI retry, timeout or assertion weakening occurred.

## Final history and equality

Root traced ownership to ordinary-localization129679b4. The temporary normally
hooked fixup1c2cfe4b23bf69be36b787a01250772fc524be05 is retained only as the tested
pre-consolidation ref. Its entire tree equals finaldbfbe6b5313150ca5a1135f295e36e4f2d4ed1a5 exactly.
The correction was folded into owning localization9f4ed12e; final537b..successor
has the accepted five purposes, without a sixth transient fix purpose:

```text
3af143d96ee4ca0244afc5a86573c30b36768871 api: evaluate incident escalation through site policy
9f4ed12e4a332d0ee5ffe142b09a36d9ce9636f6 api: localize ordinary oomd incident reports
cbba38a03715cc2b1f48d483d537b9312bd32dd2 webui: show incident history and unknown runtime limits
3ca3ceef8a6b580cdbfbefe7e8e8ebe0da8061b0 docs: explain isolated MariaDB locking settings
024ab881be181fad839751de9efe60a44fecbe39 api: preserve transactional fixture connection leases
```

reviewed-to-final-range-diff.txt shows first API/runtime purpose identical,
ordinary localization changed only by this fixture plus explanatory commit body,
and PHP/MariaDBdocs/sharedfixturelease patches byte-identical. In particular,
the independently justified fifth shared fixture-support patch remains separate
and equal to reviewed cb8. history-equivalence.json binds raw patch SHA equality,
complete old/new series and exact tested/final tree identity. final-correction.diff
SHA9585b1d90854ac9d2314a40713fbafb579499adbc2760734bc8ed603b7d2f121; final full537b..successor plain diff
SHA1724744c81a1ed22df39096832aa5ed3071c41a1526a2feb4ee429d225b35987.

Preserved refs under refs/review/2026-10-30-oomd-abuse-policy/ include original
15ed/cb8, nov16-api43911462363-before, -published15ed, -publishedcb8,
-tested-preconsolidation and -final. All older reviewed/diagnostic/consumed refs
remain. Original migration20261030180000 bytes remain f1e6bc75aeffb14d2d14676a908fc4332d7f42f79ee29fe54f48def8e2756c7a;
conservative additive20261115120000 remains b9d894772f61c65dd40952db0eacc04783cbc940144377f1a783d34b2a4a441c.
Historical production consumption remains unknown; nothing rewrote lineage.

All other tracked bytes equal cb8, including schema, runtime/API, packages/locks,
flake, exporter and old four-case fixture regression. Prior b72340context evidence
is retained within its unchanged selected file/helper/dependency inputs; it was
not repeated or relabeled as a new native run. Original15edSMTP proof remains
its exact old source/package result, with no new Nix derivation claim. Root
explicitly requested neither original40 nor SMTP repeat for this test-only edit.
No SDK/export scope follows from this correction. Default25b's packaged3.0.3
update was not added during this history fold; defaultintegration remains a
separate explicit preparation/input assessment, as in the accepted cb8 packet.

The candidate is held for root's narrow-fix/history inspection before publication
or longer checks. Last accepted canonical feature is still cb8; final publication
will need fresh remote/default checks and exact expected-cb8 lease for rewritten
feature history under root release. Owner3's d1e235dc pin selects cb8 and awaits
accepted published successor proof; this package does not release downstream work.
No provider observation, push, export, SDK generation, physical test, deployment,
default integration, manual cleanup or session lifecycle action follows from
this preparation. All owned native handles are joined/terminal; source is frozen.

Documentation routing: test-fixture invariant -> developers -> inline spec comment;
individual failed CI/reproduction/history evidence -> lead/reviewer -> this
existing-home diagnosis and final-receipt.json. Main state/plan remains root-owned.
Stable portal: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-30-oomd-abuse-policy/

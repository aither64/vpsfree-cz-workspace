# Keep maintenance-lineage fixtures independent of the checkout version

The first 0.31.0 release build failed seven server lineage examples with
`Expected own 0.30 patch version`. The fixture builder called the intentionally
0.30-only performance normalizer on the checkout version before replacing it
with a synthetic maintenance version. Worker input and HTML examples also used
the checkout where they needed a synthetic 0.30 source.

Read the template VERSION without normalizing it, construct synchronized fixture
sources, and validate those completed fixtures. Keep temporary source roots and
loaded component-version stubs scoped to each example. Preserve the production
minor restriction; widening it would change the reviewed benchmark contract.

The correction includes a synthetic 0.32 template regression that derives a
valid 0.30.2 fixture and still rejects synchronized 0.32 input. At source version
0.31.0, all 18 lineage examples and targeted RuboCop passed. The existing
`nix develop -c make test-performance` then passed all 160 examples before the
tagged release build was retried.

The failed run retained no artifact and uploaded no package. Retagging required
the user's explicit fix-and-retry direction; this is not general permission to
move failed tags. See [release recovery and review](../../work/2026-10-27-prepare-client-releases/state.md).

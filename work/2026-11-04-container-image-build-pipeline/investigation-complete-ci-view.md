# I9: complete, immutable image view for full CI

2026-11-05, implementer0; prior packages accepted, capacity confirmed.
Session/current and both environment bindings match; unchanged workspace
guidance/skills reused, repository AGENTS reread. Canonical bare vpsadminos
source `2951a632c4254a44747a8da326e3dde897eaa0e2`; all citations use it.
Reuses I0/I4/I5 evidence. Only this file written; no code/runtime/Git mutations.
Central SSH staging is the user's current preference; interfaces below are
proposals, not deployed or verified production behavior.

## A versus B

| View | Consumer changes and tradeoff |
| --- | --- |
| A: candidate-only plus explicit changed-tuple selection; public unchanged | Requires per-tuple routing/required-set checks in tests or a helper adopted by raw CT commands. Two sources remain, and generic fallback can hide a failed candidate (I0). Useful for targeted tests, but full CI needs widespread tuple/alias classification. |
| B: run-scoped complete baseline plus verified replacements | Ordinary default-repository CT commands remain unchanged. One common URL/configuration/readiness seam replaces per-test dispatch. Requires a real complete payload view and immutable baseline storage; an index alone cannot redirect payload origins (I2 contract). |

Recommend **B** for full CI. Preserve parallel, streaming image build/test/
artifact receipts from I5, then await selected builds and seal once before
starting full-suite consumers. This deliberate consumer barrier removes an
image-dependency scheduler and prevents tests observing changing tags/indexes.
It does not require waiting to ingest or independently publish good images.

## Minimal test/configuration changes

- `tests/make-test.nix:112-120` supplies common vpsAdminOS test modules;
  `tests/configs/vpsadminos/base.nix:9-11` also has the optional tests.nix
  override seam. Supply one non-secret run URL through common configuration,
  setting `osctl.pools.<test pool>.repositories.default.url`; do not add a
  second public fallback repository. Existing module
  `os/modules/osctl/repositories.nix:26-36` updates the default URL.
- `--test-config` currently carries runtime data only
  (`make-test.nix:353-365`; `tests/test-configs/ci.nix` contains docker/podman
  settings). A new image-repository URL entry needs one common consumer:
  bridge it into that module or configure/assert default in shared test setup.
  Adding the entry alone changes no repository. Avoid a CLI shell-text proxy.
- Repository configuration service starts **after** pool active
  (`repositories.nix:95-99`), while `osvm/lib/osvm/vpsadminos_machine.rb:65-66`
  returns from pool waiting on active alone. Shared setup must wait for or
  apply/assert the exact run URL before the first normal image fetch. Include
  runtime-created pools; do not assume the declarative tank setup covers all.
  This is one repository readiness contract, not per-image test dispatch.
- Keep deliberate custom-repository protocol fixtures explicit. Fresh test
  pools/caches avoid stale fallback bytes; ordinary tests should assert the
  selected default and no unintended enabled public repository. Most existing
  `osctl ct new` strings need no edits. Complete pool/setup coverage still
  needs confirmation before claiming every normal consumer uses the run URL.

## Proposed staging expected/ready/finalize/failure contract

1. **Create run:** central SSH operation records run/source identity, a pinned
   full baseline snapshot/index identity, and expected selected images expanded
   to full vendor/variant/arch/distribution/version tuples plus intended tags
   and defaults. Return a run URL early, but do not advertise it ready. Current
   changed detector yields image-script names, not this manifest
   (`.github/workflows/scripts/changed-image-scripts.rb:89-102,124-177`;
   `.github/workflows/image-scripts.yml:89-97,124`). Expand variants explicitly.
2. **Receive:** upload into temporary run-owned storage over SSH; verify tuple,
   format/hash and successful same-run build/image-test receipt, then mark that
   expected result verified. Failed/cancelled/not-built entries remain distinct
   from verified entries. A copied old baseline file is never a candidate receipt,
   even if its bytes happen to equal a new successful build's bytes.
3. **Finalize:** after all selected work is terminal, require every expected
   tuple/variant to have its verified same-run receipt; verify final tuple and
   alias/default resolution and artifact hashes match those receipts. Require
   unchanged references resolve against the pinned baseline. Atomically seal
   a complete read-only repository view and publish ready evidence binding its
   index/manifest identity. Subsequent uploads cannot mutate this test URL.
4. **Failure:** any missing/failed expected candidate prevents ready status and
   full-candidate-CI success; old baseline content cannot satisfy its slot.
   Report the failed expected set and fail aggregate CI. A baseline-only or
   partial diagnostic run may be labelled as such, never candidate-complete CI.
5. **Consume/retain:** CI waits for sealed ready evidence, then all normal
   consumers use that one HTTP repository URL; SSH is writer transport only.
   Retain baseline/run payloads through consumers and publication receipts;
   snapshot/GC details belong to the staging owner, not test scripts.

## Coverage and publication remain separate

Full-public snapshot does not prove all suite references exist: old versions,
moving tags or special variants may already be absent. Preflight required image
references for the selected suite (at least `tests/distributions.nix` sets;
I0 cites their registration) against the proposed sealed resolution. An absent
unchanged tuple is a **preexisting dependency gap**, not permission to rebuild
everything or silently fall back live. Broader explicit test-image references
are not inventoried by this bounded investigation; declare that coverage gap.

Verified default-branch successes remain independently eligible for their
authorized publication path, even if another image fails or full CI is blocked.
Do not make full CI a universal publication gate. Test-view readiness and
publication are separate outcomes; failed runs still preserve good receipts.

Unresolved interfaces: authoritative name→tuple/variant/tag expansion; staging
snapshot/payload retention and finalize receipt; common URL/readiness wiring for
all pools; required-suite image inventory. These need bounded design ownership,
not per-test tuple routing or streaming-consumer scheduling.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-04-container-image-build-pipeline/>.

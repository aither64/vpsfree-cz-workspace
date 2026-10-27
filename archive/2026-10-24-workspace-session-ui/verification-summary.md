# Verification summary

Final published head: `9293e314e6028d71a57595073117b51bdc53c8ff`, base
`10bb047513c82d1310e8fcaa797e8772f948dd8a`, codex-web pin
`872c7ad3962f9fa9b17358244e27f3e3fac59fc5`. Final source equals the passed
prepared snapshot for all590 tracked blobs/modes; only four expected generated
asset extras are outside Git. Final CI40143026250 passed at this exact head. No deployment
or default-branch integration.

| Check | Tested input | Result | Evidence |
| --- | --- | --- | --- |
| Focused handler proof | New pinned handler; final test source fd20d158… |37 leaf cases pass | refresh-validation-unit.log/.exit |
| Flake evaluation |01218bf9 | PASS47s | refresh-evaluation.log/.exit |
| CI-aligned fast/package selection |01218bf9 | PASS594s | refresh-fast.log/.exit |
| Message delivery browser |01218bf9, locked Chromium and Firefox | PASS | refresh-browser.log |
| Composer browser |01218bf9, locked Chromium | PASS | refresh-browser.log |
| Paging/unread browser |01218bf9, locked Chromium | PASS | refresh-browser.log |
| Portal improvements browser | Exact012 snapshot + held fixture cc99efe0… + four pinned generated editor assets | PASS full scenario including actual editor | portal-prepared-browser.log/.exit; prepared-input provenance |
| Five admission contracts | Pinned codex-web via consuming portal module | PASS | refresh-admission.log/.exit |
| Two HTTP delivery contracts | Same pin/module graph | PASS | refresh-delivery.log/.exit |
| Private native cold recovery/FIFO | Exact selected Codex0.163.0 package + pinned module | PASS14.20s | refresh-native.log/.exit; native-watcher-result.md |
| CI40140692767 | Exact published01218bf9 | fast/archive/creation success; host skipped | https://github.com/aither64/dev-workspace/actions/runs/40140692767 |
| CI40143026250 | Exact final published9293e314 | fast/package, archive and creation success; host skipped | [result](ci-final-result.json); [watcher receipt](ci-final-watcher-result.md) |

Raw-source portal browser failures are preserved. The first exposed two stale
draft-retention expectations after durable capture; the held fixture now checks
saved text/ID, immutable retry and newer draft preservation. The later editor
failure came from generated assets absent in the raw source Go embed. Package
preBuild supplies those assets. The successful prepared run uses that existing
recipe, without application changes or synthetic editor assertions.

[Prepared-input provenance](implementer1-refresh-evidence/portal-editor-prepared-input.json)
binds the590 tracked blobs/modes, exact held fixture, four generated asset hashes,
immutable assets output/deriver and complete input graph. The generated assets
remain build inputs; they are not feature-source additions.

Native package identity before final fixture fold:
`/nix/store/dcqiflilwlrmq0p9qz3rwamckjjx2l5p-codex-package-0.163.0.drv` ->
`/nix/store/3lrchzhnd3iiknvkim8ivq77h6i1gdlv-codex-package-0.163.0`.
[Input hashes](refresh-native-inputs.sha256) and
[derivation receipt](native-derivation-before-fixture-fold.json) are retained;
final identity compares exactly equal in native-derivation-final.json. Go/Nix
inputs and all product assets are unchanged by the final fixture fold.

Independent review covered all affected lanes and complete history/migrations.
R5 was the sole refreshed Important finding and received direct narrow repair
inspection/checks. Original R1–R4 evidence remains retained. See
[refresh review](refresh-review.md) and [disposition](refresh-review-disposition.md).
The fixture correction keeps the already-reviewed delivery contract and adds no
new design/API/migration. Lead inspected its diff and prepared browser evidence.

Browser FIFO proves this tab's dispatch order. The native fixture proves cold
activation/recovery and queued FIFO; it does not prove model consumption order
for multiple steers or combined execution order across clients.

Final whole-branch inventory: five coherent commits, settings/unread literally
unchanged, composer includes the bounded fixture correction, quiet/docs remain
patch-equivalent to012. No fixups, superseded streams, migrations or product
changes since012. Exact012..final diff equals the accepted fixture patch
(SHA256908227aa32cc81247ec2ad8f6ceab0afbd2e4a2d1cb72e70f1d31f0ea2670424).
[Final diff](final-ready.diff), [final history](final-ready-history.txt),
[fixture correction](portal-fixture-final.diff). Final native derivation/output
identity equals its successful tested identity, not merely source tree equality.
Final-head full CI passed. All jobs are completed; the watcher exited0 and no
verification process remains. The branch is ready, awaiting merge approval.

# Prepared status-only R workflow verification

Source is local `d4c816bbf7ad22b9b2dcb424c1f316b1d0b6c6aa`, following the reviewed/published R adoption and
independent vendor fix. Only app_routes_test.go changes in the third independent
test compatibility commit. Provider remains R
`5436d3d7c36d3d5174eab3c44e3578830749d3db`. No other consumer pattern or provider
startup repeat is requested. Source publication and completed focused final
status review must precede launch. No command below has run.

The lead supplies the actual completed status review path in
`STATUS_METRICS_REVIEW_RECEIPT`, then launches through the serialized fresh
Luna monitor. From `/home/aither/workspace/ai/vpsfree.cz`, with GITHUB_TOKEN in
the private environment:

```sh
set -euo pipefail
: "${GITHUB_TOKEN:?Supply GITHUB_TOKEN privately}"
: "${STATUS_METRICS_REVIEW_RECEIPT:?Set the completed focused status review path}"
python3 work/2026-10-24-flake-update-downgrade-guard-replacement/package-c-status-metrics-post-review.py \
  --root /tmp/flake-update-guard-status-metrics-workflow-2026-10-24-1 \
  --review-receipt "$STATUS_METRICS_REVIEW_RECEIPT" project vpsf-status
```

Frozen driver SHA-256: `bd02cae3875da143dc5d18ed40790bbda4bc751528607271d5ea80912650afd6`.
Frozen manifest SHA-256: `2ff0856b83e0b6dd8247f37e6e8b9a1759d36e6dcae391e8e6129c03e544399f`.
Static Python AST/JSON, exact source trees/files/blobs and extracted Bash syntax
passed; updater blocks contain no external publication or unresolved expression.
Workflow steps, complete baseline lock and provider are exactly unchanged from
the original R manifest. The new manifest adds the corrected test source hash
and binds the new complete status tree.

Reuse exact successful R startup/package/check/input identity receipts and the
retained owned link
`/tmp/flake-update-guard-2026-10-24-provider-r-1/startup/confctl-package`.
This command creates a new owned root/attempt and fresh SSH checkout at the
published exact status head, disables external push, saves the original lock,
installs ordinary hooks and executes all complete status workflow blocks. It
captures generated commits, final committed-blob guard, Go tests, Nix package
and full source/input/derivation/runtime receipts. Status parent identities
must remain unchanged during the selected leaf update. No update selection,
metrics behavior or dependency pin is changed by this test correction.

Stop and report any nonzero result, unexpected local kernel build or unfinished
owned process. No automatic retry, alternate command, diagnosis, source edit,
publication, machine action, integration or lifecycle action belongs to the
watcher. The driver interrupts only its owned process group on an unexpected
kernel build, preserving native cleanup. Quiet output is not a deadline.

Original failed R checkout/receipt/out-link and diagnostic compatibility fixture
remain preserved. The lead's separate IRC/D/race/VM plan stays independent.

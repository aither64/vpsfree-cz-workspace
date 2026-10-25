# A narrow review correction: quick evidence

Reviewed baseline `96077b6257bd7dac05930312a29eaf00fc900b3c` is preserved in
`package-a-reviewed-96077.{patch,md}`, `package-a-reviewed-96077-final.diff` and
`package-a-reviewed-96077-history.txt`. Correction: `package-a-review-correction.diff`.

- The corrected regression overlaid on reviewed production source fails all
  three buffered permanent/progress/terminal cases with `retry=true`; late
  equivalents pass. Exact red output is `package-a-review-red.log`.
- `nix develop --command go test -mod=readonly ./codex -run '^TestEphemeral' -count=1 -timeout=45s`: PASS 3.209s.
- `nix develop --command python3 test/codex_protocol_contract.py --coverage-only codex/client.go`: PASS.
- `nix develop --command go test -mod=readonly -tags=codex_integration ./codex -run '^TestEphemeral(PostCompletionErrorRevokesRetry|Integration(OverloadAdvice|HTTPFallbackResponder))$' -count=1 -timeout=45s`: PASS 0.129s. Tagged compilation and local responder checks only; no native server/model run.
- `git diff --check`: PASS.

The shared lock-required error validator now runs before the error guard during
replay as well as delivery. All six paired cases require false direct/wrapped
accessor, empty output, no diagnostic leakage, exactly one start/unsubscribe and
zero interrupts. The late test emits its error only on unsubscribe, proving
binding/settlement before delivery. Existing returned categories remain intact:
early replay returns protocol error; a late cleanup-frame invalidation keeps
the already-returned server category while revoking proof. No API/classification,
bounds, ownership, isolation, model/catalog or cleanup policy changed.

Declared Nix environment used. No hook framework or active Git hooks are declared
for codex-web; no bypass. No migrations, long tests/builds, deployment, claims,
master integration or lifecycle actions. Lead owns focused inspection under the
mandatory-review narrow-remediation policy.

Later fixture-only correction at `4300c40b6406161afc74c124c40155f28a557032` deletes13 rejected reserved-provider
override lines relative to f722; product code unchanged. Focused tagged combined
regression/responder/progress/terminal checks PASS0.725s, diff check PASS.
Exact delta: `package-a-native-fixture-correction.diff`; failed native execution
evidence: `verification-native-f722-failed.*`. Lead owns diagnosed rerun.

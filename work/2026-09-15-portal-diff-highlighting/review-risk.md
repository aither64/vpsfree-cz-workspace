# Risk and compatibility review

## Findings

No Blocking, Important, or Advisory findings.

## Reviewed commits and contracts

Reviewed the complete single-commit series in each supplied range, applicable
`AGENTS.md`, plan/state/diagnosis, relevant tests, package construction, and runtime
and extension documentation:

- `dev-workspace`: `9a1b16464e45d722110b448a79315a0f3ce134aa` →
  `5d853b6b0c2608549a1f0e940c680ccb40a14bec`.
- `vpsfree-dev-workspace`: `c6afe2905506fba0b8e372e0436b570f5597f8bd` →
  `b75cc8a6270219ca2fc25c1e292ce030fc33e45d`.
- `workspace`: `259c0c3fe7d4f3d454f8b27172cb7a8f99ca79be` →
  `80b93a8c6b120ce178b4a6479901fde12156e3d5`.

At runtime head, `portal/review-ui/editor-model.js:1` selects the existing
`presentableDiff` export from locked `@codemirror/merge` 6.12.2. Its implementation
calls the same bounded `diff` and then cleans up character ranges. The model
still validates Git ranges, compares only replacement-block contents, and clips
marks to their source rows (`editor-model.js:51–106`). Git classification,
source text, source-line maps, and context validation remain unchanged.
`editor.js:97–104` uses those ranges solely for fixed-class decorations in the
existing read-only editor. No HTML insertion, authority, credential, API, or
persisted-state path changes.

Both pin commits select exactly the reviewed predecessor change. The extension
changes only its runtime lock node; the workspace changes only the extension
and runtime lock nodes. `lib.mkPackage`, `siteConfig`, Codex, cluster inputs,
host paths, activation code, and runtime/state contracts are unchanged.
`nix/review-ui.nix` includes the edited model in its source and runs the editor
tests during packaging, so no generated asset commit is required.

Old and new browser bundles consume identical payloads. Switching the complete
site package through the existing user-profile path needs no state migration or
special mixed-version sequencing. Its documented previous-generation rollback
remains applicable (`dev-workspace/docs/workspace-portal.md:64–77,156–167`).
Existing activation refusals must be respected, as the packet already requires.

## Verification and residual gaps

- Independently ran `nix shell nixpkgs#nodejs -c npm test` from the runtime's
  `portal/review-ui`: **13/13 passed**. This includes both readability examples
  in both layouts, source and line-map invariants, exact Git totals, malformed
  range rejection, and bundled-asset checks.
- Full package checks, CI completion, served-asset identity, and real-browser
  acceptance of the original saved comparison are subsequent planned checks;
  this review does not claim deployment or rollback execution.
- Presentation remains heuristic, as explicitly accepted in the packet.
  Maximum-size adversarial text was not newly benchmarked. The existing
  512-KiB/12,000-line preview bounds and raw diff scan/timeout configuration are
  unchanged; presentation cleanup itself is outside the raw diff timeout.

Reviewer: risk and compatibility lane, `gpt-6-astra`, `xhigh`.
No product code or session state was changed by this reviewer.

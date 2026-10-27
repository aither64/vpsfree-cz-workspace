# Historical candidate preflight failure

Owner: implementer2. Session/environment identity matched
`2026-10-24-workspace-session-ui` and `/home/aither/workspace/ai/vpsfree.cz`.
This record is bounded read-only diagnosis after the deployment hold. No checker
normalization, product/configuration edit, build, claim, activation, native restart
or lifecycle action was performed.

The preserved parent-owned watcher v2 log is
`../deployment-candidate-check-v2.log`; result is
`../deployment-candidate-watcher-v2-result.md`. Capture completed with exit 0;
comparison failed with exit 1 at `compare.py:70`, which required the selected,
actual daemon-launch and candidate runtime contracts to be wholly equal.

The old selected package was
`/nix/store/8ph05i3nps8xi1jfs450b16aysc16nvg-dev-workspace-0.2.0`.
Its immutable daemon launch provenance identifies
`/nix/store/s4fbv3hya8l09jh4a67rd4brdkwx4piz-dev-workspace-0.2.0`.
These two preserved packages alone fail that equality: the launch contract lacks
five capability fields present in the old selected contract.

| Field | Old selected | Actual launch package |
| --- | --- | --- |
| `codexProviderForkCreationPolicy` | 1 | absent |
| `codexProviderScopedStateSchema` | 2 | absent |
| `codexProviderScopedTransitionPolicy` | 1 | absent |
| `turnRetrySessionPolicy` | 1 | absent |
| `turnRetryStateSchema` | 1 | absent |

All other parsed runtime-contract fields agree. This is not a package-dependent
reporting executable path difference. No compatibility conclusion or permission
to omit those fields follows from this diagnosis.

Source reason, inspected in this session's own dev-workspace Git history:

- `d99f468edcb2ff91137b3473c9b52c5669465751` added scoped provider state/transition
  capabilities.
- `8054ac27603b27608dd2a7a3a48a797d5b254451` added fork-provider capability.
- `b3c7187c6e26e269994433716a0ee719d0a7edf7` added retry-state capability.
- `7844c9c39347c46756fa7d64099ccac045c83eca` added retained session retry-policy
  capability.
- `git diff 10bb047513c82d1310e8fcaa797e8772f948dd8a
  9293e314e6028d71a57595073117b51bdc53c8ff --
  portal/internal/session/runtime-contract.json` is empty.

The immutable extension catalog points the old selected runtime skill to
`/nix/store/r2pxv5h275gk9njy59rbk4ydsjy38hx4-source`; the actual launch package
points to `/nix/store/hhfvx30ryhbw4yalrc1jybcg9nrzyl9a-source`.
The feature's runtime contract is unchanged from its base; the launch marker
preserves an older startup package. The supported host code separately checks
reporting-policy/complete argv equivalence in `registration_argv_equivalent?`
and native invocation in `marker_has_semantics?`. That observation is not a
replacement compatibility rule for this evidence script.

## Resume-time drift and limits

Fresh read-only identity checks found both live system and system profile at
`/nix/store/1bnl145ln79094l10j60cp4631a69vww-nixos-system-aitherdev-26.05.20261021.da6dc0e`,
with selected workspace profile
`/nix/store/48011krllhj3428878a8h55sb6x4wky0-dev-workspace-0.2.0`.
Native PID remains 3387667; portal PID is now 374159. The immutable launch marker
still records the same actual launch package, native codex path, reporting policy
1, argv, digest and actual required native child capacity 0.

Frozen candidate
`/nix/store/nz0cj6j634gy3y9hddznz8a0zmgpmhvj-dev-workspace-0.2.0` is absent
at diagnosis. No cause is inferred. Its recorded build/output/graph receipts are
preserved under `../workspace-input-preparation/`; they are historical evidence,
not proof that the output remains available. No rebuild or candidate check ran.

The lead reports a foreign aitherdev machine owner. No other-session records,
worktrees, source or roster were inspected and no ownership action was attempted.
Resource waiting and missing artifact/current-live preparation are separate from
the historical assertion failure.

The exact five-field mismatch and source provenance were sent directly to
architect0 (message ID `427d082c-58d8-4b7f-9b2c-6b5989ea7f76`) and the lead.
Architect owns the capability/current-drift disposition. Scripts remain unchanged
and no resumed check is authorized until a new architect/lead package. Preserve
failed artifacts and use fresh names for any later authorized receipts.

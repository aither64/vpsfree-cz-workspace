# Independent remediation review

No findings in the affected general, architecture and risk/compatibility lanes.
R1 and R2 from `independent-review.md` are resolved by the reviewed changes.

Reviewer remains `/root/optional_questions_review`, the same independent
standalone reviewer with configured `gpt-6-astra` / `xhigh` settings. Original
review identity and catalog provenance remain in `independent-review.md`.
No application edits, nested agents, commits, deployment or long tests were
performed. This report supplements the original four-lane review.

## Exact reviewed heads

| Repository | Base | Final head |
| --- | --- | --- |
| codex-web | `c064ce09cfcea8d8af6bf676635a53cd823f772c` | `641907fb3afa2977050fe61331f9a3411c091245` |
| dev-workspace | `09a407953026514ae84be81dab9442fd74b6a362` | `911ed5298912db88fe462cc78180570e3281c8fc` |
| workspace | `94eb7c055b44e37c5b82902788e36eb05c37179f` | `29723cf41376946d29d0e18c02eff13af5e16c1d` |
| vpsfree-cz-configuration | `a2ad6da408715de811cc6d8ea7b29ac55ea341ec` | `fb6e89299249ff06cf44f34caa914eabab3b521c` |

Inspected the committed provider delta from `803e877c`, consumer delta from
`f2b3e827`, and both deployment-pin deltas from their originally reviewed heads.
All four worktrees were clean, with the listed bases equal to their merge bases.

## Remediation assessment

- R1: permanent expiry now follows terminal turn status or a different latest
  turn. Transient native thread idleness no longer clears an unfinished turn's
  questions. Regression coverage includes idle, reload and actual completion.
- R2: the controller measures the complete UTF-8 reply envelope before storing
  or sending an attempt. A fresh local failure or HTTP 400/413 validation
  rejection releases the unsent attempt and retains an editable draft. Existing
  uncertain attempts retain their exact identity even if a subsequent retry
  fails locally or is rejected. The ordinary handler performs validation before
  native send; native send failures remain HTTP 503, preserving this distinction.
- The optional `maxMessageBytes` helper argument uses the existing default
  48 KiB handler budget. The portal obtains its actual limit from the rendered
  composer attribute, populated from the same `session.MaxMessageBytes` value
  used by the handler. Documentation explains the override and encoded-byte
  check. This preserves provider ownership without duplicating framing rules.
- Custom writable clients now derive question storage from the same validated
  canonical endpoint identity as ordinary durable sends. Built-in clients retain
  their existing canonical identity. No endpoint authority is accepted from
  transcript content and existing trusted-target/send guards remain in force.

## Verification and history conclusion

Independently ran the eight committed question-controller Node tests through Nix;
all passed. Also ran a focused read-only probe: an uncertain first send, reload,
then HTTP 400 on retry retains the original message/ID and blocks a different
answer. The lead reports the remaining focused Go/browser checks passing.

Each final base-to-head range contains exactly one logical feature or final pin
commit. Corrections and generated dependency updates are consolidated; no
obsolete approaches, fixup series or repeated update streams remain. Workspace
and configuration lock the identical runtime `911ed529` and codex-web `641907fb`
revisions and content hashes. The site extension remains `767dfd58`; unrelated
inputs are unchanged. The earlier fixture correction remains folded into the
consumer's feature commit.

No migrations. Server ledger, session format, database and native protocol
migration conclusions are unchanged. No new rollback or mixed-version boundary
was introduced by these corrections. Actual-template Playwright, native reply
reconciliation and package/deployment checks remain the planned later gates;
they were not represented as completed by this review. Deployment and default-
branch integration remain separate actions under their existing authorization
and ownership requirements.

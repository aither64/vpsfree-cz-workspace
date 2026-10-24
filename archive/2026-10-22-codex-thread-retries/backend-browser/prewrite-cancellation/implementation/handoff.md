# A pre-write cancellation isolation: published handoff

A `11ec57d2203fc735696fe75a837d47da55a5c6af`, tree `407762bc074c009540a6e2b5ca363fef1cc178f6`, is committed, clean, source-frozen and published by normal SSH fast-forward push. Independent remote lookup matched the exact feature head; remote master stays `ea64ef57fdd2ff5fd60715b62f2d1696bc0133e5`. The tested index tree equals the committed tree. Ordinary hooks were enabled; this repository declares no hook framework and had no active hooks or custom hooksPath.

The distinct eighth commit follows unchanged accepted5743 and all previous seven commits. `codex/client.go` adds eight lines: observe caller ctx.Err only after write/admission locks and generation/prompt-claim revalidation, release held locks and return the existing TransportError before entering connection.Write. No no-write observation calls markDisconnected. All post-Write errors and stale prompt/generation handling stay as before. No retry, detached context, error-string inference, ledger/native/UUID/options or API change.

## Focused evidence

- `red-before-guard.*`: exact old producer with the new tests failed both cancellation cases while all five existing checks passed; raw JSON/streams/argv/full source hashes retained.
- `normal-final.*`: seven named tests PASS, no fail/skip; 6.657s shell wall (compilation included).
- `race-final.*`: same seven named tests PASS, no fail/skip; 12.854s shell wall.
- gofmt and diff/cached-diff checks passed. Full source hash maps match before/after normal/race and the committed source.

The deterministic fixture uses disposable Unix WebSockets, pending-call registration and writeMu ownership. A live sibling is already on the wire with its response held. Cancellation is observed before releasing the waiting writer, and an ordered barrier then proves that only the sibling and barrier frames arrived. It asserts existing TransportError/context.Canceled, same ready connection/generation, sibling success and no reconnect. The already-canceled case shares that wire proof. Existing actual write-failure, stale-generation and changed-prompt guards remain selected. This is fixture evidence, not native/model/browser verification.

## Exact source and adoption metadata

- Source: `/nix/store/549mbnzpbcs81ccvvv4wrh9xmjrxg86n-source`
- NAR: `sha256-tWV8OX1uCr9fjcCvZBgwYYn+O9XvM1xpY+kPv4vgFSY=`
- lastModified `1792852844`; revCount `116`
- Go module `github.com/aither64/codex-web` version `v0.0.0-20261024144044-11ec57d2203f`
- Sum `h1:cod93lovFHu5adtEqQy7QyE1E5YIFJrTkCnjB3phFgw=`
- GoModSum `h1:SfoFFfEnXQusGm701eWJpCbrkwia5g1biF5KD9RIqr0=`

`source-proof.json` compares all116 tracked blobs/modes to the immutable source, independently rehashes its NAR, verifies no missing/extra paths, binds both quick input maps to committed bytes and compares module key files. `source-metadata.stdout` and `final-flake.lock` retain the full locked input graph. No build/derivation equivalence is claimed.

## Preserved history and review packet

`preservation.json`, `accepted-5743.bundle` and dedicated ref `2026-10-22-codex-thread-retries-accepted-5743-prewrite` retain the exact accepted source. `source-unchanged-proof.json` establishes every other tracked file and accepted UI asset remains exact5743. Dependencies, lock, catalog, protocol and docs are unchanged.

Full range `ea64ef57..11ec57d2` is eight commits. See `full-eight-series.txt`, `full-base-to-final.diff`, `new-transport-unit.diff`, `range-diff.txt`, full tree/path inventory and verified `final-11ec57d2.bundle`. First seven commits are exact; no style fold, baseline move, pin stream or migration was added. Existing deployed5743 remains an exact ancestor, preserving all its supported state and review evidence. No database migration or format transition is introduced by this successor.

README/reference transport and durable reconciliation wording still applies. The sole added near-code comment was accepted unchanged by lead; no UI/public error/help/docs prose change. Exact attempt9 own-cancellation versus sibling-disconnection inner attribution remains unmeasured. Original FAIL and negative gates remain valid; no queue404 exemption.

Next: lead accepts this handoff and releases B owner1's sole consolidated A pin, then retained affected final review and only separately authorized fresh browser/native/package gates. No B/W/C/pins, CI queries, live/native/model/build/deployment/lifecycle action was performed. Old-target operations preparation stays held.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-22-codex-thread-retries/

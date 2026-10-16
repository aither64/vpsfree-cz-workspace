# Affected-lane follow-up

Same independent reviewer/settings and mandatory-change-review procedure.
Read the risk/compatibility and general lane references. Do not rerun unaffected
architecture/scope lanes. Read-only review; write a supplemental report here.

Native integration at reviewed cweb 8851f1c failed because it expected top-level
instructions. Exact candidate source core/src/client.rs now prefixes input with
BaseInstructionsFragment; context/base_instructions.rs defines developer role.
The selected source is now realized at
/nix/store/9is267xl3palxb615kk86qlli9nggkf9-source/codex-rs.

Inspect codex-web 8851f1c..a0561fad8decb794117f8959fa2dd629547c5ba7,
including the new strict first-developer-message predicate, six quick passing
shape cases, and reference clarification. It changes fixture verification only,
with no library behavior change. Assess whether the assertion preserves the
isolation/instruction proof against the actual source. Complete original series
still has two commits; the fixture adaptation is folded into the existing
upgrade commit, with no migrations. The full current range is 5238651..a0561fa.

Runtime B1 is fixed by catalog size 62680 and exact source prerequisite update;
focused length/hash binding passes. A clean CI build additionally found the stale
vendor hash; the previous local probe was a cached false pass. The generated
hash was corrected mechanically, and will need another refresh for the new Go
pseudo-version before clean final package builds. Consumer pin refreshes pending.

Do not run long tests/builds/deployment, or edit project source. Report any
Blocking/Important findings before native rerun. Save followup-review-report.md
beside this packet and return its path.

# System selector JSON wrapper correction

Status: bounded verification-schema proposal for lead disposition; no execution
or owner1 runner edit. Session/current/environment pair and live architect0
Astra/xhigh/workspace_write settings verified. Applicable unchanged workspace,
session, documentation and verification guidance remains read in this context.
Only this own artifact was written; accepted design6bcf remains unchanged.

## Evidence and limit

The lead reports outer31569's three actual Nix commands exited0 (metadata,
build plan, system selector). The runner then exited1 on Python string indexing.
The retained selector JSON contains `toplevel` and `autoRollback` as output-path
strings, with the expected key/input/machine selection. Preserve those original
command receipts, stdout and aggregate failure; this is not a failed Nix build
or evidence of a wrong confctl source selection. Architect did not rerun or
independently inspect the store/output paths.

Selected Nix2.34.9 manual root:
`/nix/store/addg4icdw1xadiwh6bk4lql8bxbvf11i-nix-manual-2.34.9/share/doc/nix/manual/`.
File-only reads establish:

- `language/builtins.html:2604`, `builtins.toJSON`: “Sets (except derivations)
  are represented as objects. Derivations are translated to a JSON string
  containing the derivation's output path.”
- The same file at2626, `builtins.toString`, explicitly accepts a set containing
  `{ __toString = self: ...; }` or `{ outPath = ...; }`.
- `command-ref/new-cli/nix3-eval.html:256` documents `--json` as JSON output.

The manuals document the special string-compatible `outPath` shape and ordinary
record representation; they do not spell out every internal JSON attrset
detection predicate. The actual retained selector output supplies the concrete
evidence of string coercion here. Do not claim an inspected implementation
predicate, a timing cause, lost derivation or a new application defect.

Manual SHA256:
`language/builtins.html` =
`a56c1f2eaef72ffe65f64c1d505aa358172c47f76be907fce662418a94191164`;
`command-ref/new-cli/nix3-eval.html` =
`0875f6132161ad7cad377041447c22f38b391b6f35206644710b75c7a8821a66`.

## Smallest successor

In each of the two literal wrapper objects, rename the left-hand JSON schema
keys only:

```text
drvPath = <existing derivation expression>;
outPath = <existing output expression>;
```

becomes:

```text
derivation = <the identical existing derivation expression>;
output = <the identical existing output expression>;
```

Keep outer keys `toplevel` and `autoRollback`, the confctl-owned key resolution,
all right-hand selectors, machine/input fields, locked sources and command
settings unchanged. Construct fresh literal records; do not inherit the selected
derivation attrset or retain `outPath`, `__toString` or `type="derivation"` on
these wrappers. No `builtins.toJSON` around the whole expression (which would
double-encode the result), string coercion workaround, output-path-derived
guess of a `.drv`, or source/helper change is required.

Owner1 updates only the successor verification expression and its bounded JSON
decoder. Before indexing, require both wrapper values to be JSON objects with
exactly `derivation` and `output`, each a nonempty string. Require canonical
store derivation paths ending `.drv` and canonical selected output paths;
retain existing identity/role checks. Require each `output` to equal the actual
corresponding original string saved by outer31569. New derivation values are
new observations, not facts to backfill into the old receipt. A malformed
object/type/key, changed machine/source/input/output identity or command error
stops with a clear category and preserves raw output.

This is a caller-owned transport schema correction, not a change to confctl,
the system expression's selected derivations, runtime behavior or public APIs.
No application design amendment or new framework is needed.

## Bounded continuation

Preserve the old runner/manifest/three command receipts and aggregate exit1.
Prepare a fresh no-clobber successor packet with exact expression delta and
hash, parser delta, unchanged source/tool guards and a single new corrected
system-selector invocation. Lead accepts/releases it; parent supplies the fresh
watcher under existing max1 policy. No execution is released by this artifact.

Reuse actual metadata/build-plan successes only with their original bound
inputs and unchanged guards. Do not rerun those commands to correct JSON
wrapper names. After the corrected selector actually passes shape/identity
checks, perform only the previously unrun validity, archive, role-NAR and
recursive metadata gates under the applicable accepted release. Immediate
derivation file/readability evidence remains required before recursive graph
acceptance; JSON strings alone do not prove availability. Any changed dependency
or selection returns to lead rather than being normalized into new expectations.

No output build, source fetch, root mutation, helper installation, current-target
change, claim, deployment or session lifecycle action is included. Session stays
open.

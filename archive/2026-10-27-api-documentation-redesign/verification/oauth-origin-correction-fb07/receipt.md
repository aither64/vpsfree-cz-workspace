# OAuth native form Origin correction

Complete sidecar `6f7aa4449759260e6095870ffccb2fd0870284d6`, tree `e526e62753d6c18218074995761a944e6e61bdd5`, on clean fb07. Scope is exactly the
module, existing OAuth spec and approved generic guide paragraph. The document
uses strict-origin; sensitive OAuth responses default to no-referrer. Exact
Origin, cookie/session CSRF, parser and revocation semantics stay unchanged.

Focused OAuth specs: **80 passed**, seed16029,7.06s plus1.23s load. Two changed
Ruby files lint clean; whitespace and ordinary pre-commit/commit-msg hooks pass.
`make doc` ran exactly once; only the ignored packaged OAuth guide changed,
SHA256 `cd890eb49bcb371d3e484d95ecc1341ecbfccbecbe70e1b6088edbcf1971768d`. All2148
protected inputs,23roots, other905 tracked files, other packaged docs and preview
inputs remain unchanged. No dependency installation or graph change.

Detailed proof: [commit-receipt.json](commit-receipt.json), source-ready.json,
environment.json, doc-copy.json, oauth-spec.log and commit.log.
Rack tests do not establish browser-generated Origin. Affected HIGH auth/security
review and peer native Chromium acceptance follow separately. Correction belongs
to Optional, with later fold/replay owned by2; no fold or push ran here.

Source/Git/hooks ownership released; no active command/uncertain effect. HTTP
preview and session remain open and untouched.

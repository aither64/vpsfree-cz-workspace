# Package 1: Python required login input correction

Owner: implementer1. Baseline `ee150c8515aae399dc14e0fe9daefeb95a8bb17e`.
Design: [api-doc-python-login-contract.md](api-doc-python-login-contract.md).
Diagnosis: [package1-python-challenge-diagnosis.md](package1-python-challenge-diagnosis.md).
Lead granted execution, accepted the bounded helper/Python/harness delta and
applied the main prose pass to the guide. Implementer0 owns all Git/index/hooks.
Prior failed logs, artifacts and receipts remain preserved.

## Implemented behavior

A shared accessor reads actual advertised token request parameters; the existing
JS-facing helper retains exactly its name-based exclusions. Python-only initial
login selection merges in advertised required parameters, including lifetime or
interval when required. It emits the existing JSON environment input convention.
Optional lifetime/interval stay omitted. Existing-token bypass, challenge-owned
continuation tokens, runtime validators/defaults, schema, routes and JS behavior
are unchanged. The acceptance harness supplies JSON `"fixed"`, an explicit
choice from the unchanged advertised enum; no optional interval is supplied.

## Exact owned paths

```text
servers/ruby/lib/haveapi/client_examples/dynamic_helpers.rb
servers/ruby/lib/haveapi/client_examples/python_client.rb
servers/ruby/spec/client_examples/dynamic_python_spec.rb
servers/ruby/spec/client_examples/dynamic_acceptance.rb
servers/ruby/test_support/dynamic_python_login_spec.rb
servers/ruby/spec/client_examples/dynamic_acceptance.md
```

Implementer0 separately owns the shared Makefile target addition, invoking the
new native test beside `test_support/dynamic_protocol_spec.rb`. The native
Python dependency remains outside ordinary Ruby spec discovery, with the same
explicit prepared locked Python component prerequisite; no skip or auto-install.
No client-runtime, generated, dependency or release-artifact path changed here.

## Quick evidence

Prepared tools-only root Nix shell:

```sh
cd servers/ruby
bundle exec rspec spec/client_examples/dynamic_python_spec.rb \
  test_support/dynamic_python_login_spec.rb \
  spec/client_examples/dynamic_acceptance_spec.rb
```

**16 examples, 0 failures**, seed 47466, 3.02 seconds. This includes:

- Both rendered Python mappings use actual unchanged Rack token-request metadata.
  The native test AST-evaluates each emitted `begin_token_login` dictionary with
  explicit JSON environment values, then calls real parse_description,
  parse_resources and build_request. It does not substitute a handwritten map
  for renderer output or replace validation.
- Each mapping sends user/password/scope plus explicit lifetime at exact mounted
  token route, with no optional interval. The actual descriptor's lifetime enum
  is checked to include the explicit test choice.
- Removing lifetime produces exact native errors
  `{'lifetime': ['required parameter is missing']}` before any transport.
- Ordinary pure renderer tests cover required interval selection, optional
  interval omission, existing-token branch and continuation-token exclusion.
- Existing syntax/example and diagnostic subprocess/Rack controls remain green.

RuboCop inspected all five changed Ruby files: **no offenses**.
`git diff --check` passed. `git diff --name-only -- clients/python clients/js`
returned no output. No listener, installed acceptance, build/package operation,
new dependency installation or Git mutation was run by this owner. No command
remains active. Implementer2 received a direct request for bounded API/test
fidelity assessment without source edits or repeat checks.

## Remaining gates

Exact six-path source yield and shared target wiring go through implementer0 for
required hooks and Version-last history consolidation. All intended source must
be committed/clean and the same reviewer must complete the affected four-lane
final review before any installed wheel/sdist acceptance retry. Earlier reviewed
heads and green core checks do not validate the newly corrected renderer.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-22-haveapi-release/

Post-yield read-only proof: implementer0 committed all six owner paths as
`bda2376d` (`fixup! servers/ruby: document maintained dynamic clients`). Exact
owned-path status and the index are empty. Shared target wiring, final fold/head
and affected-lane review remain implementer0/lead-owned; no source write or
verification operation remains active in this owner.

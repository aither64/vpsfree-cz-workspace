# R3 corrected supported-schema remediation — committed

Commit `18b9c73621bb7865bb2f320a7fec295c960734d8`; tree
`543cd44c4a1863489ae2289d2a8769a60e7c1b85`; parent and original reviewed
boundary `b8697c428e759f05d1d9a12f3d83692d02b330de`.
Exact four paths and checked hashes are in `r3-ready.json` and
`r3-commit-after.json`.

The Ruby token client's actual initial-request filter omits false/nil. Ruby's
renderer selects true for an unconstrained Boolean, or another advertised
allowed truthy choice; false/null-only constraints yield an honest limitation.
PHP's real isset filter preserves false but omits null. Its renderer excludes
only null from login choices. Neither public client runtime is changed.

PHP null guard retained on supported OPTIONAL nullable Custom metadata. The
actual server Params object confirms optional?/nullable?: explicit custom:null
validates as null, while omitted custom fills public-choice. Thus omission has
different supported semantics. The real PHP requestToken method demonstrably
omits explicit null, preserves false, and transmits the advertised scalar
alternative public-choice. The renderer never consults the test's default.
An optional null-only choice yields a limitation rather than silently omitting
the field. Continuation false/null and shared JS/Python false/null remain
unchanged, with no input metadata mutation.

Required nullable null was an invalid schema in the earlier supplemental
fixtures. Required-null fixtures and claims are withdrawn, including the
continuation fixture. `19-r3-final-focused.log` and the old readiness snapshot
are retained only as historical evidence, not supported-null proof. Corrected
optional-null proof passed in logs21/22. Final fixture uses a scalar allowed
alternative to avoid relying on empty-container language representation.

Final affected command: syntax_spec.rb plus dynamic_metadata_spec.rb, seed81106,
`23-r3-supported-final-focused.log`:15 examples/0 failures,
0.69717s plus1.6s load. Four-file RuboCop passed in
`24-r3-supported-final-lint.log`. Earlier failures/style results and invalid-scope
checks remain preserved; no broad or long gate was run.

Ordinary frozen-root-bundle commit -F passed mandatory HaveapiI18n, RuboCop,
SingleLineSubject, TrailingPeriod and TextWidth hooks, exit0 in8.623s. No bypass,
setup, installs, config or input changes. Checked=staged=committed=index=current
owned bytes. Source/index clean; all904 other tracked paths/modes, logical flags,
hook files and2148 protected input hashes unchanged. All owned test/lint/commit
commands returned; no utility, watcher or runner is active. Detailed before,
staged, operation and after evidence use the existing r3-* files.

No guide change was useful: adjacent runtime-specific comments explain the
representability constraint and current guide already explains honest limitations.
No make doc, network, listener, dependency, preview, peer, lifecycle or history
operation. SOURCE/Git/hooks slot released to lead; owner2 owns later Core folding.
Lead reconciles narrow correction under mandatory-review step9, preserving the
original full review and recovery boundary.

## Historical initial snapshot — superseded, not current schema proof

The following original ready report contains the invalid required-null claim
explicitly withdrawn above. Its original JSON is preserved in
`r3-ready-before-supported-schema-correction.json`.

# R3 direct review remediation — source/check ready

Original committed review boundary b869 remains unchanged; no Git/index/hooks.
Four owned paths/hashes in r3-ready.json. Runtime control flow confirms
Ruby Token#request_token copies login values only if truthy (false/nil omitted),
PHP Token::requestToken copies only isset values (null omitted, false preserved).
No runtime source/dependency changed.

Existing auth literal selector can exclude renderer-unrepresentable login
values. Default behavior is unchanged; continuation generation bypasses login
hooks. Ruby's hook excludes false/nil, PHP's excludes nil. Unconstrained Ruby
Boolean chooses true; advertised finite choices can supply another representable
value. An explicit false/null-only constraint becomes the existing honest
limitation rather than a runnable-looking example; optional explicit constraints
are not silently dropped. Existing type/finite validation still applies.
No new catalog, solver, framework, config, profile or credential source.

Focused owning syntax/metadata regression proves actual Ruby request_token input
receives truthy options and PHP's actual requestToken preserves false. Both use
existing actual runtime filter methods with only the next request boundary
captured. False/null continuation values and shared JS/Python values remain
unchanged; required false/null-only include/accept cases and optional explicit
false render limitations at both details. Caller description stays unchanged.

19-r3-final-focused.log:15examples/0failures,seed81106,0.727s+1.75sload.
20-r3-final-lint.log:fourRubyfiles clean. One posttest style edit replaced a
redundant Boolean ternary with its identical predicate; no behavioral delta.
First16failure preserved: spec directly called an inherited protected helper;
corrected the test to send, without changing visibility or runtime.18lint style
findings retained/corrected. All16otheracceptedsource/guidehashes unchanged;
all2148protectedinputs unchanged. Whitespace/finalnewline checks clean.

Existing guide already says unrepresentable required fields yield limitations;
no technical fact needs rewriting or make doc. No guide/template/JS/Python/runtime
source, dependency graph, longgate/compiler/listener/network/install/testsetup
or service changed. No active owned process/utility; source/check quiet pending
lead's coordinated reviewfix commit grant. Mandatory review's direct narrow-fix
rules read; no independent reviewer rerun or original-head movement by1.

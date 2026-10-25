# Session observer syntax and signature inspection

Syntax-only command passed exit 0 in 0.404s using the accepted rooted optional
bundle. See [exact argv/result](result.json) and [raw output](syntax.log).
Observer SHA-256 remains
`8d83a20b31634acbf271f3ff1aaf9469a4ff43b5eebc19490cdd510dbb8e4629`.
Actual acceptance runner SHA is
`c62cdc3ba0bf8ea8c6a6c847001ec1739013779a39ceec0caf322dbaa6147cd6`, including the
two accepted legacy-only finalization calls. All six application SHA values
match the yielded/committed receipt before and after this syntax-only action.

Source inspection (no helper/observer execution or reflection):

| Actual interface | Observer forwarding |
| --- | --- |
| public `run!` with no arguments | Calls implicit `super`; ensure records server state after actual shutdown/join. |
| private `prepare_sdk(dir)` | Same argument to `super`; reads/copies the owned generated tree in ensure. |
| private `prepare_programs(dir)` | Same argument to `super`; retains real unformatted renderer output in ensure. |
| private `serve(request, response)` | Same objects to `super`; logs only method/path/status after actual fixture handling. |
| private `verify(name, expected, stdout)` | Same objects to `super`; same return/exception; no replacement assertions or expected values. |
| public `Open3.capture3(*cmd)` | Wrapper accepts `*args, **options, &block` and implicit `super` forwards the same call; returns the same stdout/stderr/status triple. |

Selected Ruby's actual standard library source is
`/nix/store/7b77drpxxyywsxq9hf4y0fc8c56pfivl-ruby-3.4.11/lib/ruby/3.4.0/open3.rb:648`;
it takes `*cmd` and extracts a trailing options hash. The helper's actual call
passes the environment hash, command strings and optional chdir; the wrapper
forwards those, records only allowlisted Go environment fields and does not
modify their contents. It excludes fixture credential variables/HTTP auth headers.

The observer calls actual `GoDocumentationAcceptance.run!` once. The required
helper file's CLI guard does not run on require. Snapshots copy/hash the owned
generated tree at actual prepare/render/formatter/build/final verification
boundaries before the native tempdir lifetime ends. Test and command failures
remain original failures; evidence-write failures are recorded and also prevent
an overall successful observer result. The actual runner/oracle is unchanged.

No syntax or signature defect was found; no observer edit/new SHA was needed.
No helper load, runtime call, test/spec, listener, generation, compiler or network
request ran. This is syntax/source inspection only, **not observer runtime proof**.
The later granted actual batch remains the oracle. No Git action by owner2.

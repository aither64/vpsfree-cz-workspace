# Python supplemental oracle correction — complete

Commit `da1e8186dc5582b198b6838844d6a50ac07bc0ab`; tree `0e72671b95ef3d0893eb83271c4ef2b78993d57a`; parent `5114746f3a9f87e91c704147c0d99dd4f0d32f02`.
Only `servers/ruby/test_support/dynamic_python_login_spec.rb`, SHA256
`bd962c27dafde9e9db18b67169e60096b12d4007e8ff528f4d78b1bd58be52e0`; delta3insertions/11deletions.

Retained release40796243237/511CI step8 rawlog showed7examples/2failures at
seed2782: both sync/async expected fixture-user/fixture-password/all, while M8
correctly rendered user/secret/scope/fixed. The one-file correction uses
ast.literal_eval on the exact begin_token_login argument, removes the obsolete
HAVEAPI_AUTH/SimpleNamespace/eval shim, and asserts envelope status:true before
using its response. Exact body/URL, mandatory lifetime, include-fixed,
optional interval and missing-lifetime ValidationError assertions remain. Native
parse_description rejects unsuccessful envelopes and subprocess status gates
all returned data; no failure is suppressed or counted as success. No runtime,
renderer, fixture, provider, schema or guide changed.

The existing two-spec supplemental command ran once at seed2782:
7examples/0failures,8.95s+1.21s load (focused.log). Scoped RuboCop1file clean
(lint.log), whitespace clean. Existing Python .venv/rooted3.11.17 and immutable
Ruby3.4.11/frozen server bundle used; no setup, package resolution or install.
Ordinary commit-F passed mandatory HaveapiI18n/RuboCop and message hooks,
exit0/5.993295s (commit.log and commit-exit.json). No bypass or retries.

Checked=staged=committed=index=current owned bytes. Other907tracked source
modes/hashes,2148protected inputs,root/server/Python locks,logical flags and
hook bytes unchanged. Source/index clean, owned rspec/lint/commit handles ended,
no owned processes/utility. Before/staged/after proofs preserve exact bindings;
old CI failures remain untouched. SOURCE/Git/hooks slot explicitly RELEASED to
lead and owner2 for authorized one-file Core folding. No push/fold/CI/network/
makeDoc/preview/service/provider/lifecycle or other gate executed here.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-27-api-documentation-redesign/

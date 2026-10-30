# M8 Rust CI wording correction — SOURCE/CHECK READY

Raw CI run40773074124 rust-client generator unit step at reviewed24ec records
159examples/15failures. Thirteen invalid-source cases expect old visible wording
`invalid Rust SDK source`; production already emits `invalid Rust API client source`.
Two async/blocking unavailable-provider examples expect `authorized Rust SDK
profile`; production already emits `authorized Rust API client profile`.
The original raw CI log remains unchanged; hash and exact result are in ready.json.

Only two expected string occurrences changed, one each in
clients/rust/spec/unit/documentation_factory_spec.rb and
clients/rust/spec/unit/documentation_performance_spec.rb. The first shared
expectation still executes all13 invalid source cases. All rejection/error type/
provider/privacy/schema/normalization/performance assertions and fixtures remain.
No production/runtime/machine identifier/workaround or broader SDK replacement.
Exact full-index diff: expected-only.patch; checked file hashes:

- `clients/rust/spec/unit/documentation_factory_spec.rb`: `e4008d66d311f5ae1d2862b90d70c4047dea1ea4ccdbed31b94a7b1c82c339b2`
- `clients/rust/spec/unit/documentation_performance_spec.rb`: `8294316723beb4c71b24366926c6cc3f3a258291b3da103b1d94bae49680ff94`

Affected existing two Ruby unit files ran ONCE:46/0, seed50232. Scoped lint2files
clean. Uses exact declared Ruby3.4.11, existing isolated Rust frozen bundle and
normal default gems, no dependency resolution/install, Nix realization, compiler/
rustfmt/generator/wire/performance gate/tool-version/listener/network/utility or
make doc. Logs/commands/exits/elapsed are adjacent. These checks do not claim
all159 CI examples, compiler acceptance or a successful rerun of CI.

All2148 protected hashes/root+component locks preserved. Logical index+flags and
HEAD unchanged; owned changes UNSTAGED. Other owners' paths were not edited; their
observed concurrent status is retained before/after. Owner0 boundaries are
validators_spec/identity_and_guides/documentation_validators/brand, no overlap.
Direct confirmation was twice refused by session-command contention; lead is
informed. No Git mutation/hooks/commit occurred, no active owned command.
Await M8 written adapter/handler design grant; later collective-quiet serial
commit will include this with the whole owned modern adapter package.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-27-api-documentation-redesign/

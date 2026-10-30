# Go mounted-context capture fixture correction

Commit `463e503db3611cc0f37958ad522801eb17bff361`, parent `24ec424c9592951da38584379b43379b0c39f115`,
tree `bdc83a4e1dc3636bd890f46dc83bdc49a6f1cec6`. Only servers/ruby/spec/documentation/client_examples_spec.rb changes.
The capture case intentionally stubs Go availability/render without a configured
profile. Its remaining real capability query dereferenced that absent profile.
The mock now declares the wrapper's inherited frozen detail pair alongside its
availability. Both variants and all existing URL/context/resource/action/sample
assertions remain; production availability/query/profile strictness is unchanged.

Existing file6/0, seed65511; scoped lint1 clean and owned whitespace pass.
The first lint run required receive_messages; that diagnosed log is preserved.
Ordinary HaveapiI18n/RuboCop/precommit and message hooks all pass with existing
repository-declared immutable Ruby/Git/Bash tools and frozen root/server bundles.
No tool restoration, installation/resolution, network, compiler/listener/full
suite, docs copy, CI retry, utility or runtime normalization was performed.

Checked/staged/committed/current SHA256 `fcde0dcfec2facacd3faa4c0279c88737061b2a53bc5d89f87696d347b318835`; exact one-path
full-index delta in delta.patch. Index/worktree clean;2148 protected hashes,
root/server locks and logical index flags unchanged. Existing24ec CI failures,
allclient/timing results and performance exports retain their actual scope.
No production boundary defect was identified by this fixture correction.
No active/uncertain process; SOURCE/Git/hooks slot explicitly RELEASED.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-27-api-documentation-redesign/

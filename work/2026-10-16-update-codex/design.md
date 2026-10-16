# Codex upgrade and layered procedures

## Ownership and scope

The operating conversation owns design and implementation; no team was selected
at shell-only creation. Native conversation binding is being established for
review/deployment coordinates, without assigning application work to that idle
anchor. Use the installed default review-purpose policy for independent review
if no eligible retained reviewer exists. Substantive design uses xhigh.

Four skills have distinct names: update-codex (workspace),
update-aitherdev-codex (configuration), update-dev-workspace-codex (runtime),
update-codex-web (protocol library). Each repository's instructions link its own
entry point. The parent reads the dependency skill from an explicit checkout or
the exact selected source; it must not silently use an unrelated checkout.
The call order is workspace -> configuration -> runtime -> protocol library.
Parents coordinate session/review/deployment gates once and carry the returned
selected version, source revision, catalogs, commits and check evidence upward.
Standalone calls follow their local repository's normal gates. The runtime
installs its own and the selected codex-web skill through the core catalog; the
workspace installs its entry point through the existing extension override while
preserving organization skills.

## Selected input and interfaces

Freeze Codex 0.163.0 from llm-agents revision
e85b99217baf13a38fc887b31338b1833f1159c0, checked against upstream's stable release
on 2026-10-16. No new public Go API or browser capability is intended. Validate
all existing request sites, consumed event fields and fixed policy keys/types
against exact candidate schemas; retain tenant/browser capability boundaries.

Refresh the full upstream catalog fixture and provenance, then derive the Luna
catalog with only the existing direct tool mode, empty experimental tool list
and disabled Responses Lite changes. Recalculate immutable hash bindings in
client preflight, package assertions and docs. Update naming's exact version
prerequisite and its actual-binary tests together. Keep old manifest/version
fixtures where they test retained installations; do not globally replace 0.160.0.

Publish codex-web first, then align the runtime's Nix source pin, Go pseudo-version
and checksum. Freeze llm-agents at the selected revision, not a later moving main.
Configuration updates use confctl channel set for exact feature/runtime and
llm-agents revisions; keep generated commit messages. Workspace uses the existing
direct nested runtime override and scoped flake update. Do not change extension
pins or unrelated sibling lock identities. Each pin stream has one final commit.

## Native package and persisted state

Keep mkCodexPackage because upstream resources are still linked. Upstream now
patches native daemon selection to its immutable original Nix-store output,
disables upstream release updates for that selection and attempts a GC root.
The copied executable can therefore start that original output rather than the
assembled copy. Its embedded original reference retains that closure; verify
this and document actual installed-package behavior. Preserve existing roots and
retained releases. Do not alter the Rust patch locally or remove assembly in
this initiative merely because upstream added a manifest.

No workspace state migration is introduced. Each old/new package retains its
own protocol client and immutable catalogs. Native state migrations remain an
upstream compatibility concern: use private disposable old/new homes and saved
threads to test startup, resume/fork and reader behavior. Do not expose copied
production credentials or rewrite shared Codex configuration. Application
recovery stays forward-only; system generations remain available, but downgrade
state support must be demonstrated before it is recommended.

## Verification and acceptance

Quick checks: skill-creator quick_validate, source diff checks, focused Go/Ruby
and browser tests from declared Nix environments, request corpus coverage,+candidate generated experimental protocol and exact config-schema validation.
Resolve unsupported requests/policies without weakening utility restrictions.
After final commits and quick checks, run independent general, architecture,
scope and risk review including whole-branch histories and no-migration inventory.

Long checks after review: repository Nix checks, package layout/native identity
and closure tests; native namespace ownership before hostile-dispatch ephemeral
integration for GPT-5.5 and Luna; managed naming child lifecycle, ordinary-daemon
continuity, positive naming canary within ten seconds; retained conversation
startup/resume/fork and mixed old/new state probes. Fresh Luna/low watchers own
long commands and report exact revisions/logs. Build the exact final workspace
application and aitherdev configuration and run the existing composed deployment
contract. No unexpected local kernel builds are acceptable.

## Deployment and recovery

The user authorized system and application rollout, not default-branch merges.
Use one coordinator aitherdev reservation and explicit system-before-profile
dependency. Prepare and copy outside mutation claims. Changed native invocation
requires idle sessions: wait without interrupting unrelated work or bypassing
admission. Verify exact running system/profile/native identities, service health,
provider startup, naming and retained conversations. Keep reservation through
review; release requires normal final integration proofs and therefore is not
claimed while branches are unmerged. Reconcile uncertain effects through the
original jobs and preserve journals, native roots and prepared artifacts.

## Managed DeepSeek profile acceptance correction

The native 0.163.0 schema rejects preferred_auth_method and
model_supports_reasoning_summaries. Remove those obsolete managed settings.
DeepSeek's env_key supplies its API authentication independently of the shared
OpenAI login. Remove forced_login_method from this custom-provider profile:
native exec enforces that restriction against shared auth before selecting the
provider and can remove a conflicting ChatGPT credential. Keep the endpoint,
model, effort, key source and catalog selection unchanged. The user base
configuration and credential storage remain outside the implementation change.

Validate credential preservation using synthetic auth and an empty prompt before
any real request. Run the one real provider canary in a private home containing
only the exact corrected managed profile, with no copied login credentials.
After final activation, prove actual deployed profile loading stops at the empty
prompt without changing shared authentication; compare semantic profile and
wrapper identities with the isolated provider canary. Help output short-circuits
configuration loading and is insufficient evidence. Preserve all failed-attempt
and recovery records privately without credential values.

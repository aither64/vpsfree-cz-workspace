# GitHub IRC notification filtering

## Goal and authorization

Implement the plan requested by the user on 2026-10-02: filter push commits by
original author in #vpsfree, suppress wholly ignored pushes, and add exactly six
repository routes to #vpsadminos. The user selected author-only matching and
explicitly declined other repository additions. Implementation and verification
are authorized. Default-branch integration and production rollout are not.

## Affected repositories and ownership

- vpsfree-irc-bot: optional channel filtering, parsing/rendering, specs and docs.
- vpsfree-cz-configuration: Libera instance routes/filter and fixed bot source pin.

architect0 updates design.md before substantive code; implementer0 owns source
edits, hooks, quick checks and focused fixtures. Lead owns tracking, scope,
user-facing prose polish, review coordination and acceptance. reviewer0 remains
independent under mandatory-change-review. Fresh catalog Luna/low utilities own
long or uncertain verification. Saved team settings/access are retained.

## Accepted behavior

Use optional per-channel ignored_users, empty by default. Enable only on
#vpsfree for github-actions[bot]. For nonempty push payloads, filter original
authors using author.username; when absent derive username from a GitHub noreply
email (plain or numeric-ID-prefixed). Unknown identities remain. Do not use
committer/pusher/event sender to override commit author. If no commits remain,
send/log nothing. Mixed pushes display only retained commits in source order,
with retained counts/overflow and at most ten displayed. If exclusions occurred,
label the summary as announced commits with ignored count. Keep the original
full comparison URL. Force/fast-forward pushes retain their update heading and
show retained commits when filtering is enabled. Originally empty eligible
pushes retain old ref-update behavior and use sender filtering. Non-push events
filter sender. Preserve existing gates, signature verification, legacy arrays
and exact behavior for absent/empty filters. Avoid shared-event mutation and
filter independently for each destination.

Add ONLY these full names to #vpsadminos, preserving existing coverage:

- vpsfreecz/vpsadmin-webui
- vpsfreecz/vpsfree-kb-contracts
- vpsfreecz/ruby-lxc
- vpsfreecz/vpsf-status
- vpsfreecz/ssh-exporter
- vpsfreecz/syslog-exporter

Template routing is already correct; no rename repair. Existing configuration
has one IRC instance (Libera) and a Matrix bridge for both channels.

## Compatibility, deployment and recovery

No schema/persistent-state or protocol changes and no vpsAdminOS fleet update.
New bot with old/empty configuration retains behavior. Old bot ignores the new
option and resumes automation noise: activate the tested bot pin/hash together
with configuration in any later authorized rollout. The Nix module uses free
settings attrs; no module or flake-lock update. Preserve logs/state and rollback
the bot/config pair together. In-memory queues may lose pending events on
restart. Hook coverage, private overrides and actual deployed revision remain
unverified. No production messages/replays during local tests.

## Documentation

Design.md is the implementation/verification brief. Bot README/sample config
own the durable option/behavior contract. Session records own source heads,
review inventory, test evidence and future rollout details. Apply the main-agent
vpsfree-user-facing-writing skill before committing user-visible prose.

## Verification and readiness

Quick RSpec/lint/hooks cover all-ignored/mixed/human/unknown author pushes,
identity conflicts, noreply fallback, force/fast-forward/empty pushes, display
limits and cross-channel isolation; preserve legacy behavior. After intended
changes are committed, inventory complete branch series/diffs and no-migration
provenance, then mandatory independent review (general/architecture/scope/risk).
After resolving findings, run isolated signed-webhook-to-IRC coverage and scoped
configuration build through fresh watchers. Publish feature refs if needed to
resolve the fixed source pin, retaining refs and SSH remotes. No merge/deploy.

## Verification-discovered logger reliability correction

The two-channel VM reached the expected IRC output but exposed missing second
channel logging. Implementer reproduced a pre-existing HtmlLogger race with
immutable Nix assets: concurrent constructors copy to a shared destination before
chmod, and one raises EACCES before ChannelLog assigns its logger. Root cause
for the VM is inferred because initial journal was not captured, while the
constructor failure is directly reproduced. This blocks meaningful archive
verification and can affect cold-start multi-channel logging.

Lead authorizes a bounded reliability correction within implementation;
architect records minimal synchronization, permissions/update semantics and
deterministic regression before edits. Keep notification contract/routes intact.
No persisted format/dependency/module changes. A separate functional logger
fix commit remains reviewable; final package pin follows final bot head/hash.
Expanded final source range gets independent review before VM rerun.

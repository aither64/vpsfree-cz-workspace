# Disabled v0.1.0 recovery proposal

The reviewed additive fix is `b6f84679d33ff041388535dcf4dc060aeb0d1b9d`. Its real credential-free SDK candidate passed. The new automatic feature CI is still being observed. No tag recovery is authorized or performed.

The existing public `v0.1.0` annotated object `c4f258b77dadf8057630c371152a607151b1c3e1` points to `63b87e9a`. That source’s workflow fails after a successful dry run because it looks at the standalone-package output path. Its run, protected approval, full logs and absent candidate/publish artifacts remain retained unchanged. The source fix does not change that public tag.

If the user still requires version 0.1.0, the proposed ordinary workflow route needs explicit authorization for exactly one tag replacement and an exception to the repository instruction **“Never move a release tag or overwrite a published version.”** Preserve the original annotated object in an exclusive local archive ref and its raw object/remote proofs before constructing a distinct annotated object at the reviewed fix. A later authorized remote update must use an exact-old-object compare-and-swap lease; any drift or ambiguous effect stops for reconciliation. No blind force, tag deletion window or source history rewrite is proposed. Main integration is unnecessary and remains unauthorized.

Only after that explicit decision and a separate concrete lead route may a new release workflow be dispatched at the new immutable object. It must perform its own mandatory verification and run-lock resolution; protected approval remains lead-owned. Preserve each original native candidate and actual upload archive and obtain independent public checksum/content proof. A local dry-run or CI package cannot stand in for the upload stream. Any needed public registry-state check belongs to its assigned owner, not this proposal.

If the user declines the exception, preserve the old tag and ask for a version choice. This packet does not choose a new version or create a fallback publication procedure. [binding.disabled.json](binding.disabled.json) records exact accepted source/native evidence and all disabled effects. No Git/ref/provider/registry/settings/credential operation was executed for this proposal.

[Session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-22-haveapi-release/)

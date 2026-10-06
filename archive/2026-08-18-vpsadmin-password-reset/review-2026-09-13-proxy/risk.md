# Risk and compatibility review

Reviewer: fresh risk-and-compatibility lane. I reviewed the committed proxy
correction and retained configuration series directly. I did not launch nested
agents, mutate a project, branch, cluster or session, install dependencies, or
run builds or integration tests.

## Findings

No Blocking, Important or Advisory findings.

## Evidence

I inspected the correction delta
`a4c43133ee98057e79a3355ecb5d4bad814b4957..0e0a985ad5daa12ab5ad50fec5ac4cf55b204358`
and the retained series
`8ef765d339ac792ef4f01a5c7a160e48600adcaf..0e0a985ad5daa12ab5ad50fec5ac4cf55b204358`,
including commit topology and messages. The candidate descends from the fetched
default head. Its four pre-existing retained feature patches correspond to the
pre-correction series, while the temporary local route commit is absent and the
new cleanup commit follows those four patches. A direct range diff confirms the
four retained patches are equal and marks only the route patch as dropped.

The proxy still declares only its established `nixos-stable`, `os-staging` and
`vpsadmin` channels at
`cluster/cz.vpsfree/containers/prg/proxy/module.nix:3-10`. Removing the machine
overrides therefore resolves it to `nixpkgsStable` at
`21a67dc470149f337cecafbe965d8d252a390518`, `vpsadminosOsStaging` at
`c065fa2f8485399737e20e8ef9e44299d0766654`, and `vpsadminServices` at
`050ea5263812a76dc39f14c5b58a0e88714d634d`. The packet's
`input-validation.json` compares all 108 exported machine mappings: only the
proxy changes. Its recursive lock check also shows that every retained root
input graph and revision is unchanged; the four removed root inputs and nine
removed transitive nodes are unreachable after the override removal. I found
no pin mismatch, accidental change to another machine, or node deployment or
protocol change.

The final
`cluster/cz.vpsfree/vpsadmin/common/frontend.nix` is byte-for-byte equal to the
same file at configuration default head `8ef765d3`, so removing the local route
does not retain a second owner. At exact vpsAdmin pin `050ea526`,
`nixos/modules/vpsadmin/frontend.nix:246-289` emits `/_auth`, `/webauthn` and
`/oauth2/password-reset` for every configured auth virtual host. All three use
the same `isUnderMaintenance` predicate from lines 174-179. The supplied
18-value evaluation covers the production and administrative auth hosts under
normal operation, selected global production maintenance, and instance
maintenance; the recovery route matches the established auth-route proxy/503
behavior in every case. The full proxy toplevel also evaluates to a concrete
NixOS derivation with the intended new `nixpkgs` revision.

Mixed-version behavior is safe within the documented rollout boundary. The
runbook keeps recovery disabled until templates, migrations, both APIs, both
WebUIs, the auth frontend and OAuth-client settings are ready at
`docs/operations/vpsadmin-password-recovery-deployment.md:105-113`. It deploys
the proxy only after both APIs and both WebUIs are upgraded, then verifies the
generated route and its disabled-feature response at lines 279-299. If the new
API is temporarily paired with the old proxy, recovery remains inaccessible;
if the new proxy is paired with an API where the endpoint is disabled or
absent, the added proxy location conveys no additional backend authority.

The dependency advance affects all services on the shared proxy, not only the
auth route. The runbook states that scope, requires review of the system
generation diff, and requires retaining the preceding generation at lines
25-30. Its rollback restores that exact generation, keeps recovery disabled,
and calls for verification of the other proxied sites at lines 466-476. This
provides a compatible rollback boundary for the route and package/module
changes without changing persisted application or node state.

## Residual validation limits

The candidate proxy toplevel has been evaluated but has not yet been built.
Consequently the actual old/new closure package diff, build-time module checks,
and final generated Nginx configuration have not been inspected. Those checks
are particularly relevant because the proxy moves from its June/July
`nixpkgs`, vpsAdminOS and vpsAdmin baselines to September channel revisions and
hosts unrelated shared-proxy workloads. The packet explicitly places the full
proxy build, closure review and generated-Nginx inspection after this mandatory
review, and the runbook makes the generation diff a deployment prerequisite;
this is a remaining integration gate rather than a defect in the committed
change.

No live proxy switch or rollback has been exercised. The retained-generation
procedure therefore remains operationally unproved for this exact closure, and
the eventual rollout must preserve the preceding generation until all proxy
workloads have passed their checks. The current declarative health checks cover
Nginx plus the main website and Czech KB; they do not by themselves exercise
every virtual host or exporter on the shared proxy.

The route matrix evaluates the exact pinned frontend module in isolation with
representative host names. It proves route ownership and maintenance selection,
but the final proxy build and `nginx -T` check are still needed to detect an
interaction introduced elsewhere in the complete machine composition. No API
or application tests were repeated because that implementation is unchanged
by this correction.

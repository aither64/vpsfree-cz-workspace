# Independent final review

Reviewer `/root/final_review`, native thread
01a18207-9269-71d0-8c5a-f2c6c6face8a, gpt-6.1-sol/xhigh verified from its
thread_settings_applied record. Installed default delegated reviewer fallback;
threadless operational session has no roster. All four mandatory lanes covered.

Reviewed runtime 4a002f52..a77fcc8f and workspace 60ed89b75..fecd5aed.
Scope was proportionate. Each branch contains one coherent feature/guidance
commit, with no obsolete approaches, fixup history or repeated update streams.
No migrations: private schema 1 introduced directly, unmerged, undeployed,
unreleased and not externally consumed. Chat consent is lead policy under the
trusted-local-operator model. Browser origin/generation and native MCP caller
binding were accepted. Mechanical deployment pins need final confirmation.

One Important finding (general/risk): admission used the full 16 MiB state limit,
leaving no space for later envelope/options/receipt or revocation/cancellation.
This could leave a grant active and archive/delete stuck after journaling.

Remediation: store the message envelope on admission, reserve bounded delivery
options/receipt plus transition overhead for every live message and grant.
New work refuses before using recovery capacity. Oversized options hold before
submission; unexpectedly large native receipts retain confirmed delivery status
without the receipt. Boundary tests fill the admission budget and prove delivery,
revocation, pending cancellation and lifecycle expiration remain writable.
The new explicit option/receipt bounds receive focused general/risk follow-up.

Remaining verification at original review: Playwright, packaged/native checks,
and deployed lifecycle/exchange acceptance. No long tests ran during review.

Follow-up: same reviewer accepted the capacity fix at d812fe68, confirming
reserved growth, boundary coverage, consolidated history and no migrations.
It identified one Important upgrade-documentation omission: policy-1 host
commands cannot decode policy-2 startup registration. Corrected the guide to use
`nix run .#workspace-host -- switch --source "$PWD" --from-candidate` for the
initial upgrade, retaining claims, idle checks and recovery; linked the existing
candidate transition explanation. This is the reviewer's narrow requested doc
fix, verified by direct source/anchor inspection without another review turn.
No unresolved Blocking or Important findings remain. Long checks may proceed.

Supplemental UI/history review passed without findings in
transcript-final-review.md. After the packaged lead-policy regression, the same
reviewer accepted the narrow binding correction and final histories/pins in
policy-followup-review.md. Final runtime e9153e61, workspace 31a3deb34 and
configuration b4b0c17b. No unresolved findings; long checks may resume.

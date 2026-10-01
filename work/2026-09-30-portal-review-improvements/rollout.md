# Aitherdev rollout record

This record describes the individual aitherdev rollout for the portal review
initiative. Reusable deployment and recovery behavior remains in the owning
project documentation.

## Selected revisions

- Configuration: `ee99382c8c448a15347052a6964030f838cb0381`
- Deployed workspace composition: `45cce0a87d3f0c8d2b404ce7188d8fa0d9098154`
- Deployed generic portal: `50af66d9cfc1be07dcc4cb084de4887dd97a343c`
- Deployed extension: `8e04f2626a3abd492768f15ae8d843c8e527f2cd`
- Codex package input: `af40d966859ec4075ecc172dbb39e53f474dc5d9`
- vpsAdmin API: `5c76e3290481b297dcd0baa76d246133f0353d8f`
- vpsAdmin WebUI: `534caa83a5f97d2b40b4a126886649b14dc9e8d3`

The deployed runtime revisions are generic `50af66d9`, extension `8e04f262`
and workspace `45cce0a8`. Configuration `d24b2515` remains an unselected DNS
candidate. Generic final branch head
`50586880` is a separately reviewed verification-fixture correction with
unchanged runtime source; the architect and reviewer accepted retaining the
existing runtime pins and built package. The Origin-label and React-container
autostart corrections are selected in the user profile and cluster. The
internal-DNS candidate is committed but publication to its four shared
consumers remains unapproved.

Mandatory final review found no Blocking or Important issue at those four
heads or in the bounded fixture follow-up. Final generic, extension and
workspace flake checks pass at the runtime revisions, and the final
workspace package is
`/nix/store/51i6gp92srgvqcmmwfv8qsg9xq9xfdqf-dev-workspace-0.2.0`. Build-only
evaluation also passes for each of the four exact internal-DNS consumers.

The optional fixture correction at generic `50586880` passed its independent
follow-up review, declared Node syntax, three focused lifecycle runs, all six
browser cases, generic flake checks and exact-head CI. The retained extension
`8e04f262` also passed the complete rooted packaged smoke. The unrooted attempt
was interrupted by host GC, as proved by its journal; the rooted retry needed
no source change. Detailed results and log paths are in [state.md](state.md).

## Executed system and profile rollout

Fresh Luna/low watchers built only `cz.vpsfree/machines/aitherdev`, dry-activated
generation `2026-09-30--21-42-52`, and switched that same generation. The
running system is
`/nix/store/cb7sziy9ijyf2sxw1ajdbjwrzj2ac591-nixos-system-aitherdev-26.05.20260928.7fc6f2c`
with Codex 0.159.2. Firewall state, system and user units, and the workspace
router/portal/Codex services were healthy after the switch.

The guarded user-profile transition selected
`/nix/store/aidlqw1p8dxijyd35jn7fxr6avzkqvc9-dev-workspace-0.2.0` after an
earlier in-progress-turn refusal. Reconciliation finished successfully and left
no pending marker. The live portal lists exact `gpt-6.1-sol`; an atomic settings
write to that model with xhigh effort persisted on readback. Disposable staged,
unstaged and untracked probes returned immutable comparisons and were removed.

After the final checks, the user ran the verified guarded transition while this
conversation was idle. The selected profile now resolves to
`/nix/store/51i6gp92srgvqcmmwfv8qsg9xq9xfdqf-dev-workspace-0.2.0`, built from
workspace `45cce0a8`. The live portal renders `Origin`, ships Load all diffs and
the atomic settings client, and lists exact `gpt-6.1-sol` with every supported
effort.

## Executed bridge-cluster rollout

A fresh Luna/low watcher started the session's single-node bridge cluster. The
selected result reported clean pinned WebUI revision `534caa83`. The existing
PHP UI was available, while the first React requests returned 502 because
`container@newadmin.service` was inactive, linked and had no install target.
This identified the missing container autostart setting now being corrected in
the unmerged extension feature commit.

A supported manual service restart started `newadmin` for diagnostic acceptance.
The following checks then passed:

- public React routes, health, static asset, config and build metadata;
- cluster-CA trust and expected certificate names;
- legacy PHP availability;
- API CORS for the OAuth token header without credentialed cross-origin use;
- loopback-only nginx and BFF listeners and nginx configuration validation;
- exact clean frontend/BFF build revision and absence of retired secret
  environment names;
- real seeded-user OAuth login and callback, one-use state rejection,
  authenticated session and API access;
- forced access-token expiry followed by refresh and accepted refreshed token;
- stable session identity after a BFF restart;
- two repeated OAuth seed executions;
- logout, anonymous session readback and rejection of the revoked access token.

Credentials, cookies, authorization codes, states and tokens were kept in
mode-0600 temporary files and deleted after the checks. Their values were not
recorded in session artifacts or command output.

## Final runtime activation

A fresh real OAuth login established an authenticated session before the final
update. A fresh Luna/low watcher then ran the selected helper's supported
`update 2026-09-30-portal-review-improvements services`; it completed in about
7m25s and activated services system
`/nix/store/vv7b9mhcrmj1fii3jb6r0k1craclnynq-nixos-system-vpsadmin-services-26.05pre-git`.

Post-update checks prove that the cluster is running, ready, single-node and on
bridge networking. `container@newadmin.service` is active, enabled and wanted
by `machines.target`; it requires and starts after the successful OAuth seed.
The selected source record is the clean session worktree at exact WebUI
`534caa83`. Nginx and the BFF are active, ports 18082 and 3001 remain bound to
loopback, health and legacy PHP return 200, the authenticated session retained
the same session key, and authenticated API and CORS probes return 200. The
path-based local WebUI build reports unavailable embedded Git metadata; the
cluster's immutable selected-result source record remains the authority for
the exact clean worktree revision. Temporary credentials, cookies, states,
codes and tokens were removed after the checks.

No default-branch integration is part of this rollout.

## Prepared internal DNS generations

Configuration candidate `d24b2515` is built for all four independent private
zone consumers. Complete build output:
`/tmp/portal-review-internal-dns-four-builds-d24b251.log`. Each generated BIND
configuration references a rendered zone with serial `2026093000` and exactly
one newadmin CNAME to the existing aitherdev frontend. Validation with that
generation's BIND `named-checkzone` returned OK for all four.

| Target | Built generation | System toplevel |
| --- | --- | --- |
| cz.vpsfree/containers/prg/int.ns1 | 2026-09-30--23-24-31 | `/nix/store/aq3qibcnf3d4byw5c9sfi98d9yf4k1qx-nixos-system-ns1-26.05.20260928.7fc6f2c` |
| cz.vpsfree/containers/brq/int.ns1 | 2026-09-30--23-27-01 | `/nix/store/imcbgk4d5gb12lgm254l4sk8i5fk0v6z-nixos-system-ns1-26.05.20260928.7fc6f2c` |
| cz.vpsfree/containers/prg/int.mon1 | 2026-09-30--23-27-52 | `/nix/store/as30hhqffjmldi8qcjj1w0xdgb359p80-nixos-system-mon1-26.05.20260928.7fc6f2c` |
| cz.vpsfree/containers/prg/int.mon2 | 2026-09-30--23-28-53 | `/nix/store/zxn6i3r0r341lbvn0qbrdh4arngxxhfz-nixos-system-mon2-26.05.20260928.7fc6f2c` |

Dry activation and publication require explicit approval for these exact four
shared hosts. That approval request is pending. Building and validating these
generations did not publish the zone.

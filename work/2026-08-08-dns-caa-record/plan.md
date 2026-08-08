# 2026-08-08-dns-caa-record

## Goal

Add CAA records to vpsAdmin's internally sourced primary DNS zones. Users and
administrators must be able to create, inspect, update, disable, and delete CAA
records through the existing API and WebUI, and both authoritative DNS servers
must serve the expected RDATA.

The initiative also pins the final reviewed vpsAdmin feature revision in the
`vpsadmin` channel of `vpsfree-cz-configuration`, prepares any affected Czech
and English KB documentation, and deploys the local workspace VM dev cluster
for end-to-end review. It does not deploy live systems or publish production KB
pages.

## Repositories and interfaces

- `vpsadmin`: add `CAA` to `DnsRecord::RECORD_TYPES`. Keep the existing API
  shape and store CAA `content` canonically as `<flags> <tag> "<value>"`, for
  example `0 issue "letsencrypt.org"`.
- `vpsfree-cz-configuration`: create the same-slug feature worktree from a
  freshly fetched `origin/master` and pin the final reviewed vpsAdmin SHA with
  `confctl inputs channel set --commit vpsadmin vpsadmin REV`. Keep this change
  on the feature branch; do not integrate configuration `master` or deploy any
  live host.
- `vpsadmin-kb-captures`: pin the same vpsAdmin SHA, run the documentation
  contract, and prepare bilingual candidate changes for the existing primary
  DNS pages when needed. Do not invent a navigation concept or screenshot and
  do not publish without later explicit production approval.

No database migration, generated client update, HaveAPI change, vpsAdminOS
change, or DNS node protocol field is required.

## vpsAdmin implementation

- Accept flags `0` and `128` and the dnsruby-supported non-reserved tags
  `issue`, `issuewild`, `issuemail`, `issuevmc`, `iodef`, `contactemail`, and
  `contactphone`.
- Normalize outer/inter-field spaces and tag case. Require a non-empty,
  single-line printable-ASCII value; preserve spaces and semicolons, including
  the denial value `;`, but reject embedded quotes and backslashes. Do not
  interpret tag-specific parameters or alter issuer names and URLs. Reject a
  CAA priority through the existing non-MX/SRV rule.
- Limit canonical CAA content to 64,512 bytes. This leaves a deterministic
  1-KiB margin below BIND's 64-KiB rendered-record boundary, including the
  owner, TTL, class, type, whitespace, and newline added by the zone renderer.
- Add model validation and operation normalization, exhaustive API valid and
  invalid cases, explicit create/update normalization examples, and metadata
  coverage for the WebUI CAA choice.
- Add CAA-aware Prometheus answer comparison by numeric flags,
  case-insensitive tag, and exact value. Keep libnodectld's generic non-TXT
  renderer unchanged and freeze its create/update/delete pass-through behavior
  in specs.
- Add CAA to the existing DNS runtime tables. Exercise creation, BIND health,
  authoritative lookup, update, and deletion through the transaction and
  reload path, and reject malformed/multiline content before creating a chain.

## Compatibility and deployment

- Existing rows and transaction payloads remain unchanged. New APIs work with
  old libnodectld because canonical quoted CAA content uses the existing generic
  renderer; no coordinated DNS node or vpsAdminOS rollout is required.
- An old API can still load and serve persisted CAA rows after rollback, but it
  cannot validate edits. Remove CAA rows or roll forward before a planned API
  downgrade.
- Pin the exact final reviewed vpsAdmin feature SHA downstream. If review fixes
  change that SHA, regenerate the configuration and capture pins before long
  tests.
- Build all `vpsadmin`-tagged configuration consumers in a single confctl
  process. If the known unrelated `vpsfreeWeb` NAR hash mismatch blocks
  evaluation, record it and continue local dev-cluster validation without
  changing that input.
- Use the single-node workspace VM topology and bridge network. Before start,
  ensure no other VPN-visible cluster is running and shared
  `dev-clusters/vpsadmin` tooling contains no unresolved unowned changes. Leave
  the healthy cluster running for user review.

## Verification and order

1. Implement vpsAdmin and run focused API, operation, Prometheus, libnodectld,
   WebUI source, RuboCop, CI-selection, and hook checks.
2. Commit and push vpsAdmin. Pin its exact SHA in configuration and captures,
   validate both downstream repositories, commit, and push their feature
   branches.
3. Run the required standalone fresh-context mandatory change review across
   all committed repositories. Resolve significant findings and refresh pins
   when the vpsAdmin head changes.
4. Run `dns/server-zone-lifecycle`, `tasks/prometheus-export`, and
   `webui#networking-dns`; inspect pushed GitHub Actions and failed artifacts.
5. Enumerate `confctl ls --tag vpsadmin`, then run
   `nix develop -c confctl build -y --tag vpsadmin` without parallel confctl
   processes.
6. Start with
   `dev-clusters/vpsadmin/bin/devcluster start 2026-08-08-dns-caa-record
   --topology single --network bridge`. Verify VM/systemd/API/WebUI/DNS health.
   Create a `.test` zone and `0 issue "letsencrypt.org"` CAA record in the
   WebUI, query both `172.16.106.61` and `172.16.106.62`, update it to an
   `issuewild` value with a parameter, verify again, then delete it and the
   temporary zone. Check API, named, and nodectld logs and leave the cluster
   running.

Standards: RFC 8659 and the IANA Certification Authority Restriction
Properties/Flags registries.

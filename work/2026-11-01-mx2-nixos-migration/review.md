# Independent final review — mx2 import/rebase

Reviewer0 report delivered via report_to_lead; recorded by lead because reviewer
is read-only. No Blocking or Important findings for the bounded import/rebase.
Proceed to targeted build. This does not approve production replacement.

## Findings and lead reconciliation

1. **Advisory, risk/compatibility:** inherited configuration cannot receive/relay
   public backup-MX mail. Config transports three domains, but effective
   `relay_domains` is empty, `mydestination` is local-only, and
   `reject_unauth_destination` applies. Transport maps do not authorize relay.
   Exact generated firewall permits TCP 22 and source-restricted exporter 9100,
   with no TCP 25 allowance. Firewall derivations:
   `/nix/store/zqc2visy8486qlw7khilnm02dvxyjk0w-firewall-start.drv` and
   `/nix/store/da1s56vvl9i6q67iwmfk6ydgx5zd06q5-unit-firewall.service.drv`.
   Agree intended relay domains/recipient policy and IPv4/IPv6 SMTP exposure,
   then implement and test before replacement.
2. **Advisory, risk/security:** TLS/filtering requires explicit cutover acceptance.
   Milter points to localhost:11332 with failure action accept, but none enabled.
   Inbound TLS level is none with no chain files; outbound TLS is opportunistic.
   `reject_unlisted_recipient` supplies no recipient directory. Reconcile actual
   CentOS recipient/backscatter, TLS and spam policies; test Postgrey/DNSBL/milter
   failure behavior. These are inherited gaps, not introduced regressions.
3. **Advisory, operations:** inherited ID, target, addresses, key, placement and
   auto-update are unverified. `tools/deploy-infra.sh:30-36` actually deploys the
   auto-update tag, so approved future integration can expose this host to that
   operational selection. Internal DNS IPv6 differs from public/module address.
   Queue/Postgrey conversion and CentOS rollback compatibility remain untested.
   Keep independent host state and retain/drain NixOS accepted mail after any
   ingress rollback.

Lead accepts all three residuals for this source-preservation request, records
them as blockers to production replacement and makes no source redesign here.
No findings require code fixes or review reruns. Build may proceed; no integration,
deployment, production access or mail authorization follows from this decision.

## Identity, range, lanes and scope

Retained reviewer `reviewer0`, thread `01a19caf-15c8-74a2-baf1-6594cf30d117`,
saved `gpt-6.1-sol` / `xhigh`, read_only. Reviewer independently verified
current/environment binding to this exact session/workspace. No override,
fallback or nested reviewer. High risk classification; general,
architecture/repetition, scope/proportionality and risk/compatibility lanes.
Skill, four references and applicable workspace/repository instructions read.

Full reviewed range: `c040c14cdbacc07998700b524996a89306188d7f` to
`e4c1ac0c5ae7426fb019b79ba936b30ce63e6e6c`; merge-base equals base.
One logical commit, five paths/94 additions; original patch had 68 lines, extra
26 due to RFC formatting. Only functional adaptation is channel option rename.
All five paths needed for host/service/key/placement. Identities/stateVersion/mail
policy preserved. No new abstractions, framework, redundant behavior or dependency.
Scope is proportionate; one coherent commit appropriate. Brief accepted 14:49 UTC,
committed candidate 14:58 UTC; earlier time coverage incomplete. No efficiency
claim based on missing earlier data. Proposal uses conventional tools, introduces
no permanent harness, and is correctly kept in session records.

## Explicit whole-history/migration conclusion

Complete final series is only `e4c1ac0c`, `cluster: add mx2.vpsfree.cz`.
No obsolete approaches, fixups, transitional paths or superseded implementation
history remain. Original `40411d67` import ref preserved. Replay is documented
honestly; range-diff shows allowed option/format/message changes, without falsely
claiming original commit ancestry. Cache commit exactly equals upstream
`17ac0d2b842a88ae7f7b76b1651f36d984dadb2c`; dropping it is correct.
No final cache delta; newer upstream settings preserved.

No repeated dependency/channel/input/generated update streams or superseded pin
commits. Flake/input lock, shared profile and deploy configuration unchanged.
**No database/schema migrations.** No intermediate migration lineage.
StateVersion preserved; no CentOS state conversion claimed. Historical deployment
or external consumption remains unknown; original source is not certified as
undeployed and no merged-history rewrite is authorized.

## Independent evidence and limitations

Reviewer inspected full series/diff/range-diff, plan/state/design/packet and
final import/evaluated-mail records, preserved originals and source snapshots,
shared profiles and pinned nixpkgs modules. Independently confirmed whitespace,
clean worktree, ancestry, source snapshot equality, exact remote feature head and
unchanged master, source/input identities and generated mail/firewall defaults.
No build, production query, mail, deployment or Git mutation performed.

Final evaluated drv:
`/nix/store/0b88m9lch1bcvzn6iwbp60i7lf7jb5ip-nixos-system-mx2-26.05.20261026.718f670.drv`;
output `/nix/store/yi0wph12csy27bzvwdj7idpd70wpyxd6-nixos-system-mx2-26.05.20261026.718f670`.
Lock blob `ec3d5aea9a7e55e69778e3ae4136cf2b3bb84e86`, SHA-256
`505f6c89e18972827beecc29a0c7c85e1df2576ed4074205501167a3dd6f326a`.
Complete graph is recoverable at reviewed commit; see import-rebase.md.
Evaluation is not realized build/runtime proof. No machine claim/profile deployed.

Next gate: fresh utility runs targeted confctl build. Runtime verification must
still prove controlled delivery and relay denial, recipient policy/content
integrity, outage queue persistence across restarts and recovery, filtering/TLS
failure behavior, preproduction identity/network checks and queue-safe rollback.

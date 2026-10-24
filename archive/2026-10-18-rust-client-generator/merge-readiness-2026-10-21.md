# Approved default-branch integration preparation

User direction: merge the code into default branches, no releases yet.
HaveAPI/master and vpsadmin-rust-client/main are the affected targets. No
registry release, tag, workflow dispatch or credential setup/read is authorized
in this operation. The RubyGems pending publisher is user-reported configured.

The actual feature heads remain independently reviewed and clean:
HaveAPI9e4c29a (three feature commits over5266481), client091bd70 (four commits
over neutralb67). Lead compared actual heads/trees/series against final review
reports and retained exact-head CI: all5HaveAPI workflows passed9e4; client
run39318944837 passed091. Complete inventories are saved in
artifacts/approved-default-integration/lead-premerge-inventory.json.
No obsolete history, repeated update streams or migrations in those reviews.

Fresh SSH fetch found HaveAPI/master7835aca, 21upstream commits beyond5266481.
Its new Python and JS changes do not touch clients/rust or servers/ruby. Four
shared overlap paths: Makefile, README.md, flake.nix and development instructions.
Nix pin02c087 and Ruby3.4 replace previous input identities, so no whole-matrix
reuse claim is made. Implementer1 owns scoped rebase/quick hooks and exact input
inventory, before affected final review and fresh watcher verification. Preserve
upstream additions. One mechanical client source-provenance rebind can follow
the final HaveAPI head; runtime/schema/output must remain unchanged.

Client/main is still neutralb67. Implementer3 prepared a clean detached target
at worktrees/2026-10-18-rust-client-generator/vpsadmin-rust-client-merge-target.
No claims or target mutations occurred in preparation. Lead will integrate one
repository at a time with short acquire/finalcheck/ffmerge/SSHpush/proof/release.
A changed baseline or hook intervention returns to unclaimed preparation;
uncertain effects must be reconciled before release. Feature refs are retained.

## Final committed rebase and metadata boundary

HaveAPI frozen68cc80b over7835, three commits77dd0418/03c765bd/68cc80b.
Rust subtree byteequal9e4; all56nonoverlapfeature+183nonoverlapupstream blobs
match. Solemanualconflictdevelopment shelllist keeps Python andRust. All3final
explicittempfile-Famendhooks passed undernewRuby3.4.11/Overcommit0.73.0.
Ruby26syntax/Nixparse/diffcheckpassed; exacttool/runtimefmt coveredfreshCI.
Preparedclean targethaveapi-master-integration at7835, detached.

Clientfirst frozen56c4c9d changed onlyoneprovenanceline to68cc; no source/schema/
lock/toolchanges and4logicalcommits retained. Affected review established no
Blocking/Important finding; one Advisory corrects stale sharedNixpin wording in
docs/development.md. Lead applied2lineown-pinwording, ownerfoldsinto package;
finalheadwillbe recorded without rerunning originalreview.

No claims/remoteupdates/defaultmerges/releases/tokenaccess yet. No registry
credential configuration required or used for Git integration.

# Navigation inventory can lag production page deletions

## Symptom

After fetching a complete production snapshot and building schema-5 managed
page candidates, `tools/check-kb-annotations.rb` reports that the page identity
inventory differs even though the source and candidate page sets are equal.

## Cause

`contract/kb-navigation-inventory.yml` still lists five Czech pages that no
longer exist in production:

- `navody:distribuce:nixos:nginx`
- `navody:distribuce:nixos:zaciname`
- `navody:server:nginx`
- `navody:server:openshift_centos`
- `navody:server:wireguard:openwrt`

The checker compares both complete page sets with this static inventory before
checking annotations, so an unrelated managed-page release cannot make the
global check pass.

## Workaround and follow-up

Confirm independently that source and candidate inventories are identical,
then rely on managed-page reconciliation and the schema-5 manifest checks for
the scoped release. Reconcile the navigation inventory in its own reviewed
change rather than folding unrelated page removals into another documentation
update.

Related initiative: `work/2026-08-17-image-build-failures/`.

# Firewall reload readiness can match the old table

Related initiative:
`work/2026-07-13-security-advisory-automation/`

## Symptom

The vpsAdminOS full CI run `29691200484` failed only
`firewall/conntrack#no-conntrack`. In randomized order, the compatibility-chain
assertion ran after the reload example and observed the protected TCP refuse
rule while the corresponding UDP rule was absent.

## Cause

`sv 1 firewall` only queues the runit control action. It can return before the
firewall service begins rebuilding the nftables table. The reload test's old
readiness predicate was already true in the pre-reload table, so it could return
immediately. A following example could then inspect the table partway through
the asynchronous rebuild.

## Fix

Before signalling the reload, add a deliberate third comment-tagged notrack
rule. Wait until the rebuilt table has exactly the expected two notrack rules,
both protected TCP and UDP refuse rules, the INPUT hook, and no temporary drop
chain. The old table cannot satisfy this predicate.

## Verification

The nine conntrack examples passed with seed 0, which forces the reload before
the compatibility-chain assertion, and passed again in normal randomized order
with an isolated test-runner state directory. Nix formatting and commit hooks
passed. Full vpsAdminOS CI run `29701842763` then passed all 75 tests at commit
`478c6abd707a7f5653c9475d216016e52007eaee`.

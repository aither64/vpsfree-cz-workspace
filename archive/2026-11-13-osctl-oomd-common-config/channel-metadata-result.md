# Channel metadata evaluation

- Result: passed; exit status 0
- Tested revision: `11d6d55924d531d6311dc5a98283d980c9818bb0`
- `flake.lock` SHA256: `683a79dbf4b85f51a6ba79646d5bf131b9362ec16ad49a9228f5bcee638ee02b`
- confctl: `d8ab7d4c062a5d0b36ff65ac42c8617f10fb8c49`
- OS pins: `b86287c105b749827cd63632ac35936533910f63`
- vpsAdmin pins: `4062a8da3314aa7b48170b0d6f441446bad9b207`
- Elapsed: 28 seconds (2026-11-23T21:09:53Z–21:10:21Z)
- Effective watcher policy checked: catalog `7659519e2fbe326ba88f3f4e4b07169f291b61a907be06e5b9e374d27fced37e`, `full_access`, `gpt-6-luna`/low.

Exact target/channel output:

- Nodes: `brq/node5`, `brq/node6`, `pgnd/node1`, `prg/backuper2`, and `prg/node19` through `prg/node25` use `production`.
- Nodes: `stg/node1` and `stg/node2` use `staging`.
- Container `cz.vpsfree/containers/brq/int.ns1` uses `nixos-stable` and `os-staging`.

Complete output: `channel-metadata.log`.

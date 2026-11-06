# Native driver type-check remediation

Predecessor: `53d1310dd1be1c35ea83317a620ce9f6a7fae227`.

[Batch 1](verification-run-1.md) stopped after command 1 failed in native driver
preparation, before VM runtime. The actual failure log is
`verification-1-build-mx2.log`, despite that filename's build-mx2 label. Its
`testScriptWithTypes:205:12` diagnostic reports that `get_payload()` may return a
Message or list, which do not have `replace`. No later batch commands ran.

Only the existing `check_message` helper changes: bind the payload, require
`isinstance(payload, str)`, then keep the exact CRLF-normalized body assertion.
This enforces the fixture's known plain-message contract and retains native type
checking. There is no production, DNS, fixture, dependency or test-scope change.

Focused checks passed without a VM or product build. Recreated the exact pinned
native driver's header and vlan/machine hints with the corrected script, then ran:

```sh
/nix/store/zjmwcyva2jwli0d6vhvnvigg45m6743k-ty-0.0.38/bin/ty check \
  --extra-search-path /nix/store/8hlnfxwkpfsnqplfnp1n92py9kszyw63-nixos-test-driver-1.1/lib/python3.13/site-packages \
  /tmp/mx2-native-typecheck/testScriptWithTypes
/nix/store/k0yjvdmnmgl3sd2002kwsxd46j2kqrsq-ruff-0.15.14/bin/ruff check \
  --select F /tmp/mx2-native-typecheck/testScriptWithTypes
PYTHONPYCACHEPREFIX=/tmp/mx2-python-check python3 -m py_compile tests/mx2.py
```

The extra search path supplies the already-realized native `test_driver` imports;
no diagnostic, rule or type-check gate is disabled. Full-range whitespace checks
also pass. The normal test commit is amended under repository hooks, preserving
the three logical commits, original source ref and reviewed-import ref. Exact
new identities/publication follow below before handoff. Lead owns direct narrow
acceptance under review step 9 and a fresh batch 2 utility; no blind or long rerun
is launched by this remediation.


## Final candidate and evaluation

Head `9738dfbc66bd06b75670d8efd93c684a174acbee`, tree
`0b7b874297f9ea4c66ad8728f910122dd019582f`. The exact
[source/range delta](typecheck-remediation-diff.md) is one driver file, three
additions and one deletion. Host `36ae652962d0217dd5b22965cd44fd711790d77a` and
DNS `91595bef8847063d76246b292293a687362af420` remain unchanged; the final owning
test commit includes this fix without a separate follow-up commit. Normal hooks
passed, with advisory message-width warnings only.

Both exact-head Nix evaluations passed without realizing the new outputs:

| Item | Derivation | Expected output |
| --- | --- | --- |
| VM check | `/nix/store/9mhwvmqyw73w1728k4q8631f2rsc35bq-vm-test-run-mx2.drv` | `/nix/store/dygdv79bp9j3jzq0m429q4vzipd05rsf-vm-test-run-mx2` |
| Production MX | `/nix/store/x5sk6qwy1gq63b8wgwfrnkbnnb9rql10-nixos-system-mx2-26.05.20261026.718f670.drv` | `/nix/store/xdymq4gy8igrf5acdga1hf2sxhqvlwwi-nixos-system-mx2-26.05.20261026.718f670` |

The base remains freshly fetched `c040c14cdbacc07998700b524996a89306188d7f`.
Complete source/input graph is bound by the final head and unchanged lock blob
`ec3d5aea9a7e55e69778e3ae4136cf2b3bb84e86`, SHA-256
`505f6c89e18972827beecc29a0c7c85e1df2576ed4074205501167a3dd6f326a`.
Recover the full transitive graph with `git show
9738dfbc66bd06b75670d8efd93c684a174acbee:flake.lock`. Shared production and fixture
policies, all timing overrides and existing fidelity evidence are unchanged.

The owned feature is published with an exact predecessor `53d1310d` lease. Native
comparison is refreshed. Fresh remote proof shows current feature
`9738dfbc66bd06b75670d8efd93c684a174acbee` and unchanged master/base above; branch
CI is empty, with no superseded run to cancel. Worktree is clean and no other
source path differs. Source `40411d67` and reviewed-import `e4c1ac0c` refs remain
exact and retained. No command or VM is left running. Lead accepts the focused correction
and launches a new utility for batch2; no long rerun, production action, default
merge or lifecycle operation is performed by the remediation owner.

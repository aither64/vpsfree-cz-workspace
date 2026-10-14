# Visibility review assertion correction

Root accepted the Important finding against V d7d7fb66865fd1a5548a45a559f5c2be436bc470:
network_write_spec.rb's existing member test still expected a disabled network
from Index(enabled:false). The accepted enabled-only member list intersects that
filter, so its successful list response is empty.

The only source edit renames that existing example and replaces the two list
assertions with an empty-response assertion. Its forbidden write403, disabled
Show200 and statefalse coverage is unchanged. Product, fixtures, docs, schema,
migrations, other specs and all UI sources remain unchanged. The exact one-file
source diff is visibility-review-fix.diff. This is narrow review step9 remediation,
not a new API contract. The independent reviewer retains its original snapshot.

After root inspection, a fresh watcher may run exactly:

```bash
bash /home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter/visibility-review-fix-quick1.sh
```

The frozen wrapper checks exact head/branch, only one unstaged spec path, no
configured database and unchanged schema/migrations before/after each step. It
runs Ruby syntax plus scoped root RuboCop with force-exclusion, then the entire
network_write_spec.rb in core-none seed36954 and full-all seed9346. Each API run
uses normal automatic unique MariaDB with TMPDIR=/tmp and helper-owned normal-exit
cleanup. Runtime versions/effective Gemfile.lock SHA appear in its log; native
RSpec JSON, per-step log/status and aggregate log/status stay in tracking. It
refuses existing outputs and stops on the first failure.

No Ruby/RSpec/Nix runtime check, commit, ref update, push, pin, CI, deployment or
lifecycle action has been launched by the implementer. Shell syntax was parsed
only while preparing the packet. Root owns execution/evidence interpretation,
normal-hook owning-commit amendment, exact-head publication and canonical pin
refresh. All previous heads/receipts/helpers remain untouched; this source and
packet are held after freeze.

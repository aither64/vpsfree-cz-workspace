# Bounded owned-fixture capacity inventory

Read-only; existing waiter87249 and its80GiB guard remain unchanged. One topology
read establishes `/tmp` and the permitted workspace both use `/dev/vda1`, ext4,
mounted at `/`. Relocation between these paths frees no filesystem blocks.
Ongoing capacity remains the watcher's receipt, not a new monitor.

| Exact owned path | Allocated bytes | Completed outcome |
| --- | ---: | --- |
| `/tmp/h32s.vg93tm18` | 3,018,752 | 0312 services native0/expected_success/32 assertions; separate wrapper1 artifact-selection gap retained |
| `/tmp/h31s.o6fahg9y` | 3,047,424 | 0311 services native0/expected_success/32 assertions |
| `/tmp/ha3.ssn7ogsv` | 458,752 | Original console native expected_success; separate identity guard failure retained |
| `/tmp/hdq.c1ebeF` | 14,049,280 | Actual archive/sample checks pass; first core5 pass/3 oracle failures retained |
| `/tmp/hdq.K2vnpl` | 16,384 | Full8 pass; zero-example core wrapper explicitly excluded |
| `/tmp/hdq.0Zs0oV` | 12,288 | Final targeted core3 pass |

`du -B1` measures allocated blocks without following GC-root symlinks; total
20,602,880 bytes(19.65MiB), far below the roughly4.7GiB deficit in the last watcher
receipt. All exact roots are same-session owned, uid1000/gid100, mode0700,
bound by retained ownership/state-path receipts. Old services/console native
results and reconciliation confirm normal guest exit/destroy; disk images are
already gone. Current argv/cwd/FD checks find no dependent process. The first
inventory saw only its transient shell command; that PID has ended and the
ancestor-excluded check is empty. No process was signalled.

Do not retire whole roots: each contains ordinary GC roots preserving prior
source/test/API/PHP closures or d67 proof inputs. Keep those symlinks, the Nix
objects they protect, native result/log/config receipts, full source/derivation/
closure graphs, wrapper-gap evidence and exact lock/source hashes. The current
batch reads retained archive/source proof from tracking and retains its own
state; it does not consume these old mutable fixture outputs.

No useful owned candidate exists in this small set. Removing all physical
contents would recover at most19.65MiB and would lose retained roots/evidence;
retiring only redundant outputs gains less. Same-filesystem reversible relocation
cannot fix the boundary. Proposed action: none on these paths. Lead must select
a separate concrete capacity remedy; no broad scan, global Nix query/GC, root
removal, relocation, prune, lifecycle or cluster action was performed.

[Exact inventory/root links/process evidence](capacity-inventory.json).

# Final fixture correction publication and pins

Prepared for root inspection only. The implementer has executed none of these
operations. Application source, approved prose, schema, original review artifacts
and previous operation helpers are unchanged by this preparation.

## Exact revisions and receipts

- Selected V: `be136b6c00f03b85b7a12cc57550b4a1394a94a7`, two logical commits.
- Selected W: `e4c49bcdc91b33b7f644a2f125231cb413cf4bf4`, one logical commit.
- Expected remote V lease: `30603a832d2848207bd7319c79c6b0388bc8646a` on
  `2026-10-05-network-ipv4-left-counter`.
- Expected remote W lease: `b3b756a7b45864459bd39481a0d5245886777660` on
  `dev/network-enabled`.
- Unpublished C: `a6243f09265398368e07695dd531e4a0e312350b`, two pin commits
  above `cde8451718d75929c931db63626b48f7de92fc4f`.
- Unpublished K: `8c396b88ff10bf71c47e2364e7ea1ee34f20d184`, one pin commit
  above `873758fd6aec0c03f50a94600e0ceab97946f255`.

The packet accepts V/W heads as command arguments and requires these settled
exact values. It also requires root's `fixture-final-source-w.sha` to match.
All fixture quick2 receipts, desktop/mobile/build receipts under `post-review3`,
and `fixture-final-docs2.exit` must be zero; their current bytes are frozen with
the helper packet. The desktop/mobile/build revision is
`e00336ccf06fe701116c63623a5d8bf93b201dbb`. Root established that the final W
change contains documentation prose only, with an empty diff across application,
browser, tooling, package, lock and flake sources. This packet records that
unchanged-code proof; it does not claim the browser ran on the later prose SHA.

## Prepared operations

From the verified tracking directory, root may select these dependent steps
after inspecting the frozen scripts and evidence. Shell startup or pin duration
uncertainty belongs to a fresh watcher. No source check is repeated here.

```sh
tracking=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter
v_sha=be136b6c00f03b85b7a12cc57550b4a1394a94a7
w_sha=e4c49bcdc91b33b7f644a2f125231cb413cf4bf4
bash "$tracking/fixture-final-operations.sh" publish-v "$v_sha" "$w_sha"
bash "$tracking/fixture-final-operations.sh" publish-w "$v_sha" "$w_sha"
bash "$tracking/fixture-final-operations.sh" cancel-v "$v_sha" "$w_sha"
bash "$tracking/fixture-final-operations.sh" cancel-w "$v_sha" "$w_sha"
bash "$tracking/fixture-final-operations.sh" config "$v_sha" "$w_sha"
bash "$tracking/fixture-final-operations.sh" kb "$v_sha" "$w_sha"
```

Each invocation verifies the bound identity, sets both markers, retains its own
aggregate `.log`/`.exit` and per-step evidence under `fixture-final-*`, refuses
overwrites, and stops at the first failure. It does not retry. The aggregate
subshell keeps `errexit` active without being placed in an OR list.

Publication runs in the declared V/W Nix shells, checks the exact clean feature
head, SSH remote and freshly fetched default ancestry, then uses an explicit
`--force-with-lease=refs/heads/BRANCH:OLD_SHA`. It verifies the new remote head
before updating only that feature's remote-tracking ref with an explicit leading
`+` refspec. Downstream preparation repeats the remote-head proof before its
explicit forced feature tracking fetch. This handles W's absent fetch refspec
and stale tracking state without changing another ref or remote configuration.

Cancellation runs through a `gh`-capable Nix shell. It inventories at most 1,000
queued/running runs per status without `--branch`, then selects the exact owned
feature branch locally. This avoids the previously observed empty branch-filtered
result despite active same-branch runs in the unfiltered inventory. It refuses
a saturated inventory and rechecks each candidate and the current remote head.
It cancels only active same-branch runs with a different SHA. No current-head run,
other branch, completed run or new CI run is selected; no CI wait is included.

## Configuration and KB preparation

Both source publications must match their receipts before either pin operation.
C/K must still be on the exact clean unpublished heads and dated branches above.
Each old commit is checked for pin-only paths and a single parent. The current
remote default must remain an ancestor of the original base; a divergent or
advanced default stops preparation. Original exact head/tree/history/binary
diff are saved separately before a declared-shell
`git -c rebase.autoStash=false rebase --onto BASE OLD_HEAD` drops only that pin
series. No reset, clean, stash or default integration is used.

C verifies active signed Overcommit hooks and refuses bypass variables. It runs
exactly these canonical commands inside its Nix shell:

```sh
confctl inputs channel set --commit --no-editor vpsadmin vpsadmin "$v_sha"
confctl inputs channel set --commit --no-editor vpsadmin-webui vpsadmin-webui "$w_sha"
```

Changelogs stay enabled and the two commit messages remain generated. The packet
requires exactly two commits from the original base, verifies the selected lock
revisions and `vpsadminWebui.inputs.vpsadmin = [ "vpsadminServices" ]`, and checks
the whole lock graph against inspected C head `a6243f0`. Only the selected inputs'
revision, content hash and timestamp may differ. Other nodes, identities and
follows must match. Final hashes, history and diff use `fixture-final-pin-c-*`
and `fixture-final-config-final*`. Root still inspects the complete generated
diff before accepting it; no configuration build or deployment is included.

K replaces only the exact source revision in `flake.nix`, `captures.json`,
`contract/navigation.yml` and `contract/pages.yml`, then runs targeted
`nix flake update vpsadmin` and `bin/check` inside its existing Nix shell.
The whole lock graph must match inspected K head `8c396b8` apart from the selected
vpsAdmin locked revision/hash/time and exact original revision. The four source
records must be byte-identical to that inspected head after substituting only
the source SHA. Fingerprints, bindings and page prose cannot change silently.
The operation leaves HEAD at the original base with an uncommitted five-file
candidate, records `fixture-final-kb-candidate.diff` and `.sha256`, and stops for
root inspection. A later normal-hook K commit is owned by root and is not part
of this packet.

The existing bilingual `networking/ip-address-list` capture impact remains
selected. Its supported execution environment prerequisite is still unresolved;
this static pin/check operation does not regenerate captures or certify them.
No cluster helper, lifecycle action, staging/publication command, production
write, deployment, merge, default push or deliberate integration run is present.

If a step fails, retain its actual state and evidence for root. A partially
completed operation cannot be rerun against the old-head guards; select a new
bounded recovery packet rather than resetting or weakening the guards.

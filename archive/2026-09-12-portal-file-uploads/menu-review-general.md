# General review: compact attachment menu

Reviewed the committed follow-up series described in `menu-review-packet.md`:

- codex-web `7b79942eee2d7bcaf52252249d8599db76c033b2..aa26ec23712e7bdcefd5545ca7715d9bff00f8b7`
- dev-workspace `30bfb2a378138a7fdfe8f6aaa05fcbf8d98037b3..4ddf911fc73e2c8d3c96e1b713cea404dacc7296`
- vpsfree-dev-workspace `9db07ad92eeb62490dbb14cdb5b9cd9a47b4412c..905f7a52b766d219d90940885d6cccb3de5a0360`
- workspace `a3b8e6b4945dfedcee48c6a732e933df4dc48f45..19dc77784383ae0063ed240a2210347cb74c3f46`
- vpsfree-cz-configuration `63652724f9ed0202d6f9c842d842da89ab33bbaa..3d3fa67dd306e1261237cb7df331b664b8b0e8e1`

## Findings

### Important: `destroy()` does not restore the cards root's prior visibility

In codex-web commit `aa26ec23712e7bdcefd5545ca7715d9bff00f8b7`,
`conversation/assets/uploads.js:241` hides a separate cards root during mount
and `:254` subsequently changes that same host-owned `hidden` property according
to component state. `destroy()` at `:356-360` clears the root but leaves its
last `hidden` value behind. An initially visible root therefore remains hidden
after an empty separated-root uploader is destroyed; if cards were visible at
teardown, the inverse can leave an empty visible row. Either case affects later
host reuse and falls short of the stated owned-cleanup contract. Capture the
root's initial `hidden` value before the new mutation and restore it on destroy;
cover at least the initially visible separated-root case with a focused test.

### Advisory: the codex-web pin leaves obsolete checksums in `go.sum`

Dev-workspace commit `e153449999732207ef68cb023eb448abc9d3835a`
adds the two checksums for codex-web `aa26ec23712e` at
`portal/go.sum:3-4`, but retains the now-unused `7b79942eee2d` checksums at
`:1-2`. `GOWORK=off GOFLAGS=-mod=mod go -C portal mod tidy -diff` exits 1 and
reports only deletion of those two old lines. Remove them so the dependency pin
and generated module metadata describe the final dependency set directly.

No Blocking findings.

## Commit series and verification

The provider behavior, public option, focused browser contract, CSS and README
form one reviewable commit. Dev-workspace keeps the provider pin separate from
its consumer layout, and each downstream repository contains one coherent pin
update. The generated configuration commit message is unchanged. The lock-file
graph consistently selects provider `aa26ec2`, runtime `4ddf911`, organization
package `905f7a5`, and workspace package `19dc777`; no unrelated committed
changes were found.

Reviewer verification passed for provider JavaScript syntax and all five Node
browser contracts, and for runtime JavaScript syntax plus
`go test ./internal/web/...`. `git diff --check` passed for every reviewed
range.

## Residual gaps

The Node DOM double does not exercise native popover light dismissal, focus
movement, trusted picker activation or viewport placement. The packet's planned
real Firefox checks at desktop and narrow widths remain necessary after the
Important fix. Packaged checks, downstream builds, live smoke testing and
deployment are intentionally later phases and were not repeated by this lane.

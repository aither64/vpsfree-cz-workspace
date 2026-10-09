# Evaluate a compiled confctl rewrite

## Goal and scope

Evaluate Go and Rust from confctl source and the Ruby extensions shipped by
vpsfree-cz-configuration. Recommend a language and a staged migration that
preserves user-facing commands and cluster-script functionality. This request
is investigation and proposed design only; no implementation or deployment.

## Affected repositories

- confctl: read-only examination of current upstream source and documentation.
- vpsfree-cz-configuration: read-only extension inventory and dependency analysis.

## Approach

The retained architect owns the nontrivial proposed design and records source
findings and a verification brief in design.md. The lead independently examines
code and extension contracts, checks language claims against primary sources,
and integrates the recommendation. No application edits are assigned.

## Compatibility and deployment

Assess CLI flags, output, exit status, Ruby script and hook APIs, Nix inputs,
SSH/process behavior, persistent build/GC-root/generation state, mixed old/new
clients, deployment order and rollback. Preserve existing Ruby extensions first;
consider a separate Ruby runner rather than requiring a simultaneous rewrite.
No production or cluster commands are authorized by this investigation.

## Documentation and readers

Keep the proposal, source references, unknowns and verification evidence in this
session for the maintainer deciding whether and how to rewrite confctl. Project
documentation remains unchanged until an implementation is selected.

## Verification

Read and cross-check source paths at recorded revisions. Distinguish plausible
performance improvements from measurements; do not claim benchmark results.
Recommend bounded read-only benchmarks and characterization tests for a future
implementation. Routine findings and proposals do not trigger final code review.

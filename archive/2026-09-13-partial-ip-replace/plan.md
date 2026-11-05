# 2026-09-13-partial-ip-replace

## Goal

I have an interesting question about vpsAdmin. I have a user who has created VPS in Playground environment and now wishes to migrate them to Production. Now, in vpsAdmin deployment at vpsFree.cz, playground has distinct network by default (both IPv4 and IPv6). There are two cases:

1) VPS with public IPv4 and IPv6
2) VPS with private IPv4 and IPv6

What should happen during the migration is this:

1) public IPv4 is replaced by address from production networks, IPv6 is also replaced
2) private IPv4 is kept and transferred (reallocated to environment production, since the private network is configured to be available both in Production and Playground), IPv6 is replaced

Now, the migration has parameters to replace IPs and to transfer them... but does that support the partial scenario I have described? Or would it replace/transfer all IPs? I'm afraid that this partial scenario is not supported. Please investigate.

## Affected repositories

- `vpsadmin`: read-only investigation of migration API parameters, IP selection,
  address allocation and transfer chains, and WebUI migration controls.
- No implementation or deployment changes are requested.

## Approach

1. Inspect the current upstream source from the canonical bare repository.
2. Trace both migration flags through validation and transactions, distinguishing
   address selection from environment resource-accounting changes.
3. Evaluate public IPv4 + IPv6 replacement and private IPv4 preservation with
   IPv6 replacement, including combinations of both flags.
4. Record evidence, limitations, and the smallest conceptual change if needed.

## Compatibility and deployment

- Investigation only: no database, persisted state, API, daemon protocol, client,
  configuration, or deployment changes. No migration will be executed.
- Evaluate the network availability described by the user as the deployment
  premise; source inspection alone does not prove the running production revision.
- Any proposed fix must preserve existing defaults and resource accounting and
  consider old/new API-client and node combinations before implementation.

## Testing plan

- Trace source and existing regression coverage at an explicit upstream commit.
- Use a focused, isolated check if necessary to resolve ambiguous branching.
- No production mutation, full integration suite, or change review is necessary
  unless the investigation turns into an explicitly requested implementation.

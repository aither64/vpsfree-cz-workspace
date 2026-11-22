# Add complete IPv6 accounting to a default review fixture

Initiative: work/2026-09-09-ip-release-mechanism.

The default single-node development seed had no IPv6 ClusterResource, not just a
zero member allowance. Preparing owned IPv6 allocations therefore requires the
resource definition, default VPS allocation and member environment allowances
before invoking normal allocation chains. Use the existing resource contract
(`object` type and `Ip::Free` cleanup) and count addresses as
`2**(128 - split_prefix)`. Network#subnet_size is protected.

The initiative's review-fixtures.rb prepares this explicitly. Failed initial
preflight attempts occurred before allocations; the corrected fixture produced
two owned /64 review subnets and a separate /64 for smoke tests with exact quota
accounting.

An IP release without asynchronous cleanup can complete synchronously and have
no release_chain. A live-check wait helper must allow this case and then assert
released_at, ownership and quota, rather than unconditionally calling reload on
a missing chain. The synchronous IPv6 release and asynchronous IPv4/PTR release
both passed in the review cluster.

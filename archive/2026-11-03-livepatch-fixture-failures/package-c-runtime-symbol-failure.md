# C followup: defined runtime symbols versus module imports

Tested source: `48f2983e3cf6b5b72a21c254f744ad8e7d62a123`, base
`742eb30cb1a8b6766c85e915d26b0400e38244b1`. Run `41740116653`, attempt 1,
Intel job `126293359412`.
Session/env and retained implementer3 Sol/xhigh workspace-write binding were
reverified. This note records that failed attempt separately from the earlier
`efc5f8fe` cache-preparation failure. Original review/history receipts remain
unchanged. The first correction was committed as
`65d43eececbd0d13a3863c554e86e22680fbff84` and rejected by independent review
finding DS1 before publication. Its source and 53-example green history are
retained below. The narrow DS1 remediation was subsequently committed as
`5235bfd57c92bc05a25946937fe77f9803fe1c93`; the lead reconciled the requested
fix in [defined-symbol-review-reconciliation.md](defined-symbol-review-reconciliation.md).
The source remains frozen for exact-final-head verification.

Subsequent read-only audit accepts the actual corrected fragment witness in
run `41773470432`, Intel job `126392676335`, on exact `5235...`: current
module-scoped probe, nonzero hash-node link, lock 1, one hit/zero misses and
normal completion. [Acceptance evidence and boot-identity limit](package-c-fragment-runtime-acceptance.md)
preserve its precise scope; this is not whole-matrix or FUSE/TCP acceptance.

## Primary evidence

[Raw job log](ci-41740116653-126293359412.log), lines 382–403: only
`kernel/livepatch-inet-frag` failed; ten other Intel scripts passed. Result
evaluation's exit 1 reports that failure. Log upload succeeded.

The single requested artifact is `os-test-logs-41740116653-1-livepatch-intel`,
ID `13294011506`, 366187 bytes, ZIP SHA-256
`0547b8aca3557008b5e1de4037c56099b86548d3ac8955fa3776a091035ff7d5`.
The sole watcher supplied the requested case logs and identities beneath
`ci-41740116653-intel-evidence/`; C did not duplicate download or monitoring.

Its `os-test-kernel__livepatch-inet-frag-144ad4d5/test-runner.log`, line 8,
reports:

```text
missing or ambiguous symbol inet_frag_find livepatch_7: ["ffffffffc1c91f50", "ffffffff92f7fd20"]
```

The case's `machine-shell.log`, lines 1100–1106, records the actual query:

```sh
awk '$3 == "inet_frag_find" && $4 == "[livepatch_7]" { print $1 }' /proc/kallsyms
```

It returned both addresses. The native baseline previously observed one hit,
zero misses, `next=0x0` and `lock=0` at immutable boot offset `+0x22f`.
Module insertion succeeded and transition completed. The exception occurs
before target probe installation, so it supplies no target hash/lock result.

The uploaded record identifies normal producer `qi47yi2...livepatch_7`,
module SHA `7c4da9d643d45ad9c07bde72b0180175519c5e7a15a6f2aec9e54831aee8455f`,
site output `aiqijlwh...livepatch-candidate-sites`, source `48f2983e...` and
lock SHA `604e01bde4cf21e1532e9ed6e6cfb993da28439355ad7dceb5560447827c5baa`.
The fragment descriptor selects `livepatch_7:inet_frag_find`, position 0,
`.text`, offset 950, size 1928, and the validated timer ABI.

## ELF classification and rejected first correction

Read-only `readelf --wide --symbols` on that exact normal module shows both:

```text
3422: 0000000000044e50 1928 FUNC   LOCAL  DEFAULT 13  inet_frag_find
5680: 0000000000000000    0 NOTYPE GLOBAL DEFAULT UND inet_frag_find
```

The same name is a local executable definition and a resolved external import.
Exact module qualification does not distinguish those entries in a loaded
livepatch's kallsyms table.

Pinned kernel source was read directly from
[a2384967 kernel/module/kallsyms.c](https://raw.githubusercontent.com/vpsfreecz/linux/a2384967b90f24d2470c9eb15f0e66d938df7e08/kernel/module/kallsyms.c),
function `elf_type()` (the read covered lines 1–110). Its relevant branches are:

```c
if (sym->st_shndx == SHN_UNDEF)
    return 'U';
/* intervening absolute/reserved-section checks */
if (sechdrs[sym->st_shndx].sh_flags & SHF_EXECINSTR)
    return 't';
```

The first attempt, `65d43ee...`, excluded only uppercase `U` and explicitly
treated lowercase `u` as a defined symbol. That conclusion stopped before the
final proc formatting stage and was wrong for the pinned kernel. Independent
[review DS1](defined-symbol-review.md) rejected the attempt; its host-only
53-example pass did not establish the actual runtime formatting contract.

## DS1: final proc presentation and narrow remediation

The full source chain is `elf_type()` to the module typetab, then
`module_get_kallsym()` to the iterator, and finally `s_show()` to proc output.
`module_get_kallsym()` returns the type and `is_exported(name, value, mod)`.
The same pinned kernel's
[kernel/kallsyms.c](https://raw.githubusercontent.com/vpsfreecz/linux/a2384967b90f24d2470c9eb15f0e66d938df7e08/kernel/kallsyms.c),
`s_show()` at lines 742–752, changes module type case before printing:

```c
type = iter->exported ? toupper(iter->type) : tolower(iter->type);
```

C directly read both the getter and formatter at that exact source revision.
The reviewer additionally verified the selected module has no `__ksymtab`
exports and the pinned livepatch path retains all symbols. Thus the strong
undefined import is printed as lowercase `u` for this module. This is a
source/ELF-derived classification: the original failing query printed only
addresses, not type characters. GNU nm's lowercase-`u` meaning does not define
this proc interface.

The architect and lead approved excluding both printed undefined-import markers,
`U` and `u`, before the unchanged exactly-one validation. Both queries use
`$2 !~ /^[Uu]$/`. Exact name/module selection, four-field module and three-field
native scopes, address checks and duplicate rejection remain. Defined text and
data, including `x2avic_enabled`, remain eligible. Duplicate rows are rejected
even if addresses are equal. Original FUSE positions 0/1 still require exactly
one eligible definition; no first-match, address heuristic or schema change.

Changed paths only:

- `tests/suite/kernel/livepatch-6.12.95-common.nix`
- `tests/suite/kernel/livepatch-inet-frag.nix`
- `test-runner/spec/test_runner/livepatch_runtime_sites_spec.rb`

No descriptor/schema, resolver, ABI, producer input, boot offset or historical
lane changed. Current fragment lock/hash/nonzero-hit/zero-miss assertions and
all hold/receiver/arithmetic controls are unchanged. The existing documented
contract already requires unique module-owned symbols; local comments explain
the import distinction, so no product-doc rewrite is needed.

## Checks and remaining gate

The persistent consumer spec executes each actual rendered AWK query against
kallsyms fixtures containing native, target, same-module import, unrelated and
wrong-module same-name rows. DS1 controls cover both printed import cases,
reject import-only rows and two defined rows including identical-address
duplicates, preserve native and real data lookups, and check FUSE positions
0/1 beside each import type, unsupported positions and position-1 ambiguity.

Retained first-attempt evidence, insufficient for runtime acceptance:

- Before source fix: 53 examples, six expected regression failures, including
  both original candidate/import ambiguities and import-only acceptance.
  [Red log](package-c-symbol-red.log), [status](package-c-symbol-red.exit).
- First correction source: 53 examples, zero failures, body 1.86 seconds, through the
  declared test-runner shell and existing native `RUBYLIB` receipt.
  [Final log](package-c-symbol-final.log), [status](package-c-symbol-final.exit).
- Cached declared Ruby/RuboCop: one file, no offenses.
  [Lint log](package-c-symbol-rubocop-final.log).
- Cached declared Nixfmt 1.5.0, both Nix parse checks, Ruby syntax and whitespace
  checks pass. No broad shell realization, old-Nix or kernel build was launched.

DS1 remediation evidence:

- Source-grounded fixtures against unchanged `65d43ee...` lookup predicates:
  57 examples, six failures. Both lowercase-import candidate lookups reproduce
  the original ambiguity, both lowercase import-only lookups incorrectly
  succeed, and FUSE positions 0/1 fail beside lowercase imports.
  [DS1 red log](package-c-ds1-red.log), [status](package-c-ds1-red.exit).
- After the two-marker correction: 57 examples, zero failures, body 1.84 seconds,
  using the same declared test-runner shell and native-path receipt.
  [DS1 green log](package-c-ds1-green.log), [status](package-c-ds1-green.exit).
- Cached declared RuboCop: one file, no offenses.
  [DS1 lint log](package-c-ds1-rubocop.log). Nixfmt 1.5.0, both Nix parse checks,
  Ruby syntax and whitespace checks pass.

Helper C SHA remains
`d9226b31152ce994b16e5733f8e801329ff8e8ca1b22074e2b0bee36373b3977`;
the prior source-bound helper compile and 49/19 import-CRC evidence remains
applicable. No helper compilation was repeated.

No Git/index mutation, CI rerun/cancel/dispatch/push, VM, deployment or lifecycle
action was performed by C. Lead inspection of the requested DS1 narrow fix and
coordinated consolidation precede replacement CI. Live target hash/lock observations and full exact-final-head CI
remain required; the focused host checks are not runtime qualification.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-03-livepatch-fixture-failures/>

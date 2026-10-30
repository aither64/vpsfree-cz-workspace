# Current exact lineage inventory and validation bindings

Base `846bb469505789ba0b2a405fa5905ba6d8253006`; old isolated owner8 `19562b6449f01ca4939d57f70ee59de8af13880f`;
unchanged parent/first7 head `39b6f68f245d6ebddf40a5ffc8e2e9485a9a8a17`. Shared feature stays9bea.
The first7 are identical commit objects, hence exact parents/trees/patches/
authors/dates/messages; no first7 reconstruction is proposed.

| Owner | Exact existing commit | Tree | Parent-to-owner full-index patch SHA256 | Commit body SHA256 | Author/date |
| --- | --- | --- | --- | --- | --- |
| 1 | `ae33b06b0264b2aabcb5af21bb47c029a6a3f091` | `9f11aceece3a979778ebfdf0e61421504d3898af` | `afb97236a667bff97bed3259d69e76e814a06c50b7bc47f495c0bc8fab13fba3` | `e389feb33e71e7a42e81ef5fc8326c3581e0831be39f47da482adb5ad3af15aa` | Jakub Skokan <jakub.skokan@havefun.cz> 2026-10-22T20:53:13+02:00 |
| 2 | `be4ec430d49395513a0c7188bffcd78f17cd4ae9` | `1b4af65d1134e32a4fe681245af560b920289bf9` | `bc9ec71cab0dd364273559d58f0a5f34978c9f80674d70b29f3a57b85557e919` | `3c054dd9b1716527ae8f2bd3567b51e84177ed5c7218e0aee2255e24b5ccb933` | Jakub Skokan <jakub.skokan@havefun.cz> 2026-10-22T23:06:34+02:00 |
| 3 | `50a796f2824424252be177aedafb277b6f149073` | `29b00319a5aedaa44a56d60bc6d0b70083a8ac16` | `a56ebac93270e4df8932c749600fda34e8dc4a383c13660feb26746a667e5bba` | `6a7d7d163c70f7c7f7bea6031d9da774d785d2530de115c86e24f5ff71c055dc` | Jakub Skokan <jakub.skokan@havefun.cz> 2026-10-22T23:34:44+02:00 |
| 4 | `247c091e6a48083099395e5e1f4847ef5a585be6` | `274e2524effff73896b1fb972c592954b01b31c2` | `9fdedffcdc111d414e51767d9bac2978c73996546bf1b42f6766d5eed211aaec` | `7fcbd5c86b329563e74cb23b3c18138b9d9b76faaf343e675d9941451140a7a2` | Jakub Skokan <jakub.skokan@havefun.cz> 2026-10-22T23:50:50+02:00 |
| 5 | `a1c4dc932b953cc21fde47a2fc2e6f85bb03e8f8` | `ed46a15a29f43e50998d5e0cb781cf667d726783` | `c20cb00ffc11b55550c96532795219e3d011a29cb84c8555265a1b46fc896b92` | `853b08ad5bdbf05190d177d7cedd8ae1723e6d007c6efa244526211c508e0018` | Jakub Skokan <jakub.skokan@havefun.cz> 2026-10-23T18:42:38+02:00 |
| 6 | `a2e4c097103eeeba8ae016571ffbe25316ceb10f` | `e5e074bad8c74a27eb3dc422e44cb8e08389a245` | `9d282605c8702e9d6cd8330e889be63d9b69f31d126700b4cc9f24712addc83a` | `d77074360fdff27ac45f19e59b252ba81d0a491e4c5b8bcf482e747a0f865830` | Jakub Skokan <jakub.skokan@havefun.cz> 2026-10-23T18:42:41+02:00 |
| 7 | `39b6f68f245d6ebddf40a5ffc8e2e9485a9a8a17` | `f2c5065769c36058fe6605993e39f598d9f721ff` | `c50cbb9c75cb862d348cfe241c5c3db2dd7e191f53b3cba72db97dd1157a8194` | `1511567c0623887be139e4d2de4cf01b8fc1b1227ed06a0e8c801d6b9a66c19b` | Jakub Skokan <jakub.skokan@havefun.cz> 2026-10-23T18:52:58+02:00 |
| 8 | `19562b6449f01ca4939d57f70ee59de8af13880f` | `3e04ce2bd85f871c3f40f86db5668f30684100a4` | `b7caf38ef94ec6a928f5aa36a76881bb25a6e3a4865139f40ac78d0dcf46c343` | `9d40e02361c0bd82bb23acd1621610b108268b95f9a47c41bb8c8fcad2598560` | Jakub Skokan <jakub.skokan@havefun.cz> 2026-10-23T19:03:55+02:00 |

Reused independent whole-history/migration/repeated-stream conclusions:
[final-review.md](../../../final-review.md), SHA256 `0dc073b0aa0b7fffa689509956b0dd07d3b3002324b46e90ce1f8c65ae118169`;
[final-review-remediation.md](../../../final-review-remediation.md), SHA256 `4082e47b1f2cd00d89d9aff11edc8e1eb36cf8e1ce45bfe363965451a3711915`.
Eight coherent owners; no ninth repair/fixup. No migrations/new persisted schema/
format; no merged/released/deployed/external migration boundary. No repeated
dependency/channel/input/kernel-pin/generated update stream or changed lockfile.
New C/docs counter correction changes only stricter diagnostic completeness and
additive stderr, not ABI/event decoder/fleet ordering. Lead retains final affected
review disposition after committed exact changes; no gate closure is claimed.

- `repair/hotplug/recursion-build-1-owner-assessment.json` SHA256 `eb45e8c20c2a50a5d22ab7d187c97d538271e30e25d6aeed3b41127c81f1bdfc`.
- `repair/hotplug/recursion-build-1-owner0-validation.md` SHA256 `193164267de72711d1b30d01b1e989a856017c7e380f7a4ad1671c4ddb6118a5`.
- `repair/hotplug/recursion-build-1-owner-package-binding.json` SHA256 `e490629f593ec6e9504b4f09365928cf1173f940d80c974d0acac9dcdb3c3485`.

Current validation is C55a syntax/PASS73 actual-C fake-boundary checks,
source-bound rnaq->lpz C/BPF compile/help/selected rejected CLI/query result.
Old41/build4 are historical files only, not current suffix validation.
Package native0/guard1/outer0 printing status; permanently INCOMPLETE. Qualified
current readable effectsd9f064 do not prove protected-ended/peak/allocation or
actual barrier/verifier/load/attach/count/loss/hotplug/aging. No warning cause.

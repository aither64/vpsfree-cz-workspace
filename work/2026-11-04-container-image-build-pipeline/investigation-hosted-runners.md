# GitHub runner feasibility evidence

Package I3; owner: implementer3; checked **2026-11-04**. External documentation
investigation only. No project source inspected, runner probed, build started,
external service changed, or commit created. Session command and both environment
identity values matched `2026-11-04-container-image-build-pipeline` in
`/home/aither/workspace/ai/vpsfree.cz`; same-session roster confirmed retained
settings and workspace-write access.

The six primary sources below support the proposal's capacity and operational
constraints. A redundant billing page was also consulted before architect0's
current-package clarification requested self-hosted PR security evidence: seven
pages consulted in total, with that bounded extension reported to the lead.

## Capacity and virtualization

[1. GitHub-hosted runners reference](https://docs.github.com/en/actions/reference/runners/github-hosted-runners)
lists these standard Ubuntu VM resources:

| Repository visibility / architecture | CPUs | RAM | SSD | Example label |
| --- | ---: | ---: | ---: | --- |
| Public, x64 | 4 | 16 GB | 14 GB | `ubuntu-24.04` |
| Private, x64 | 2 | 8 GB | 14 GB | `ubuntu-24.04` |
| Public, arm64 | 4 | 16 GB | 14 GB | `ubuntu-24.04-arm` |
| Private, arm64 | 2 | 8 GB | 14 GB | `ubuntu-24.04-arm` |

The reference also documents passwordless `sudo` on Linux VMs and Linux hardware
acceleration for Android SDK tools. The separate `ubuntu-slim` label has 1 CPU,
5 GB RAM and 14 GB SSD, executes inside an unprivileged container, lacks operations
such as filesystem mounts and low-level kernel access, and has a 15-minute timeout.
It is unsuitable for treating the runner as an ordinary privileged VM host.

**Capacity implication (inference):** architect0 reports that I0 found a current
test-guest request of **24 GiB RAM**. This exceeds either standard VM's documented
host RAM before host overhead. Standard hosted execution therefore does not fit
that requested capacity envelope. This is peer-provided project evidence, not a
source inspection or measurement by I3; memory overcommit is not validated here.
The 14 GB SSD entry does not establish measured free space for a particular job.
Nix inputs/outputs, guest disks, images and upload staging need a measured peak
space budget before claiming a standard runner fits.

[2. GitHub-hosted runners concepts](https://docs.github.com/en/actions/concepts/runners/github-hosted-runners)
says nested virtualization is technically possible, but unsupported and
experimental, with no stability, performance or compatibility guarantees.
Eligible standard 2-core/4-core Linux jobs may be scheduled across AWS and Azure.

**KVM conclusion:** these pages neither guarantee `/dev/kvm` access for every
Linux runner nor establish that every hosted runner forbids KVM. Documented
Android acceleration is positive evidence for a specific use case, not a support
contract for arbitrary vpsAdminOS guests. A chosen label/image needs an actual
KVM-access and guest-boot probe; one success would establish that run's evidence,
not universal availability. This investigation ran no such probe.

## Duration and artifact constraints

[3. Actions limits](https://docs.github.com/en/actions/reference/limits)
sets the general GitHub-hosted job execution ceiling at **6 hours**; reaching it
terminates and fails the job. The specific `ubuntu-slim` exception is above.
The whole workflow limit is 35 days including waits/approvals, which does not
extend a hosted job's execution allowance. Self-hosted jobs have a 5-day ceiling.
The artifact storage table lists 500 MB for Free/Free organizations, 1 GB Pro,
2 GB Team and 50 GB Enterprise Cloud. These plan allowances do not establish a
per-file upload ceiling or this organization's available quota.

[4. Official upload-artifact documentation](https://github.com/actions/upload-artifact)
documents a **500-artifact limit per job**, shared storage quota constraints,
unique artifact names, and immutable uploads; overwriting replaces an artifact
with a new ID. It exposes artifact ID and SHA-256 digest outputs. Missing files
warn by default; `if-no-files-found: error` makes absence fail. Hidden files are
excluded by default. Zipped upload does not preserve original file permissions;
the documented workaround is a tar file (the current README also describes
single-file `archive: false`). Already compressed large files can avoid redundant
compression work. README examples currently use `@v7`; selecting/pinning an action
release is outside this evidence package.

**Extraction implication (inference):** first copy the tested image archive out
of the guest into an explicit host output path, then upload that file and its
identifying evidence. Artifact upload itself does not extract guest files.
Preserve filesystem metadata inside the image archive rather than depending on
the artifact wrapper. Measure output size, staging space and transfer duration;
no individual artifact byte ceiling was established by the inspected pages.

[5. Organization retention documentation](https://docs.github.com/en/organizations/managing-organization-settings/configuring-the-retention-period-for-github-actions-artifacts-and-logs-in-your-organization)
sets default retention to 90 days. Public repositories permit 1–90 days; private
repositories permit 1–400 days, bounded by organization/enterprise policy.
Workflow artifacts therefore need an explicit retention choice and are not a
permanent image distribution channel by default.

## Persistent self-hosted runners and untrusted PRs

[6. Secure use reference: self-hosted runners](https://docs.github.com/en/actions/reference/security/secure-use#hardening-for-self-hosted-runners)
warns that untrusted workflow code can persistently compromise a self-hosted
runner, and strongly discourages public-repository use because users can open
malicious PRs. Environment secret approvals do not isolate the executing code.
Repository/runner groups can limit compromise scope. Just-in-time runners execute
at most one job, but reused hardware still requires a clean environment.

**Proposal implication (inference):** an adequately sized dedicated self-hosted
runner addresses capacity, but does not by itself make public untrusted PR
execution acceptable. The design must establish which revisions/events can
reach that persistent host and its network/credentials. A test guest inside QEMU
does not automatically isolate host-side workflow scripts. This is a constraint
on the architect's runner/event choice, not a broad architecture recommendation.

## Remaining evidence and delivery

- Hosted execution remains unverified: exact-label KVM access, guest boot and
  peak RAM/disk/runtime/artifact size have not been measured.
- The reported 24 GiB guest request is above standard hosted capacity; a smaller
  guest would need a separately justified and measured configuration.
- Organization plan, current artifact quota/billing policy and effective
  retention settings were not queried. No paid service choice was made.
- The redundant seventh page was [GitHub Actions billing](https://docs.github.com/en/billing/concepts/product-billing/github-actions);
  the conclusions above use the six primary sources. Avoid inferring unlimited
  artifact storage from free public-runner compute.
- Investigation evidence requires no application checks or automatic change
  review. The lead owns linking this file in the existing package/state records;
  architect0 owns incorporating these constraints into the proposal.

[Session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-04-container-image-build-pipeline/)

# Livepatch lifecycle scripts require matching host CPU vendors

`./test-runner.sh test 'kernel/livepatch-lifecycle@6.12.95#intel'`
on an AMD host boots the guest but fails the `GenuineIntel` assertion before
loading a patch. Selecting a script does not emulate its named CPU vendor.
The scripts declare `labels.cpuVendor`; CI sends them to `amd-livepatch` and
`intel-kvm` runners and tests the corresponding nested KVM module.

Check `/proc/cpuinfo` and select the matching `#amd`/`#intel` script for local
validation. Preserve the vendor guard. On this AMD EPYC host the AMD lifecycle
passed, while the explicit Intel attempt was inapplicable and powered off.

Related initiative: `work/2026-09-12-nfs-cancellation/`.

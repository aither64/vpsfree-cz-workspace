# Fedora 45 image verification conclusion

The canonical image CI passed on exact feature head
`dd188397abe37d0bc33f4c5dfb3605206ce5e326`.
[Run 41666620408](https://github.com/vpsfreecz/vpsadminos/actions/runs/41666620408)
finished successfully. Its full transcript is
[image-ci-41666620408.log](image-ci-41666620408.log).

The transcript confirms all three jobs succeeded: OS/cache preparation,
changed-image detection, and image build/testing. Detection selected only
`fedora-45`. The actual image job invoked `image-scripts/test@{fedora-45}`,
with `VPSADMINOS_CONFIG` empty; the runner reports
`image-scripts/test@fedora-45` successful in 1079.28 seconds. This validates the
canonical target rather than merely an OS build or test discovery.

The canonical test calls `osctl-image test` without a subtest selector, which
selects the normal image suite, including SSH key and password tests; any
failed nested result makes the CLI exit nonzero. Successful CI does not retain
or print its nested image output, so no raw CI `15/15` count is claimed.

## Local evidence and residual

The [first local attempt](fedora-45-image-test-result.md) failed before VM
startup because the immutable linked-worktree snapshot lacked usable host
revision metadata. The [prepared metadata recovery](image-test-recovery.md)
changed only declared test-host revision/version metadata; image source and
feature head remained unchanged.

The [metadata-adjusted local run](fedora-45-image-test-metadata.log) reached
Fedora image build and ran 15 image checks: 13 passed; `ssh_key` and
`ssh_password` failed at TCP port-22 readiness (`ssh not responding`). Both
containers entered `RUNNING`, and their preceding ping readiness checks passed.
Neither test reached SSH authentication assertions. Other checks, including
networking and `systemctl`, passed.

The precise local TCP-22 failure cause remains unexplained. Per-test cleanup
removed the failed containers before final diagnostics; retained destroyed
container logs are empty, so their SSH journals/listener/firewall state are
unavailable. Passing exact-head CI is evidence against a deterministic recipe
defect, but does not prove a particular local environment cause. No source fix,
test weakening or blind rerun is justified by the available evidence.

Original native evidence is preserved at
`/tmp/f45-20261103-dd188/os-test-image-scripts__test__fedora-45-07b223fa`;
original pre-VM failure state also remains untouched. No operation remains
running under implementer ownership. The exact-head canonical CI pass satisfies
the targeted image-test requirement. General CI and its separate failures are
tracked by the lead; they are not reclassified by this image conclusion.

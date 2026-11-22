# Check dependent cumulative livepatch inputs sequentially

Passing dependent patches together to `git apply --check` does not compose the
first patch's changes before checking the second. This can falsely report a
failure when the uname patch depends on the cumulative patch.

Copy the exact pinned base files into disposable scratch space, then apply each
input in package order with `git apply`. Both existing 6.12.95 nfs-cancel inputs
apply successfully to the repaired base e232e2bdc this way. Building and loading
the livepatch are separate validation steps.

Related initiative: work/2026-09-12-nfs-cancellation/.

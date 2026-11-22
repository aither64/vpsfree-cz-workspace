# Destroy DOM components before restoring test globals

In the upload browser contract fixture, Node test after-hooks ran in registration
order. Restoring global window event methods before mountUploads.destroy caused
teardown to fail with `globalThis.removeEventListener is not a function`, although
the behavioral assertions passed.

Register component destruction before the global-restoration hooks. The complete
provider browser suite then passed (41 tests). This ordering also prevents active
components from leaking listeners into a later test.

Related initiative: work/2026-09-16-portal-upload-recovery/.

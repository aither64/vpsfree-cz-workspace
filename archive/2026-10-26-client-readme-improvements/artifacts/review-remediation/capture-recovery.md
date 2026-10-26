# Focused review remediation check capture

The first and only launch used run-affected.sh at reviewed HEAD
ea0932808c3bbcf70801d1728848e52507eb6193 plus the narrow remediation diff.
The watcher stored the exec session handle, then attempted to store an undefined
exit_code while the check was still running; that serialization error prevented
its initial output summary and log write. The original process completed.

The original functions.exec session handle 96905 was recovered from the watcher's
stored watch_session value. write_stdin returned exit 0, two examples and zero
failures in 44.47 seconds. That authoritative output and exit are saved as
affected.log and affected.exit. No check was relaunched or retried.

The checked examples are the complete new-mode replay including hostile SHA256
ambient directory/GIT_DIR, invalid GIT_DIR, default hash and injected config,
plus tampered blobs, and the RUBYGEMS_GEMDEPS deletion assertion.

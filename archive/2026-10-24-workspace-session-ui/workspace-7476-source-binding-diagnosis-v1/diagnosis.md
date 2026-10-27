# Saved-only workspace source-binding refusal diagnosis

All five common tool records match accepted v3 exactly. Nix also matches the
metadata-v5 selected/resolved/hash triple. The sixth record, nix-store, is absent
from accepted v3/metadata-v5 guards; it copied the old source-root capture's
supplied resolvedTool/toolSHA256 fields. That capture records supplied tool data
and procExe but does not independently resolve/hash the selected legacy alias.
No current alias identity or static typo is established by these records alone.
Do not remove the guard, accept a new tool identity, or retry the binding.

The generic failure happened before result/import/Nix/current source guards.
Original packet/release/failure remain unchanged. No config source/result file was
inspected; only explicitly assigned watcher evidence was read. No live tool,
source/index/store/Git/SSH/Nix observation was performed.

The proposed pinned isolated Python command reads only the exact six declared
tool entries and emits actual resolved paths/SHA256 in JSON, with no subprocess,
source/index/Git/Nix/store query or directory scan. A separate parent release is
required before it can run. Failure of an old binding does not authorize refresh.

Saved raw c31 metadata contains url with immutable revision+narHash query. The
successor must retain metadata['url'] verbatim, validate scheme/path/revision and
its decoded single narHash against actual locked metadata, and label any separately
constructed URI derived. It must not label the old synthesized URI as observed.
This URL correction can accompany the evidence-supported minimal tool fix after
observation/disposition. No source-binding successor/retry has been launched.

Lead owns disposition/release. Source/Git frozen; session open.

# Missing publication step display

Investigation 70c3c940-767d-4654-ab4d-0b486302786b, architect0, 2026-10-24.

GitHub returns no step records for [publication job 120934872467](https://github.com/vpsfreecz/haveapi/actions/runs/40114719358/job/120934872467), matching the empty UI. Its whole-job log records the publication work. The underlying reason for the missing provider metadata is unknown; the evidence does not establish a release workflow defect, skipped publication, or that refreshing the browser will fix it.

One fresh exact-job GET at **17:28:32 UTC** returned HTTP 200, `completed` / `success`, `steps: []`, attempt 1, source `1c3c98f0d77e0b23c8da1a8937f25c5799864a3b`. It agrees with the retained terminal observation. The job ran from 17:17:35 to 17:22:04 UTC. See [fresh observation](publication-step-metadata/observation.json) and [raw response](publication-step-metadata/job-get.raw), SHA-256 `f3dcaef73fd01b4399c9dde2cbd84216529693e8ce2b0c86ea97e085331f87de` (2,277 bytes).

The exact [committed workflow](https://github.com/vpsfreecz/haveapi/blob/1c3c98f0d77e0b23c8da1a8937f25c5799864a3b/.github/workflows/release.yml#L123) defines **eight separate publication steps**, including checkout, Nix, download, artifact verification/draft preparation, RubyGems authentication, registry preflight, PyPA upload and final publishing. These are separate actions/commands, not one opaque step. The job's tag condition passed; the conditional PyPA action also executed.

The retained [whole publication log](release-0-30-1-successor-publication-observer/raw-member-0000.log) is 169,588 bytes / 1,544 lines, SHA-256 `6b07a325cf80f8012107654b435addd39a63be7ad1770191ee4e73a1c6bd1e7d`. Execution markers occur at lines 40, 314, 752, 783, 1061, 1072, 1099 and 1369, covering all eight stages. Lines 1406–1421 record the four gem registrations; line 1496 records npm `haveapi-client@0.30.1`; line 1527 records `Release complete` at 17:22:01 UTC. Credentials are not reproduced here.

The retained [downloadable full log ZIP](release-0-30-1-successor-publication-observer/terminal-full-run-logs-ZIP.raw) is 166,545 bytes, SHA-256 `e9e13dc3ea7af8d808d151a96c4d1a17e8178084294213e0efffbde60b0afb44`. Its 15 members include publication whole-job/system logs but **no numeric publication step files**. In contrast, it includes 11 numeric build-step files. The archived `0_Publish approved artifacts.txt` is byte-identical to the retained whole publication log. See [member inventory](release-0-30-1-successor-publication-observer/raw-log-members.json).

This is consistent with a provider step-metadata/log-indexing anomaly. Available evidence cannot identify its backend cause or expected duration. No rerun, upload or source change is justified by the display issue. Independent verification of destination identities and original artifact hashes remains separate and continues under owner1; this investigation does not replace it.

Network scope used: one exact-job GET. No additional job-log GET, check-run GET, polling, settings access, rerun or mutation. The existing ZIP and whole log provide a read-only way to inspect execution despite the empty step UI. Session identity and architect0's ready/design/Astra/xhigh/workspace-write settings were confirmed. No application changes or verification campaign was started.

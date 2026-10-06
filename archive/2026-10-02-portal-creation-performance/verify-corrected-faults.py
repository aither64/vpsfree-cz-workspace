#!/usr/bin/env python3
"""One use: two fresh fault cases; preserve the stranded receipt and original result.

--preflight is local read-only metadata validation, without RPC or subprocesses.
See verification-corrected-fault-preparation.md before parent-authorized execution.
"""

import argparse
import copy
import importlib.util
import os
from pathlib import Path
import stat
import sys

sys.dont_write_bytecode = True
SPEC = importlib.util.spec_from_file_location("old_fault_verification", Path(__file__).with_name("verify-fault-creation.py"))
f = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(f)
h, w, d = f.h, f.w, f.d
ROOT, PACKAGE = f.ROOT, f.PACKAGE
PROVIDER_PACKAGE = Path("/nix/store/xl9mvbb5j19anfbx6qj3lrw8k7a9vnz2-dev-workspace-0.2.0")
PROVIDER_SHA256 = "ac2bf71e98d1bafb4357bbf0bb7b7d1140f0bb4a1a903147cff67790284e9c4c"
ROOT_SLUG = "2026-10-02-creation-root-loss-corrected"
MEMBER_SLUG = "2026-10-02-creation-member-loss"
CLAIM = ROOT / "corrected-fault-continuation"
RESULT = ROOT / "corrected-fault-result.json"
OBSERVATION = w.PROOF.with_name("root-observation.jsonl")
OBSERVATION_SHA256 = "4127dfe5cf3f7f62272232fb92c48d3e1591c3b09adfdaa579a86cade4e082ee"
SOURCES = {
    "verify-creation.py": "afd95a7de8483b0726223cbce37a2ec316a184c81eba8a388a261800f36cc304",
    "verify-fault-creation.py": "6a9ea19a49d8e61c88ca6b8e0b24085dae7fba7fdd5d7aef57d84839f25048c4",
    "verify-started-creation.py": "86228a7a44e44bfeb323f0df261490a901566188d64336935fb9e59550d47f57",
    "verify-warmup-creation.py": "d45a474c5ef69dde3038474398bb2a4bf90e10dcb6956bdc9df6d6fbbb691b47",
}


def require_provider(package, expected_sha, config):
    h.require(package == PROVIDER_PACKAGE and expected_sha == PROVIDER_SHA256
              and package.resolve(strict=True) == package, "not the parent-frozen corrected provider")
    selected = {"path": str(package / "bin/workspace-portal"), "sha256": expected_sha}
    h.require(h.root_recovery_provider({**config, "rootRecoveryProvider": selected},
              ["thread", "create", "--session-slug", ROOT_SLUG]) == selected["path"],
              "corrected provider dispatch refused")
    h.require((package / "libexec/codex/bin/codex").resolve(strict=True) == Path(config["codex"]),
              "corrected provider selects different Codex")
    for name in ("share/workspace-portal/runtime-contract.json", "share/dev-workspace/agent-teams.json"):
        h.require((package / name).read_bytes() == (PACKAGE / name).read_bytes(),
                  "corrected provider contract or installed catalog changed")
    return selected


def validate_fixture(package, provider_sha):
    """Only the exact diagnosed after-five-samples fixture, with two absent slugs."""
    h.require(f.digest(f.PACKET) == f.PACKET_SHA256, "original evidence packet changed")
    packet = h.read(f.PACKET)
    h.require(packet["root"] == str(ROOT) and not os.path.lexists(f.CLAIM)
              and not os.path.lexists(CLAIM) and not os.path.lexists(RESULT), "prior fault claim/result exists")
    for name, expected in SOURCES.items():
        h.require(f.digest(Path(__file__).with_name(name)) == expected, "reviewed prototype dependency changed")
    info = ROOT.lstat()
    h.require(ROOT.resolve(strict=True) == ROOT and stat.S_ISDIR(info.st_mode)
              and info.st_uid == os.geteuid() and stat.S_IMODE(info.st_mode) == 0o700,
              "private evidence root changed")
    for name, children in packet["layouts"].items():
        path = ROOT / name
        info = path.lstat()
        h.require(stat.S_ISDIR(info.st_mode) and info.st_uid == os.geteuid() and not info.st_mode & 0o022
                  and sorted(p.name for p in path.iterdir()) == children,
                  f"retained creation layout changed: {name}")
    f.require_records({**packet["records"], **packet["priorClaims"]})
    for path in (ROOT / "codex/auth.json", OBSERVATION):
        info = path.lstat()
        h.require(stat.S_ISREG(info.st_mode) and info.st_uid == os.geteuid()
                  and stat.S_IMODE(info.st_mode) == 0o600, "private auth/observation metadata changed")
    h.require(f.digest(OBSERVATION) == OBSERVATION_SHA256, "frozen root observation changed")
    previous, config, preset = (h.read(ROOT / name) for name in ("result.json", "config.json", "preset.json"))
    h.require(previous["state"] == "incomplete" and previous["candidate"] == str(PACKAGE)
              and previous["error"] == f"creation {f.SLUG} ended as failed; private receipt retained"
              and previous["resumedFrom"] == "warmup-continuation/result.json" and "faults" not in previous
              and previous["codexVersion"] == "codex-cli 0.160.0", "not the known original fault failure")
    h.require(config["root"] == str(ROOT) and config["package"] == str(PACKAGE)
              and config["workspace"] == str(ROOT / "workspace") and "rootRecoveryProvider" not in config,
              "original consumer configuration changed")
    # Original receipt/root/journal/no-goal/no-roster facts are bound by packet hashes.
    # No read/resume of the stranded root is needed or authorized here.
    f.require_services(config)
    f.require_successes(previous, config, preset)
    for slug in (ROOT_SLUG, MEMBER_SLUG):
        for name in (f"workspace/work/{slug}", f"workspace/archive/{slug}", f"workspace/worktrees/{slug}",
                     f"workspace/worktrees/.locks/{slug}.creation.json",
                     f"state/portal/{w.NAMESPACE}/creations/{slug}.json",
                     f"state/codex-teams/{w.NAMESPACE}/{slug}.json", f"r/bench/authority/{slug}.json",
                     f"events/{slug}.jsonl"):
            h.require(not os.path.lexists(ROOT / name), "fresh fault destination already exists")
    selected = require_provider(package, provider_sha, config)
    return previous, config, preset, packet, selected


def preserve_failure(packet, selected):
    CLAIM.mkdir(mode=0o700)  # Exclusive and never removed, even on incomplete preservation.
    sources = [(name, ROOT / name) for name in packet["records"]]
    sources += [("fault-records.json", f.PACKET), ("root-observation.jsonl", OBSERVATION),
                ("warmup-host-proof.json", w.PROOF), ("host-process-proof.json", d.PROOF),
                ("host-socket-alias-proof.json", d.ALIAS_PROOF)]
    sources += [("sources/" + name, Path(__file__).with_name(name))
                for name in [*SOURCES, Path(__file__).name]]
    for name, source in sources:
        target = CLAIM / name
        target.parent.mkdir(parents=True, exist_ok=True, mode=0o700)
        with target.open("xb") as stream:
            os.fchmod(stream.fileno(), 0o600)
            stream.write(source.read_bytes())
            stream.flush()
            os.fsync(stream.fileno())
    provenance = {"provider": selected, "runtime": "924c0ec28c41dd8b56aaf17f2212b302ca614899",
                  "workspace": "1b670e0329c80b5ed266f6edb92ac2096134677c", "oldReceiptUntouched": f.RECEIPT_ID,
                  "oldRootUnavailable": f.ROOT_ID, "originalRecords": packet["records"],
                  "priorClaims": packet["priorClaims"], "sources": {**SOURCES, Path(__file__).name: f.digest(Path(__file__))},
                  "observationSHA256": OBSERVATION_SHA256, "createdAt": h.stamp()}
    with (CLAIM / "provenance.json").open("xb") as stream:
        os.fchmod(stream.fileno(), 0o600)
        stream.write((h.json.dumps(provenance, indent=2) + "\n").encode())
        stream.flush()
        os.fsync(stream.fileno())
    for directory in [p for p in CLAIM.rglob("*") if p.is_dir()] + [CLAIM, ROOT]:
        descriptor = os.open(directory, os.O_RDONLY | os.O_DIRECTORY)
        try:
            os.fsync(descriptor)
        finally:
            os.close(descriptor)


def run_fault(config, preset, name, kind):
    result = h.create(config, preset, name, 180, kind)
    slug = "2026-10-02-" + name
    h.require(result["slug"] == slug, "fixed fault slug changed")
    receipt, roster = h.ready_evidence(config, {"slug": slug}, preset)
    h.require(receipt["attempt"] == 2 and receipt["receiptId"] == result["firstAttempt"]["receiptId"]
              and receipt["goal"] == h.GOAL and receipt["directTeam"] == preset,
              "fault retry changed receipt, goal or frozen Full preset")
    if kind == "root-response":
        h.require(result["fault"]["rootThreadID"] == roster["rootThreadId"] == result["rootThreadID"]
                  and result["rootOutcome"] == "same ID recovered", "corrected fault replaced its root")
    f.require_dispatches(config, slug, 2)
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--provider-package", type=Path, required=True)
    parser.add_argument("--provider-sha256", required=True)
    parser.add_argument("--preflight", action="store_true", help="no RPC, subprocesses, claims or writes")
    args = parser.parse_args()
    previous, config, preset, packet, selected = validate_fixture(args.provider_package, args.provider_sha256)
    h.require(h.dt.datetime.now(h.dt.timezone.utc).date().isoformat() == "2026-10-02",
              "fixed fault date changed; parent must diagnose")
    if args.preflight:
        print("Read-only fresh-fault preflight passed; no RPC, claim or mutation.", flush=True)
        return 0
    f.require_records({**packet["records"], **packet["priorClaims"]})
    f.require_services(config)
    os.umask(0o077)
    preserve_failure(packet, selected)
    result = {"state": "running", "verificationKind": "old-consumer/new-thread-create-provider fresh faults",
              "originalResultSHA256": packet["records"]["result.json"], "oldReceiptUntouched": f.RECEIPT_ID,
              "oldRootUnavailable": f.ROOT_ID, "originalCandidate": str(PACKAGE),
              "providerPackage": str(args.provider_package), "rootRecoveryProvider": selected,
              "originalTiming": copy.deepcopy(previous["timing"]), "faults": [], "startedAt": h.stamp()}
    config = {**config, "rootRecoveryProvider": selected}
    try:
        h.save(ROOT / "config.json", config)
        h.save(RESULT, result)
        for name, kind in (("creation-root-loss-corrected", "root-response"),
                           ("creation-member-loss", "member-progress")):
            h.require(h.dt.datetime.now(h.dt.timezone.utc).date().isoformat() == "2026-10-02",
                      "fixed fault date changed between cases; do not retry")
            result["faults"].append(run_fault(config, preset, name, kind))
            h.save(RESULT, result)
        f.require_records({**{k: v for k, v in packet["records"].items() if k != "config.json"},
                           **packet["priorClaims"]})
        f.require_services(config)
        result.update(state="passed", finishedAt=h.stamp(),
                      retained="Original result, stranded receipt and five samples unchanged; no activation.")
        h.save(RESULT, result)
        print("Both fresh provider faults passed; original result retained. Full-package canary still required.", flush=True)
        return 0
    except Exception as error:
        result.update(state="incomplete", finishedAt=h.stamp(),
                      error=str(error) if isinstance(error, h.Failure) else type(error).__name__)
        h.save(RESULT, result)
        print("Fresh fault verification incomplete; preserve evidence and services. Do not retry.", flush=True)
        return 1


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as error:
        reason = str(error) if isinstance(error, h.Failure) else type(error).__name__
        print(f"Fresh fault verification refused: {reason}; no automatic retry.", file=sys.stderr)
        sys.exit(1)

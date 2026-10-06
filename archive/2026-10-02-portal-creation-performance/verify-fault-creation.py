#!/usr/bin/env python3
"""One use: verify two faults with old Ruby and a pinned corrected thread/create provider.

--preflight performs local metadata checks only. Read verification-fault-preparation.md.
"""

import argparse
import copy
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import stat
import statistics
import sys
import time

sys.dont_write_bytecode = True
SPEC = importlib.util.spec_from_file_location("warmup_verification", Path(__file__).with_name("verify-warmup-creation.py"))
w = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(w)
d, h = w.d, w.h
ROOT, PACKAGE = w.ROOT, w.PACKAGE
SLUG = "2026-10-02-creation-root-loss"
ROOT_ID = "01a0fe38-b8e0-76c1-b8f0-fd84783964a5"
MEMBER_SLUG = "2026-10-02-creation-member-loss"
RECEIPT_ID = "a4ad299484ab1972eb099a9b08793976cc442dc0ce8bae6fa768bba282e37634"
CLAIM = ROOT / "fault-continuation"
PACKET = Path(__file__).with_name("verification-fault-records.json")
PACKET_SHA256 = "260a13f810d5ab3213ce392613ea14c694e217de43ee0df905963d5334d9a36c"
TIMES = [6.121214866638184, 6.401348829269409, 6.332730054855347,
         6.500733852386475, 6.4283411502838135]


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def require_records(records):
    for name, expected in records.items():
        path = ROOT / name
        info = path.lstat()
        h.require(stat.S_ISREG(info.st_mode) and info.st_uid == os.geteuid()
                  and not info.st_mode & 0o022 and digest(path) == expected,
                  f"retained record changed: {name}")


def require_services(config):
    for path, expected in ((w.PROOF, w.PROOF_SHA256), (d.PROOF, d.PROOF_SHA256),
                           (d.ALIAS_PROOF, d.ALIAS_PROOF_SHA256)):
        info = path.lstat()
        h.require(stat.S_ISREG(info.st_mode) and info.st_uid == os.geteuid()
                  and stat.S_IMODE(info.st_mode) == 0o600 and digest(path) == expected,
                  "parent process/socket proof changed")
    proof, original, alias = h.read(w.PROOF), h.read(d.PROOF), h.read(d.ALIAS_PROOF)
    h.require(proof["root"] == str(ROOT) and proof["candidate"] == str(PACKAGE)
              and proof["originalProcessProofSHA256"] == d.PROOF_SHA256
              and proof["originalAliasProofSHA256"] == d.ALIAS_PROOF_SHA256,
              "original process proof ancestry changed")
    w.require_retained_services(proof, original, alias, h.native_codex_entrypoint(config["codex"]))
    processes = h.read(ROOT / "processes.json")
    h.require([{k: p[k] for k in ("label", "pid", "startedAt")} for p in processes] ==
              [{k: p[k] for k in ("label", "pid", "startedAt")} for p in proof["processes"]],
              "retained process sequence changed")
    profile = (ROOT / "profile").lstat()
    h.require(stat.S_ISLNK(profile.st_mode) and profile.st_uid == os.geteuid() and
              [profile.st_dev, profile.st_ino, profile.st_ctime_ns, profile.st_mtime_ns,
               os.readlink(ROOT / "profile")] == d.PROFILE_IDENTITY,
              "selected private profile changed")


def require_provider(package, expected_sha, config):
    h.require(package.is_absolute() and package.resolve(strict=True) == package
              and package.parent == Path("/nix/store") and package != PACKAGE,
              "an explicit different immutable provider package is required")
    provider = (package / "bin/workspace-portal").resolve(strict=True)
    selected = {"path": str(provider), "sha256": expected_sha}
    h.root_recovery_provider({**config, "rootRecoveryProvider": selected},
                             ["thread", "create", "--session-slug", SLUG])
    h.require((package / "libexec/codex/bin/codex").resolve(strict=True) == Path(config["codex"])
              and (package / "share/workspace-portal/runtime-contract.json").read_bytes() ==
              (PACKAGE / "share/workspace-portal/runtime-contract.json").read_bytes(),
              "provider Codex selection or public runtime contract differs")
    return selected


def require_successes(previous, config, preset):
    h.require([x["slug"] for x in previous["results"]] ==
              [f"2026-10-02-creation-sample-{i}" for i in range(1, 6)]
              and [x["acceptanceToReadySeconds"] for x in previous["results"]] == TIMES
              and previous["timing"] == {"allSeconds": TIMES, "medianSeconds": statistics.median(TIMES),
                                          "maxSeconds": max(TIMES), "passed": True}
              and statistics.median(TIMES) < 10 and max(TIMES) < 15,
              "original five timing samples or gates changed")
    team_ids = set()
    for entry in [previous["warmup"], *previous["results"]]:
        receipt, roster = h.ready_evidence(config, entry["firstAttempt"], preset)
        h.require(receipt["attempt"] == 1 and receipt["receiptId"] == entry["firstAttempt"]["receiptId"]
                  and receipt["goal"] == h.GOAL and entry["rootThreadID"] == roster["rootThreadId"]
                  and entry["memberThreadIDs"] == {m["address"]: m["threadId"] for m in roster["members"]}
                  and entry["readyAt"] == receipt["updatedAt"] and entry["model"]["initialUserMessages"] == 1
                  and entry["model"]["firstAssistantAt"] and entry["model"]["turnCompletedAt"],
                  "retained successful creation evidence changed")
        h.progress_evidence(config, entry["slug"], preset)
        team_ids.update([entry["rootThreadID"], *entry["memberThreadIDs"].values()])
    for i, entry in enumerate(previous["results"], 1):
        h.require(h.read(ROOT / f"creation-sample-{i}-result.json") == entry,
                  "retained individual sample differs from original result")
    paths = list((ROOT / "codex/sessions").rglob("*.jsonl"))
    seeds = [p for p in paths if not any(p.name.endswith(t + ".jsonl") for t in team_ids)]
    history = h.read(ROOT / "history.json")
    h.require(len(team_ids) == 24 and len(paths) == 3403 and len(seeds) == 3379
              and previous["history"] == history and history["activeRollouts"] == 3379
              and history["paddingBytesPerThread"] == 16384 and history["archivedRollouts"] == 0
              and sum(p.stat().st_size for p in seeds) == history["bytes"] == 208256155
              and not (ROOT / "codex/archived_sessions").exists(), "retained history metadata changed")
    for path in paths:
        info = path.lstat()
        h.require(stat.S_ISREG(info.st_mode) and info.st_uid == os.geteuid() and not info.st_mode & 0o022,
                  "retained rollout ownership/type changed")
    h.require(all(p.stat().st_size >= 16384 for p in seeds)
              and not any(ROOT_ID in p.name for p in paths), "seed sizes or unmaterialized root changed")


def validate_fault_fixture(package, provider_sha):
    """Finite read-only preflight: no RPC, subprocess, model or rollout payload reads."""
    h.require(digest(PACKET) == PACKET_SHA256, "reviewed evidence packet changed")
    packet = h.read(PACKET)
    h.require(packet["root"] == str(ROOT) and not os.path.lexists(CLAIM),
              "wrong fixture or prior fault continuation claim")
    for name, expected in packet["sources"].items():
        h.require(digest(Path(__file__).with_name(name)) == expected, "reviewed prototype dependency changed")
    info = ROOT.lstat()
    h.require(ROOT.resolve(strict=True) == ROOT and stat.S_ISDIR(info.st_mode)
              and info.st_uid == os.geteuid() and stat.S_IMODE(info.st_mode) == 0o700,
              "private evidence root changed")
    for name, children in packet["layouts"].items():
        path = ROOT / name
        info = path.lstat()
        h.require(stat.S_ISDIR(info.st_mode) and info.st_uid == os.geteuid() and not info.st_mode & 0o022
                  and sorted(p.name for p in path.iterdir()) == children,
                  f"retained session/creation layout changed: {name}")
    require_records({**packet["records"], **packet["priorClaims"]})
    auth = (ROOT / "codex/auth.json").lstat()
    h.require(stat.S_ISREG(auth.st_mode) and auth.st_uid == os.geteuid()
              and stat.S_IMODE(auth.st_mode) == 0o600, "retained auth metadata changed")
    previous, config, preset = (h.read(ROOT / name) for name in ("result.json", "config.json", "preset.json"))
    h.require(previous["state"] == "incomplete" and previous["candidate"] == str(PACKAGE)
              and previous["error"] == f"creation {SLUG} ended as failed; private receipt retained"
              and previous["resumedFrom"] == "warmup-continuation/result.json" and "faults" not in previous
              and previous["codexVersion"] == "codex-cli 0.160.0",
              "not the known after-samples fault failure")
    h.require(config["root"] == str(ROOT) and config["package"] == str(PACKAGE)
              and config["workspace"] == str(ROOT / "workspace") and "rootRecoveryProvider" not in config,
              "original consumer/config identity changed")
    require_services(config)
    receipt, roster = h.snapshot(config, SLUG)
    journal = h.read(ROOT / "workspace/worktrees/.locks" / (SLUG + ".creation.json"))
    fault = h.read(ROOT / "fault.json")
    before = h.read(ROOT / "creation-root-loss-before-retry.json")
    h.require(receipt["schema"] == 3 and receipt["state"] == "failed" and receipt["attempt"] == 2
              and receipt["receiptId"] == RECEIPT_ID and receipt["directTeam"] == preset
              and receipt["goal"] == h.GOAL and roster is None
              and journal["state"] == "creating" and journal["direct_team"] == preset
              and fault["kind"] == "root-response" and fault["slug"] == SLUG and fault["armed"] is False
              and fault["rootThreadID"] == ROOT_ID and not fault.get("injectionError")
              and before["receipt"]["receiptId"] == RECEIPT_ID and before["receipt"]["attempt"] == 1
              and before["roster"] is None, "diagnosed root-fault identity changed")
    # The exact pinned YAML contains no root ID and attempted=false; never rewrite it.
    require_successes(previous, config, preset)
    selected = require_provider(package, provider_sha, config)
    return previous, config, preset, packet, selected


def preserve_failure(packet):
    CLAIM.mkdir(mode=0o700)  # Exclusive and never removed, including on failure.
    sources = [(name, ROOT / name) for name in packet["records"]]
    sources += [("fault-records.json", PACKET), ("warmup-host-proof.json", w.PROOF),
                ("host-process-proof.json", d.PROOF), ("host-socket-alias-proof.json", d.ALIAS_PROOF)]
    for name, source in sources:
        target = CLAIM / name
        target.parent.mkdir(parents=True, exist_ok=True, mode=0o700)
        with target.open("xb") as stream:
            os.fchmod(stream.fileno(), 0o600)
            stream.write(source.read_bytes())
            stream.flush()
            os.fsync(stream.fileno())
    for directory in [p for p in CLAIM.rglob("*") if p.is_dir()] + [CLAIM, ROOT]:
        descriptor = os.open(directory, os.O_RDONLY | os.O_DIRECTORY)
        try:
            os.fsync(descriptor)
        finally:
            os.close(descriptor)


def require_dispatches(config, slug, count):
    events = [json.loads(line) for line in (ROOT / "events" / (slug + ".jsonl")).read_text().splitlines()]
    dispatches = [e["providerDispatch"] for e in events if "providerDispatch" in e]
    h.require(len(dispatches) == count and all(
        item["path"] == config["rootRecoveryProvider"]["path"] and
        item["sha256"] == config["rootRecoveryProvider"]["sha256"] for item in dispatches),
        "corrected thread/create provider was not used exactly as expected")


def retry_root(config, preset):
    before = h.read(CLAIM / "creation-root-loss-before-retry.json")
    failed = h.read(CLAIM / f"state/portal/{w.NAMESPACE}/creations/{SLUG}.json")
    accepted = {"startedAt": before["receipt"]["startedAt"]}
    result = {"slug": SLUG, "acceptedAt": accepted["startedAt"], "firstAttempt": before["receipt"],
              "failedSecondAttempt": failed, "fault": h.read(CLAIM / "fault.json")}
    start = time.monotonic_ns()
    retried = h.http(config, "POST", f"/api/sessions/{SLUG}/creation/retry",
                     {"receiptId": RECEIPT_ID, "attempt": 2})
    h.require(retried["attempt"] == 3 and retried["receiptId"] == RECEIPT_ID and retried["slug"] == SLUG,
              "root retry receipt identity changed")
    status = h.wait_creation(config, retried)
    receipt, roster = h.ready_evidence(config, status, preset)
    h.require(receipt["attempt"] == 3 and receipt["receiptId"] == RECEIPT_ID
              and roster["rootThreadId"] == ROOT_ID, "retained root was replaced or retry identity changed")
    result["retryAcceptedAt"] = retried["startedAt"]
    result["retryAcceptanceToReadySeconds"] = h.instant(receipt["updatedAt"]) - h.instant(retried["startedAt"])
    result = h.complete_creation(config, preset, "creation-root-loss", SLUG, 180, "root-response",
                                 start, accepted, result, None, status)
    require_dispatches(config, SLUG, 1)
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--provider-package", type=Path, required=True)
    parser.add_argument("--provider-sha256", required=True, help="parent-reviewed compiled Go binary SHA256")
    parser.add_argument("--preflight", action="store_true", help="read-only checks; no claim, writes or RPC")
    args = parser.parse_args()
    previous, config, preset, packet, selected = validate_fault_fixture(args.provider_package, args.provider_sha256)
    if args.preflight:
        print("Read-only fault preflight passed; no claim, RPC or writes.", flush=True)
        return 0
    h.require(h.dt.datetime.now(h.dt.timezone.utc).date().isoformat() == "2026-10-02",
              "fixed member-fault creation date changed; parent must diagnose")
    require_records({**packet["records"], **packet["priorClaims"]})
    require_services(config)
    os.umask(0o077)
    preserve_failure(packet)
    result = copy.deepcopy(previous)
    result.pop("error")
    result.pop("finishedAt", None)
    result.update(state="running", resumedFrom="fault-continuation/result.json", faults=[],
                  verificationKind="old-consumer/new-thread-create-provider faults",
                  providerPackage=str(args.provider_package), rootRecoveryProvider=selected)
    config = {**config, "rootRecoveryProvider": selected}
    try:
        h.save(ROOT / "config.json", config)
        h.save(ROOT / "result.json", result)
        result["faults"].append(retry_root(config, preset))
        h.save(ROOT / "result.json", result)
        result["faults"].append(h.create(config, preset, "creation-member-loss", 180, "member-progress"))
        require_dispatches(config, MEMBER_SLUG, 2)
        h.require(result["results"] == previous["results"] and result["timing"] == previous["timing"]
                  and result["warmup"] == previous["warmup"] and len(result["faults"]) == 2,
                  "retained timing/model evidence changed")
        result.update(state="passed", finishedAt=h.stamp(),
                      retained="All evidence, claims and services retained; full-package canary still required.")
        h.save(ROOT / "result.json", result)
        print("Both provider compatibility faults passed; five original timings retained. No activation.", flush=True)
        return 0
    except Exception as error:
        result.update(state="incomplete", finishedAt=h.stamp(),
                      error=str(error) if isinstance(error, h.Failure) else type(error).__name__)
        h.save(ROOT / "result.json", result)
        print("Fault continuation incomplete; evidence and services retained. Do not retry.", flush=True)
        return 1


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as error:
        reason = str(error) if isinstance(error, h.Failure) else type(error).__name__
        print(f"Fault continuation refused: {reason}; no automatic retry.", file=sys.stderr)
        sys.exit(1)

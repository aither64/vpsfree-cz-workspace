#!/usr/bin/env python3
"""Session-only native RSpec JSON parity check for the approved static rebalance.

Usage: python3 compare-results.py BASELINE_DIR CANDIDATE1_DIR CANDIDATE2_DIR
       python3 compare-results.py --self-test

Directories must contain separately extracted artifacts from explicit runs and
attempts. Result filenames are rspec-results-<full|core>-<topic>.json; artifact
subdirectories are allowed. File-manifest coverage remains the workflow gate's
responsibility. No test selection, duration balancing, or artifact fetching.

Each result must have sibling rspec-environment-<mode>-<topic>.json metadata.
Exit 0 means example/dependency parity passed (or self-tests passed); exit 1
means invalid, incomplete or unequal evidence; exit 2 means CLI misuse. Overall
benchmark acceptance (workflow gate, timings, source equality) is not assessed.
"""

import argparse
from collections import Counter
import copy
import json
import math
from pathlib import Path
import re
import sys
import tempfile


OLD_TOPICS = (
    "smoke", "coverage", "routes", "engine", "plugins", "supervisor", "dns",
    "storage", "network", "mail", "users-auth", "vps", "platform",
)
NEW_TOPICS = (
    "foundation", "plugins", "dns", "storage", "mail", "vps",
    "platform-infrastructure", "platform-operations", "platform-config",
    "auth", "users", "ip-ownership", "network",
)
MODES = ("full", "core")
ENVIRONMENT_KEYS = ("ruby", "bundler", "rspec", "gemfile_lock_sha256")


class InvalidResults(ValueError):
    pass


def require(condition, message):
    if not condition:
        raise InvalidResults(message)


def unique_keys(pairs):
    result = {}
    for key, value in pairs:
        require(key not in result, f"duplicate JSON object key: {key!r}")
        result[key] = value
    return result


def reject_constant(value):
    raise InvalidResults(f"non-finite JSON number: {value}")


def normalized_path(value):
    require(isinstance(value, str), "file path must be a string")
    while value.startswith("./"):
        value = value[2:]
    require(value.startswith("spec/") and value.endswith(".rb"),
            f"expected API-relative Ruby source path: {value!r}")
    require("\\" not in value and not any(p in ("", ".", "..")
                                          for p in value.split("/")),
            f"noncanonical spec path: {value!r}")
    return value


def normalized_example(example):
    require(isinstance(example, dict), "example must be an object")
    required = {"id", "file_path", "status", "pending_message"}
    require(required <= example.keys(), f"missing example fields: {required - example.keys()}")
    identity = example["id"]
    require(isinstance(identity, str), "example ID must be a string")
    match = re.fullmatch(r"(.+)\[([1-9][0-9]*(?::[1-9][0-9]*)*)\]", identity)
    require(match is not None, f"missing/invalid full scoped example ID: {identity!r}")
    path = normalized_path(example["file_path"])
    identity_path = normalized_path(match[1])
    require(identity_path.endswith("_spec.rb"), f"ID must identify a spec file: {identity!r}")
    # RSpec IDs use rerun_file_path; shared examples can have a support .rb
    # definition file_path. Preserve and compare both without conflating them.
    status = example["status"]
    require(status in ("passed", "pending"), f"failed or unknown example status: {status!r}")
    pending = example["pending_message"]
    require(pending is None or isinstance(pending, str), "invalid pending_message")
    require(status != "pending" or isinstance(pending, str), "pending example lacks reason")
    require(status != "passed" or pending is None, "passed example has pending reason")
    return f"{identity_path}[{match[2]}]", (path, status, pending)


def read_result(path):
    try:
        data = json.loads(path.read_text(encoding="utf-8"),
                          object_pairs_hook=unique_keys, parse_constant=reject_constant)
        require(isinstance(data, dict), "result must be an object")
        examples, summary = data.get("examples"), data.get("summary")
        require(isinstance(examples, list), "missing examples array")
        require(isinstance(summary, dict), "missing summary object")
        rows = [normalized_example(example) for example in examples]
        expected = {
            "example_count": len(rows), "failure_count": 0,
            "pending_count": sum(row[1][1] == "pending" for row in rows),
            "errors_outside_of_examples_count": 0,
        }
        for key, count in expected.items():
            value = summary.get(key)
            require(type(value) is int and value == count,
                    f"summary {key}: expected {count}, got {value!r}")
        duration = summary.get("duration")
        require(type(duration) in (int, float) and math.isfinite(duration) and duration >= 0,
                "summary duration must be finite and nonnegative")
        require(type(data.get("seed")) is int and data["seed"] >= 0,
                "missing/invalid randomized-run seed")
        require(isinstance(data.get("version"), str) and data["version"],
                "missing RSpec version")
        return rows, data["seed"], data["version"]
    except (OSError, UnicodeError, json.JSONDecodeError, InvalidResults) as error:
        raise InvalidResults(f"{path}: {error}") from error


def read_environment(path, mode, topic, rspec_version):
    try:
        data = json.loads(path.read_text(encoding="utf-8"),
                          object_pairs_hook=unique_keys, parse_constant=reject_constant)
        require(isinstance(data, dict), "environment must be an object")
        require(data.get("mode") == mode and data.get("topic") == topic,
                "environment mode/topic does not match result filename")
        for key in ENVIRONMENT_KEYS:
            require(isinstance(data.get(key), str) and data[key].strip(),
                    f"missing/invalid environment {key}")
        require(re.fullmatch(r"[0-9a-f]{64}", data["gemfile_lock_sha256"]) is not None,
                "invalid lockfile SHA256")
        require(data["rspec"] == rspec_version, "native JSON/environment RSpec version mismatch")
        return {key: data[key] for key in ENVIRONMENT_KEYS}
    except (OSError, UnicodeError, json.JSONDecodeError, InvalidResults) as error:
        raise InvalidResults(f"{path}: {error}") from error


def load_run(directory, topics):
    require(directory.is_dir(), f"not an extracted artifact directory: {directory}")
    expected = {f"rspec-results-{mode}-{topic}.json": (mode, topic)
                for mode in MODES for topic in topics}
    for kind in ("results", "environment"):
        names = {name.replace("rspec-results-", f"rspec-{kind}-") for name in expected}
        found = sorted(p for p in directory.rglob(f"rspec-{kind}-*.json") if p.is_file())
        counts = Counter(p.name for p in found)
        missing = sorted(names - counts.keys())
        extra = sorted(counts.keys() - names)
        duplicate = sorted(name for name, count in counts.items() if count != 1)
        require(not (missing or extra or duplicate),
                f"{directory}: expected exactly 13 {kind} files per mode; "
                f"missing={missing}, extra={extra}, duplicate={duplicate}; "
                "incomplete evidence leaves parity unresolved")
        if kind == "results":
            files = found
    modes = {mode: {} for mode in MODES}
    evidence = {mode: {"seeds": {}, "rspec_versions": set()} for mode in MODES}
    environments = {}
    for path in files:
        mode, topic = expected[path.name]
        rows, seed, version = read_result(path)
        environment = read_environment(path.with_name(f"rspec-environment-{mode}-{topic}.json"),
                                       mode, topic, version)
        require(mode not in environments or environments[mode] == environment,
                f"{directory}: differing dependency fingerprints within {mode}, topic {topic}")
        environments[mode] = environment
        evidence[mode]["seeds"][topic] = seed
        evidence[mode]["rspec_versions"].add(version)
        for identity, value in rows:
            require(identity not in modes[mode],
                    f"{directory}: duplicate {mode} example ID {identity!r}")
            modes[mode][identity] = value
    for mode, rows in modes.items():
        require(rows, f"{directory}: no executed examples in {mode} mode")
        evidence[mode].update({
            "examples": len(rows),
            "pending": sum(value[1] == "pending" for value in rows.values()),
            "rspec_versions": sorted(evidence[mode]["rspec_versions"]),
            "environment": environments[mode],
        })
    return modes, evidence


def compare(baseline, candidate1, candidate2):
    directories = (baseline, candidate1, candidate2)
    require(len({p.resolve() for p in directories}) == 3,
            "baseline and candidate directories must be distinct")
    runs = [load_run(path, OLD_TOPICS if i == 0 else NEW_TOPICS)
            for i, path in enumerate(directories)]
    for index in (1, 2):
        for mode in MODES:
            old, new = runs[0][0][mode], runs[index][0][mode]
            missing, extra = sorted(old.keys() - new.keys()), sorted(new.keys() - old.keys())
            changed = sorted(key for key in old.keys() & new.keys() if old[key] != new[key])
            require(not (missing or extra or changed),
                    f"candidate{index}/{mode}: parity mismatch; "
                    f"missing={missing}, extra={extra}, changed={changed}")
            require(runs[0][1][mode]["environment"] == runs[index][1][mode]["environment"],
                    f"candidate{index}/{mode}: dependency fingerprints differ from baseline")
    return {
        "example_parity": "passed",
        "benchmark_acceptance": "not_assessed",
        "dependencies": {"status": "passed", "scope": "within mode, all jobs and all three runs"},
        "runs": {label: {"directory": str(path.resolve()), "modes": result[1]}
                 for label, path, result in zip(
                     ("baseline", "candidate1", "candidate2"), directories, runs)},
    }


def self_test():
    """Tiny fixtures exercise comparison boundaries without running any specs."""
    with tempfile.TemporaryDirectory(prefix="api-spec-parity-") as temporary:
        roots = [Path(temporary) / name for name in ("baseline", "candidate1", "candidate2")]
        fixtures = {}
        for run, root in enumerate(roots):
            topics = OLD_TOPICS if run == 0 else NEW_TOPICS
            for mode in MODES:
                for index, topic in enumerate(topics):
                    identity = index if run == 0 else (index + run) % 13
                    file_path = f"spec/demo_{identity}_spec.rb"
                    if run == 0:
                        file_path = "./" + file_path
                    pending = identity == 0
                    artifact = root / f"rspec-results-{mode}-{topic}"
                    fixtures[artifact / f"rspec-results-{mode}-{topic}.json"] = {
                        "version": "3.13.6", "seed": 100 + run,
                        "examples": [{"id": file_path + "[1:1]",
                                      "file_path": "spec/support/shared.rb" if identity == 5 else file_path,
                                      "status": "pending" if pending else "passed",
                                      "pending_message": "requires plugins" if pending else None}],
                        "summary": {"duration": 0.01, "example_count": 1, "failure_count": 0,
                                    "pending_count": int(pending), "errors_outside_of_examples_count": 0},
                    }
                    fixtures[artifact / f"rspec-environment-{mode}-{topic}.json"] = {
                        "mode": mode, "topic": topic, "ruby": "ruby 3.4.6 fixture",
                        "bundler": "2.6.9", "rspec": "3.13.6",
                        "gemfile_lock_sha256": ("a" if mode == "full" else "b") * 64,
                    }
        for path, data in fixtures.items():
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(json.dumps(data))
        require(compare(*roots)["example_parity"] == "passed", "reshuffle failed")
        checked = ["passing topic reshuffle, ./ normalization, separate full/core locks",
                   "shared example definition path differs from rerun ID path"]
        target = roots[1] / "rspec-results-full-network" / "rspec-results-full-network.json"  # pending ID 0
        original = fixtures[target]

        def check_bad(name, data=None, raw=None, remove=False):
            if remove:
                target.unlink()
            else:
                target.write_text(raw if raw is not None else json.dumps(data))
            try:
                compare(*roots)
            except InvalidResults:
                checked.append(name)
            else:
                raise AssertionError(f"invalid fixture accepted: {name}")
            finally:
                target.write_text(json.dumps(original))

        check_bad("malformed JSON", raw="{")
        check_bad("missing JSON", remove=True)
        for name, edit in (
            ("duplicate example IDs", lambda d: d.update(
                examples=d["examples"] * 2,
                summary={**d["summary"], "example_count": 2, "pending_count": 2})),
            ("pending reason drift", lambda d: d["examples"][0].update(pending_message="new skip")),
            ("outcome drift", lambda d: (
                d["examples"][0].update(status="passed", pending_message=None),
                d["summary"].update(pending_count=0))),
            ("scoped ID drift", lambda d: d["examples"][0].update(
                id="spec/demo_0_spec.rb[1:2]")),
            ("definition file drift", lambda d: d["examples"][0].update(
                file_path="spec/support/changed.rb")),
            ("incoherent summary", lambda d: d["summary"].update(example_count=2)),
            ("outside-example errors", lambda d: d["summary"].update(errors_outside_of_examples_count=1)),
            ("failed example", lambda d: d["examples"][0].update(status="failed")),
            ("unknown status", lambda d: d["examples"][0].update(status="skipped")),
        ):
            changed = copy.deepcopy(original)
            edit(changed)
            check_bad(name, data=changed)
        target = target.with_name("rspec-environment-full-network.json")
        original = fixtures[target]
        check_bad("missing metadata is incomplete/unresolved", remove=True)
        for name, edit in (
            ("metadata topic mismatch", lambda d: d.update(topic="platform")),
            ("metadata mode mismatch", lambda d: d.update(mode="core")),
            ("within-mode dependency drift", lambda d: d.update(gemfile_lock_sha256="c" * 64)),
            ("native/metadata RSpec version mismatch", lambda d: d.update(rspec="3.13.5")),
        ):
            changed = copy.deepcopy(original)
            edit(changed)
            check_bad(name, data=changed)
        duplicate = roots[1] / "duplicate" / target.name
        duplicate.parent.mkdir()
        duplicate.write_text(json.dumps(original))
        try:
            compare(*roots)
        except InvalidResults:
            checked.append("duplicate metadata filename in separate artifact")
        else:
            raise AssertionError("duplicate metadata accepted")
        duplicate.unlink()
        for path, data in fixtures.items():
            if roots[1] in path.parents and path.name.startswith("rspec-environment-full-"):
                path.write_text(json.dumps({**data, "gemfile_lock_sha256": "c" * 64}))
        try:
            compare(*roots)
        except InvalidResults as error:
            require("differ from baseline" in str(error), "cross-run fixture failed too early")
            checked.append("cross-run dependency drift with coherent per-mode metadata")
        else:
            raise AssertionError("cross-run drift accepted")
        return {"self_tests": "passed", "cases": checked}


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("directories", nargs="*", type=Path,
                        metavar="ARTIFACT_DIR")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if (args.self_test and args.directories) or (not args.self_test and len(args.directories) != 3):
        parser.error("use three explicit directories, or --self-test alone")
    try:
        report = self_test() if args.self_test else compare(*args.directories)
    except InvalidResults as error:
        print(json.dumps({"example_parity": "failed", "error": str(error)}, indent=2), file=sys.stderr)
        return 1
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    sys.exit(main())

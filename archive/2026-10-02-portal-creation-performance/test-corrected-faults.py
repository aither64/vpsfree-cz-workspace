#!/usr/bin/env python3
"""Focused pure/mocked checks. No fixture writes, subprocesses, RPC or model calls."""

import ast
from contextlib import ExitStack, redirect_stdout
import copy
import hashlib
import importlib.util
import io
from pathlib import Path
import sys
from types import SimpleNamespace
import unittest
from unittest.mock import patch

sys.dont_write_bytecode = True
SPEC = importlib.util.spec_from_file_location("corrected_faults", Path(__file__).with_name("verify-corrected-faults.py"))
m = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(m)
h, f = m.h, m.f


class CorrectedFaultTests(unittest.TestCase):
    def setUp(self):
        self.stack = ExitStack()
        self.addCleanup(self.stack.close)
        for obj, name in ((h, "http"), (h, "save"), (h, "append"), (h, "wait_model"),
                          (h.subprocess, "Popen"), (h.subprocess, "run"), (h.os, "execv")):
            self.stack.enter_context(patch.object(obj, name, side_effect=AssertionError("unexpected runtime/write action")))

    def test_unchanged_acceptance_and_shared_tail(self):
        tree = ast.parse(Path(h.__file__).read_text())
        funcs = {n.name: n for n in tree.body if isinstance(n, ast.FunctionDef)}
        names = ("initial_goal_parts", "wait_model", "ready_evidence", "progress_evidence",
                 "finish_creation_samples", "forward_stderr")
        gates = ast.Module(body=[funcs[n] for n in names], type_ignores=[])
        self.assertEqual(hashlib.sha256(ast.dump(gates).encode()).hexdigest(),
                         "32d44fa49aa2a83114da1aa4090365005eae296ab46046d2700d1fb1c24338b6")
        tail = ast.Module(body=funcs["complete_creation"].body[1:], type_ignores=[])
        self.assertEqual(hashlib.sha256(ast.dump(tail).encode()).hexdigest(),
                         "967b9906a9f5bbc3e13d565b66788a6ced57116e7d5ff716a86c3bd0e31a9cc7")

    def test_provider_exact_new_scope_and_old_fault_preserved(self):
        binary = b"\x7fELFmock"
        selected = {"path": str(m.PROVIDER_PACKAGE / "bin/workspace-portal"),
                    "sha256": hashlib.sha256(binary).hexdigest()}
        config = {"root": str(m.ROOT), "package": str(m.PACKAGE), "rootRecoveryProvider": selected}
        original = str(m.PACKAGE / "bin/workspace-portal")
        for slug in (f.SLUG, "another-slug"):
            self.assertEqual(h.root_recovery_provider(config, ["thread", "create", "--session-slug", slug]), original)
            self.assertEqual(h.creation_fault_path(config, slug), m.ROOT / "fault.json")
        for slug in (m.ROOT_SLUG, m.MEMBER_SLUG):
            argv = ["thread", "create", "--session-slug", slug, "--lead-instructions", "frozen"]
            before = argv[:]
            with patch.object(Path, "resolve", lambda self, strict=True: self), \
                    patch.object(Path, "is_file", return_value=True), patch.object(Path, "read_bytes", return_value=binary), \
                    patch.object(h.os, "access", return_value=True):
                self.assertEqual(h.root_recovery_provider(config, argv), selected["path"])
                self.assertEqual(argv, before)
                with self.assertRaises(h.Failure):
                    h.root_recovery_provider({**config, "rootRecoveryProvider": {**selected, "sha256": "0"*64}}, argv)
                with patch.object(Path, "read_bytes", return_value=b"#!/bin/sh"), self.assertRaises(h.Failure):
                    h.root_recovery_provider(config, argv)
            self.assertEqual(h.creation_fault_path(config, slug), m.ROOT / "corrected-fault.json")
            ordinary = {k: v for k, v in config.items() if k != "rootRecoveryProvider"}
            self.assertEqual(h.creation_fault_path(ordinary, slug), m.ROOT / "fault.json")
            self.assertEqual(h.root_recovery_provider(config, ["team", "apply-preset", "--session-slug", slug]), original)

    def test_frozen_provider_and_prior_claim_refusals(self):
        with self.assertRaises(h.Failure):
            m.require_provider(Path("/nix/store/wrong"), m.PROVIDER_SHA256, {})
        with self.assertRaises(h.Failure):
            m.require_provider(m.PROVIDER_PACKAGE, "0"*64, {})
        with patch.object(f, "digest", return_value=f.PACKET_SHA256), \
                patch.object(h, "read", return_value={"root": str(m.ROOT)}):
            for existing in (f.CLAIM, m.CLAIM, m.RESULT):
                with self.subTest(existing=existing), patch.object(m.os.path, "lexists", side_effect=lambda p: p == existing), \
                        self.assertRaises(h.Failure):
                    m.validate_fixture(m.PROVIDER_PACKAGE, m.PROVIDER_SHA256)

    def test_preservation_is_exclusive_and_fsynced_without_auth(self):
        events = []

        class Stream(io.BytesIO):
            def fileno(self):
                return 47

        def opening(path, mode):
            self.assertEqual(mode, "xb")
            self.assertNotIn("auth.json", str(path))
            events.append(("open", path))
            return Stream()

        with patch.object(Path, "mkdir", side_effect=lambda *a, **k: events.append(("mkdir", k))), \
                patch.object(Path, "open", opening), patch.object(Path, "read_bytes", return_value=b"metadata"), \
                patch.object(Path, "rglob", return_value=[]), patch.object(f, "digest", return_value="digest"), \
                patch.object(h, "stamp", return_value="now"), patch.object(m.os, "fchmod"), \
                patch.object(m.os, "fsync", side_effect=lambda fd: events.append(("fsync", fd))), \
                patch.object(m.os, "open", return_value=48), patch.object(m.os, "close"):
            m.preserve_failure({"records": {"result.json": "old", "fault.json": "old-fault"}, "priorClaims": {}}, {})
        self.assertEqual(events[0], ("mkdir", {"mode": 0o700}))
        self.assertEqual(events[-2:], [("fsync", 48), ("fsync", 48)])
        with patch.object(Path, "mkdir", side_effect=FileExistsError), patch.object(Path, "read_bytes") as read:
            with self.assertRaises(FileExistsError):
                m.preserve_failure({}, {})
            read.assert_not_called()

    def test_shared_create_requires_exact_root_and_receipt(self):
        result = {"slug": m.ROOT_SLUG, "firstAttempt": {"receiptId": "same"}, "rootThreadID": "original",
                  "fault": {"rootThreadID": "original"}, "rootOutcome": "same ID recovered"}
        receipt = {"attempt": 2, "receiptId": "same", "goal": h.GOAL, "directTeam": {}}
        with patch.object(h, "create", return_value=result) as create, \
                patch.object(h, "ready_evidence", return_value=(receipt, {"rootThreadId": "original"})), \
                patch.object(f, "require_dispatches") as dispatch:
            self.assertEqual(m.run_fault({}, {}, "creation-root-loss-corrected", "root-response"), result)
            create.assert_called_once_with({}, {}, "creation-root-loss-corrected", 180, "root-response")
            dispatch.assert_called_once_with({}, m.ROOT_SLUG, 2)
            for wrong in ("replacement", None):
                with patch.object(h, "ready_evidence", return_value=(receipt, {"rootThreadId": wrong})), self.assertRaises(h.Failure):
                    m.run_fault({}, {}, "creation-root-loss-corrected", "root-response")
            with patch.object(h, "ready_evidence", return_value=({**receipt, "attempt": 3}, {"rootThreadId": "original"})), \
                    self.assertRaises(h.Failure):
                m.run_fault({}, {}, "creation-root-loss-corrected", "root-response")

    def test_original_fault_injection_and_immediate_retry(self):
        # The shared helper must retry only after a triggered boundary and use the same receipt.
        accepted = {"slug": m.ROOT_SLUG, "attempt": 1, "receiptId": "receipt", "startedAt": "now"}
        failed = {**accepted, "state": "failed"}
        fault = {"armed": False, "rootThreadID": "original"}
        with patch.object(h, "http", side_effect=[accepted, {**accepted, "attempt": 2}]) as rpc, \
                patch.object(h, "wait_creation", side_effect=[failed, {**accepted, "state": "ready", "attempt": 2}]), \
                patch.object(h, "read", return_value=fault), patch.object(h, "snapshot", return_value=(failed, None)), \
                patch.object(h, "save"), patch.object(h, "complete_creation", return_value="done"):
            self.assertEqual(h.create({"root": str(m.ROOT)}, {"id": "full", "catalogDigest": "frozen"},
                                     "creation-root-loss-corrected", 180, "root-response"), "done")
            self.assertEqual(rpc.call_args_list[1].args[2:],
                             (f"/api/sessions/{m.ROOT_SLUG}/creation/retry", {"receiptId": "receipt", "attempt": 1}))
        for bad_fault in ({"armed": True}, {"armed": False, "injectionError": "missed"}):
            with patch.object(h, "http", return_value=accepted) as rpc, patch.object(h, "wait_creation", return_value=failed), \
                    patch.object(h, "read", return_value=bad_fault), patch.object(h, "save"), self.assertRaises(h.Failure):
                h.create({"root": str(m.ROOT)}, {"id": "full", "catalogDigest": "frozen"},
                         "creation-root-loss-corrected", 180, "root-response")
            self.assertEqual(rpc.call_count, 1)

    def test_preflight_order_separate_result_and_stop_on_failure(self):
        previous = {"timing": {"allSeconds": f.TIMES, "passed": True}}
        config = {"root": str(m.ROOT), "package": str(m.PACKAGE)}
        packet = {"records": {"result.json": "original", "fault.json": "original-fault", "config.json": "before"},
                  "priorClaims": {"seeded-continuation/result.json": "preserved"}}
        selected = {"path": str(m.PROVIDER_PACKAGE / "bin/workspace-portal"), "sha256": m.PROVIDER_SHA256}
        events = []
        fake_dt = SimpleNamespace(datetime=SimpleNamespace(now=lambda tz: SimpleNamespace(
            date=lambda: SimpleNamespace(isoformat=lambda: "2026-10-02"))), timezone=SimpleNamespace(utc=None))
        with patch.object(m, "validate_fixture", return_value=(previous, config, {}, packet, selected)), \
                patch.object(f, "require_records"), patch.object(f, "require_services"), \
                patch.object(m, "preserve_failure", side_effect=lambda *a: events.append("preserved")), \
                patch.object(m.os, "umask"), patch.object(h, "dt", fake_dt), patch.object(h, "stamp", return_value="now"), \
                patch.object(h, "save", side_effect=lambda p,v: events.append((p, copy.deepcopy(v)))), \
                patch.object(m, "run_fault", side_effect=lambda *a: events.append(a[2:]) or {"fault": a[3]}) as run, \
                redirect_stdout(io.StringIO()):
            argv = ["verify-corrected-faults.py", "--provider-package", str(m.PROVIDER_PACKAGE),
                    "--provider-sha256", m.PROVIDER_SHA256]
            with patch.object(sys, "argv", [*argv, "--preflight"]):
                self.assertEqual(m.main(), 0)
                self.assertEqual(events, [])
            with patch.object(sys, "argv", argv):
                self.assertEqual(m.main(), 0)
            self.assertEqual(events[0], "preserved")
            self.assertEqual(events[1], (m.ROOT / "config.json", {**config, "rootRecoveryProvider": selected}))
            self.assertEqual([c.args[2:] for c in run.call_args_list],
                             [("creation-root-loss-corrected", "root-response"), ("creation-member-loss", "member-progress")])
            self.assertEqual(events[-1][1]["state"], "passed")
            self.assertEqual(events[-1][1]["originalTiming"], previous["timing"])
            self.assertFalse(any(e[0] in (m.ROOT / "result.json", m.ROOT / "fault.json") for e in events if isinstance(e, tuple)))
            events.clear()
            with patch.object(m, "run_fault", side_effect=h.Failure("boundary missed")) as failed, patch.object(sys, "argv", argv):
                self.assertEqual(m.main(), 1)
                self.assertEqual(failed.call_count, 1)
            self.assertEqual(events[-1][1]["state"], "incomplete")


if __name__ == "__main__":
    unittest.main()

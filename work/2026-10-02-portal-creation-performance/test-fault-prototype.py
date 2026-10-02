#!/usr/bin/env python3
"""Focused in-memory checks only. Never launches the fixture or reads rollout payloads."""

import ast
from contextlib import ExitStack, redirect_stdout
import copy
import hashlib
import importlib.util
import io
from pathlib import Path
import stat
import sys
from types import SimpleNamespace
import unittest
from unittest.mock import patch

sys.dont_write_bytecode = True
SPEC = importlib.util.spec_from_file_location("fault_verification", Path(__file__).with_name("verify-fault-creation.py"))
m = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(m)
h = m.h


class FaultPrototypeTests(unittest.TestCase):
    def setUp(self):
        self.stack = ExitStack()
        self.addCleanup(self.stack.close)
        for obj, name in ((h, "http"), (h, "save"), (h, "append"), (h, "wait_model"),
                          (h.subprocess, "Popen"), (h.subprocess, "run"), (h.os, "execv")):
            self.stack.enter_context(patch.object(obj, name, side_effect=AssertionError("unexpected runtime/write action")))

    def test_original_acceptance_ast(self):
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

    def test_provider_dispatch_scope_and_identity(self):
        binary = b"\x7fELFfocused fixture"
        selected = {"path": "/nix/store/corrected/bin/workspace-portal",
                    "sha256": hashlib.sha256(binary).hexdigest()}
        config = {"root": str(m.ROOT), "package": str(m.PACKAGE), "rootRecoveryProvider": selected}
        original = str(m.PACKAGE / "bin/workspace-portal")
        for argv in (["team", "apply-preset", "--session-slug", m.MEMBER_SLUG],
                     ["thread", "create", "--session-slug", "another-session"], ["serve"], []):
            with self.subTest(argv=argv):
                self.assertEqual(h.root_recovery_provider(config, argv), original)
        argv = ["thread", "create", "--session-slug", m.SLUG, "--lead-instructions", "frozen"]
        frozen = argv[:]
        with patch.object(Path, "resolve", lambda self, strict=True: self), \
                patch.object(Path, "is_file", return_value=True), patch.object(Path, "read_bytes", return_value=binary), \
                patch.object(h.os, "access", return_value=True):
            for slug in (m.SLUG, m.MEMBER_SLUG):
                argv[3] = slug
                self.assertEqual(h.root_recovery_provider(config, argv), selected["path"])
            argv[3] = m.SLUG
            self.assertEqual(argv, frozen)
            for field, value in (("root", "/tmp/another"), ("package", "/nix/store/another"),
                                 ("rootRecoveryProvider", {**selected, "extra": True}),
                                 ("rootRecoveryProvider", {**selected, "sha256": "0" * 64}),
                                 ("rootRecoveryProvider", {**selected, "path": "/tmp/workspace-portal"})):
                with self.subTest(field=field, value=value), self.assertRaises(h.Failure):
                    h.root_recovery_provider({**config, field: value}, argv)
            with patch.object(Path, "read_bytes", return_value=b"#!/bin/sh\n"), self.assertRaises(h.Failure):
                h.root_recovery_provider(config, argv)

    def test_changed_record_and_prior_claim_refuse(self):
        info = SimpleNamespace(st_mode=stat.S_IFREG | 0o600, st_uid=h.os.geteuid())
        with patch.object(Path, "lstat", return_value=info), patch.object(m, "digest", return_value="correct"):
            m.require_records({"result.json": "correct"})
            with self.assertRaises(h.Failure):
                m.require_records({"result.json": "wrong"})
            info.st_mode = stat.S_IFREG | 0o622
            with self.assertRaises(h.Failure):
                m.require_records({"result.json": "correct"})
        with patch.object(m, "digest", return_value=m.PACKET_SHA256), \
                patch.object(h, "read", return_value={"root": str(m.ROOT)}), \
                patch.object(m.os.path, "lexists", return_value=True), self.assertRaises(h.Failure):
            m.validate_fault_fixture(Path("/nix/store/corrected"), "0" * 64)

    def test_timing_samples_cannot_be_dropped_or_changed(self):
        results = [{"slug": f"2026-10-02-creation-sample-{i}", "acceptanceToReadySeconds": t}
                   for i, t in enumerate(m.TIMES, 1)]
        for values in (results[:-1], list(reversed(results)),
                       [*results[:-1], {**results[-1], "acceptanceToReadySeconds": 15.0}]):
            with self.subTest(values=values), self.assertRaises(h.Failure):
                m.require_successes({"results": values}, {}, {})

    def test_retry_exact_receipt_original_root_and_shared_tail(self):
        initial = {"startedAt": "2026-10-02T20:00:00Z"}
        accepted = {"startedAt": "2026-10-02T20:01:00Z", "attempt": 3,
                    "receiptId": m.RECEIPT_ID, "slug": m.SLUG}
        receipt = {"attempt": 3, "receiptId": m.RECEIPT_ID, "updatedAt": "2026-10-02T20:01:13Z"}
        with patch.object(h, "read", side_effect=[{"receipt": initial}, {"attempt": 2}, {"rootThreadID": m.ROOT_ID}]), \
                patch.object(h, "http", return_value=accepted) as rpc, \
                patch.object(h, "wait_creation", return_value={"state": "ready"}), \
                patch.object(h, "ready_evidence", return_value=(receipt, {"rootThreadId": m.ROOT_ID})), \
                patch.object(h, "complete_creation", side_effect=lambda *a: a[8]) as complete, \
                patch.object(m, "require_dispatches"):
            result = m.retry_root({}, {})
            self.assertEqual(result["retryAcceptanceToReadySeconds"], 13)
            rpc.assert_called_once_with({}, "POST", f"/api/sessions/{m.SLUG}/creation/retry",
                                        {"receiptId": m.RECEIPT_ID, "attempt": 2})
            complete.assert_called_once()
        for changed in ("replacement", None):
            with self.subTest(root=changed), patch.object(h, "read", side_effect=[{"receipt": initial}, {}, {}]), \
                    patch.object(h, "http", return_value=accepted), patch.object(h, "wait_creation", return_value={}), \
                    patch.object(h, "ready_evidence", return_value=(receipt, {"rootThreadId": changed})), \
                    patch.object(h, "complete_creation") as complete, self.assertRaises(h.Failure):
                m.retry_root({}, {})
            complete.assert_not_called()

    def test_preflight_and_execution_order(self):
        prior = {"state": "incomplete", "error": "known", "results": [1, 2, 3, 4, 5],
                 "timing": {"passed": True}, "warmup": {"original": True}}
        config = {"root": str(m.ROOT), "package": str(m.PACKAGE), "unchanged": "args"}
        packet = {"records": {}, "priorClaims": {}}
        selected = {"path": "/nix/store/corrected/bin/workspace-portal", "sha256": "a" * 64}
        events = []
        fake_dt = SimpleNamespace(datetime=SimpleNamespace(now=lambda tz: SimpleNamespace(
            date=lambda: SimpleNamespace(isoformat=lambda: "2026-10-02"))), timezone=SimpleNamespace(utc=None))
        with patch.object(m, "validate_fault_fixture", return_value=(prior, config, {}, packet, selected)), \
                patch.object(m, "require_records"), patch.object(m, "require_services"), \
                patch.object(m, "preserve_failure", side_effect=lambda p: events.append("preserve")), \
                patch.object(m.os, "umask"), patch.object(h, "dt", fake_dt), patch.object(h, "stamp", return_value="now"), \
                patch.object(h, "save", side_effect=lambda p,v: events.append((p.name, copy.deepcopy(v)))), \
                patch.object(m, "retry_root", side_effect=lambda *a: events.append("retry-root") or {"root": "same"}), \
                patch.object(h, "create", side_effect=lambda *a: events.append(("member", a[2:])) or {"member": "passed"}) as create, \
                patch.object(m, "require_dispatches"), redirect_stdout(io.StringIO()):
            argv = ["verify-fault-creation.py", "--provider-package", "/nix/store/corrected", "--provider-sha256", "a"*64]
            with patch.object(sys, "argv", [*argv, "--preflight"]):
                self.assertEqual(m.main(), 0)
                self.assertEqual(events, [])
            with patch.object(sys, "argv", argv):
                self.assertEqual(m.main(), 0)
            self.assertEqual(events[0], "preserve")
            self.assertEqual(events[1], ("config.json", {**config, "rootRecoveryProvider": selected}))
            create.assert_called_once()
            self.assertEqual(create.call_args.args[2:], ("creation-member-loss", 180, "member-progress"))
            final = events[-1][1]
            for key in ("results", "timing", "warmup"):
                self.assertEqual(final[key], prior[key])
            self.assertEqual(len(final["faults"]), 2)
            events.clear()
            with patch.object(m, "retry_root", side_effect=h.Failure("refused")), \
                    patch.object(h, "create") as forbidden_member, patch.object(sys, "argv", argv):
                self.assertEqual(m.main(), 1)
                forbidden_member.assert_not_called()
            self.assertEqual(events[-1][1]["state"], "incomplete")


if __name__ == "__main__":
    unittest.main()

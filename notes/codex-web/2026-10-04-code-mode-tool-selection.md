# Model metadata overrides Code Mode feature flags

Initiative: `work/2026-10-03-automatic-session-slugs/`.
Inspected native source: pinned Codex 0.160.0.

A native utility check advertised `functions.exec`, `wait` and an async question
despite false Code Mode flags. `core/src/tools/mod.rs:75-99` gives a model's
explicit `tool_mode` precedence over those flags. The original Luna catalog
sets `code_mode_only`; `spec_plan.rs:819-937` registers exec/wait and moves clock
into the nested tool inventory. A function payload named exec does not exercise
the real custom-tool interpreter.

The interpreter uses bare V8 and an explicit backend inventory. Its name alone
does not establish shell access or prove isolation. Verify the actual captured
registry and representative dispatch, rather than accepting or rejecting a
wrapper solely by name. No file/network APIs or imports are installed by the
inspected runtime; action handlers still need independent restrictions.

Yielded cells can outlive a completed turn. In this version, exact turn/interrupt
rejects terminal turns, unsubscribe only removes the listener, and no public
scoped thread shutdown/cell join request exists. Enabling CodeModeInterrupt only
changes active-task aborts. Eventual daemon unload is not a bounded teardown
acknowledgement. See design.md's Yielded-cell teardown decision for checked
methods and source locations.

The original `gpt-5.5` metadata resolves to Direct mode under false Code Mode
flags. The coordinator selected it explicitly for naming. A dedicated standard
App Server child receives the unchanged full original catalog at startup;
config/read must report its path with a sessionFlags origin. The ordinary daemon
retains dynamic metadata. Public model/list does not expose tool mode, so a
one-time cache check cannot establish that boundary. Availability, actual tool
surface, naming latency and diagnostic logging still require separate checks.
Implementation is in progress; no isolation or activation pass is claimed.

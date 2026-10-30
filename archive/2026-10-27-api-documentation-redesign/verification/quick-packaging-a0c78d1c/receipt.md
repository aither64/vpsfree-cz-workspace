# Upstream 0.31 quick/package verification: stopped on failure

Tested source: `a0c78d1c0e5ef84b5e746d9bba4bc51830c77139`, tree
`3c62ce89c1ac356116aef9c59cf34398bd3130bf`. The source/index is clean and
unchanged after the operation. No verification process remains running.

One fresh retained-catalog verification utility (`gpt-6-luna`, low,
`dw_261a10738ad06c003118fa86a9c9a7ce71a28ba2529d3b2b`) launched the exact
one-operation driver. The retained catalog digest is
`3ff7a2129ed39b4d6774466e53060bbff33d2cd2d893aa168c87cb3d64bd6b41`.
Current installed full-access execution was resolved independently; the actual
standalone CLI used explicit danger-full-access and approval never. Binding
checks ran outside Nix/Bundler. Full policy/argv/prompt are retained locally.

| Stage | Result | Wall time |
| --- | --- | --- |
| `make doc` | exit 0 | 1.09 s |
| `ruby utils/release/cli.rb check-clean --master` | exit 0 | 1.19 s |
| Existing loaded-source identity probe | exit 0; sibling server/Ruby client/TypeScript 0.31.0, JSON 2.21.2 | 2.55 s |
| Focused release lineage and three profile files | exit 1; 51 examples, 2 failures | 11.88 s |

The failing examples are in `spec/client_examples/profile_mount_spec.rb`:

- Line 190, private schema/sequential users/locales/HTML/samples: the expectation
  at line 198 did not find `PRIVATE_SAMPLE` and `Visible English action`.
- Line 230, generated TypeScript panel beside dynamic tabs: the expectation at
  line 238 did not find `PRIVATE_SAMPLE`.

Raw failure output: `04-lineage-profiles.log`. The operation stopped at the
first failing stage, without retry, diagnosis or source repair. Exact commands,
working directories, exits and times are in `stages.json`; combined output and
exit are `operation.log` and `operation.exit`. Watcher result/events are
`watcher-result.log` and `watcher.jsonl`; `watcher.exit` is the watcher CLI exit,
not the driver/check exit.

The three packaging examples, new gem build/extraction and performance exports
were **not run**. `performance-a0c78d1c/commands.md` contains future commands only;
no archive, prepared-input result, benchmark pilot, scaling or measurement exists
for this operation. Original `performance-82a7f2ab` evidence remains unchanged.

All 1,872 protected input/evidence hashes were checked unchanged after the
failure, including retained component locks, frozen benchmark inputs and all old
export files. No unused standalone component lock appeared. No dependency,
application-source, Git/hook, live-preview, OAuth, TLS, publication or lifecycle
mutation occurred. The only build output was the authorized ignored shared
documentation from `make doc`. Original-owner diagnosis/next lead assignment is
required before continuation. This is not a completed quick/package pass or a
performance gate result.

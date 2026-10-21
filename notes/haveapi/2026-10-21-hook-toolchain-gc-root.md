# Keep a GC root for a prepared native hook interpreter

During Rust-generator integration, the prepared Ruby3.4.11 Nix store path was
collected after dependency setup exited. A later hook invocation used ambient
Ruby3.4.9 instead; the target-owned json extension correctly failed because it
linked libruby-3.4.11.so.3.4. No Git push occurred and hooks were not bypassed.

Restore and root the exact declared input while merge preparation uses its
native gems. This session used nixpkgs02c087f3fe673c9e317f206a627cb6b910336dbe:

```sh
nix build github:NixOS/nixpkgs/02c087f3fe673c9e317f206a627cb6b910336dbe#ruby_3_4 \
  --out-link /path/to/session/artifacts/hook-ruby
```

Verify the resolved output and interpreter version match the original setup
receipt before resuming. Put that interpreter and the prepared gem bin directory
first in PATH. Do not rebuild native gems with a guessed ambient interpreter or
disable hook verification. The restoration substituted cached outputs and
returned the exact same Ruby3.4.11 path; no source/config/lock change was needed.
Remove only the owned GC-root link after all hook-dependent operations finish.

Related session: work/2026-10-18-rust-client-generator; hook setup result under
artifacts/integration-hook-setup and approved-default-integration/hook-ruby.

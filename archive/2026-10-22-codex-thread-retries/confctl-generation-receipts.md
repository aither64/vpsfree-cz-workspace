# Exact confctl build and health receipts

Planning supplement to [verification-build-brief.md](verification-build-brief.md),
2026-10-22. Source reads only; no check, evaluation, build, copy, SSH, native
execution, claim or activation was performed for this supplement. Lead owns
activation; fresh utilities run only their assigned verification/build packet.

Configuration is `81d0e68c52762d3804e00e4c4ef99a421bafc05f`; its locked confctl
is `7bee58a52372b95c2198ce3f2a719807a3c2c66b`. Use the final A/B/W/C identities
at the top of the main brief and its literal `$C`, `$RUN`, `$MACHINE` paths.
All following commands require **CWD `$C`**, including `nix develop "$C"`.
Keep artifacts in the owned RUN directory, never the configuration repository.
The site route remains `docs/operations/codex-providers-aitherdev.md`, with
the selected runtime's `workspace-host coordination guide` before activation.

## Build, then bind the exact returned generation

Before building, retain clean exact C HEAD/tree and `flake.lock` SHA256 with
the complete lock graph; repeat the HEAD/tree/cleanliness comparison afterward.
The existing composed-lock check and final W/C packaged checks remain required.
Capture stdout/stderr, exit status, command/CWD and elapsed time for the existing
scoped build. Noninteractive flags avoid an unattended confirmation prompt:

```sh
cd "$C"
CONFCTL_TTY=0 nix develop "$C" -c confctl --color never build --yes "$MACHINE"
```

Only after exit 0, take the exact name printed under **Built generations:**
for the one selected machine. The name has shape `YYYY-MM-DD--HH-MM-SS`.
The command may reuse a previously built matching generation, so neither
current time nor the newest directory identifies this build. Set the name from
that retained stdout, then inspect it explicitly:

```sh
SYSTEM_GENERATION='EXACT_NAME_FROM_SUCCESSFUL_BUILD_STDOUT'
CONFCTL_TTY=0 nix develop "$C" -c confctl --color never generation ls \
  --local "$MACHINE" "$SYSTEM_GENERATION"
GENERATION_DIR="$C/.confctl/generations/cz.vpsfree:machines:aitherdev/$SYSTEM_GENERATION"
cp "$GENERATION_DIR/generation.json" "$RUN/system-generation.json"
sha256sum "$RUN/system-generation.json" > "$RUN/system-generation.sha256"
readlink -f "$GENERATION_DIR/toplevel"
readlink -f "$GENERATION_DIR/auto_rollback"
```

Retain the listing, named directory, generation JSON and resolved links in the
receipt. Listing is human-readable, not a JSON metadata export. Require one
matching machine/name row. Do not pass `current`, a numeric offset or a pattern
to later copy/activation. Preserve the original generation directory/GC roots.

`generation.json` records `mode`, `date`, `toplevel`, `auto_rollback`, per-role
input store paths in `inputs`, and per-role revisions in `inputs_info`. It does
**not** record the configuration repository commit. That commit is embedded in
the built system's `etc/confctl/configuration-info.json`; the built system also
contains `etc/confctl/inputs-info.json`. The following future receipt command
uses Ruby from C's declared shell and verifies their identities without another
Nix evaluation:

```sh
nix develop "$C" -c ruby -rjson -rdigest - "$GENERATION_DIR" <<'RUBY' > "$RUN/system-build-receipt.json"
dir = ARGV.fetch(0)
metadata_path = File.join(dir, 'generation.json')
g = JSON.parse(File.read(metadata_path))
abort 'not a flake generation' unless g.fetch('mode') == 'flakes'
top = g.fetch('toplevel')
abort 'toplevel link mismatch' unless File.realpath(File.join(dir, 'toplevel')) == File.realpath(top)
abort 'rollback link mismatch' unless File.realpath(File.join(dir, 'auto_rollback')) == File.realpath(g.fetch('auto_rollback'))
config_path = File.join(top, 'etc/confctl/configuration-info.json')
inputs_path = File.join(top, 'etc/confctl/inputs-info.json')
config = JSON.parse(File.read(config_path))
inputs = JSON.parse(File.read(inputs_path))
abort 'wrong or dirty configuration' unless config.fetch('schemaVersion') == 1 && config.fetch('revision') == '81d0e68c52762d3804e00e4c4ef99a421bafc05f' && config.fetch('revisionDirty') == false
abort 'input metadata mismatch' unless inputs == g.fetch('inputs_info')
abort 'wrong runtime' unless inputs.fetch('devWorkspace').fetch('rev') == 'd819ad044ef7fcc7bb4a111dc7676fe251383249'
puts JSON.pretty_generate({
  schema: 1, machine: 'cz.vpsfree/machines/aitherdev',
  generation: File.basename(dir), generationDirectory: dir,
  metadataSHA256: Digest::SHA256.file(metadata_path).hexdigest,
  configurationInfoSHA256: Digest::SHA256.file(config_path).hexdigest,
  inputsInfoSHA256: Digest::SHA256.file(inputs_path).hexdigest,
  metadata: g, configuration: config
})
RUBY
```

Require receipt exit 0 and retain complete metadata, not only short revisions.
The receipt binds the selected output; the separate clean-source/command/input
graph records bind the build invocation. Compare it with the main brief's exact
closure/derivation receipts. Use this same literal `SYSTEM_GENERATION` for the
already-documented `deploy --generation ... --copy-only --no-reboot`, and later
lead-owned dry-activate/switch. Retain each command's independent result; build
success does not prove copy or activation. Missing metadata/mismatches stop the
packet; do not fall back to current or silently rebuild during activation.

## Scoped status and health receipts after authorized activation

These are future live read/check commands, not run by the architect:

```sh
cd "$C"
CONFCTL_TTY=0 nix develop "$C" -c confctl --color never status --yes \
  --generation "$SYSTEM_GENERATION" "$MACHINE"
CONFCTL_TTY=0 nix develop "$C" -c confctl --color never ls \
  --output name,checks "$MACHINE"
CONFCTL_TTY=0 nix develop "$C" -c confctl --color never health-check \
  --yes --max-jobs 2 "$MACHINE"
```

Always supply the named generation to `status`: omitting it invokes a build.
Status renders the one machine, online/uptime, `ok` or `outdated`, generation
counts and input-role state; exit 0 alone is not a match assertion. Require the
expected row and `ok`, and independently retain both live system/profile links
as required by the site guide. `generation ls --remote` is available but is not
needed to identify the local build and does not replace these receipts.

Health output is the selected machine header, log path, numbered check/result
lines and `N checks passed, 0 failed`; failed checks raise a nonzero command
result. The inspected host configuration defines two baseline checks:
systemd `SystemState=running` and `firewall.service ActiveState=active`.
Require the enumerated count and all expected checks, not a zero-check success.
The default property checks retry for 60 seconds with a 3-second cooldown;
this is not an end-to-end SSH deadline. Retain bounded summary plus complete
stdout/stderr/exit artifacts. A printed internal log may be removed on success,
so external capture is the receipt. This scoped host check does not prove portal
health, naming, conversation continuity or UI acceptance; retain the main
brief's separate acceptance steps and machine hold.

## Pinned source and outstanding prerequisites

All confctl references below are at `7bee58a52372b95c2198ce3f2a719807a3c2c66b`:

- `lib/confctl/cli/cluster.rb:1408–1473`: build and returned generation names;
  `lib/confctl/nix_flake.rb:130–167`: matching-generation reuse/create.
- `lib/confctl/conf_dir.rb:34–59`, `lib/confctl.rb:31–32`, and
  `lib/confctl/generation/build.rb:78–89,129–154,232–259`: path, host escaping,
  named metadata and links. `cli/app.rb:551–568` and `cli/generation.rb:5–9`
  define `generation ls`; `cli/cluster.rb:1302–1325` resolves exact names.
- `nix/flake/mk-confctl-outputs.nix:24–42,255–271` creates configuration and
  input metadata; `nix/modules/confctl/{configuration-info,inputs-info}.nix`
  embeds them. Dirty configuration identity is explicit, never equivalent to
  the reviewed clean commit.
- `cli/app.rb:397–431`, `cli/cluster.rb:94–114,225–314,1037–1147` define
  health/status flags and result semantics; `lib/confctl/ui.rb:7–11` provides
  `CONFCTL_TTY=0`. Native cluster defaults at
  `nix/modules/cluster/default.nix:257–274,579–590` and configuration
  `modules/cluster/default.nix:189–209` define these two systemd checks.

No new code/configuration prerequisite was found in this bounded source read.
Concrete outstanding evidence is the in-progress full A/B result, final W/C
checks and composed-lock check, and successful exact system/profile builds with
receipts; their success is not presumed. Copy/status/health additionally need
the existing configured SSH route to aitherdev (`172.16.106.40`), but its live
availability was not probed. Use C's declared shell, including its packaged
confctl, and stop/escalate unexpected local kernel builds under the existing
verification policy. No new kernel exception, credential action, activation or
machine release is authorized by this supplement.

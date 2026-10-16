#!/usr/bin/env python3
"""Session-only static extraction and exact scope comparison; no Nix evaluation."""
import hashlib
import json
from pathlib import Path
import re
import subprocess

session = Path(__file__).resolve().parent.parent
out = Path(__file__).resolve().parent
product = session.parents[1] / "worktrees" / session.name / "vpsadminos"
relative = "tests/suite/dist-config/nixos-persistence-upgrade.nix"

def git(*args):
    return subprocess.check_output(["git", "-C", str(product), *args])

before = git("show", f"HEAD:{relative}").decode()
after = (product / relative).read_text()
old_registration = "    registration = pkgs.closureInfo { rootPaths = allClosures; };\n"
new_registration = """    registrations = lib.mapAttrs (
      _: variant:
      pkgs.closureInfo {
        rootPaths =
          builtins.attrValues variant.generations ++ builtins.attrValues (variant.failures or { });
      }
    ) guests.variants;
"""
old_share = """              # Shared closures are read-only; the host overlay store cannot be
              # ID-mapped. Container datasets keep their native mappings.
              "osctl ct mounts new --fs /nix/store --type bind --opts bind,ro,create=dir --mountpoint /nix/store --no-map-ids #{ct}",
"""
copy = """            # Use the declarative NixOS container's stopped-store copy contract.
            # Native mapping exposes these root-owned copies as guest root.
            machine.succeeds(<<~SHELL)
              set -e
              mkdir -p "#{nix_root}/store"
              while IFS= read -r store_path; do
                cp -a "$store_path" "#{nix_root}/store/"
              done < ${registration}/store-paths
              cp ${registration}/registration "#{nix_root}/nix-path-registration"
            SHELL
"""
source_query = "            nix_root = machine.osctl_json(\"ct mounts ls #{ct}\").find { |mount| mount.fetch('mountpoint') == '/nix' }.fetch('fs')\n"
changes = [
    (old_registration, new_registration),
    ("        g = variant.generations;\n", "        g = variant.generations;\n        registration = registrations.${name};\n"),
    (old_share, ""),
    (source_query, source_query + copy),
    ("nix-store --load-db < ${registration}/registration", "nix-store --load-db < /nix/nix-path-registration"),
    ("system.extraDependencies = allClosures ++ [ registration ];", "system.extraDependencies = allClosures ++ builtins.attrValues registrations;"),
]
expected = before
for old, new in changes:
    assert expected.count(old) == 1, old
    expected = expected.replace(old, new, 1)
assert expected == after, "Unaccounted source difference"
inverse = after
for old, new in reversed(changes):
    if new:
        assert inverse.count(new) == 1, new
        inverse = inverse.replace(new, old, 1)
    else:
        # This removed mount was immediately after the unchanged dataset command.
        anchor = '              "osctl ct dataset new #{ct} nix",\n'
        assert inverse.count(anchor) == 1
        inverse = inverse.replace(anchor, anchor + old, 1)
assert inverse == before, "Inverse differs from reviewed source"
(out / "scope-comparison.txt").write_text(
    "PASS: six explicit replacements recreate the complete current suite.\n"
    "PASS: reversing them recreates reviewed HEAD byte-for-byte.\n"
    "Every generation definition, wait/diagnostic wrapper, storage setup, switch,\n"
    "identity/map/payload/metadata/mount assertion and failure control is unchanged.\n"
)
(out / "store-fixture.patch").write_bytes(git("diff", "--", relative))

# Keep every optional Ruby body; replace Nix-only choices/values by inert text.
ruby = after[after.index("        require 'json'"):after.index("\n      '';", after.index("        require 'json'"))]
ruby, n = re.subn(r"describe '\$\{variantName name\} \$\{.*?\}' do", "describe 'static syntax template' do", ruby, count=1, flags=re.S)
assert n == 1
branches = re.compile(r"\$\{\n\s+if variant.layout == \"fresh\" then\n\s+''\n(.*?)\n\s+''\n\s+else\n\s+''\n(.*?)\n\s+''\n\s+\}", re.S)
ruby, n = branches.subn(lambda m: m[1] + "\n" + m[2], ruby)
assert n == 1
ruby = re.sub(r"\$\{lib\.optionalString [^\n]+ ''\n", "", ruby)
ruby = re.sub(r"^\s+''\}\n", "\n", ruby, flags=re.M)
ruby = re.sub(r"\$\{[^{}]+\}", "/fixture/source", ruby)
assert "${" not in ruby and "''}" not in ruby
(out / "upgrade-template.rb").write_text(
    "# Static syntax template only: all conditional bodies; inert Nix placeholders.\n" + ruby + "\n"
)
shell = copy.split("machine.succeeds(<<~SHELL)\n", 1)[1].rsplit("            SHELL\n", 1)[0]
shell = shell.replace("#{nix_root}", "/fixture/nix").replace("${registration}", "/fixture/registration")
(out / "store-copy-template.sh").write_text(shell)

logs = Path("/tmp/ni.boon4yad/os-test-dist-config__nixos-persistence-upgrade-8c45b496")
originals = list(sorted(logs.glob("*.log"))) + [logs / "test-result.txt"]
originals += list(sorted((session / "runtime-attempt.gv8q4a89").glob("*")))
manifest = []
for path in originals:
    if path.is_file():
        data = path.read_bytes()
        manifest.append({"path": str(path), "bytes": len(data), "lines": len(data.splitlines()), "sha256": hashlib.sha256(data).hexdigest()})
(out / "original-logs.json").write_text(json.dumps(manifest, indent=2) + "\n")
shell_lines = (logs / "machine-shell.log").read_text().splitlines()
index = []
for number, line in enumerate(shell_lines, 1):
    if line.startswith(("COMMAND:", "STATUS:", "ERROR:", "ACTION:", "PROTOCOL_ERROR:")):
        index.append(f"{number}: {line}")
(out / "all-command-statuses.txt").write_text("\n".join(index) + "\n")
print((out / "scope-comparison.txt").read_text(), end="")
print("Static Ruby and Bash templates extracted; original evidence hash inventory recorded.")

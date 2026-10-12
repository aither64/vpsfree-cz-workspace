"""Ad hoc source documentation checks; run from the vpsAdmin worktree."""
from pathlib import Path
import re
import subprocess
from urllib.parse import unquote

files = [Path("README.md"), Path("AGENTS.md"), *sorted(Path("docs").rglob("*.md"))]
errors = []
count = 0
for page in files:
    original = page.read_text()
    text = re.sub(r"^```.*?^```\s*$", "", original, flags=re.S | re.M)
    for target in re.findall(r"!?\[[^\]]*\]\(([^\s)]+)\)", text):
        if re.match(r"^[a-zA-Z][\w+.-]*:", target):
            continue
        path, _, anchor = unquote(target).partition("#")
        dest = (page.parent / path).resolve() if path else page.resolve()
        count += 1
        if not dest.exists():
            errors.append(f"{page}: missing target {target}")
        elif anchor and dest.suffix == ".md":
            headings = re.findall(r"^#{1,6}\s+(.+?)\s*#*$", dest.read_text(), flags=re.M)
            slugs = {re.sub(r"[^\w\- ]", "", h.lower()).replace(" ", "-") for h in headings}
            if anchor not in slugs:
                errors.append(f"{page}: missing anchor {target}")
    if original.count("```") % 2:
        errors.append(f"{page}: unmatched code fence")
    if page.parent != Path(".") and len(re.findall(r"^# ", original, flags=re.M)) != 1:
        errors.append(f"{page}: expected one page title")
    if page.name != "i18n-cs.md" and re.search(r"ikiwiki|\.mdwn|\[\[|OpenVZ|vzctl|vpsAdmind|vpsadmindctl", original):
        errors.append(f"{page}: obsolete documentation reference")

index = Path("docs/README.md").read_text()
for page in Path("docs").rglob("*.md"):
    if page != Path("docs/README.md") and str(page.relative_to("docs")) not in index:
        errors.append(f"{page}: missing from index")
if list(Path("docs").rglob("*.mdwn")):
    errors.append("Remaining mdwn files")
for name in ("LICENSE", "i18n-cs.md"):
    before = subprocess.check_output(["git", "show", f"f8fb5b3af:docs/{name}"])
    if before != Path("docs", name).read_bytes():
        errors.append(f"Unexpected change to docs/{name}")
print(f"Checked {count} local links in {len(files)} Markdown files")
print("\n".join(errors) if errors else "Links, anchors, index, fences, and preserved files: OK")
raise SystemExit(bool(errors))

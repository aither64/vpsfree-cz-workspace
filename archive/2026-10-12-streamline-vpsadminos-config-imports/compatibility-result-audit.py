#!/usr/bin/env python3
import json
from pathlib import Path
record=Path(__file__).resolve().parent
for name in ["compatibility-pure-rerun2","compatibility-selector-rerun1","compatibility-discovery","compatibility-kb","compatibility-hooks","compatibility-docs","compatibility-evidence-rerun1"]:
    status=(record/(name+".status")).read_text().strip()
    assert status=="0", (name,status)
text=(record/"compatibility-discovery.log").read_text()
variants=["upgrade-25.11","upgrade-26.05","upgrade-unstable","root-backed-26.05","declared-backing-26.05","dependent-mount-26.05","fresh-26.05","storage-failures-26.05"]
for name in variants:
    assert name in text, name
assert "PASS" in (record/"compatibility-pure-rerun2.log").read_text()
print("All normal quick stages pass; eight registered variants discovered.")

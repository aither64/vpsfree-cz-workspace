#!/usr/bin/env python3
from pathlib import Path
import sys
p=Path(sys.argv[1]);s=p.read_text();p.write_text(s.replace("pick ","edit ",1))

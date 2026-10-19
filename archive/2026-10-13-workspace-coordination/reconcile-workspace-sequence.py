import sys
from pathlib import Path
p=Path(sys.argv[1]);lines=p.read_text().splitlines();commits=[line for line in lines if line.startswith("pick ")];pin=[line for line in commits if "3bc9a7" in line][0];ordered=[commits[0],pin.replace("pick ","fixup ",1)]+[line for line in commits[1:] if line!=pin];p.write_text("\n".join(ordered)+"\n")

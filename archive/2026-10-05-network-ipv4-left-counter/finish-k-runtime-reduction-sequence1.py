from pathlib import Path
import sys
path = Path(sys.argv[1])
text = path.read_text()
lines = text.splitlines(keepends=True)
commands = [i for i, line in enumerate(lines) if line.startswith('pick ')]
assert len(commands) == 3
lines[commands[-1]] = lines[commands[-1]].replace('pick ', 'fixup ', 1)
path.write_text(''.join(lines))

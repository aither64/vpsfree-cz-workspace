import pathlib
import sys

p = pathlib.Path(sys.argv[1])
lines = [line.split() for line in p.read_text().splitlines() if line and not line.startswith("#")]
expected = ["7ba361d", "5436d3d", "67cb2b3"]
assert len(lines) == 3 and all(row[0] == "pick" and expected[i].startswith(row[1][:7]) for i, row in enumerate(lines)), lines
p.write_text("pick 7ba361d22a4aac044cb02abf8397800bcf5726bf\nfixup -C 67cb2b31e7cd0e5b0e8c2949c401795bc37216a1\npick 5436d3d7c36d3d5174eab3c44e3578830749d3db\n")

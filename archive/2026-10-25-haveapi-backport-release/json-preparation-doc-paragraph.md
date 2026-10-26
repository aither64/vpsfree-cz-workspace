The root, Ruby server and Rust generator development Gemfiles declare JSON
2.21.2 so fresh setup installs the recorded native dependency. Comparisons
accept only that exact declaration change in these three files. They retain
the original manifest contents, hashes and declaration evidence, then compare
normalized contents. Replay verifies the transformation from the retained raw
inputs. Other dependency requirements and manifest contents must match.

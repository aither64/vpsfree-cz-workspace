# Publication hook environment

The visibility commit d7d7fb66865fd1a5548a45a559f5c2be436bc470 passed normal
Overcommit hooks in the declared all-plugin root Nix shell. The first push
ran outside that shell and failed configuration signature verification before
publication. No pin or CI cancellation ran.

Read-only inspection proved the configuration and custom hook bytes equal
the original c4d9b50f baseline. Ambient Ruby loads Overcommit 0.71.0 from the
user gem installation; the repository bundle loads 0.73.0. Retry publication
in the same declared root Nix shell as the commit, retaining normal hooks and
signature verification. No signature bypass or source change is required.
The original failed receipts remain intact. New retry receipts use a separate
prefix; the subsequent dependent pin operations retain the reviewed helpers.

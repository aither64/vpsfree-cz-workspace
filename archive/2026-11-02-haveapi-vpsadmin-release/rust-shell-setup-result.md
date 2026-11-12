# Rust shell setup probe

- Result: passed (exit status 0)
- Revision: `1ab58627a225589fefc983829de5c4cfee770b3b`
- Command: `nix develop --no-update-lock-file --command bash -c 'ruby --version; rustfmt --version; rustc --version; cargo --version; bundle --version; pkg-config --modversion libffi'`
- Elapsed: approximately 23 seconds
- Full log: `rust-shell-setup.log`
- Version output: Ruby 3.3.10; rustfmt 1.9.0; rustc 1.98.1; Cargo 1.98.0; Bundler 4.0.9; libffi 3.8.0.
- Nix fetched dependencies from configured substituters and built the trivial `nix-shell-env` derivation. No operation remains running.

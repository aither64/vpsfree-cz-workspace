nix develop "$C" -c ruby -rjson -rdigest - "$GENERATION_DIR" <<RUBY > "$RUN/system-build-receipt.json"

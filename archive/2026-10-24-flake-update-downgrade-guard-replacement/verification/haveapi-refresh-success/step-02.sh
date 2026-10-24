set -euo pipefail
before=$(git rev-parse HEAD)
./utils/update-nixpkgs.sh
after=$(git rev-parse HEAD)

if [ "$before" != "$after" ]; then
  echo "committed=true" >> "$GITHUB_OUTPUT"
else
  echo "committed=false" >> "$GITHUB_OUTPUT"
fi

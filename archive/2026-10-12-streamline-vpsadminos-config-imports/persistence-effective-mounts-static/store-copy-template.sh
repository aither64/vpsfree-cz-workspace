set -e
# The fresh dataset root is 0750; /nix needs non-root traversal.
chmod 0755 "/fixture/nix"
mkdir -p "/fixture/nix/store"
while IFS= read -r store_path; do
  cp -a "$store_path" "/fixture/nix/store/"
done < /fixture/source/store-paths
cp /fixture/source/registration "/fixture/nix/nix-path-registration"

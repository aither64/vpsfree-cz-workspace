# Configuration base refresh

The old-base guard stopped before changing C because master advanced to
6f6aff9029cd57e1a0f9201356f7fdc9f6480671. Its three upstream commits update
the React release pin, record that release and update devWorkspace. The owning
AGENTS, flake mapping and hook/config bytes are unchanged. K master remains
873758fd6aec0c03f50a94600e0ceab97946f255.

Regenerate only the verified two pin commits on the freshly inspected C base.
Canonical confctl commands still set V d7d7fb668 and agreed W e4c49bcd. Compare
the entire generated lock graph with that fresh base, allowing only these two
selected locked revision/content/time fields. Verify W locked metadata and
follows equal the prior feature pin. Preserve every unrelated upstream change,
including devWorkspace. Retain old heads, trees, histories and remote leases.

This does not integrate feature content into a default, change W source or
rebase its branch. The final C branch has two canonical pin commits on 6f6aff90;
review/build evidence will identify that actual base. Prior failed operations
and receipts remain unchanged.

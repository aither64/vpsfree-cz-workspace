### Incident policy declaration

Set the optional `incidentPolicyFile` in the cluster's `config.json` to select
one local incident-policy declaration:

```json
{
  "incidentPolicyFile": "/absolute/site/incident_escalation.rb"
}
```

The value must be an absolute path to a readable regular file. Empty or relative
paths, missing files, directories, symlinks and other JSON types are rejected.
An absent or null value keeps the existing fixture configuration, including the
storage profile when it is enabled.

The selected file is read once and copied into the built closure as
`incident_escalation.rb`. It replaces only that file in the selected configuration
directory; sibling files and the normal preStart link installation are retained.
API, supervisor and database setup use the same directory. This selection neither
loads a whole site configuration nor executes the Ruby file during Nix evaluation.

Later host-file edits do not change the built closure. Apply a new selection
through the ordinary services build/update. Selecting null on a later update
restores the original fixture selection without changing historical incidents.
Older providers ignore this key; do not use an older provider update as recovery
when the cluster must retain a selected declaration.

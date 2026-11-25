### Incident policy declaration

To use a local incident-policy declaration, set `incidentPolicyFile` in the
cluster's `config.json`:

```json
{
  "incidentPolicyFile": "/absolute/site/incident_escalation.rb"
}
```

The value must be an absolute path to a readable regular file. Empty or relative
paths, missing files, directories, symlinks and other JSON types are rejected.
Omitting the key or setting it to null keeps the existing fixture configuration,
including the storage profile when it is enabled.

Nix reads the file once and copies its bytes into the built closure as
`incident_escalation.rb`. This replaces only the declaration in the selected
configuration directory. Sibling files and the normal preStart link installation
stay unchanged. API, supervisor and database setup use the same directory.
Selecting this file does not load the rest of the site configuration or execute
Ruby during Nix evaluation.

Later edits to the host file do not change the built closure. Apply them through
the ordinary services build/update. Setting the value to null on a later update
restores the original fixture selection without changing historical incidents.
Older providers ignore this key. Do not update with an older provider as a recovery
step when the cluster must retain the selected declaration.

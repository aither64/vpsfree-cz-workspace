# Milestone 4 authentication presentation provenance

Original owner: implementer0. Temporary history projection only; no application files changed, no application tests, Git/hooks, authentication flow changes or activation.

`basic/` preserves the final top-control layout, theme disclosure, resource context, escaped account identity and visibility note. It retains the existing Basic login and logout branches. `final/` is a byte snapshot of current owned partials. `version_sidebar.erb` is identical in both trees; it is included to preserve full current-resource presentation.

The only removed seams are the optional controls reader/local passing in brand, optional sign-in destination/data hook and POST logout form in authentication_control, and optional message in authentication_status. No authentication behavior was designed or changed in the working tree.

Replay command (inside a copy of basic):

```
patch --batch --fuzz=0 -p1 -i ../optional-oauth-controls.patch
```

Actual replay succeeded at fuzz 0 without offsets. Every reconstructed file equals final/source bytes. Working-tree source bytes were rechecked unchanged after replay. The previous provenance directory and receipts were untouched.

| File | Basic SHA-256 | Final/source SHA-256 |
| --- | --- | --- |
| `servers/ruby/lib/haveapi/views/version_sidebar.erb` | `b6e66182abf304e6a054c44f1aa72f5e14a600c83ba3f9ae7650e5b952682674` | `b6e66182abf304e6a054c44f1aa72f5e14a600c83ba3f9ae7650e5b952682674` |
| `servers/ruby/lib/haveapi/views/version_sidebar/brand.erb` | `011e342f59a2c5247f10c6b6457c287c2c14fb67bce813a3ec7371d5feef075f` | `0c89cb836798bd2a9c2a11b57d9e8dbd8da37bf83b6dfc62018e918407863f8a` |
| `servers/ruby/lib/haveapi/views/version_sidebar/authentication_control.erb` | `c7d4cdb3bf67dc39139aa9ecaa5d4fad1ebb8ff2fb049fc4be9ca05e9f9a68d5` | `0516a30ffbb72519074b8686e30d0ffaf1b8101ed2a3282d9ec8b18c27e06057` |
| `servers/ruby/lib/haveapi/views/version_sidebar/authentication_status.erb` | `f1453cd02276ccd7eeedcd4feb069868e1c117ca082e1e250e760839bc46792f` | `9261f20a3c21e45f2f54dcfe9d126a03d7c67af0641747318e15f151abf2c616` |

Restoration patch SHA-256: `c65ea2c5c0f4c4e5c734de9c184a67e1d043faeb2c05fc6b7235d0c145708568`.

# Avoid database queries while vpsAdmin models are loaded

## Symptom

A fresh vpsAdmin dev cluster failed before its first migration with
`Mysql2::Error: Table 'vpsadmin.languages' doesn't exist` while loading
`SecurityAdvisoryNodeStatus`.

## Cause

The model class body queried `Language.all` to define localized accessors.
Database setup loads the application models before a new database has created
the `languages` table, so class loading itself prevented migrations from
starting.

## Fix and verification

Keep model class bodies independent of database contents. Define dynamic
accessors from the API resource after the schema is available. A storage-topology
dev cluster using the bridge network then completed all migrations and seeds;
the localized-note migration was recorded, its translation table existed, and
the removed legacy `note` column did not.

Related initiative:
`work/2026-07-20-security-advisory-review/`.

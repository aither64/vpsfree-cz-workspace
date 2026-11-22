# vpsAdmin Component Specs Need Test DB

Related initiative: `work/2026-05-30-dev-vpsadmin-clusters`.

Symptom:

- `nix develop .#api --command ... bundle exec rspec ...` and
  `nix develop .#libnodectld --command ... bundle exec rspec ...` can install
  dependencies but fail before running examples with:
  `No test DB configured. Set DATABASE_URL or create api/config/database.yml
  with a 'test:' section.`

Cause:

- The API spec helper establishes an ActiveRecord test database connection
  during load. `libnodectld` specs reuse that helper, so even small isolated
  component specs require a configured test DB.

Workaround:

- Provide `DATABASE_URL`, or create `api/config/database.yml` with a `test:`
  section before running those specs.
- During the devcluster work, an API status spec was run successfully by
  pointing `DATABASE_URL` at a temporary DB through an SSH tunnel to the
  services VM; remove the temporary DB/user afterwards.

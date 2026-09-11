# vpsAdmin devcluster CLI uses an upstream test URL

The services VM includes vpsadminctl configured for api.vpsadmin.test. The
packaged devcluster overrides the API domain with the consuming workspace value.
An acceptance probe using the wrapper's default URL therefore failed even though
the API service and database were healthy.

For tests in an owned disposable services VM, derive /root/.haveapi-client.yml
from /etc/haveapi-client.yml with only the URL changed to the cluster API URL,
using umask 077; pass that same URL with vpsadminctl -u. Authentication settings
are keyed by URL, so changing the command URL alone does not select the fixture
credentials. Do not print or copy credential values to tracking artifacts.
Verified node show 101 returned the seeded node through the configured API.

Related initiative: work/2026-09-11-devcluster-packaging-investigation.

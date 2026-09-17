# Project map

Required workspace procedure, selected by the routing table in `AGENTS.md`.
Its rules retain workspace scope and precedence. Paths and commands are relative
to the coordination workspace unless the text specifies another repository.

## Project Map

These repositories are in scope for this workspace:

- `dev-workspace`: reusable development-session lifecycle, user-profile
  runtime, host module and portal shell. Its
  canonical remote is `git@github.com:aither64/dev-workspace.git`.
- `vpsfree-dev-workspace`: vpsFree.cz KB commands, workspace skills,
  development-cluster providers and migration tooling. Its canonical remote is
  `git@github.com:vpsfreecz/dev-workspace.git`; concrete site configuration is
  supplied by this workspace.
- `codex-web`: reusable Go client, capability-checked HTTP integration and
  framework-free browser module for Codex App Server. Its canonical remote is
  `git@github.com:aither64/codex-web.git`.
- `vpsadminos`: NixOS, ZFS, and LXC-based host OS for containers. It is the
  core runtime for vpsFree.cz nodes and many integration tests.
- `vpsadmin`: Ruby/PHP control panel and API for managing VPSes on top of
  vpsAdminOS.
- `security-advisories`: evidence-backed vpsFree.cz platform security
  assessments, including vpsAdmin Node evidence collection, advisory
  evaluation, and preparation of unpublished vpsAdmin drafts.
- `vpsfree-kb-contracts`: independent, reproducible Czech/English page,
  runtime-test, screenshot, and WebUI documentation contracts for an explicit
  subset of the vpsFree.cz knowledge bases. Its canonical
  `docs/webui-change-workflow.md` must be followed when a vpsAdmin feature can
  change visible labels, navigation, forms, layout, or screenshots.
- `ruby-lxc`: Ruby native extension wrapping liblxc. It is consumed by
  vpsAdminOS `osctld` and may need coordinated gem releases for Ruby or LXC
  upgrades.
- `haveapi`: framework for self-describing APIs. It underpins vpsAdmin's API
  shape and client generation.
- `vpsf-status`: Go status page and monitoring-facing status service for
  vpsFree.cz.
- `vpsadmin-go-client`: generated Go client library for the vpsAdmin API.
- `confctl`: Ruby/Nix deployment management tool used with NixOS and
  vpsAdminOS fleets.
- `vpsfree-cz-configuration`: production vpsFree.cz cluster configuration in
  Nix.
- `vpsadminos-org-configuration`: vpsadminos.org cluster configuration in Nix.
- `vpsfree-irc-bot`: IRC bot for vpsFree.cz channels and infrastructure
  integration.
- `vpsfree-mail-templates`: localized mail templates consumed by vpsAdmin.
- `terraform-provider-vpsadmin`: Go Terraform/OpenTofu provider for vpsAdmin.
- `web`: PHP and server-side-include website for vpsFree.cz and its
  translations.
- `ssh-exporter`: Prometheus exporter that checks systems over SSH and exports
  metrics.
- `syslog-exporter`: Prometheus exporter that parses syslog streams into
  metrics.
- `vpsfree-client`: Ruby CLI and client library for the vpsFree.cz API, built
  on vpsAdmin and HaveAPI clients.
- `vpsfree-maintenance-tasks`: dated operational scripts for maintenance work.
- `linux`: Linux kernel tree used by vpsAdminOS. Treat it as reference material
  unless the task explicitly targets kernel work.
- `zfs`: OpenZFS tree used by vpsAdminOS. Treat it as reference material unless
  the task explicitly targets ZFS work.

Common dependency flow: HaveAPI defines the API framework and client-generation
model. vpsAdmin consumes HaveAPI and manages infrastructure running on
vpsAdminOS. The Go client, Ruby client, and Terraform provider consume the
vpsAdmin API. The configuration repositories deploy NixOS and vpsAdminOS
systems, usually with confctl. Status, exporters, web, IRC bot, mail templates,
and maintenance tasks support operations around the core platform. This
coordination workspace selects `dev-workspace`, which in turn consumes
`codex-web`; keep that dependency direction one-way.

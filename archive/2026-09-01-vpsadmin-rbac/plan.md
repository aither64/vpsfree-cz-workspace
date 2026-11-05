# 2026-09-01-vpsadmin-rbac

## Goal

Design role-based access control for vpsAdmin so that every account represented
by an existing `User` becomes its own security/tenancy boundary. The account
owner can invite or create additional login identities, organize them into
groups, assign roles, and delegate access at the whole-account or resource
scope.

The design must:

- preserve strict isolation between existing accounts;
- keep authentication identities separate from resource/account ownership;
- preserve existing owner access and platform-administrator behavior;
- replace the numeric `User#level` hierarchy completely with explicit domain
  and platform roles/permissions;
- prove that the compatibility migration cannot give any existing principal
  access they do not have before RBAC;
- make permission grants reviewable, explainable, and safe to delegate;
- work with API tokens, OAuth2, the WebUI, plugins, transaction chains, and
  generated clients;
- build on the event and notification architecture from
  `2026-06-15-vpsadmin-events` without treating notification history as an
  audit ledger; and
- allow incremental deployment without requiring a coordinated vpsAdminOS
  node update.

This initiative is currently an architecture exploration. It does not yet
authorize implementation or production deployment.

## Baseline inspected

The design baseline is the pushed vpsAdmin events branch at
`131ef638075a652cdfaecdbe163f137f7716056f`. On 2026-09-01, that branch was
127 commits ahead of and 55 commits behind current `origin/master`
`cbd0fa16434947a4273610389d84216bcde35e72`. Its merge base is
`0b066c42814d3a9f5b0b8f8e3ed7910ae20a4fac`.

Before implementation begins, the events branch must be integrated or rebased
onto the then-current vpsAdmin default branch. RBAC work should not be stacked
on its presently stale base.

### Current identity and authorization model

`User` currently represents several different concepts at once:

- an authenticating person or API principal, including password, MFA,
  WebAuthn, OAuth, sessions, devices, language, and time zone;
- a member/account and resource owner, including VPSes, datasets, IP
  addresses, DNS zones, exports, quotas, environment configuration, payments,
  incidents, notifications, and account lifecycle;
- a coarse platform privilege level, exposed through `User#role` as `user`,
  `support`, or `admin`; and
- the actor stored on transaction chains through `User.current`.

`User#level` also combines unrelated meanings. The declared values are 1
(`Poor user`), 2 (`User`), 3 (`Power user`), 21 (`Admin`), 90
(`Super admin`), and 99 (`God`). `User#role` collapses these to `user` at 1,
`support` at 21, and `admin` at 90, but raw numeric comparisons are still used
for system-configuration visibility, monitoring-event visibility, console
authentication, administrator recipient selection, DokuWiki groups, and API
input/output. Replacing `role == :admin` alone would therefore miss authority
encoded by raw levels.

The target model has no numeric user level. Every use must be classified as a
domain permission, platform permission, product/account entitlement, public
visibility rule, or obsolete distinction before the column is removed.

HaveAPI token and OAuth sessions already carry action/path scopes. These are a
useful upper bound on a token, but they do not grant access to another user's
resources and are not a replacement for RBAC.

Platform administrators can create a detached token session for another user.
The session keeps the target in `user_id` and the original administrator in
`admin_id`; the WebUI calls this a context switch. This is impersonation and
must remain distinct from an ordinary domain member selecting their own
domain.

Authorization is highly distributed:

- approximately 526 `authorize` declarations across 104 core/plugin Ruby
  files;
- approximately 433 explicit `role == :admin` bypasses;
- approximately 110 `restrict user_id: ...` declarations;
- approximately 210 uses of `with_restricted`; and
- additional direct `current_user.id`, `current_user.role`, association, and
  query checks in actions and models.

Simple `restrict user_id: current_user.id` rules cannot express group-based or
resource-scoped grants. Retaining these rules alongside a new grant database
would produce inconsistent decisions and likely object-level authorization
gaps.

### Current event model

The events branch deliberately defines the Event API as notification delivery
history, not an audit log. An emitted candidate is persisted only when routing
produces executable delivery work. Absence of an Event therefore does not
prove that no action occurred.

The branch nevertheless provides useful RBAC seams:

- typed public resource events declare their account owner explicitly;
- event payloads already distinguish `actor_user_id`, `admin_user_id`, and
  `user_session_id`;
- event visibility is already a service (`Event.visible_to`), rather than a
  materialized list of every possible viewer;
- route contexts already distinguish an event subject from a route owner; and
- `rbac` and `rbac_route` are reserved routing-context values. The events
  initiative plan explicitly says that future RBAC should extend visibility
  and route-context calculation.

There is no RBAC implementation behind those reserved values yet. Events and
routes still use `user_id` as their primary subject/owner identity, and the
indirect-route candidate search currently considers only platform admins.

## Terminology

Use these terms consistently:

- **Principal**: an authenticated human or service identity. Initially this
  remains a `User` row.
- **Access domain**: the tenant/security boundary that owns resources,
  entitlements, billing state, and account-wide configuration. Each existing
  user account receives one during migration.
- **Membership**: a principal's relationship to an access domain.
- **Group**: a domain-local collection of memberships; it answers "who".
- **Permission**: one stable operation on a class of resources, such as
  `vps.read` or `iam.grants.manage`.
- **Role**: a named permission bundle; it answers "what".
- **Role binding**: assignment of a role to a membership or group at a domain
  or resource scope; it answers "where".
- **Platform role**: a code-owned installation-wide permission bundle that
  replaces numeric support/administrator levels. Its assignments are
  independent of domain roles and cannot be managed by a domain administrator.
- **Legacy account user**: the existing `User` row whose ID temporarily
  remains the account/resource ownership key. For an existing account this row
  is also its initial login principal, but those two meanings are separated by
  the new domain and membership records.

An Active Directory domain is a directory and administrative/security
boundary, not an RBAC role. The closest mapping is therefore one vpsAdmin
access domain per existing member account, containing its principals, groups,
roles, and resources. The product-facing term can still be "account" or
"team" if that is clearer to members; `AccessDomain` is an unambiguous
internal name that does not collide with DNS domains.

## Design principles

The intended model is scoped RBAC with explicit resource relationships, not a
copy of Active Directory's ordered allow/deny ACLs.

1. Deny by default and require a declared access policy for every API action
   and non-API entry point.
2. Permissions are granted only through roles. A role may be bound directly
   to a membership, but groups are preferred for routine assignments.
3. Groups identify subjects, roles bundle permissions, and bindings connect
   them at a scope. Do not conflate these concepts.
4. Every request is checked at both function level and object/query level.
5. The authenticated principal, active domain, resource-owning account, and
   optional impersonator are separate values in request context.
6. Token/OAuth scopes and RBAC are intersected. A token scope can reduce a
   principal's authority but never increase it.
7. Resource-scope inheritance is explicit and reviewed. It is never inferred
   by walking arbitrary Active Record associations.
8. No explicit deny grants, nested groups, cross-domain trusts, dynamic group
   expressions, or role activation are needed for the first release. These
   features add disproportionate evaluation and explanation complexity.
9. Permission and role identifiers are stable and immutable even if their
   labels change.
10. Authorization decisions are explainable: the API should be able to show
    the role, binding, group membership, and scope that supplied a permission.
11. Domain membership or resource identifiers are never accepted as proof of
    access. The server resolves and checks them on every request.
12. Account ownership is a protected invariant, not an ordinary removable
    grant.
13. Before delegation is enabled, an RBAC decision may only preserve or reduce
    existing access. A candidate allow that the legacy system denies is a
    release-blocking security discrepancy.
14. A newly invited member has no permissions by default. Being a member of a
    domain, knowing its ID, or sharing its e-mail domain grants nothing.
15. Numeric ordering is not part of the target authorization model. Platform
    and domain permissions are explicit and independently reviewable.

This follows the useful parts of the NIST and Microsoft models: permissions
are attached to roles/groups rather than scattered as individual rights,
least privilege is the default, and access can inherit from a deliberately
defined container/resource scope. It avoids the parts of AD that vpsAdmin does
not need, such as forests, trusts, universal/global/domain-local group scopes,
ordered deny ACEs, and unrestricted group nesting.

## Recommended data model

Names are provisional, but the relationships are the important part.

### `access_domains`

- `id` and an immutable public identifier;
- `label`;
- `legacy_account_user_id`, unique and immutable during the compatibility
  phase;
- `owner_membership_id`, referencing a membership in this same domain;
- lifecycle/feature state;
- `authorization_version`, monotonically incremented for cache invalidation;
- timestamps.

Every existing `User` gets one access domain and an owner membership. Platform
administrators also receive independent platform-role assignments. The legacy
account user is an ownership compatibility key, not the mutable domain owner:
transferring domain ownership changes `owner_membership_id`, never every
resource's old `user_id`.

### `access_domain_memberships`

- `access_domain_id` and `user_id`;
- state such as `active`, `suspended`, or `removed`;
- inviter, invitation/join timestamps, and optional expiry;
- unique `[access_domain_id, user_id]`.

`access_domains.owner_membership_id` is the single source of truth for
ownership; do not duplicate it with an independently editable owner role or
membership flag. A composite foreign key from
`[owner_membership_id, access_domain.id]` to
`[membership.id, membership.access_domain_id]` can enforce that the owner is in
the same domain. Because MariaDB does not defer foreign keys, domain creation
can use a short-lived `initializing` state with a nullable owner, then create
the membership and activate the domain in the same transaction.

The schema should allow one principal to join multiple domains even if the
first WebUI exposes only one membership for sub-users. This avoids duplicated
credentials and a later identity migration.

Pending invitations should live in a separate `access_domain_invitations`
table with an expiring single-use token digest. A membership should not contain
a nullable or guessed `user_id`. On acceptance, the invite is linked either to
an already authenticated `User` principal or to a newly created identity-only
`User`, and the membership is created transactionally.

### `access_groups` and `access_group_memberships`

Groups are always local to one access domain. A group membership references a
domain membership, not a raw user ID, so cross-domain membership cannot be
created accidentally. Group names are unique within a domain.

The first release should not support nested groups. If nesting is later shown
to be necessary, add cycle prevention, bounded traversal, effective-membership
explanation, and explicit performance tests before enabling it.

### `access_roles` and `access_role_permissions`

Permissions come from a code-owned, versioned registry. Roles refer to stable
permission keys. Built-in roles are immutable definitions supplied by
vpsAdmin; custom roles belong to one domain and may contain only permissions
the creating administrator is allowed to delegate.

Likely built-in roles, subject to a full permission inventory:

- Domain Owner: implicit full domain authority and ownership transfer;
- Access Administrator: member, group, custom-role, and grant management,
  constrained by anti-escalation rules;
- Infrastructure Administrator: resource administration without IAM,
  personal credentials, or billing authority;
- Operator: routine lifecycle operations without destructive ownership/IAM
  changes;
- Viewer/Auditor: read-only resource and permitted event access;
- Billing Manager: payment/accounting access without infrastructure control;
- Notification Manager: domain notification routing where shared routing is
  enabled.

Avoid wildcard permission strings in user-created roles. New API actions must
not silently enter old custom roles merely because their names match a broad
pattern.

### Role bindings and scopes

A conceptual binding contains:

- access domain;
- exactly one subject: domain membership or group;
- role;
- scope kind and scope reference;
- grantor principal/session;
- optional expiry;
- timestamps.

Physically, prefer separate `access_membership_role_bindings` and
`access_group_role_bindings` tables. This is less clever than a polymorphic
subject and lets MariaDB enforce that subject, role, and scope all belong to
the same domain through composite foreign keys.

Use an `access_scopes` table with an enumerated shape for the resource kinds
that are actually grantable. For example, a first version can have `kind` plus
nullable `vps_id`, `dataset_id`, and `dns_zone_id` columns, with check
constraints requiring exactly the column appropriate to `kind`. Do not accept
an unconstrained arbitrary model-name/model-ID pair.

### `platform_roles` and assignments

Installation-wide authority is stored separately from domain delegation:

- code-owned `platform_roles` with stable keys;
- `platform_role_permissions` using `platform.*` permission keys; and
- `platform_role_assignments` joining a principal to a platform role, with
  grantor, expiry, and audit attribution.

Domain role tables cannot contain `platform.*` permissions, and domain
administrators cannot read or mutate platform assignments through domain IAM
actions. This is a deliberate security boundary, even if both role kinds use
the same in-process permission evaluator.

### `security_audit_entries`

Security-sensitive identity and access changes require an append-only audit
record independent of notification routing. At minimum record:

- domain;
- actor principal, session, and impersonator/platform admin;
- stable action;
- target principal/group/role/binding/scope;
- success or failure outcome;
- bounded, redacted before/after details;
- request/correlation ID, source IP, and timestamp.

Successful IAM changes can additionally emit ordinary Events for notification
and external automation. Event retention must not be the only evidence that a
role or group changed.

## Concrete first schema shape

The first implementation should use `users` as the principal table. Existing
rows keep their IDs and authentication data. A newly invited sub-user is also a
normal `users` row, but has only domain memberships and does not automatically
become an independent resource-owning account.

The relevant shape is approximately:

```text
users
  id, login, password/authentication/profile fields, state, ...
  level                                      # transitional, removed later

access_domains
  id, public_id, label, state
  legacy_account_user_id -> users.id         # unique, immutable bridge
  owner_membership_id                        # same-domain membership
  authorization_version

access_domain_memberships
  id, access_domain_id, user_id              # principal membership
  state, authorization_version, joined_at, expires_at
  UNIQUE(access_domain_id, user_id)

access_domain_invitations
  id, access_domain_id, invited_identifier
  token_digest, invited_by_user_id, expires_at, accepted_at

access_groups
  id, access_domain_id, public_id, name

access_group_memberships
  access_domain_id, access_group_id, access_domain_membership_id

access_permissions
  key, realm, delegable, allowed_scope_kinds  # synchronized from code

access_roles
  id, access_domain_id, stable_key, label, kind, definition_version

access_role_permissions
  access_domain_id, access_role_id, permission_key

access_scopes
  id, access_domain_id, kind
  vps_id | dataset_id | dns_zone_id           # constrained by kind

access_membership_role_bindings
  id, access_domain_id, membership_id, role_id, scope_id
  granted_by_membership_id, expires_at

access_group_role_bindings
  id, access_domain_id, group_id, role_id, scope_id
  granted_by_membership_id, expires_at

platform_roles / platform_role_permissions
platform_role_assignments
  user_id, platform_role_id, granted_by_user_id, expires_at

security_audit_entries
  access_domain_id, actor_user_id, user_session_id,
  impersonator_user_id, action, target type/ID, outcome,
  redacted changes, request/correlation data, created_at
```

Tables participating in domain IAM should carry `access_domain_id` even where
it is derivable. Give memberships, groups, roles, and scopes unique composite
keys such as `[id, access_domain_id]`, then reference those pairs from join and
binding tables. This lets the database reject a Domain A group containing a
Domain B member or a binding that points at a Domain B role.

`user_sessions` gains `access_domain_id` and
`access_domain_membership_id`. Its existing `user_id` remains the authenticated
principal. The membership/domain/principal tuple should be protected by a
composite foreign key. Platform impersonation receives explicit impersonator
attribution instead of being confused with ordinary domain selection.

For each resource family as it becomes grantable, add `access_domain_id` while
retaining its old `user_id`. For example:

```text
vpses.user_id                      = domain.legacy_account_user_id
vpses.access_domain_id             = domain.id
transaction_chains.user_id         = actual acting principal
transaction_chains.access_domain_id = active domain
```

Where practical, a composite foreign key from
`[resource.access_domain_id, resource.user_id]` to
`[access_domains.id, access_domains.legacy_account_user_id]` should prove that
the old and new ownership columns agree. Authorization uses
`access_domain_id`; existing quota, billing, and node integrations continue to
use the old account `user_id` until their own migration slice.

There is intentionally no `subusers` table and no `users.parent_id`. “Sub-user”
is a product term for a principal with a non-owner domain membership. One
principal can safely be an owner in one domain and a delegated member in
another without duplicating credentials.

## Compatibility bridge for legacy ownership

Adding `domain_id` to every resource and moving all account fields away from
`User` in one release would be too risky. Start with a compatibility adapter:

- each access domain points to its immutable legacy account `User`;
- existing resource `user_id`, quota, environment configuration, billing,
  and node-facing semantics continue to point to that legacy account row;
- a sub-user creating or changing a resource acts as the authenticated
  principal, but the resource keeps the access domain's legacy account
  `user_id` and receives the domain's `access_domain_id`;
- transaction chains and audit/event actor fields retain the actual principal;
- business code obtains quotas and account state from
  `RequestContext.current.account`, not the principal; and
- new sub-users are never treated as independent resource-owning accounts.

This is the main reason not to model sub-users with only a `users.parent_id`.
A parent pointer would leave identity, quotas, billing, ownership, and
delegation ambiguous and would not represent groups or membership in more than
one domain.

After RBAC is stable, account-owned tables can gain explicit `access_domain_id`
columns in small, tested groups. Principal data such as passwords, MFA,
WebAuthn credentials, devices, and sessions stays on `User`; account data such
as quotas, billing, resources, and account lifecycle moves to the access
domain. Compatibility readers and dual writes should be removed only after a
stable deployment cycle.

New identity-only users must be created through a separate invitation/identity
operation, not the existing account-provisioning transaction chain. That path
must not allocate quotas, resources, default account configuration, or a home
domain. Conversely, code that assigns resource ownership must accept an access
domain/account context, never the acting principal's `user_id`.

## Complete replacement of numeric user levels

`users.level` is a migration source, not part of the target schema. Do not
recreate the hierarchy as a differently named integer, and do not make domain
roles inherit from platform roles.

Before conversion, inventory the distinct level values present in production
and every comparison against them. Translate behavior by meaning:

- ordinary account levels such as 1/2/3 receive no platform authority merely
  because of their number; any real commercial or operational distinction
  becomes an explicit domain/account tier or entitlement;
- support, administrator, and break-glass authority become code-owned platform
  roles with enumerated permissions;
- `SysConfig#min_user_level` becomes an explicit public visibility or required
  permission classification;
- monitoring `access_level` becomes an explicit audience/permission
  classification rather than an ordinal comparison;
- queries such as `User.where(level: 90..)` become queries for a precise
  platform permission or role assignment;
- DokuWiki groups derive from explicit platform/domain assignments; and
- console validity depends on the issuing principal's active membership and
  current VPS-console permission, not their former numeric level.

Do not map names blindly. For example, level 21 is labeled `Admin` but
`User#role` exposes it as `support`, while levels 90 and 99 both expose
`:admin` even though raw level-99 configuration gates exist. The migration must
derive an explicit old-access matrix for every distinct production value and
construct platform permission bundles that are equivalent, not broader.

Roll this out in four states:

1. backfill platform role assignments and explicit visibility classifications
   while all legacy level checks remain authoritative;
2. evaluate level-based and permission-based decisions side by side;
3. make authorization require both decisions, then remove all level reads from
   code after equivalence is proven; and
4. retain the unchanged column for one rollback window, then drop `level`,
   `min_user_level`, and obsolete ordinal visibility columns in a later
   migration.

Add CI guards that fail on new `User#level`, `User#role`, `min_user_level`, or
numeric user-access comparisons. The final public User API has no writable
`level` field.

## Permission and scope model

Permissions should describe stable business capabilities, not every HTTP verb
mechanically. An initial catalog will likely include families such as:

- `domain.read`, `domain.update`;
- `members.read`, `members.invite`, `members.suspend`;
- `groups.read`, `groups.manage`;
- `roles.read`, `roles.manage`, `grants.manage`;
- `vps.read`, `vps.create`, `vps.update`, `vps.power`, `vps.console`,
  `vps.delete`;
- `dataset.read`, `dataset.create`, `dataset.update`, `dataset.snapshot`,
  `dataset.export`, `dataset.delete`;
- `network.read`, `network.manage`;
- `dns.read`, `dns.manage`, with secret/key operations separate;
- `events.read`, `events.read_security`, `events.routes.manage_own`, and
  `events.routes.manage_domain`;
- `audit.read`;
- `billing.read`, `billing.manage`; and
- personal credential/session permissions that never inherit merely from
  infrastructure administration.

The inventory must decide where sensitive fields or actions need a separate
permission. VPS user-data content, private keys, API tokens, webhook secrets,
MFA state, login IPs, billing details, and security events must not be exposed
by a broad `read` permission accidentally.

Initial binding scopes should be deliberately small:

1. whole access domain;
2. one VPS, with an explicit list of child resources and operations;
3. one dataset subtree; and
4. one DNS zone.

Possible later scopes include resource collections/tags. Do not make every
Active Record model independently grantable.

The resource hierarchy must be declared next to the public resource policy,
similar in spirit to the event branch's explicit `resource_events` owner and
VPS resolvers. Examples require design review:

- a VPS grant can cover console sessions, interfaces, addresses assigned to
  that VPS, VPS-specific user data, and its dedicated root dataset;
- a dataset grant covers its declared descendant datasets and snapshots;
- a DNS-zone grant covers records and transfers in that zone; and
- shared resources, credentials, account quotas, payments, and unrelated
  datasets do not inherit from a VPS merely because an association exists.

The typed public event resource catalog is a useful starting inventory, but it
cannot be the authorization registry: it excludes read-only resources and its
audience/owner declarations do not express action-specific permissions.

## Authorization request flow

Introduce an immutable per-request context with at least:

- authenticated principal;
- active access domain;
- legacy account user/domain owner used by compatibility business logic;
- user session and token/OAuth scopes;
- platform role;
- impersonating administrator, if any.

For every request:

1. Authenticate the principal.
2. Resolve the domain fixed to the session/token; never trust an arbitrary
   request-body domain ID.
3. Check platform administration rules independently.
4. Check that the domain and membership are active.
5. Resolve the target's domain and declared authorization scope.
6. Intersect the session's HaveAPI action/path scopes with effective RBAC role
   bindings.
7. Apply business-state constraints such as object lifecycle, maintenance,
   quota, `user_editable`, or `user_destroy`. These constraints can deny but
   must never grant authority.
8. Execute and record actor/domain attribution for mutations.

Single-domain legacy users and old sessions should have their home domain
selected automatically, preserving current clients. A multi-domain or service
token should be issued for one explicit domain. Fixing domain context at token
issuance is safer than allowing each request to switch domains with a header.
The browser can obtain a separate domain-bound session when the user changes
domain.

## HaveAPI and vpsAdmin enforcement

The existing authorization DSL provides coarse allow/deny, simple equality
restrictions, and input/output filtering. It does not provide arbitrary
permission-scoped query relations. Its `pre_authorize` hook runs before input
validation and action preparation, and `safe_exec` currently proceeds directly
through `validate!`, `prepare`, `pre_exec`, and `exec`. This is not a sufficient
place to authorize a validated create parent or a loaded object safely.

The clean design should therefore include a small, backward-compatible change
to the HaveAPI Ruby server. HaveAPI should supply generic enforcement
primitives, while all vpsAdmin domain, role, permission, and scope semantics
remain in vpsAdmin:

1. Add a deny-only authorization-guard hook for immutable function-level
   checks. Unlike the existing first-decision `pre_authorize` blocks, an
   application guard must not be able to accidentally grant past an action's
   own denial.
2. Add a guard point after input validation so resource-valued parameters and
   create parents can be checked before action preparation.
3. Add a second authorization lifecycle point after `prepare`, but before
   `pre_exec` or `exec`. It receives the action instance, context, and prepared
   value so vpsAdmin can recheck the resolved target before any mutation.
4. Add a generic relation-scoping primitive, such as
   `authorized_scope(relation, purpose:)`, that application policies can
   transform. The default is backward-compatible identity scoping; vpsAdmin
   uses it for index/count/show/update/delete loaders.
5. Add a record-authorization primitive used consistently by resource-valued
   input parameters and nested/expanded resource serialization. This prevents
   a related object from bypassing the same policy used by its Show action.
6. Preserve input, output, and metadata filtering after the new checks, and add
   framework tests that prove a denial occurs before `pre_exec`/`exec` and that
   unauthorized associations remain unresolved.

No HaveAPI wire-protocol or generated-client change is required for these
server lifecycle primitives. vpsAdmin may separately publish effective
capabilities in its API metadata. Do not put permission names or a database
role model into HaveAPI itself.

The exact hook names should be prototyped in HaveAPI before the vpsAdmin policy
conversion. Avoid a vpsAdmin monkey-patch that copies `HaveAPI::Action#safe_exec`:
the events branch demonstrates that wrapping the whole method is possible, but
RBAC needs a stable check specifically between preparation and execution.
Make `prepare` explicitly side-effect free as part of that lifecycle contract;
refactor any action that currently mutates before the prepared-object guard.

On top of these primitives, add a declarative vpsAdmin access-policy registry.

Each mounted action should declare, directly or through a validated standard
inference:

- required permission;
- domain resolver;
- target/scope resolver;
- query scoper for indexes;
- create-parent resolver where applicable;
- sensitive input/output policy; and
- an explicit reason for public, platform-only, internal, or temporarily
  legacy-owner-only behavior.

Enforcement has two stages:

- function-level authorization controls whether the action is described or
  callable at all in the active domain; and
- object-level authorization scopes database queries and rechecks loaded
  objects/parents. An inaccessible object should normally look not found,
  preventing cross-domain enumeration.

Index actions must start from a tenant- and permission-scoped relation. Show,
update, and delete actions must load through the same scope. Create actions
must authorize their parent/domain after validated resource parameters are
resolved. Client-supplied `user_id` or domain fields are derived or checked
server-side.

Add strict coverage tests, modeled after the events initiative's action-policy
inventory, that enumerate:

- every mounted HaveAPI action, including plugins;
- WebAuthn/OAuth/authentication endpoints outside normal resources;
- callbacks and background operations;
- node/supervisor entry points where user authority is relevant; and
- bulk or indirect mutations.

No action may be silently unclassified. During migration, unconverted actions
can declare `legacy_account_owner_only` with a concrete reason. The old and new
checks should be intersected in shadow/enforcement transition phases so a
partial conversion cannot widen access.

The WebUI currently caches the caller-specific API description and also stores
coarse `is_admin`/`is_poweruser` flags. Domain permissions must come from the
API description/current-domain capability data. The PHP UI may hide controls
for usability, but only the API is authoritative.

## Delegation and escalation invariants

These invariants are mandatory:

- The domain owner has an implicit, non-removable owner role. Ownership
  transfer is a dedicated, strongly authenticated transaction that preserves
  exactly one owner.
- A grantor can bind only permissions they currently hold and that the
  permission catalog marks delegable, at the same or a narrower scope.
- A custom role cannot be edited to contain authority its editor cannot
  delegate.
- Adding someone to a security group is itself an access grant. The caller
  must be allowed to confer every effective role binding currently attached to
  that group. A generic "group owner" must not become a privilege-escalation
  path.
- Removing/suspending a membership invalidates every session for that domain
  and increments the domain authorization version.
- Revocation must become effective predictably. Begin with database-backed
  checks; if caching is added, key it by domain/principal authorization
  versions and use a short bounded lifetime.
- Group, role, binding, ownership, invitation, and membership lifecycle
  changes are transactional and audited.
- Domain A identifiers supplied while operating in Domain B are rejected or
  treated as not found before any sensitive fields are returned.
- Platform administration and impersonation remain separately attributable;
  a platform admin must not become an unrecorded domain principal.
- Invitations do not let a domain admin choose a reusable password for another
  person. The invitee claims an expiring, single-use invitation and establishes
  their own authentication credentials.

Prefer group bindings for normal administration, but allow direct membership
role bindings for the owner, emergency access, and small teams. Direct raw
permission grants are not allowed.

## Events integration

The events initiative can support delegated visibility without becoming the
authorization database.

Add indexed event attribution when RBAC is implemented:

- `access_domain_id`, nullable only for genuinely global/system events;
- `actor_user_id`, nullable for automated producers;
- retain the current subject `user_id` during compatibility, treating it as
  the legacy account or identity the event is about; and
- retain `admin_user_id`/session attribution in the typed payload until a
  later normalized schema decision.

For domain-owned resource events:

- the event domain is resolved from the resource's legacy account owner;
- the subject can remain the legacy account user during compatibility;
- the actor is the sub-user who performed the action; and
- the initial owner therefore continues to receive normal self-route behavior.

For principal-specific security events, such as a sub-user login or session
change, the subject remains that principal while `access_domain_id` identifies
the active domain. Domain security administrators may see these events only
through a distinct sensitive permission such as `events.read_security`.

Extend `Event.visible_to` and route-context calculation through the central
authorization service. A member with the relevant event permission receives
relation `rbac` and source `rbac_route`. Replace the current admin-only
indirect-route candidate search with a domain-prefiltered set of active
members that have enabled visible routes, then verify each candidate with the
policy service before evaluating routes. Do not materialize every potential
viewer for every event.

Personal routes can remain owned by a user, but they should be tied to an
access domain. A domain-managed catch-all/shared route may be useful for an
operations or security team; whether it is required in the first release is an
open product decision.

The owner and delegated users can "get events from sub-users" in two distinct
senses:

- notification/history: configure an authorized visible route, which causes
  the event and delivery history to be retained; and
- complete audit: use the separate internal IAM audit log and, for the full
  general event stream, configure a catch-all route to a durable external
  receiver as required by the events contract.

Do not promise that the Event index alone contains every sub-user action.

## Proposed API and WebUI surface

Provisional API resources:

- `domain#index/show/current`;
- `domain.membership#index/show/invite/update/remove`;
- `domain.group` and nested group membership actions;
- `domain.role` and role-permission metadata;
- `domain.role_binding` / `domain.access_grant`;
- resource-filtered grant views such as one VPS's effective access;
- `authorization.explain` for administrators and support diagnostics;
- `security_audit_entry#index/show`; and
- active-domain/session selection at login/session issuance.

`user#current` should expose active-domain and membership information without
exposing other domains. API descriptions and metadata should publish stable
permission names, grantable scope kinds, built-in role definitions, and
caller capabilities so clients do not hard-code role labels.

WebUI concepts:

- Members;
- Groups;
- Roles;
- Access grants;
- an Access tab on grantable resources;
- effective-access explanation;
- domain event/security history; and
- a domain selector that is visually and technically distinct from platform
  administrator impersonation.

Every visible WebUI change requires the canonical
`vpsfree-kb-contracts/docs/webui-change-workflow.md` flow and bilingual
documentation/capture review.

## Phased implementation

### Phase 0: refresh prerequisites and inventory

- Integrate or rebase the events initiative onto current vpsAdmin master.
- Create the RBAC vpsAdmin worktree only after that baseline is chosen.
- Prototype and release the generic HaveAPI authorization lifecycle and
  relation/record-scoping primitives before depending on them in vpsAdmin.
- Enumerate every API action, external endpoint, background mutation, current
  ownership check, sensitive field, and resource-owner path.
- Inventory every production `users.level`, `min_user_level`, and monitoring
  `access_level` value and the exact access it currently confers.
- Define the stable permission catalog and explicit grantable resource graph.
- Decide the first pilot permissions and scopes.

### Phase 1: additive domain and identity boundary

- Add access domains and memberships.
- Backfill exactly one owner domain/membership for every existing account.
- Add domain context to sessions with legacy single-domain inference.
- Add platform roles/assignments and backfill them from the verified legacy
  access matrix, without using them to authorize requests yet.
- Introduce `RequestContext` with principal, domain, account, session,
  platform role, and impersonator.
- Preserve all current authorization behavior; expose no sub-users yet.
- Add migration invariants proving that every legacy-owned object resolves to
  exactly one domain.

### Phase 2: policy registry in shadow mode

- Add declarative action/resource policies and strict coverage inventory.
- Implement domain/permission query scoping.
- Compute new decisions beside old decisions without granting new access.
- Compare decisions in tests and bounded diagnostic logging; never log
  secrets or full payloads.
- Treat every candidate allow paired with a legacy denial as a security defect,
  not an expected migration discrepancy.
- Classify every unconverted surface explicitly as owner-only, platform-only,
  public, or internal.

### Phase 3: current-owner and platform-role equivalence

- Enforce the new policy for existing owners and platform admins while still
  intersecting legacy checks.
- Replace every numeric level decision with an explicit platform permission,
  domain/account entitlement, or visibility classification.
- Replace ownership uses of `current_user`/`User.current` with explicit
  principal versus account context.
- Verify quotas, billing, lifecycle, transaction chains, plugins, and node
  messages remain based on the domain account where appropriate.
- Do not create or authenticate sub-users until every API worker runs this
  code.
- Remove all runtime reads of `users.level`, while retaining the unchanged
  column for one bounded rollback window.

### Phase 4: delegated-access pilot

- Add invitation, membership, group, built-in role, and binding APIs.
- Start with non-nested groups and domain plus single-VPS scopes.
- Pilot a Viewer and an Operator role on one VPS and its explicitly declared
  children.
- Add WebUI management and effective-access explanation.
- Add RBAC event visibility and a visible route for a delegated member.
- Keep unconverted resource families owner-only.
- Until the transitional `level` column is dropped, store the fail-closed
  sentinel `0` for an identity-only user; no authorization may consult it.

### Phase 5: expand resource families and custom roles

- Convert datasets, DNS, network, exports, notifications, incidents,
  requests, payments, and plugins in reviewed slices.
- Add custom roles only after anti-escalation and permission-catalog behavior
  are proven with built-ins.
- Generate/update clients and Terraform resources only as their public support
  is introduced.

### Phase 6: explicit domain ownership

- Complete the `access_domain_id` rollout across account-owned data in small
  migration groups; grantable resources receive it in their earlier slices.
- Move quota, billing, account lifecycle, and contact semantics out of the
  principal model where appropriate.
- Dual-read/write during a bounded compatibility window, verify backfills,
  then remove the legacy account-user adapter in a later release.
- Drop `users.level`, `sysconfig.min_user_level`, and replaced ordinal
  visibility columns after their rollback windows and CI-proven zero usage.

## Compatibility and deployment

### Database and persisted state

- Initial migrations are additive and backfilled before any behavior changes.
- Use database uniqueness and cross-domain referential constraints wherever
  MariaDB permits them; do not depend solely on controller checks.
- Do not add defensive migration guards for unsupported stale development
  schemas. Reset disposable databases after draft migrations are rewritten.
- Existing resource `user_id` values and node-facing account IDs remain stable
  through the compatibility phases.
- New tables remain after rollback; old code ignores them.

### API and clients

- Existing single-domain owners and tokens continue in their home domain by
  default.
- New resources and fields are additive until delegated access is enabled.
- Token/OAuth action scopes continue to work and reduce RBAC permissions.
- Multi-domain and service tokens are domain-bound.
- Old clients must tolerate additional resources/fields and event types.
- The generated Go client must be regenerated for public API changes.
- `vpsfree-client` and Terraform provider behavior must be evaluated; provider
  support for users/groups/grants should be a separate reviewed slice rather
  than implied automatically.

### Mixed versions and activation

Schema deployment and owner-only policy shadowing can support mixed API
versions. Actual sub-user login cannot safely support old API workers: old
code may deny delegated resources inconsistently or treat a sub-user as an
independent resource-owning account.

Use a server-side feature gate. Before enabling the first sub-user:

1. deploy schema and compatible code;
2. restart/update all API, WebUI, and relevant worker processes;
3. verify every process advertises the RBAC-capable policy version;
4. enable RBAC for one pilot domain; and
5. retain an immediate switch that suspends delegated sessions without
   affecting legacy owners.

Rollback after sub-users have been enabled requires disabling delegated login,
closing domain-member sessions, and returning access to legacy owners before
old code is started. Do not drop RBAC state during rollback.

### vpsAdminOS and services

No node protocol or vpsAdminOS change is expected in the compatibility design:
resources continue to carry the legacy account `user_id`, and vpsAdmin remains
the policy authority. If implementation reveals a node-visible identity or
protocol change, it needs a separate compatibility analysis and deployment
order. No coordinated update of all vpsAdminOS machines is currently
justified.

### Events dependency

RBAC depends on the events branch's actor attribution, explicit owner
resolvers, visibility service, and route contexts. Implement RBAC after that
architecture is integrated. Adding RBAC directly to the 55-commit-behind
branch would create avoidable rebase and review risk.

## No-privilege-expansion proof

“Be careful” is not a sufficient control. The migration needs an explicit
invariant and release gates.

For every pre-existing principal, session kind, existing action, target, input
shape, and output field before delegation is enabled:

```text
effective_allow = legacy_allow AND candidate_rbac_allow
candidate_rbac_allow AND NOT legacy_allow = release-blocking security mismatch
legacy_allow AND NOT candidate_rbac_allow = compatibility mismatch to resolve
```

This intersection must happen at function, relation, object, input-field, and
output-field levels. Comparing only HTTP 200/403 status is insufficient: an
index returning one extra row, a count revealing another domain, or an
expanded association exposing one field is also privilege expansion.

Additional controls:

- New memberships, groups, roles, and bindings have no effect while shadow
  mode is active.
- Unconverted actions are explicitly `legacy_account_owner_only`; a delegated
  member is denied rather than executed as the domain's legacy account user.
- Never make `User.current` equal the legacy account user for a sub-user. The
  actor remains the sub-user and the account is a separate context value.
- Each converted delegated action is enabled from a positive allowlist behind
  a per-domain feature gate. There is no broad “RBAC enabled” fallback.
- A differential harness runs the same fixture/request matrix against the
  frozen legacy evaluator and the candidate evaluator and compares status,
  selected object IDs, counts, metadata, associations, and field sets.
- Shadow telemetry in a representative deployment records bounded,
  pseudonymized decision tuples and mismatch reasons, never request payloads,
  credentials, secrets, or sensitive object values.
- Activation requires zero deny-to-allow mismatches on the existing API
  surface. Sampled absence is not enough for the generated action/fixture
  matrix.
- The delegated pilot has a kill switch that closes member sessions and stops
  issuing new ones without changing owner or platform access.

Once a sub-user receives an explicit grant, access to the converted scope is
an intentional new capability and cannot be compared to a legacy identity
that did not exist. It is instead proven against the exact binding: the result
set and permitted operations must be a subset of the role's permission and
scope closure. Everything outside that closure remains denied.

The new IAM control-plane actions have no legacy equivalent. Treat them as a
separate, positively enumerated surface: owner-only at first, domain-bound,
anti-escalation checked, fully audited, and incapable of directly reading or
mutating unrelated business resources. Their intended effect is to create the
explicit grants against which delegated access is then tested.

## Security and correctness testing

At minimum:

- permission-registry and role truth tables;
- generated coverage proving every API action and external entry point has one
  access policy;
- a legacy-versus-candidate differential matrix for every existing level,
  platform role, authentication method, token scope, and object state;
- generated assertions that candidate query IDs, counts, associations,
  metadata, and output fields are subsets of legacy results before delegation;
- two-domain isolation tests for every action, including guessed IDs, nested
  input resources, filters, counts, pagination, metadata, and output fields;
- owner-equivalence tests proving no existing owner loses or gains access;
- anti-escalation tests for role edits, bindings, group membership, scope
  broadening, expiry, suspension, and ownership transfer;
- transactional race tests for concurrent group/role/binding changes and last
  owner protection;
- session and token tests for active domain, multiple memberships, OAuth,
  HaveAPI scope intersection, revocation, and impersonation attribution;
- resource-graph tests proving intended child inheritance and rejecting
  unrelated/shared resources;
- query-count and representative large-domain performance tests;
- transaction-chain tests proving actor principal and legacy account owner are
  both preserved through success, failure, rollback, retry, and deletion;
- event tests for self, platform-admin, RBAC, sensitive-security, muted,
  unmatched, and delivery-only cases;
- append-only IAM audit tests independent of notification delivery;
- plugin tests and strict CI topic/selection coverage;
- WebUI PHPUnit and Playwright coverage, including domain switching and hidden
  controls backed by API rejection tests;
- migration tests from the immediately preceding schema and rollback/feature
  disable tests;
- static CI rejection of old numeric level/role checks and unscoped model
  loaders in converted actions;
- targeted mutation tests showing that removing a policy declaration, query
  scope, object recheck, or domain predicate makes the test suite fail; and
- bridge-network dev-cluster acceptance with two domains, multiple members,
  group changes, resource delegation, revocation, event routing, and existing
  owner operations.

Run the mandatory standalone change review after each coherent implementation
slice is committed and quick checks pass, before long integration tests.

## Affected repositories

Definite or likely:

- `vpsadmin`: primary schema, policy service, API, WebUI, events integration,
  plugins, tests, and deployment modules;
- `haveapi`: definite small Ruby-server extension for deny-only guards,
  post-prepare authorization, relation scoping, and record authorization;
- `vpsadmin-go-client`: generated client changes for new public resources;
- `vpsfree-kb-contracts`: WebUI documentation contract, runtime tests, and
  screenshots;
- `vpsfree-cz-configuration`: eventual reviewed source pin and activation
  configuration;
- `terraform-provider-vpsadmin`: optional later support for domain IAM
  resources; and
- `vpsfree-client`: compatibility evaluation and optional domain-aware CLI
  support.

No vpsAdminOS repository change is currently expected.

## Alternatives not recommended

### Self-referential parent/sub-user rows only

Adding `users.parent_id` would not separate principals from accounts, would
not model groups or scoped roles cleanly, would duplicate or confuse quotas
and billing, and would make multi-domain membership difficult. It is not a
sufficient tenancy model.

### Clone Active Directory ACLs

Per-object ordered allow/deny ACEs, nested group scope types, and cross-domain
trusts offer flexibility that vpsAdmin does not presently need. They make
effective access and delegation escalation much harder to explain and test.
Use positive scoped role bindings first.

### Use event routing as the audit database

The events contract intentionally drops candidates without executable
delivery work. Auto-creating a route would help external streaming but would
not turn delivery history into reliable internal IAM evidence. Keep a small
append-only security audit store.

### External Zanzibar-style authorization service immediately

The relationship model is useful, but an external consistency-critical
service adds deployment and failure modes before vpsAdmin has a stable
permission/resource graph. Begin with one centralized in-process policy
service and transactional MariaDB state. Re-evaluate a tuple service only if
scale or cross-service authorization requires it.

### Add `access_domain_id` to every table at once

This maximizes migration, rollback, and mixed-version risk. The legacy-owner
adapter permits an incremental migration while keeping node and accounting
semantics stable.

## Recommended first prototype

After the events baseline is refreshed, the smallest useful end-to-end
prototype is:

1. one access domain and owner membership per existing account;
2. one invited member and one non-nested group;
3. immutable built-in Viewer and VPS Operator roles;
4. a role binding at one VPS scope;
5. declarative owner-only policies for every unconverted action;
6. converted VPS index/show, power, and console actions with explicit child
   scope rules;
7. domain-bound sessions and unchanged legacy account ownership/quotas;
8. actor/domain attribution in transaction chains and events;
9. one RBAC-visible event route proving the owner and delegated member receive
   the intended event; and
10. immediate revocation proving the member loses API, WebUI, console, and
    event access while the owner remains unaffected.

This prototype should run only in tests and a bridge-network development
cluster. It should not enable production sub-users.

## Open product and architecture decisions

1. Should one identity be allowed in multiple domains in the first UI, or only
   in the schema/API initially? Recommendation: support it in the model from
   the beginning.
2. What member-facing term is clearest: account, team, organization, or
   domain? Recommendation: internal `AccessDomain`, user-facing "account" or
   "team" after copy review.
3. Are custom roles required for the first release? Recommendation: prove
   built-in roles and anti-escalation first, but design storage for custom
   roles.
4. Which resource scopes are essential beyond whole domain and one VPS?
5. Which sub-user authentication/security events may domain owners and
   security administrators see? Login IPs, MFA, sessions, and credential
   events need an explicit privacy policy.
6. Are personal visible routes sufficient initially, or must domains own
   shared notification receivers/routes?
7. Is a complete in-product activity/audit history required beyond IAM
   changes? If yes, that is a separate audit-ledger requirement from the
   delivery-only Event API.
8. How should an invitation match an existing identity when e-mail is not
   currently a unique User attribute?
9. Do production levels 1/2/3 encode any non-authorization business or account
   distinctions that must survive as explicit entitlements? This must be
   answered from production data and behavior, not from the old labels.

## Research references

- NIST's RBAC FAQ distinguishes users, roles, permissions, role hierarchy,
  sessions, and separation-of-duty constraints:
  <https://csrc.nist.gov/Projects/role-based-access-control/faqs>
- Microsoft documents AD security groups and their domain scopes:
  <https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/understand-security-groups>
- Microsoft documents ACL inheritance and delegated administration:
  <https://learn.microsoft.com/en-us/windows/win32/ad/inheritance-and-delegation-of-administration>
- Microsoft's Azure RBAC guidance recommends least privilege, narrow scopes,
  stable role IDs, and group assignments:
  <https://learn.microsoft.com/en-us/azure/role-based-access-control/best-practices>
- OWASP recommends deny-by-default, checking every request and object, and
  centralized, tested authorization:
  <https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html>
- Google's Zanzibar paper is useful background for relationship-based resource
  authorization, but does not imply that vpsAdmin needs a separate Zanzibar
  service now:
  <https://research.google/pubs/zanzibar-googles-consistent-global-authorization-system/>

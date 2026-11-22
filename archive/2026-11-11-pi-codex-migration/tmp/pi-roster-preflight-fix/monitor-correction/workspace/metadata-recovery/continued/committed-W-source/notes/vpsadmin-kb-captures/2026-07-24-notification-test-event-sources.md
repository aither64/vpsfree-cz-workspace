# Notification test events and source-backed templates

Related initiative: `work/2026-06-15-vpsadmin-events/`.

The notification `Test event` action creates an event for the selected type,
but it does not reconstruct the type's normal source object. In particular, a
synthetic `vps.*` event can contain `vps_id` and `vps_hostname` matcher fields
while `event.vps` remains unset. Delivery templates that dereference the real
VPS or incident can therefore fail even though route matching succeeds.

Use `user.test_notification` for testing a new Telegram or SMS connection when
the delivery action has a source-independent template. For a webhook, a
synthetic `vps.resources_changed` event is safe because its serializer uses
the stored event and matcher fields; temporarily put that route first and set
`Continue` to no so the event cannot also reach the default e-mail template.
Verify source-backed `vps.suspended`, incident, and monitoring deliveries from
the next real event or from the route hit count.

Fixture `EventRouteMatch` rows are evaluation snapshots. Keep the oldest
fixture event and its URL stable across ordinary seed reruns. If a route
matcher deliberately changes, refresh that fixture once as an explicit part
of the change instead of deleting and recreating every fixture on every seed.
The notification screenshot seed removes duplicate fixture events but reuses
the oldest matching event.

The screenshot seed passed repeatedly after applying these rules. Consecutive
Czech captures had the same capture-result hash, as did consecutive English
captures. Role, incident-mute, OOM-mute, Telegram, SMS, and webhook assertions
all matched their intended routes.

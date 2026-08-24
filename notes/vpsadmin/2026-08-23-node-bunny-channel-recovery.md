# NodeBunny publishers can race channel recovery

## Symptom

After a RabbitMQ channel-open timeout, nodectld can loop on
`CHANNEL_ERROR - expected 'channel.open'`. RabbitMQ logs show `basic.publish`
arriving on a channel that was not reopened. Restarting nodectld clears the
state.

## Cause

Bunny 2.24.0 reopens its connection, marks connection recovery false, and only
then recovers registered channels. `NodeBunny#create_channel` waits for its
recovery generation, but `publish_wait` and `publish_drop` publish directly.
A publisher can therefore use an exchange after the connection opens but
before its channel has reopened, causing the broker to close the connection
again.

## Fix and verification

Gate every publisher on the recovery-completed generation. Waiting publishers
should block; drop-mode publishers should return false while recovery is
incomplete. Test concurrent publication during delayed or timed-out
`channel.open`, and assert that no `basic.publish` precedes the recovered
channel open.

Related initiative: `work/2026-08-23-vpsadmin-supervisor-issue/`.

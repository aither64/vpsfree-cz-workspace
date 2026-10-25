# vpsAdmin Rust client

Rust client library for [vpsAdmin](https://github.com/vpsfreecz/vpsadmin)
API 7.0, with async and optional blocking clients. Requires Rust 1.95 or newer.

## Installation

Add the client and Tokio to your application:

```toml
[dependencies]
vpsadmin-client = "0.1"
tokio = { version = "1", features = ["macros", "rt-multi-thread"] }
```

Building the TLS dependencies may require a C toolchain.

## Usage

Create a client with the server's base URL, without `/v7.0/`. Public actions
work without authentication:

```rust,no_run
use vpsadmin_client::Client;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let api = Client::builder("https://api.vpsfree.cz").build()?;
    let response = api.cluster().public_stats().send().await?;
    println!("VPS count: {:?}", response.output.vps_count);
    Ok(())
}
```

Resource methods return action builders. Pass resource IDs to methods such as
`show(id)`, set input fields, then call `.send().await?`. The response contains
typed `output`, action metadata in `meta`, and `http_status`.

### Authentication

Configure an existing HaveAPI token with `.token(...)`:

```rust,no_run
use vpsadmin_client::Client;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let api = Client::builder("https://api.vpsfree.cz")
        .token(std::env::var("VPSADMIN_TOKEN")?)
        .build()?;
    let vps = api.vps().show(123).send().await?.output;
    println!("{}", vps.hostname.as_deref().unwrap_or("<not returned>"));
    Ok(())
}
```

HTTP Basic authentication uses `.basic_auth(username, password)`; OAuth2 access
tokens use `.oauth2_token(token)`. Choose one authentication method when
building the client. Token login, challenges, renewal and revocation are
explicit actions under `api.authentication__token__token()`; the client does
not acquire or refresh tokens automatically.

### Input parameters

Only fields set on an action builder are sent. For example, this request changes
the VPS info field and leaves other fields untouched:

```rust,ignore
api.vps().update(vps_id).info("Maintenance note").send().await?;
```

Setters preserve `false`, zero and empty strings. Use a field's `_null()` setter
to send an explicit null where supported:

```rust,ignore
api.dns_record().update(record_id).ttl_null().send().await?;
```

Custom parameters accept `serde_json::Value`. Response fields use `Option`
because permissions and partial responses can omit them. Related objects can
also be partial; the client does not fetch them automatically.

For pagination, use the action's `.limit(...)` and `.from_id(...)` setters.
Nested resources take the parent ID and join resource names with double
underscores, for example `api.dataset__plan(dataset_id).show(plan_id)`.

### Timeouts and errors

The default request timeout is 30 seconds and the connection timeout is 10
seconds. Set `.timeout(Duration::from_secs(60))` or
`.connect_timeout(Duration::from_secs(10))` on `Client::builder(...)` to change
them, using `std::time::Duration`.

Requests return errors for invalid inputs, transport failures, unsuccessful
HTTP or API responses, and invalid response data. Redirects and automatic
retries are disabled. A timeout can occur after the server has applied a
change, so check its state before repeating a mutation. Some successful actions
start background work; a successful response does not mean that work has finished.

## Blocking client

Enable the `blocking` feature:

```toml
[dependencies]
vpsadmin-client = { version = "0.1", features = ["blocking"] }
```

Use `vpsadmin_client::blocking::Client` with the same action builders and
response types. Calls end in `.send()?`:

```rust,no_run
use vpsadmin_client::blocking::Client;

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let api = Client::builder("https://api.vpsfree.cz").build()?;
    let stats = api.cluster().public_stats().send()?.output;
    println!("VPS count: {:?}", stats.vps_count);
    Ok(())
}
```

Construct, use and drop the blocking client outside an async runtime. In an
async application, use the async client or put the entire blocking-client
lifecycle inside `tokio::task::spawn_blocking`.

## Examples and documentation

See the [API reference](https://docs.rs/vpsadmin-client) for resources, actions
and response types.

The [async](https://github.com/vpsfreecz/vpsadmin-rust-client/blob/v0.1.0/examples/async_vps.rs)
and [blocking](https://github.com/vpsfreecz/vpsadmin-rust-client/blob/v0.1.0/examples/blocking_vps.rs)
examples read a VPS using `VPSADMIN_TOKEN`. From a repository checkout, prepare
a local dependency lock once before running the examples:

```sh
cargo generate-lockfile
cargo run --locked --example async_vps -- 123
cargo run --locked --features blocking --example blocking_vps -- 123
```

Set `VPSADMIN_URL` to use another server offering API 7.0. The crate version and
API version are independent.

The client is generated with [HaveAPI](https://github.com/vpsfreecz/haveapi).
See [development and regeneration](https://github.com/vpsfreecz/vpsadmin-rust-client/blob/v0.1.0/docs/development.md)
for source maintenance and release checks.

MIT licensed; see [LICENSE](https://github.com/vpsfreecz/vpsadmin-rust-client/blob/v0.1.0/LICENSE).

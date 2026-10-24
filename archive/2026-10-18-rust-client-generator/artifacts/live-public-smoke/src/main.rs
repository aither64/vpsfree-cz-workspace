use vpsadmin_client::resources::cluster::public_stats::{Meta, Output};

type SmokeResult<T> = Result<T, Box<dyn std::error::Error>>;
const BASE: &str = "https://api.vpsfree.cz";

fn validate(response: vpsadmin_client::Response<Output, Meta>) -> SmokeResult<u16> {
    if !(200..300).contains(&response.http_status)
        || response.output.user_count.is_none()
        || response.output.vps_count.is_none()
        || response.output.ipv4_left.is_none()
    {
        return Err("public stats response did not match the captured typed contract".into());
    }
    Ok(response.http_status)
}

fn run() -> SmokeResult<()> {
    // This scope destroys the async runtime before constructing the blocking
    // client. Neither client configures credentials or invokes another action.
    let async_status = {
        let runtime = tokio::runtime::Runtime::new()?;
        runtime.block_on(async {
            let api = vpsadmin_client::Client::builder(BASE).build()?;
            validate(api.cluster().public_stats().send().await?)
        })?
    };
    println!("async public_stats PASS HTTP {async_status}");

    let api = vpsadmin_client::blocking::Client::builder(BASE).build()?;
    let blocking_status = validate(api.cluster().public_stats().send()?)?;
    println!("blocking public_stats PASS HTTP {blocking_status}");
    Ok(())
}

fn main() {
    if run().is_err() {
        eprintln!("public_stats smoke FAIL");
        std::process::exit(1);
    }
}

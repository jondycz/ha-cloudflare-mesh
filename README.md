# Cloudflare Mesh for Home Assistant

Home Assistant app that runs a
[Cloudflare Mesh](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-mesh/)
node on your Home Assistant host. It wraps the official `cloudflare/mesh` image
(AMD64 and ARM64).

## Installation

1. In Home Assistant, go to **Settings** > **Apps** > **App store**.
2. Add `https://github.com/jondycz/ha-cloudflare-mesh` as a custom repository.
3. Install **Cloudflare Mesh**.
4. Enter the Mesh node token from the Cloudflare dashboard and start the app.

See [cloudflare-mesh/DOCS.md](cloudflare-mesh/DOCS.md) for configuration.

Cloudflare and the Cloudflare logo are trademarks of Cloudflare, Inc. This
project is not affiliated with or endorsed by Cloudflare, Inc.

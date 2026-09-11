# Cloudflare Mesh for Home Assistant

This repository contains a Home Assistant app for running a Cloudflare One
Mesh connector directly on a Home Assistant host.

## Installation

1. In Home Assistant, go to **Settings** > **Apps** > **App store**.
2. Add `https://github.com/jondycz/ha-cloudflare-mesh` as a custom repository.
3. Install **Cloudflare Mesh**.
4. Enter the Mesh node token generated in the Cloudflare dashboard.
5. Start the app and review its logs to confirm that the connector registered.

See [cloudflare-mesh/DOCS.md](cloudflare-mesh/DOCS.md) for configuration and
networking details.

## Images

The app image is a thin wrapper around the official `cloudflare/mesh` image.
Images for AMD64 and ARM64 are published to GitHub Container Registry.

## Trademark notice

Cloudflare and the Cloudflare logo are trademarks of Cloudflare, Inc. This
project is not affiliated with or endorsed by Cloudflare, Inc.

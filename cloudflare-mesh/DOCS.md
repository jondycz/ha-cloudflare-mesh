# Cloudflare Mesh

This app runs a Cloudflare One Mesh connector on your Home Assistant host. It
uses Cloudflare's official `cloudflare/mesh` container image and applies the
same runtime requirements as the official Docker Compose example.

## Prerequisites

- A Cloudflare One account with Cloudflare WAN enabled.
- A Mesh node created in the Cloudflare dashboard.
- The token generated for that Mesh node.
- A Home Assistant host with `/dev/net/tun` available.

## Configuration

### Mesh node token

Paste the token generated for the node in the Cloudflare dashboard into
`mesh_node_token`. The token is stored as a password field by Home Assistant
and passed to the connector as `MESH_NODE_TOKEN`.

Create a separate node and token for each connector installation. If a token
is exposed, rotate it in Cloudflare and update this app before restarting it.

### Source NAT

`srcnat_enabled` controls Cloudflare Mesh source NAT and defaults to `true`,
matching the official Compose example. Disable it only when your Cloudflare
routing design requires original source addresses and return routes are
configured correctly.

## Runtime access

The app requires the following elevated container access:

- `/dev/net/tun`
- `NET_ADMIN`
- `NET_RAW`
- IPv4 and IPv6 forwarding in the app network namespace

Cloudflare connector state is persisted at `/var/lib/cloudflare-warp` and is
included in Home Assistant app backups.

## Troubleshooting

After starting the app, inspect its log for registration or routing errors. A
failure to open the TUN device usually means `/dev/net/tun` is unavailable on
the host. Authentication failures generally indicate an expired, revoked, or
incorrect Mesh node token.

When changing the token or source NAT setting, restart the app so the official
Cloudflare entrypoint receives the new environment.

## Support boundary

This repository packages the official image but does not implement the Mesh
connector itself. Connector behavior and Cloudflare WAN configuration are
documented and supported by Cloudflare.

# Cloudflare Mesh

Runs the official [Cloudflare Mesh node](https://developers.cloudflare.com/mesh/guides/run-mesh-in-containers/)
container on your Home Assistant host.

## Before you start

1. Configure the [required Mesh account settings](https://developers.cloudflare.com/mesh/get-started/#required-account-settings)
   in Cloudflare One.
2. In the Cloudflare dashboard, go to **Networking** > **Mesh** and add a node.
3. Copy the node token.

## Configuration

| Option | Description |
| --- | --- |
| `mesh_node_token` | Token of the Mesh node. Use a separate node and token for each installation. |
| `srcnat_enabled` | Source NAT for traffic forwarded to your local network (default `true`). Disable it only if your network has return routes to `100.96.0.0/12`. See [Source NAT](https://developers.cloudflare.com/mesh/guides/run-mesh-in-containers/#source-nat). |

Restart the app after changing an option.

To make a local subnet reachable through this node, add a
[route](https://developers.cloudflare.com/mesh/features/routes/) in Cloudflare.

## Troubleshooting

- Check the app log. The node should register and report as connected.
- An invalid or revoked token prevents registration. Create a new token and
  update `mesh_node_token`.
- The node must show as **Online** in the Cloudflare dashboard. See the
  [Mesh troubleshooting guide](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-mesh/get-started/#troubleshooting).

Connector behavior and Cloudflare configuration are supported by Cloudflare.
This app only packages the official image.

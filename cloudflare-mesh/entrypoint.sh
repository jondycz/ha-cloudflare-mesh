#!/bin/sh

set -e

OPTIONS_FILE="/var/lib/cloudflare-warp/options.json"

if [ ! -f "$OPTIONS_FILE" ]; then
    echo "[ERROR] Home Assistant app configuration not found: $OPTIONS_FILE" >&2
    exit 1
fi

MESH_NODE_TOKEN="$(jq -r '.mesh_node_token // empty' "$OPTIONS_FILE")"
SRCNAT_ENABLED="$(jq -r '.srcnat_enabled // false' "$OPTIONS_FILE")"

if [ -z "$(printf '%s' "$MESH_NODE_TOKEN" | tr -d '[:space:]')" ]; then
    echo "[ERROR] mesh_node_token must be configured before the app can start" >&2
    exit 1
fi

export MESH_NODE_TOKEN
export SRCNAT_ENABLED

echo "[INFO] Enabling IP forwarding"

sysctl -w net.ipv4.ip_forward=1
sysctl -w net.ipv6.conf.all.forwarding=1
sysctl -w net.ipv6.conf.default.forwarding=1

echo "[INFO] Starting Cloudflare Mesh"

exec /entrypoint
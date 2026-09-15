#!/bin/sh

set -e

OPTIONS_FILE="/var/lib/cloudflare-warp/options.json"

if [ ! -f "$OPTIONS_FILE" ]; then
    echo "[ERROR] Home Assistant app configuration not found: $OPTIONS_FILE" >&2
    exit 1
fi

MESH_NODE_TOKEN="$(sed -n 's/.*"mesh_node_token"[[:space:]]*:[[:space:]]*"\([^"]*\)".*/\1/p' "$OPTIONS_FILE")"
SRCNAT_ENABLED="$(sed -n 's/.*"srcnat_enabled"[[:space:]]*:[[:space:]]*\(true\|false\).*/\1/p' "$OPTIONS_FILE")"

if [ -z "$(printf '%s' "$MESH_NODE_TOKEN" | tr -d '[:space:]')" ]; then
    echo "[ERROR] mesh_node_token must be configured before the app can start" >&2
    exit 1
fi

[ -n "$SRCNAT_ENABLED" ] || SRCNAT_ENABLED="false"

export MESH_NODE_TOKEN
export SRCNAT_ENABLED

exec /entrypoint
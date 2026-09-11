# Cloudflare Mesh

Home Assistant app that runs the official Cloudflare One Mesh connector image.

The app maps `/dev/net/tun`, grants the required `NET_ADMIN` and `NET_RAW`
capabilities, enables IPv4 and IPv6 forwarding, and persists Cloudflare state
across restarts.

See `DOCS.md` for installation and configuration details.

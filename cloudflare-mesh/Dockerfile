FROM golang:1.25-alpine AS launcher-build

ARG TARGETARCH

WORKDIR /build
COPY launcher.go .
RUN CGO_ENABLED=0 GOOS=linux GOARCH="${TARGETARCH}" go build -trimpath -ldflags="-s -w" -o /ha-launcher launcher.go

FROM cloudflare/mesh:latest

USER root
# Install iptables (trying both apk and apt-get to be safe against base image changes)
RUN (apt-get update && apt-get install -y iptables) || apk add --no-cache iptables

ARG BUILD_VERSION
ARG TARGETARCH

LABEL \
    io.hass.name="Cloudflare Mesh" \
    io.hass.description="Cloudflare One Mesh connector for Home Assistant" \
    io.hass.type="app" \
    io.hass.version="${BUILD_VERSION}" \
    io.hass.arch="${TARGETARCH}"

COPY --from=launcher-build /ha-launcher /ha-launcher

ENTRYPOINT ["/ha-launcher"]

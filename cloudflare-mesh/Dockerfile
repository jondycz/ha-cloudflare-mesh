FROM cloudflare/mesh:latest

USER root

ARG BUILD_VERSION
ARG TARGETARCH

LABEL \
    io.hass.name="Cloudflare Mesh" \
    io.hass.description="Cloudflare One Mesh connector for Home Assistant" \
    io.hass.type="app" \
    io.hass.version="${BUILD_VERSION}" \
    io.hass.arch="${TARGETARCH}"

COPY entrypoint.sh /entrypoint.sh

RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
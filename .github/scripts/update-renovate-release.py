#!/usr/bin/env python3

import re
from pathlib import Path


DOCKERFILE = Path("cloudflare-mesh/Dockerfile")
CONFIG = Path("cloudflare-mesh/config.yaml")
CHANGELOG = Path("cloudflare-mesh/CHANGELOG.md")


def get_base_image_version() -> str:
    text = DOCKERFILE.read_text()

    match = re.search(
        r"^FROM\s+cloudflare/mesh:(?P<version>[^\s]+)\s*$",
        text,
        re.MULTILINE,
    )

    if not match:
        raise RuntimeError(
            f"Could not find cloudflare/mesh version in {DOCKERFILE}"
        )

    version = match.group("version")

    if version == "latest":
        raise RuntimeError(
            "Dockerfile still uses cloudflare/mesh:latest"
        )

    return version


def get_app_version() -> tuple[int, int, int]:
    text = CONFIG.read_text()

    match = re.search(
        r"^version:\s*(?P<major>\d+)\.(?P<minor>\d+)\.(?P<patch>\d+)\s*$",
        text,
        re.MULTILINE,
    )

    if not match:
        raise RuntimeError(f"Could not find version in {CONFIG}")

    return (
        int(match.group("major")),
        int(match.group("minor")),
        int(match.group("patch")),
    )


def set_app_version(version: str) -> None:
    text = CONFIG.read_text()

    updated, count = re.subn(
        r"^version:\s*\d+\.\d+\.\d+\s*$",
        f"version: {version}",
        text,
        count=1,
        flags=re.MULTILINE,
    )

    if count != 1:
        raise RuntimeError(f"Could not update version in {CONFIG}")

    CONFIG.write_text(updated)


def update_changelog(version: str, image_version: str) -> None:
    text = CHANGELOG.read_text()

    if f"Updated the Cloudflare Mesh base image to `{image_version}`." in text:
        return

    if not text.startswith("# Changelog"):
        raise RuntimeError(
            f"{CHANGELOG} does not start with '# Changelog'"
        )

    entry = (
        "# Changelog\n\n"
        f"## {version}\n\n"
        f"- Updated the Cloudflare Mesh base image to `{image_version}`.\n"
    )

    remainder = text[len("# Changelog"):].lstrip("\n")

    CHANGELOG.write_text(entry + "\n" + remainder)


def main() -> None:
    image_version = get_base_image_version()

    major, minor, patch = get_app_version()
    new_version = f"{major}.{minor}.{patch + 1}"

    set_app_version(new_version)
    update_changelog(new_version, image_version)

    print(f"Cloudflare Mesh: {image_version}")
    print(f"Application version: {new_version}")


if __name__ == "__main__":
    main()
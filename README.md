# ooboundary: Sovereign EGRESS BOUNDARY

<div align="center">

```
================================================================================
                                ooboundary
               Sovereign openOODA EGRESS BOUNDARY
================================================================================
```

**Sovereign EGRESS BOUNDARY**  
*Hardware enforced kernel netfilter hook restricting agent sockets to allowed IPs.*  
*Two Faces, One Engine:* Modern terminal ergonomics for humans • Zero-leakage MCP for AI agents  
Written in 100% pure [openOODA](https://github.com/openOODA).

[![License: Apache-2.0](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![openOODA](https://img.shields.io/badge/openOODA-1.0-emerald.svg)](https://openooda.org)
[![Architecture: x86_64 | aarch64](https://img.shields.io/badge/Arch-x86__64%20%7C%20aarch64-lightgrey.svg)]()

</div>

---

## 1. Quick Install

### Automated Installer (Linux x86_64 & aarch64)
```bash
curl -fsSL https://openooda-tools.github.io/ooboundary/install.sh | bash
```

### Native Package Managers
```bash
# Arch Linux (AUR / PKGBUILD)
yay -S ooboundary-bin
# Or manual PKGBUILD:
cd packaging/arch && makepkg -si

# Debian / Ubuntu (.deb)
curl -fsSL https://openooda-tools.github.io/ooboundary/install.sh | bash -s -- --deb

# Fedora / RHEL (.rpm)
curl -fsSL https://openooda-tools.github.io/ooboundary/install.sh | bash -s -- --rpm
```

### Uninstallation
```bash
ooboundary-uninstall
# or: curl -fsSL https://openooda-tools.github.io/ooboundary/uninstall.sh | bash
```

---

## 2. CLI Usage

```
usage: ooboundary [options] [ALLOWED_IP_OR_CIDR...]

Hardware enforced kernel netfilter hook restricting agent sockets to allowed IPs.

Options:
  -P, --profile <NAME>   preset profile: isolated, local, strict [default: strict]
  -a, --allow <IP/CIDR>  permit outbound traffic to destination IP or CIDR block
  -p, --port <PORT>      permit outbound traffic to destination port
      --format <MODE>    output format: full, systemd, nftables [default: full]
      --audit            audit egress boundary against negative-trust baselines
      --json             output formatted as JSON Lines
      --color <WHEN>     colorize output: auto, always, never [default: auto]
      --mcp              run as Model Context Protocol stdio server
  -h, --help             display this help and exit
  -v, --version          output version information and exit
```

---

## 3. Theming Integration (`oote`)

`ooboundary` synchronizes visual styles and status colors with [oote](https://github.com/openOODA-tools/oote):
* **Configuration:** Reads active palette from `~/.openooda/theme.oot`.
* **Environment Overrides:** Respects `$OODA_THEME` and `$NO_COLOR`.

---

## 4. Model Context Protocol (MCP)

When invoked with `--mcp`, `ooboundary` runs a JSON-RPC 2.0 stdio server providing structured tools for AI coding agents:

* **`boundary_profile`**: Lists standard egress boundary profiles (`isolated`, `local`, `strict`).
* **`boundary_generate`**: Synthesizes systemd drop-in network confinement directives and nftables kernel rules.
* **`boundary_audit`**: Audits destination addresses and egress policies against data exfiltration risks.
* **`boundary_stats`**: Queries socket boundary status, nftables capabilities, and platform features.

```bash
ooboundary --mcp
```

---

## 5. Security & Zero Ambient Authority

* **Pure Capability Bounded:** Operates strictly with explicit tokens (&FsReadCap, &ProcessCap, &EnvCap, &McpCap). Physical absence of ambient disk/net leakage.
* **Negative-Trust Architecture:** Strict input validation and operational limits.
* **Hermetic Binary:** Standalone zero-dependency executable.

---

## 6. License

Apache License, Version 2.0. See [LICENSE](LICENSE) for details.

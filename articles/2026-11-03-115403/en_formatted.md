# Minimalist NixOS: Ultra-Low RAM Optimization Guide

*Insert header image here*

Unlock NixOS’s hidden efficiency! Learn how to strip unnecessary bloat, reduce RAM usage by **50%+**, and run a near-zero-footprint system—ideal for Raspberry Pi, VPS, or embedded deployments. Actionable tips for developers and sysadmins alike.

## 🔑 The Core of This Topic
NixOS is renowned for reproducibility and declarative configuration, but its default footprint can be **unnecessarily heavy** for constrained environments. This guide dives into **hardware-level optimizations**, **configuration tweaks**, and **runtime adjustments** to shrink NixOS’s RAM usage to **under 100MB** while retaining core functionality. The goal? A **minimalist, ultra-lightweight** system that runs efficiently on **32MB RAM** or even **embedded devices** like the Raspberry Pi Zero.

## ⚡ 5-Second Key Points
- **Use `nixos-rebuild switch --keep-going`** to avoid unnecessary rebuilds that bloat `/var` and `/nix/store`.
- **Disable `systemd` services** like `systemd-journald`, `systemd-networkd`, and `systemd-logind` via `services.systemd.journald.enable = null`.
- **Replace `systemd` with `runit` or `openrc`** to cut RAM usage by **~30-50MB** while maintaining stability.
- **Strip all unnecessary packages**—even `bash` and `coreutils` can be replaced with **BusyBox** or **minimal alternatives**.
- **Enable `nix` garbage collection** (`nix-collect-garbage`) **daily** to prevent `/nix/store` bloat.

## 📈 Detailed Breakdown
**Element 1: Strip the Systemd Overhead**
Systemd is a powerful but **RAM-hungry** init system. Even in minimal setups, it consumes **~50-100MB** just for basic services. Replace it with **runit** or **openrc** by setting:
services.runit.enable = true;
services.systemd.enable = false;
This alone can **halve your RAM usage** while keeping the system functional. For even lighter alternatives, consider **BusyBox’s `runit`** or **s6**, which are **~10MB lighter** than runit.

> 💡 **Insight**: *Systemd’s journaling and dependency management are often unnecessary for headless or embedded systems. Disable them entirely unless logging is critical.*

**Element 2: Replace Heavy Utilities with Minimal Alternatives**
Many default NixOS packages (e.g., `bash`, `vim`, `openssh`) are **overkill** for minimal setups. Replace them with:
- **BusyBox** (`busybox`) for core utilities (e.g., `busybox-suid` provides `/bin/sh`).
- **MicroSSH** (`microssh`) instead of OpenSSH (~**20MB saved**).
- **Dmenu** (`dmenu`) for window switching (~**1MB** vs. `rofi`).

Example:
environment.systemPackages = with pkgs; [ busybox microssh dmenu ];
Even **replacing `coreutils` with `coreutils-light`** can save **~15MB**.

> 💡 **Insight**: *NixOS’s `pkgs.minimal` collection is a great starting point—it includes only the essentials. Build upon it rather than default configurations.*

**Element 3: Disable Unused Services and Daemons**
Every enabled service in `configuration.nix` consumes RAM. **Disable these by default**:
- `systemd-journald` (use `rsyslog` instead if logging is needed).
- `systemd-networkd` (replace with `dhcpcd` or `wpa_supplicant`).
- `systemd-logind` (not needed for headless systems).
- `avahi-daemon` (unless mDNS is critical).

Example:
services.journald.enable = null;
services.networkmanager.enable = null;
services.dhcpcd.enable = true;

**Element 4: Optimize the Nix Store**
The `/nix/store` directory can grow **uncontrollably**, bloating RAM usage. **Mitigate this with**:
- **Daily garbage collection**: Add a cron job:
    nix-collect-garbage -d
  - **Use `nix-shell --pure`** to avoid polluting the store with temporary packages.
- **Limit store size** with:
    nix.storeMaxSize = 2 GB;
  
> 💡 **Insight**: *NixOS’s `nix` daemon (`nix-daemon`) can be **disabled entirely** if you’re using `nix-shell` directly, saving **~20MB** of RAM.*

**Element 5: Use a Minimal Kernel and Root Filesystem**
- **Compile a stripped-down kernel** with only essential drivers (e.g., `CONFIG_NETFILTER_XT_MATCH_MAC` disabled).
- **Use `ext4` instead of `btrfs`** (lower overhead).
- **Enable `zram`** for swap compression (reduces RAM pressure on low-memory systems).

Example kernel config tweaks:
kernelParams = [

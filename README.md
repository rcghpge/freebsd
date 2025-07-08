FreeBSD Source Tree
==============
[![Cross-build Kernel](https://github.com/rcghpge/freebsd/actions/workflows/cross-bootstrap-tools.yml/badge.svg)](https://github.com/rcghpge/freebsd/actions/workflows/cross-bootstrap-tools.yml)
[![Bandit](https://github.com/rcghpge/freebsd/actions/workflows/bandit.yml/badge.svg)](https://github.com/rcghpge/freebsd/actions/workflows/bandit.yml)[![CodeQL](https://github.com/rcghpge/freebsd/actions/workflows/github-code-scanning/codeql/badge.svg)](https://github.com/rcghpge/freebsd/actions/workflows/github-code-scanning/codeql)[![pages-build-deployment](https://github.com/rcghpge/freebsd/actions/workflows/pages/pages-build-deployment/badge.svg)](https://github.com/rcghpge/freebsd/actions/workflows/pages/pages-build-deployment)
[![Dependabot Updates](https://github.com/rcghpge/freebsd/actions/workflows/dependabot/dependabot-updates/badge.svg)](https://github.com/rcghpge/freebsd/actions/workflows/dependabot/dependabot-updates)

This repository tracks the official FreeBSD source tree and serves as a base for fostering base system research and development in the OSS community and FreeBSD community.

FreeBSD is a modern operating system used to power servers, desktops, and embedded platforms worldwide. Developed by a dedicated community for over thirty years, it is recognized for its advanced networking, security, and storage capabilities.

---

## 📄 Copyright

See [COPYRIGHT](COPYRIGHT) for overall copyright information.  
Additional licensing details may be found in specific source subdirectories.

---

## ⚙️ Building FreeBSD

The top-level `Makefile` supports various build targets, allowing you to build individual components or the entire system.

- See [build(7)](https://man.freebsd.org/build/7), [config(8)](https://man.freebsd.org/config/8), and these handbook sections:
  - [Building userland](https://docs.freebsd.org/en/books/handbook/cutting-edge/#makeworld)
  - [Building and configuring kernels](https://docs.freebsd.org/en/books/handbook/kernelconfig/)

---

## 🖥️ Supported Platforms

For details on CPU architectures and supported platforms, see the [FreeBSD Platforms page](https://www.freebsd.org/platforms/).

---

## 💽 Official Releases

Official bootable images can be found on the [FreeBSD release page](https://download.freebsd.org/ftp/releases/ISO-IMAGES/).

---

## 🗺️ Source Tree Roadmap

| Directory  | Description                                                                           |
|-------------|---------------------------------------------------------------------------------------|
| `bin`       | Core system/user commands.                                                           |
| `cddl`      | Commands and libraries under the Common Development and Distribution License (CDDL). |
| `contrib`   | Third-party contributed packages.                                                    |
| `crypto`    | Cryptographic components ([crypto/README](crypto/README)).                           |
| `etc`       | Templates and default configuration files for `/etc`.                                |
| `gnu`       | GPL- or LGPL-licensed commands and libraries ([COPYING](gnu/COPYING)).              |
| `include`   | System-wide include files.                                                           |
| `kerberos5` | Heimdal Kerberos 5 package.                                                          |
| `lib`       | System libraries.                                                                    |
| `libexec`   | System daemons and utility executables.                                              |
| `release`   | Release build system and related tools.                                              |
| `rescue`    | Build system for statically linked `/rescue` utilities.                              |
| `sbin`      | System-level commands.                                                               |
| `secure`    | Cryptographic libraries and utilities.                                               |
| `share`     | Shared resources and data files.                                                     |
| `stand`     | Boot loader sources.                                                                 |
| `sys`       | Kernel sources ([sys/README.md](sys/README.md)).                                     |
| `targets`   | Experimental `DIRDEPS_BUILD` support.                                               |
| `tests`     | Regression tests (see [tests/README](tests/README)).                                |
| `tools`     | Tools for testing, development, and miscellaneous tasks.                             |
| `usr.bin`   | User-level commands.                                                                 |
| `usr.sbin`  | System administration commands.                                                      |

---

## 🔄 Contributing & Upstream

This repository tracks FreeBSD development and can be used as a base for future upstream contributions.

For official contribution guidelines and ways to get involved, see the [FreeBSD Community page](https://www.freebsd.org/community/).

---

# Package Manager Builders

> *One script to install them all — the essential Windows package managers and dev toolchains.*

A PowerShell-driven Python script that installs and verifies the four major Windows package managers (WinGet, Chocolatey, Scoop, PowerShellGet) plus popular development toolchains (Node.js, Rust, vcpkg) — all from a single interactive menu.

## 🎯 Features

- **WinGet Verification** — Re-registers the built-in Windows package manager if needed
- **Chocolatey** — Installs the veteran community package manager
- **Scoop** — Sets up the portable, user-level developer tool manager
- **PowerShellGet** — Updates the native PowerShell module manager
- **Dev Toolchains** — Optional installation of Node.js (npm), Rust (Cargo), and vcpkg (C++)
- **Interactive Menu** — Pick individual tools or install all at once

## 🛠️ Requirements

- **Windows 10/11**
- **Administrative Terminal** — Must run as Administrator
- **Python 3.x** — Required to execute the installer script
- **PowerShell 5.1+** — Pre-installed on all supported Windows versions

## 📁 Project Structure

```text
packagemanger builders/
├── install_managers.py   # Main installer script with interactive menu
└── README.md
```

## 🚀 Getting Started

### Run the Installer

```powershell
# Open PowerShell or Terminal as Administrator
# Then run:

python install_managers.py
```

You'll see an interactive menu:

```
========================================================
  Windows Package Manager Installer
========================================================

  Available tasks:
    [1] WinGet
    [2] Chocolatey
    [3] Scoop
    [4] PowerShellGet
    [5] Node.js (npm)
    [6] Rust (Cargo)
    [7] vcpkg
    [A] Install ALL
    [0] Exit

  Choice:
```

### What Each Option Does

| # | Tool | What It Provides |
|---|---|---|
| 1 | **WinGet** | Native Windows package manager (`winget install ...`) |
| 2 | **Chocolatey** | Community package repository (`choco install ...`) |
| 3 | **Scoop** | Portable dev tools, no admin required (`scoop install ...`) |
| 4 | **PowerShellGet** | PowerShell module management (`Install-Module ...`) |
| 5 | **Node.js (npm)** | JavaScript runtime + npm package manager |
| 6 | **Rust (Cargo)** | Systems programming language + Cargo build tool |
| 7 | **vcpkg** | C/C++ library manager from Microsoft |

### After Installation

**Important:** Close and restart your terminal for the new commands (`choco`, `scoop`, `npm`, `cargo`, `vcpkg`) to be recognized in your PATH.

## ⚠️ Important Notes

- Always run from an **Administrative Terminal**
- The script uses `Set-ExecutionPolicy Bypass -Scope Process` to avoid permanent policy changes
- Each installer downloads from its official source (chocolatey.org, get.scoop.sh, rust-lang.org, aka.ms)

---

*Built for rapid Windows development environment setup.*

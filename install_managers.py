"""Windows Package Manager Installation Script (2026 Edition)

Installs the four major Windows package managers:
  - WinGet (pre-installed on Win 10/11; verifies registration)
  - Chocolatey (veteran community package manager)
  - Scoop (portable developer tools)
  - PowerShellGet (native module manager)

IMPORTANT: Run this script from an Administrative Terminal.
"""

import subprocess
import sys


def run_powershell(command: str, desc: str) -> bool:
    """Execute a PowerShell command and report success / failure."""
    print(f"\n>>> {desc}...")
    full_cmd = f"Set-ExecutionPolicy Bypass -Scope Process -Force; {command}"
    try:
        result = subprocess.run(
            ["powershell", "-Command", full_cmd],
            capture_output=False,
            text=True,
        )
        if result.returncode == 0:
            print(f"--- SUCCESS: {desc} ---")
            return True
        else:
            print(f"--- ERROR: {desc} failed (exit {result.returncode}) ---")
            return False
    except Exception as e:
        print(f"--- EXCEPTION: {e} ---")
        return False


def install_winget() -> None:
    """WinGet is pre-installed on modern Windows; verify / re-register."""
    print("\n--- Verifying / Installing WinGet ---")
    cmd = (
        "Add-AppxPackage -RegisterByFamilyName "
        "-MainPackage Microsoft.DesktopAppInstaller_8wekyb3d8bbwe"
    )
    run_powershell(cmd, "WinGet registration")


def install_chocolatey() -> None:
    """Install Chocolatey package manager."""
    print("\n--- Installing Chocolatey ---")
    cmd = (
        "[System.Net.ServicePointManager]::SecurityProtocol = "
        "[System.Net.ServicePointManager]::SecurityProtocol -bor 3072; "
        "iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))"
    )
    run_powershell(cmd, "Chocolatey Installation")


def install_scoop() -> None:
    """Install Scoop — portable user-level package manager."""
    print("\n--- Installing Scoop ---")
    cmd = (
        "Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser; "
        "iwr -useb get.scoop.sh | iex"
    )
    run_powershell(cmd, "Scoop Installation")


def install_powershell_get() -> None:
    """Update the native PowerShellGet module manager."""
    print("\n--- Updating PowerShellGet ---")
    cmd = "Install-Module -Name PowerShellGet -Force -AllowClobber"
    run_powershell(cmd, "PowerShellGet Update")


# ── Dev-tool installers (optional) ────────────────────────────────────────────

def install_npm_via_winget() -> None:
    """Install Node.js LTS (includes npm) via WinGet."""
    print("\n--- Installing Node.js LTS (npm) via WinGet ---")
    cmd = (
        "winget install OpenJS.NodeJS.LTS "
        "--accept-source-agreements --accept-package-agreements"
    )
    run_powershell(cmd, "Node.js LTS (npm)")


def install_cargo() -> None:
    """Install Rust toolchain (rustup + cargo)."""
    print("\n--- Installing Rust (cargo) via Rustup ---")
    cmd = (
        "Invoke-WebRequest -Uri "
        "https://static.rust-lang.org/rustup/dist/x86_64-pc-windows-msvc/rustup-init.exe "
        "-OutFile rustup-init.exe; "
        "./rustup-init.exe -y --no-modify-path; "
        "Remove-Item rustup-init.exe"
    )
    run_powershell(cmd, "Rust (Cargo)")


def install_vcpkg() -> None:
    """Install vcpkg C++ library manager."""
    print("\n--- Installing vcpkg ---")
    cmd = "iex (iwr -useb https://aka.ms/vcpkg-init.ps1)"
    run_powershell(cmd, "vcpkg")


# ── Main ──────────────────────────────────────────────────────────────────────

ALL_TASKS = [
    ("WinGet", install_winget),
    ("Chocolatey", install_chocolatey),
    ("Scoop", install_scoop),
    ("PowerShellGet", install_powershell_get),
    ("Node.js (npm)", install_npm_via_winget),
    ("Rust (Cargo)", install_cargo),
    ("vcpkg", install_vcpkg),
]


def main() -> None:
    print("=" * 56)
    print("  Windows Package Manager Installer")
    print("=" * 56)
    print()
    print("  Available tasks:")
    for i, (name, _) in enumerate(ALL_TASKS, 1):
        print(f"    [{i}] {name}")
    print(f"    [A] Install ALL")
    print(f"    [0] Exit")
    print()

    choice = input("  Choice: ").strip()

    if choice.upper() == "A":
        for name, func in ALL_TASKS:
            func()
    elif choice == "0":
        print("  Exiting.")
        sys.exit(0)
    elif choice.isdigit() and 1 <= int(choice) <= len(ALL_TASKS):
        name, func = ALL_TASKS[int(choice) - 1]
        func()
    else:
        print("  Invalid choice.")
        sys.exit(1)

    print("\n" + "=" * 56)
    print("  Done. Restart your terminal for changes to take effect.")
    print("=" * 56)


if __name__ == "__main__":
    main()

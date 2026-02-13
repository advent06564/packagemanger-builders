import subprocess
import sys

def run_powershell(command, as_admin=False):
    """Executes a command via PowerShell."""
    prefix = ""
    if as_admin:
        # Note: This checks if the current script is admin, it doesn't elevate on its own
        print(f"Running command: {command}")
    
    try:
        # Set execution policy to bypass for the duration of the command execution
        full_command = f"Set-ExecutionPolicy Bypass -Scope Process -Force; {command}"
        result = subprocess.run(["powershell", "-Command", full_command], capture_output=True, text=True, check=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {e.stderr}")

def install_winget():
    """WinGet is usually pre-installed; this forces registration if missing."""
    print("--- Verifying/Installing WinGet ---")
    cmd = "Add-AppxPackage -RegisterByFamilyName -MainPackage Microsoft.DesktopAppInstaller_8wekyb3d8bbwe"
    run_powershell(cmd)

def install_chocolatey():
    """Installs the Chocolatey veteran package manager."""
    print("--- Installing Chocolatey ---")
    cmd = "[System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))"
    run_powershell(cmd)

def install_scoop():
    """Installs Scoop for portable developer tools."""
    print("--- Installing Scoop ---")
    # Scoop requires a slightly different execution policy setup for the current user
    cmd = "Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser; iwr -useb get.scoop.sh | iex"
    run_powershell(cmd)

def install_powershell_get():
    """Updates the native PowerShell module manager."""
    print("--- Updating PowerShellGet ---")
    cmd = "Install-Module -Name PowerShellGet -Force -AllowClobber"
    run_powershell(cmd)

if __name__ == "__main__":
    print("Windows Package Manager Installation Script (2025 Edition)")
    print("IMPORTANT: Run this script from an Administrative Terminal.")
    
    # Sequential installation of the primary managers
    install_winget()
    install_chocolatey()
    install_scoop()
    install_powershell_get()
    
    print("\nAll tasks completed. Please restart your terminal for environment changes to take effect.")
import subprocess
import os

def run_powershell(command, desc):
    """Utility to run PowerShell commands and handle output."""
    print(f"\n>>> Starting: {desc}...")
    # Set execution policy to bypass temporarily for the current session
    full_cmd = f"Set-ExecutionPolicy Bypass -Scope Process -Force; {command}"
    try:
        result = subprocess.run(["powershell", "-Command", full_cmd], capture_output=False, text=True)
        if result.returncode == 0:
            print(f"--- SUCCESS: {desc} complete ---")
        else:
            print(f"--- ERROR: {desc} failed with exit code {result.returncode} ---")
    except Exception as e:
        print(f"--- EXCEPTION: {e} ---")

def install_scoop():
    """Installs Scoop for portable user-level tools."""
    # Scoop technically prefers non-admin, but can be installed via admin if needed
    cmd = "Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser; iwr -useb get.scoop.sh | iex"
    run_powershell(cmd, "Scoop Installation")

def install_npm_via_winget():
    """Installs Node.js (which includes NPM) using the native WinGet."""
    # Using Node.js LTS for stability in 2025
    cmd = "winget install OpenJS.NodeJS.LTS --accept-source-agreements --accept-package-agreements"
    run_powershell(cmd, "NPM (Node.js) via WinGet")

def install_cargo_rust():
    """Installs Rustup, which manages Rust and Cargo."""
    # Downloads the rustup-init and runs it silently with defaults
    cmd = "Invoke-WebRequest -Uri https://static.rust-lang.org/rustup/dist/x86_64-pc-windows-msvc/rustup-init.exe -OutFile rustup-init.exe; ./rustup-init.exe -y --no-modify-path; Remove-Item rustup-init.exe"
    run_powershell(cmd, "Cargo (Rust) via Rustup")

def install_vcpkg():
    """Installs vcpkg for C++ library management."""
    # Uses the official Microsoft initialization script for 2025
    cmd = "iex (iwr -useb https://aka.ms/vcpkg-init.ps1)"
    run_powershell(cmd, "vcpkg C++ Manager")

if __name__ == "__main__":
    print("====================================================")
    print("Windows Development Package Manager Installer (2025)")
    print("====================================================\n")

    # 1. Install Scoop
    install_scoop()

    # 2. Install NPM (Node.js)
    install_npm_via_winget()

    # 3. Install Cargo (Rust)
    install_cargo_rust()

    # 4. Install vcpkg
    install_vcpkg()

    print("\n" + "="*50)
    print("INSTALLATION COMPLETE.")
    print("IMPORTANT: You MUST close and restart your terminal for")
    print("the new commands (scoop, npm, cargo, vcpkg) to be recognized.")
    print("="*50)

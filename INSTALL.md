# Complete Installation Guide for SurfMap

## Quick Start

The easiest way to get SurfMap running:

```bash
pip install surfmap
```

Then run:
```bash
surfmap -u example.com -h
```

## Prerequisites

- **Python**: 3.7 or higher
- **Go**: 1.16 or higher (for installing Go-based reconnaissance tools)
- **Bash/Shell**: For running shell commands (Linux/macOS) or PowerShell/CMD (Windows)

## Installation Methods

### Method 1: PyPI Installation (Recommended)

Install directly from Python Package Index:

```bash
pip install surfmap
```

Update to the latest version:
```bash
pip install --upgrade surfmap
```

### Method 2: Install from GitHub (Latest Development Version)

```bash
git clone https://github.com/yourusername/surfmap.git
cd surfmap
pip install -e .
```

The `-e` flag installs in "editable" mode, allowing you to modify the code and see changes immediately.

### Method 3: Manual Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/surfmap.git
cd surfmap
```

2. Install the package:
```bash
python -m pip install .
```

## Setting Up External Reconnaissance Tools

SurfMap requires several external tools for full functionality. These are NOT automatically installed with pip.

### 1. Install Go (if not already installed)

**macOS** (using Homebrew):
```bash
brew install go
```

**Linux** (Ubuntu/Debian):
```bash
sudo apt-get update
sudo apt-get install golang-go
```

**Windows**:
Download and install from [golang.org](https://golang.org/)

### 2. Install Go-based Tools

Add Go binaries to your PATH, then run:

```bash
# Subfinder - Subdomain enumeration
go install github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest

# Assetfinder - Asset discovery
go install github.com/tomnomnom/assetfinder@latest

# GAU - URL collection
go install github.com/lc/gau/v2/cmd/gau@latest

# Waybackurls - Wayback Machine URL discovery
go install github.com/tomnomnom/waybackurls@latest

# Katana - Web crawler
go install github.com/projectdiscovery/katana/cmd/katana@latest

# HTTPX - HTTP probe tool
go install github.com/projectdiscovery/httpx/cmd/httpx@latest
```

Ensure your Go bin directory is in your PATH:
```bash
export PATH="$HOME/go/bin:$PATH"
```

### 3. Install Python-based Tools

```bash
pip install arjun
```

### 4. (Optional) Install JavaScript Analysis Tools

For enhanced JavaScript endpoint extraction:

```bash
# LinkFinder
git clone https://github.com/GerbenJavado/LinkFinder.git ~/tools/LinkFinder
cd ~/tools/LinkFinder
pip install -r requirements.txt

# JSParser
git clone https://github.com/nahamsec/JSParser.git ~/tools/JSParser

# xnLinkFinder
go install github.com/xnLinkFinder/xnLinkFinder@latest
```

## Verify Installation

Test that everything is installed correctly:

```bash
# Check SurfMap version
surfmap -h

# Check external tools
which subfinder
which assetfinder
which gau
which waybackurls
which katana
which httpx
which arjun
```

## Troubleshooting

### Command not found: surfmap

**Solution**: Ensure pip's bin directory is in your PATH.

For Linux/macOS:
```bash
export PATH="$HOME/.local/bin:$PATH"
```

Then add to your `.bashrc`, `.zshrc`, or `.profile` for persistence.

### Missing external tools

**Solution**: Install all required Go tools as described in section 2 above.

### Permission denied errors

**Solution**: On Linux/macOS, ensure scripts are executable:
```bash
chmod +x $(which surfmap)
```

### Windows-specific issues

If you encounter issues on Windows:
- Use PowerShell instead of CMD
- Ensure Go is installed and in PATH: `go version`
- Install Windows Subsystem for Linux (WSL) for better bash compatibility

## Updating SurfMap

To update to the latest version:

```bash
pip install --upgrade surfmap
```

## Uninstalling SurfMap

```bash
pip uninstall surfmap
```

## Development Setup

For contributing or modifying the code:

1. Clone the repository:
```bash
git clone https://github.com/yourusername/surfmap.git
cd surfmap
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install in development mode with dependencies:
```bash
pip install -e .
pip install -r requirements.txt
```

---

For more information, see [README.md](README.md) or run `surfmap -h`.

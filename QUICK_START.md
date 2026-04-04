# 🚀 SurfMap Quick Start Guide

## Installation

```bash
pip install surfmap
```

For complete setup instructions including external tools, see [INSTALL.md](INSTALL.md).

## Basic Usage

### Scan a Single Domain

```bash
surfmap -u example.com
```

### Scan Multiple Domains

```bash
surfmap -f targets.txt
```

**targets.txt** should contain one domain per line:
```
example.com
test.com
another-domain.org
```

## Common Scenarios

### 1. Skip Subdomain Enumeration (faster)

Use when you want to test the target domain directly without subfinder/assetfinder:

```bash
surfmap -u example.com -skip-sub
```

### 2. Exclude Out-of-Scope Domains

Exclude specific domains from results:

```bash
# Single domain
surfmap -u example.com -skip-u internal.example.com

# Multiple domains from file
surfmap -f targets.txt -skip-f out_of_scope.txt
```

**out_of_scope.txt** example:
```
staging.example.com
test.example.com
dev.internal.com
```

### 3. Combination: Multiple targets + Exclusions

```bash
surfmap -f targets.txt -skip-f out_of_scope.txt
```

## Output

Results are saved to the `recon/` directory with this structure:

```
recon/
├── example.com/
│   ├── all_subs.txt                    # All discovered subdomains
│   ├── alive_subs.txt                  # Live/responding subdomains
│   ├── plain_domains.txt               # Clean domain list
│   ├── all_urls.txt                    # All discovered URLs
│   ├── jsfiles.txt                     # JavaScript files found
│   ├── final_endpoints.txt             # All extracted endpoints
│   ├── endpoints_with_params.txt       # Endpoints with query parameters
│   ├── arjun_params.txt                # Discovered parameters
│   └── recon_summary_TIMESTAMP.txt     # Automated summary report
└── targets_grouped/
    ├── target1/
    ├── target2/
    └── mixed/                          # Aggregated results
```

## Understanding Results

### Key Files

| File | Purpose |
|------|---------|
| `all_subs.txt` | Every subdomain discovered (raw) |
| `alive_subs.txt` | Only subdomains that responded to HTTP/HTTPS probes |
| `plain_domains.txt` | Clean list of live domains (no URLs) |
| `all_urls.txt` | Every URL found via GAU, Wayback, and Katana |
| `jsfiles.txt` | JavaScript file URLs extracted |
| `final_endpoints.txt` | All API endpoints found |
| `endpoints_with_params.txt` | Endpoints that have query parameters |
| `arjun_params.txt` | Hidden/discovered parameters |

### Using the Output

Feed results to your security testing tools:

```bash
# Fuzz endpoints with ffuf
ffuf -u http://example.com/FUZZ -w final_endpoints.txt

# Use with Burp Suite
# Import final_endpoints.txt and endpoints_with_params.txt

# Scan for vulnerabilities
# Use endpoints_with_params.txt with parameter fuzzing tools
```

## Performance Tips

### 1. Use Multiple Threads

External tools already use multithreading. For faster results on multi-core systems, results are generally optimal.

### 2. Skip Unnecessary Stages

If you only need URL enumeration:
```bash
surfmap -u example.com -skip-sub
```

### 3. Exclude Patterns Early

Use `-skip-f` with a comprehensive exclusion list to reduce noise:
```bash
surfmap -f targets.txt -skip-f exclude_patterns.txt
```

## Control During Execution

### Interrupt Options

While SurfMap is running, press `Ctrl+C` to open the interactive menu:

```
┌────────────────────────────────────────────────────────┐
│ ⚠️ Process Interrupted!                                 │
│ 'c' to restart tool | 'n' to skip | 's' to stop scan   │
└────────────────────────────────────────────────────────┘
```

- **c**: Restart current tool
- **n**: Skip current tool, continue to next
- **s**: Stop entire scan
- **Ctrl+C again**: Force exit immediately

## Help & Info

```bash
# Show full help
surfmap -h

# Show help with all options
surfmap --help
```

## Examples

### Example 1: Full Recon on a Target

```bash
surfmap -u hackerone.com
```

Runs complete pipeline: subdomains → live hosts → URLs → JS analysis → parameters

### Example 2: Batch Testing with Exclusions

```bash
surfmap -f my_targets.txt -skip-f internal_domains.txt
```

Scans all targets in `my_targets.txt` but excludes anything in `internal_domains.txt` from results.

### Example 3: Quick Check (No Subdomain Enum)

```bash
surfmap -u api.example.com -skip-sub
```

Tests the domain directly without spending time on subdomain enumeration.

## Troubleshooting

### "Missing dependencies" Error

```bash
# Install required Go tools - see INSTALL.md
go install github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest
go install github.com/tomnomnom/assetfinder@latest
go install github.com/lc/gau/v2/cmd/gau@latest
go install github.com/tomnomnom/waybackurls@latest
go install github.com/projectdiscovery/katana/cmd/katana@latest
go install github.com/projectdiscovery/httpx/cmd/httpx@latest
pip install arjun
```

### Command Not Found: surfmap

The package wasn't installed properly. Try:
```bash
pip install --upgrade surfmap
```

### Empty Results

- Verify the domain exists: `dig example.com`
- Check internet connection
- Increase wait time (some tools are slow on first run)
- Try with `-skip-sub` for faster results

---

For complete documentation, see [README.md](README.md) and [INSTALL.md](INSTALL.md)

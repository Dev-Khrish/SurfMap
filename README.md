# ⚡ SurfMap — Advanced Reconnaissance & Analysis Suite

SurfMap is a powerful, automation-driven reconnaissance framework designed for cybersecurity professionals, bug bounty hunters, and penetration testers. It automates the complete reconnaissance lifecycle — from asset discovery to parameter extraction — into a structured, efficient pipeline.

It integrates multiple industry-standard tools into a unified workflow, enabling deep attack surface mapping with minimal manual intervention.

**➡️ [Complete Installation Guide →](INSTALL.md)**

--------------------------------------------------------------------

## 🚀 Overview

SurfMap performs end-to-end reconnaissance including:

- Subdomain Enumeration
- Live Host Discovery
- URL Collection (Historical + Crawled)
- JavaScript Analysis
- Endpoint Extraction
- Parameter Discovery
- Result Aggregation
- Automated Report Generation

--------------------------------------------------------------------

## ✨ Features

🔍 Comprehensive Recon Pipeline  
Covers the entire attack surface from domains to parameters.

⚡ Multi-Tool Integration  
Uses best-in-class tools like subfinder, assetfinder, gau, katana, arjun, etc.

🧠 Smart Filtering  
Removes invalid, duplicate, and out-of-scope data automatically.

🛡️ Interactive Interrupt Handling  
Control execution flow during runtime (restart / skip / stop).

📊 Automated Reporting  
Generates clean summaries with key metrics.

📁 Structured Output  
Organizes results in a clean, per-target directory format.

--------------------------------------------------------------------

## 🧱 Workflow

SurfMap follows a modular pipeline:

1. Target Acquisition  
2. Subdomain Enumeration  
3. Live Host Discovery  
4. URL Collection  
5. JavaScript Analysis  
6. Parameter Discovery  
7. Results Aggregation  
8. Report Generation  

Each stage enriches the dataset for the next.

--------------------------------------------------------------------

## ⚙️ Requirements

### Required Tools

- subfinder  
- assetfinder  
- gau  
- waybackurls  
- katana  
- arjun  
- httpx-toolkit OR httprobe  

### Optional Tools (Recommended)

- LinkFinder  
- JSParser  
- xnLinkFinder  

### Python

- Python 3.7+  

--------------------------------------------------------------------

## 📦 Installation

### Option 1: Install from PyPI (Recommended)

```bash
pip install surfmap
```

Then run:
```bash
surfmap -u example.com
```

### Option 2: Install from Source

1. Clone the repository:

```bash
git clone https://github.com/dev-Khrish/surfmap.git
cd surfmap
```

2. Install the package in development mode:

```bash
pip install -e .
```

3. Run SurfMap:

```bash
surfmap -u example.com
```

### Required External Tools

Install these Go-based reconnaissance tools:

```bash
go install github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest  
go install github.com/tomnomnom/assetfinder@latest  
go install github.com/lc/gau/v2/cmd/gau@latest  
go install github.com/tomnomnom/waybackurls@latest  
go install github.com/projectdiscovery/katana/cmd/katana@latest  
go install github.com/projectdiscovery/httpx/cmd/httpx@latest  
```

Install Arjun (Python-based parameter discovery):

```bash
pip install arjun
```  

4. (Optional) Clone additional tools:

   ~/tools/LinkFinder  
   ~/tools/JSParser  

--------------------------------------------------------------------

## 🧪 Usage

### Basic Scan

```bash
surfmap -u example.com
```

### Skip Subdomain Enumeration

```bash
surfmap -u example.com -skip-sub
```

### Scan Multiple Targets

```bash
surfmap -f targets.txt
```

### Exclude Domains

```bash
surfmap -u example.com -skip-u test.example.com
surfmap -f targets.txt -skip-f out_of_scope.txt
```

### Display Help

```bash
surfmap -h
```  

--------------------------------------------------------------------

## 🎯 Command Line Options

### Target Options (Required)

- **-u, --url**  
  Single target domain to scan (e.g., `example.com`)

- **-f, --file**  
  Text file containing multiple domains (one per line)

### Filter Options

- **-skip-sub**  
  Skip subdomain enumeration and use target directly

- **-skip-u, --skip-url**  
  Exclude specific domain from results

- **-skip-f, --skip-file**  
  Text file with domains to exclude (one per line)

### Miscellaneous

- **-h, --help**  
  Show help menu and exit  

--------------------------------------------------------------------

## 📁 Output Structure

recon/
  example.com/
    all_subs.txt
    alive_subs.txt
    plain_domains.txt
    all_urls.txt
    jsfiles.txt
    final_endpoints.txt
    endpoints_with_params.txt
    arjun_params.txt
    recon_summary_YYYYMMDD_HHMMSS.txt
    ...other intermediate files

For multiple targets:

recon/
  targets_file_name/
    target1/
    target2/
    mixed/

--------------------------------------------------------------------

## 🔍 Module Breakdown

### Subdomain Enumeration
Tools:
- subfinder
- assetfinder

Output:
- all_subs.txt

---

### Live Host Discovery
Tools:
- httpx-toolkit / httprobe

Output:
- alive_subs.txt
- plain_domains.txt

---

### URL Collection
Tools:
- gau
- waybackurls
- katana

Output:
- all_urls.txt

---

### JavaScript Analysis
Tools:
- LinkFinder
- JSParser
- xnLinkFinder

Output:
- jsfiles.txt
- extracted endpoints

---

### Parameter Discovery
Tool:
- arjun

Output:
- arjun_params.txt

---

### Aggregation
Output:
- final_endpoints.txt
- endpoints_with_params.txt

--------------------------------------------------------------------

## 📊 Report Generation

Automatically generates:

recon_summary_<timestamp>.txt

Includes:

- Target details  
- Scan duration  
- Subdomains discovered  
- Live hosts  
- URLs collected  
- JavaScript files  
- Endpoints  
- Parameters  

--------------------------------------------------------------------

## ⚠️ Interrupt Handling

Single Ctrl+C:
→ Opens interactive menu  

Options:

c → Restart tool  
n → Skip tool  
s → Stop scan  

Double Ctrl+C:
→ Force exit  

--------------------------------------------------------------------

## 🧹 Filtering & Exclusions

Supports:

- Single domain exclusion (-skip-u)
- File-based exclusion (-skip-f)

Applies filtering across all output files.

--------------------------------------------------------------------

## 🔗 Aggregation Mode

For multi-target scans:

- Individual results per target  
- Combined dataset in "mixed" directory  

Useful for large-scale recon.

--------------------------------------------------------------------

## 🧠 Design Philosophy

- Automation-first  
- Maximum coverage  
- Clean output  
- Modular pipeline  
- Resilient execution  

--------------------------------------------------------------------

## ⚡ Example Workflow

1. Run SurfMap  
2. Analyze endpoints_with_params.txt  
3. Feed into fuzzers (ffuf, Burp Suite, etc.)  
4. Identify vulnerabilities  

--------------------------------------------------------------------

## 🚧 Limitations

- Requires external tools setup  
- Performance depends on system resources  
- Optional tools enhance coverage  

--------------------------------------------------------------------

## 🔮 Future Improvements

- Parallel execution  
- GUI interface  
- Cloud recon support  
- Built-in vulnerability scanning  

--------------------------------------------------------------------

## 👨‍💻 Author

Created by: Khrish  
Cybersecurity Specialist & VAPT Analyst  

--------------------------------------------------------------------

## 🚦 Versions
### 1.2.0
1.2.0 - Dependency setup flow refactor, Added setup mode and environment bootstrap, Removed forced reinstall flag

### 1.0.0
1.0.0 - Base Version  
1.0.1 - Few Updates  
1.0.2 - Added interactive c, s, n to Continue, Stop, Next
1.1.0 - Python Packaging Published

--------------------------------------------------------------------

## ⚖️ Disclaimer

This tool is intended for authorized security testing and educational purposes only.

Do NOT use it against systems without permission.

--------------------------------------------------------------------

## 🔐 Final Note

SurfMap is a complete reconnaissance framework built for serious security work.

Use it responsibly. Stay ethical. Stay secure.

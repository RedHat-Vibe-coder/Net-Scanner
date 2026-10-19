# Net-Scaner 🔍

![Python Version](https://img.shields.io/badge/Python-3.8%2B-blue.svg)
![Platform](https://img.shields.io/badge/Platform-Cross--Platform-brightgreen.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

**NetScan** is a lightweight, cross-platform TCP Port Scanner & Service Detector written in Python for quick network reconnaissance. It allows security enthusiasts and developers to scan common ports or custom targets with clear service identification and colorized terminal output.

---

## ✨ Features

- **Dual Scanning Modes**: Scan a curated list of popular TCP ports or target any single custom port (1–65535).
- **Flexible Target Input**: Fully supports both raw IP addresses and domain names/URLs.
- **Service Detection**: Automatically maps open ports to common network services (e.g., SSH, HTTP, MySQL).
- **Colorized Output**: Styled terminal interface powered by `colorama` for instant visual feedback.
- **Robust Error Handling**: Built-in input validation and connection timeout management.

---

## 📋 Requirements

- **Python 3.8+**
- Dependencies (`requests`, `colorama`, `beautifulsoup4`)

---

## ⚙️ Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/RedHat-Vibe-coder/NetScan.git
   cd NetScan
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

---

## 🚀 Usage

Run the tool interactively using:

```bash
python Netscan.py
```

Upon launching, you will be prompted to choose between two scanning modes.

---

### 📂 Mode Options & Examples

#### **Option 1: Default Ports (Common Services)**
Scans a pre-configured list of popular TCP ports, including:
* **21** (FTP), **22** (SSH), **23** (Telnet), **25** (SMTP), **53** (DNS), **80** (HTTP), **110** (POP3), **143** (IMAP), **443** (HTTPS), **3306** (MySQL), **3389** (RDP), **8080** (HTTP Alt).

```text
Enter Target IP or URL: scanme.nmap.org
```

#### **Option 2: Custom Port Scan**
Allows you to target any specific TCP port within the range of **1 to 65535**.

```text
Enter Target IP or URL: example.com
Enter Target Port: 443
```

---

### 💻 Sample Terminal Output

```text
PORT      NAME      STATUS

22        SSH       OPEN
80        HTTP      OPEN
443       HTTPS     OPEN
3306      MySQL     CLOSED
```

---

## 🗂️ Project Structure

```text
NetScan/
│
├── Netscan.py          # Main application script
├── requirements.txt    # Project dependencies
└── README.md           # Documentation
```

---

## 👤 Author

- **Creator**: Ravaha Rizwan
- **Version**: 1.1.0

---

## 📜 Disclaimer

This tool is created for educational purposes, learning networking concepts, and authorized testing of systems you own or have explicit permission to assess. The developer is not responsible for any misuse or unauthorized network scanning activities.

---

## 📄 License

Distributed under the [MIT License](LICENSE). Feel free to fork, modify, and improve the project.

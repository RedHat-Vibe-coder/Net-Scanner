# NetScan

A lightweight **TCP Port Scanner & Service Detector** written in Python for quick network reconnaissance. NetScan allows you to scan common ports or a custom port on a target IP address or domain name.

> **Version:** 1.1.0

---

## Features

* Scan popular TCP ports
* Scan any custom TCP port
* Supports both IP addresses and domain names
* Displays service names for common ports
* Colored terminal output
* Input validation and error handling
* Fast and lightweight

---

## Installation

### Clone the repository

```bash
git clone https://github.com/RedHat-Vibe-coder/NetScan.git
cd NetScan
```

### Install dependencies

```bash
pip install -r requirements.txt
```

Or install manually:

```bash
pip install requests colorama beautifulsoup4
```

---

## Requirements

```
Python 3.8+
requests==2.31.0
colorama==0.4.6
beautifulsoup4==4.12.2
```

---

## Usage

Run the tool using:

```bash
python Netscan.py
```

You'll be presented with two scanning modes:

### Option 1 – Default Ports

Scans a list of common ports:

* 21 (FTP)
* 22 (SSH)
* 23 (Telnet)
* 25 (SMTP)
* 53 (DNS)
* 80 (HTTP)
* 110 (POP3)
* 143 (IMAP)
* 443 (HTTPS)
* 3306 (MySQL)
* 3389 (RDP)
* 8080 (HTTP Alternative)

Example:

```
Enter Target IP or URL: scanme.nmap.org
```

---

### Option 2 – Custom Port

Scan any TCP port between **1–65535**.

Example:

```
Enter Target IP or URL: example.com
Enter Target Port: 443
```

---

## Sample Output

```
PORT      NAME      STATUS

22        SSH       OPEN
80        HTTP      OPEN
443       HTTPS     OPEN
3306      MySQL     CLOSE
```

---

## Project Structure

```
NetScan/
│
├── Netscan.py
├── requirements.txt
└── README.md
```

---

## Disclaimer

This tool is intended for:

* Educational purposes
* Learning networking
* Testing systems you own or have permission to assess

Do **not** use this tool against networks or systems without authorization.

---

## Author

**Ravaha Rizwan**

---

## License

This project is licensed under the MIT License.

Feel free to fork, modify, and improve the project.

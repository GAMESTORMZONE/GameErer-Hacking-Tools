
# GameErer Hacking Tools 🛠️

![banner](https://github.com/GAMESTORMZONE/gamestormzone.github.io/blob/main/background.jpg)

**GameErer** is a Python-based hacking tool that combines multiple powerful commands for ethical testing, research, and learning purposes. This tool is designed for system administrators, security professionals, and Python enthusiasts.

---

## 🌟 Features
- **Wi-Fi Password Retrieval** (Windows Admin Rights)
- **Port Scanning** for open ports
- **Hash Generation and Cracking**
- **Directory Management** with `cwd`, `cd`, and `dir` commands
- **DoS Testing** for network stress analysis
- **Cross-Site Scripting (XSS) Testing**
- **OS Information Display**
- **Current User Identity (`whoami`)**
- **Many more commands** to enhance your ethical hacking needs!

---

## 📦 Installation

### 1. **Set Up a Virtual Environment**
It is recommended to use a virtual environment for isolation.
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### 2. **Clone This Repository**
```bash
git clone https://github.com/GAMESTORMZONE/GameErer-Hacking-Tools.git
cd GameErer-Hacking-Tools
```

### 3. **Install Requirements**
```bash
pip install -r requirements.txt
```

---

## 🚀 How to Use

### Run the Tool
```bash
python Storm_Tools.py
```

### Available Commands

Here is a list of commands you can execute:

| Command        | Description                                                |
|----------------|------------------------------------------------------------|
| `help`         | Displays available commands.                               |
| `clear`        | Clears the console screen.                                 |
| `exit`         | Exits the tool.                                            |
| `wifi`         | Displays saved Wi-Fi passwords (Admin rights required).    |
| `osinfo`       | Displays operating system information.                     |
| `ping <IP>`    | Pings an IP address to test connectivity.                  |
| `time`         | Displays the current system time.                          |
| `whoami`       | Shows the current logged-in user.                          |
| `cwd`          | Displays the current working directory.                    |
| `cd <path>`    | Changes the working directory.                             |
| `dir`          | Lists the contents of the current directory.               |
| `portscan`     | Scans open ports on a specified IP address.                |
| `xss <URL>`    | Performs an XSS vulnerability test on a specified URL.     |
| `hashgen`      | Generates MD5 and SHA256 hashes for a given text.          |
| `hashcrack`    | Cracks an MD5 hash using a dictionary file.                |
| `exif`         | Extracts EXIF metadata from image files.                   |
| `dos <IP>`     | Launches a simple DoS attack on a target IP and port (for testing purposes). |

---

## 📊 Analytics and Downloads

- **Total Weekly Downloads:** 200+
- **Platform Compatibility:** Windows, Linux

---

## 💬 Join Our Community

Connect with us and discuss ethical hacking tools and techniques!

---

## ⚠️ Disclaimer

This tool is intended for educational purposes only. The creators are not responsible for any misuse of the tool. Use responsibly and only on systems you own or have permission to test.

import os
import subprocess
import platform
import socket
import hashlib
from datetime import datetime

# ASCII Art
def print_ascii_art():
    art = """
\033[92m
  ██████   █████   ███    ███ ███████ ███████ ██████  ███████ ██████  
 ██       ██   ██  ████  ████ ██      ██      ██   ██ ██      ██   ██ 
 ██   ███ ███████  ██ ████ ██ █████   █████   ██████  █████   ██████  
 ██    ██ ██   ██  ██  ██  ██ ██      ██      ██   ██ ██      ██   ██ 
  ██████  ██   ██  ██      ██ ███████ ███████ ██   ██ ███████ ██   ██ 
                                                                      
                                                                      
\033[0m
"""
    print(art)

# Parancsok tárolása és magyarázata
commands = {
    "help": "Megjeleníti az elérhető parancsokat.",
    "clear": "Törli a képernyőt.",
    "exit": "Kilép a programból.",
    "wifi": "Wi-Fi jelszavak megjelenítése (csak rendszergazdaként működik).",
    "osinfo": "Az operációs rendszer információinak kiírása.",
    "ping": "Pingel egy címet. Használat: ping <cím>",
    "time": "Kiírja az aktuális időt.",
    "whoami": "Az aktuális felhasználó nevét írja ki.",
    "cwd": "Az aktuális munkakönyvtár megjelenítése.",
    "cd": "Könyvtár váltás. Használat: cd <útvonal>",
    "dir": "Könyvtár tartalmának listázása.",
    "portscan": "Port scan egy adott IP-n. Használat: portscan <IP>",
    "xss": "XSS teszt. Használat: xss <URL>",
    "hashgen": "Hash generálás szövegből. Használat: hashgen <szöveg>",
    "hashcrack": "Hash törés dictionary alapon. Használat: hashcrack <hash> <file>",
    "exif": "EXIF adatok kiolvasása. Használat: exif <fájl>",
    "dos": "DoS támadás tesztelésre. Használat: dos <IP> <port>"
}

# Help parancs
def show_help():
    print("\n=== Elérhető Parancsok ===")
    for cmd, desc in commands.items():
        print(f"{cmd:<10} - {desc}")
    print("=========================\n")

# whoami parancs
def whoami():
    print(f"Felhasználó: {os.getlogin()}")

# cwd parancs
def show_cwd():
    print(f"Jelenlegi könyvtár: {os.getcwd()}")

# cd parancs
def change_directory(path):
    try:
        os.chdir(path)
        print(f"Könyvtár váltva: {os.getcwd()}")
    except FileNotFoundError:
        print("Hiba: A megadott útvonal nem létezik.")
    except Exception as e:
        print(f"Hiba: {e}")

# dir parancs
def list_directory():
    print("\n=== Könyvtár tartalma ===")
    for item in os.listdir():
        print(item)
    print("=========================\n")

# Wi-Fi jelszavak megjelenítése
def show_wifi_passwords():
    if os.name == "nt":  # Csak Windows rendszeren működik
        try:
            networks = subprocess.check_output("netsh wlan show profiles", shell=True, encoding="utf-8")
            print("\n=== Elmentett Wi-Fi hálózatok és jelszavak ===")
            for line in networks.splitlines():
                if "All User Profile" in line:
                    ssid = line.split(":")[1].strip()
                    try:
                        details = subprocess.check_output(
                            f"netsh wlan show profile name=\"{ssid}\" key=clear", shell=True, encoding="utf-8"
                        )
                        for detail in details.splitlines():
                            if "Key Content" in detail:
                                password = detail.split(":")[1].strip()
                                print(f"Hálózat: {ssid}, Jelszó: {password}")
                                break
                        else:
                            print(f"Hálózat: {ssid}, Jelszó: (Nincs beállítva)")
                    except subprocess.CalledProcessError:
                        print(f"Hálózat: {ssid}, Jelszó: (Hiba történt)")
        except subprocess.CalledProcessError:
            print("Nem sikerült lekérni a Wi-Fi hálózatokat. Futtasd a programot rendszergazdaként!")
    else:
        print("Ez a funkció csak Windows rendszeren működik.")

# XSS teszt
def xss_test(url):
    payloads = ["<script>alert(1)</script>", "'><img src=x onerror=alert(1)>"]
    print(f"\n=== XSS Teszt: {url} ===")
    for payload in payloads:
        print(f"Próbálkozás: {url}{payload}")

# Parancs feldolgozó
def process_command(command):
    args = command.split()
    if args[0] == "help":
        show_help()
    elif args[0] == "clear":
        os.system("cls" if os.name == "nt" else "clear")
    elif args[0] == "exit":
        print("Kilépés...")
        return False
    elif args[0] == "wifi":
        show_wifi_passwords()
    elif args[0] == "whoami":
        whoami()
    elif args[0] == "cwd":
        show_cwd()
    elif args[0] == "cd":
        if len(args) > 1:
            change_directory(args[1])
        else:
            print("Használat: cd <útvonal>")
    elif args[0] == "dir":
        list_directory()
    elif args[0] == "xss":
        if len(args) > 1:
            xss_test(args[1])
        else:
            print("Használat: xss <URL>")
    else:
        print(f"Ismeretlen parancs: {args[0]}")
    return True

# Fő program
def custom_cmd():
    print_ascii_art()
    print("Üdvözöllek a hacking tool-ban! Írj 'help'-et a parancsok megtekintéséhez.")
    while True:
        command = input(">>> ").strip()
        if not process_command(command):
            break

# Program futtatása
if __name__ == "__main__":
    custom_cmd()

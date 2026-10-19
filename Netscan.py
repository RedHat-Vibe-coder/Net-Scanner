# Library Imports
import os
import socket as soc
import time
from datetime import datetime

# Enable ANSI escape sequences in Windows Command Prompt
os.system('')

# Grab current date and time dynamically
now = datetime.now()
start_time = now.strftime("%Y-%m-%d %H:%M:%S")

# Colors for Output
GREEN = "\033[92m"
RED = "\033[91m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
RESET = "\033[0m"

# --- Tool Banner ---
print(CYAN + "=" * 100 + RESET)
# Added 'r' for raw string so ASCII backslashes print properly
print(CYAN + r"""
  _   _  _____ _____ ____   ____    _    _   _ _   _ _____ ____  
 | \ | || ____|_   _/ ___| / ___|  / \  | \ | | \ | | ____|  _ \ 
 |  \| ||  _|   | | \___ \| |     / _ \ |  \| |  \| |  _| | |_) |
 | |\  || |___  | |  ___) | |___ / ___ \| |\  | |\  | |___|  _ < 
 |_| \_||_____| |_| |____/ \____/_/   \_\_| \_|_| \_|_____|_| \_\\
""" + RESET)
print(CYAN + "=" * 100 + RESET)

print(f"  {YELLOW}Creator{RESET}      : Ravaha Rizwan")
print(f"  {YELLOW}Version{RESET}      : {GREEN}1.1.0{RESET} (Advanced)")
print(f"  {YELLOW}Scan Started{RESET} : {start_time}\n")

print(RED + "=" * 100 + RESET)
print(f"  {YELLOW}Description{RESET}  : A lightweight TCP Port Scanner & Service Detector")
print(f"                 designed for quick network reconnaissance.")
print(RED + "=" * 100 + RESET)
print("\n")

print(GREEN + "=" * 100 + RESET)
print("SELECT ATTACK METHOD".center(100))
print(GREEN + "=" * 100 + RESET)

    
print("\n[1] Default Ports")
print("[2] Custom Port")

#Attack selecting

while True :
    A = (input("\n[+] Enter Attack Method (1 or 2):")).strip()

    if A in ["1","2"] :
         B = int(A)
         break
    else :
         print(f"{RED}[!] Please Select a Attack method{RESET}")
         continue
    break

#if choese attack 1 default port

if B == 1 :
    while True :

#Target Details    
        tarip = input("\nEnter Target Ip or URL : ").strip()

        #If entry field empty get error massege

        if not tarip:
            print(f"{RED}[!] Input a IP or URL.{RESET}")
            continue

        #Search the address exist

        try :
             resolveip = soc.gethostbyname(tarip)
             print(f"[{GREEN}*{RESET}] Target resolved to IP: {resolveip}")
             break
        except soc.gaierror :
             print(f"{RED}[!] Error: Invalid IP address or unreachable domain name.{RESET}")
        

# FIX 1: Convert the port string into an integer
    tarpor = {
        21: "FTP", 22: "SSH", 23: "Telnet", 25: "SMTP", 53: "DNS",
        80: "HTTP", 110: "POP3", 143: "IMAP", 443: "HTTPS", 
        3306: "MySQL", 3389: "RDP", 8080: "HTTP-Alt"
    }

#Colors for Output
    GREEN = "\033[92m"
    RED = "\033[91m"
    RESET = "\033[0m"  # Resets the color back to default

    print("   ")
    print(RED + "=" * 100)
    print("ATTACKING".center(100))
    print("=" * 100 + RESET)

    print(f"\n{'PORT':<10}{'NAME':<10}{'STATUS':<10}\n")


#Make a loop for scan all ports
    for port,service in tarpor.items():

#Tell use IPv4 & Try in TCP
        s = soc.socket(soc.AF_INET, soc.SOCK_STREAM)

#Communicate Time
        s.settimeout(5.0)

#Result of Output
# FIX 2: Added double parentheses to pass a single tuple (IP, Port)
        resault = s.connect_ex((tarip, port))

#Print Results
        if resault == 0 :
            print(f"{port:<10}{service:<10}{GREEN}{'OPEN':<10}{RESET}")
        else :
            print(f"{port:<10}{service:<10}{RED}{'CLOSE':<10}{RESET}")

        s.close()

#If choese attack method 2 custom port

else:
    while True:
        #attack method 2 ip entry

        tarip1 = input("\nEnter Target Ip or URL : ").strip()

        #attack method 2 port Entry

        if not tarip1:
            print(f"{RED}[!] Input cannot be empty.{RESET}")
            continue

        #Try if ip or url exist

        try:
             resolveip1 = soc.gethostbyname(tarip1)
             print(f"[{GREEN}*{RESET}] Target resolved to IP: {resolveip1}")
             break

        #If get error helping code
        except soc.gaierror :
             print(f"{RED}[!] Error: Invalid IP address or unreachable domain name.{RESET}")

    while True:
        try:
            #  Convert input to integer here so the comparison works!
            tarpor2 = int(input("Enter Target Port : ").strip())

            if 1 <= tarpor2 <= 65535:
                break
            else:
                print(f"{RED}[!] Port must be between 1 and 65535{RESET}")

        except ValueError:
            print(f"{RED}[!] Please enter a numeric port (e.g., 80 or 443).{RESET}")


    #UI Printing Detail
    print("   ")
    print(RED + "=" * 100)
    print("ATTACKING".center(100))
    print("=" * 100 + RESET)
        
    print(f"\n{'PORT':<10}{'NAME':<10}{'STATUS':<10}\n")

    #Tell use IPv4 & Try in TCP

    s = soc.socket(soc.AF_INET, soc.SOCK_STREAM)

    #Set a Scan time

    s.settimeout(5.0)

    #Convert int for loop to get port name output
    tarpor2 = int(tarpor2)

    por = {
        21: "FTP", 22: "SSH", 23: "Telnet", 25: "SMTP", 53: "DNS",
        80: "HTTP", 110: "POP3", 143: "IMAP", 443: "HTTPS", 
        3306: "MySQL", 3389: "RDP", 8080: "HTTP-Alt"
    }

    #Get Costom Port Name
    servis = "Unknown"

    for ports,servisnm in por.items() :
         if ports == tarpor2 :
              servis = servisnm
              break

    #Connect for target ip
    resault = s.connect_ex((tarip1, tarpor2))

    #Print Details
    if resault == 0 :
            print(f"{tarpor2:<10}{servis:<10}{GREEN}{'OPEN':<10}{RESET}")
    else :
            print(f"{tarpor2:<10}{servis:<10}{RED}{'CLOSE':<10}{RESET}")

    s.close()
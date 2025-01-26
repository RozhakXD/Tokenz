try:
    import requests
    import re
    import sys
except ModuleNotFoundError as error:
    exit(f"[Error] {str(error).capitalize()}!")

def CONVERT(cookies: str) -> None:
    with requests.Session() as session:
        params = {
            'client_id': '124024574287414',
            'wants_cookie_data': 'true',
            'origin': '1',
            'input_token': '',
            'sdk': 'joey',
            'redirect_uri': 'https://www.instagram.com/rozhak_official/',
        }
        session.headers.update(
            {
                'Origin': 'https://www.instagram.com',
                'Accept-Language': 'id,en;q=0.9',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
                'Referer': 'https://www.instagram.com/',
                'Host': 'www.facebook.com',
                'Sec-Fetch-Mode': 'cors',
                'Accept': '*/*',
                'Connection': 'keep-alive',
                'Sec-Fetch-Site': 'cross-site',
                'Sec-Fetch-Dest': 'empty',
                'Accept-Encoding': 'gzip, deflate',
            }
        )
        response = session.get('https://www.facebook.com/x/oauth/status', params=params, cookies={
            'Cookie': cookies
        })
        if '"access_token":' in str(response.headers):
            token = re.search(r'"access_token":"(.*?)"', str(response.headers)).group(1)
            print(f"\n[Info] Token Ditemukan: {token}")
        else:
            print(f"\n[Error] Token Tidak Ditemukan!")
    return None

if __name__ == '__main__':
    try:
        if len(sys.argv) != 2:
            exit("\n[Info] Usage: python Run.py \"Your Cookies!\"")
        cookies = sys.argv[1]
        CONVERT(cookies)
        exit()
    except Exception as error:
        exit(f"\n[Error] {str(error).title()}!")
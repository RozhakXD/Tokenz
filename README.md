# FACEBOOK COOKIES TO TOKEN - WITH TERMUX
<div align="center">
  <img src="Data/Tokenz.jpg">
  <br>
  <br>
  <p>
    <img alt="GitHub contributors" src="https://img.shields.io/github/contributors/rozhakxd/Tokenz">
    <img alt="GitHub issues" src="https://img.shields.io/github/issues/rozhakxd/Tokenz">
    <img src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=shields">
    <img alt="GitHub pull requests" src="https://img.shields.io/github/issues-pr/rozhakxd/Tokenz">
    <img alt="GitHub commit activity" src="https://img.shields.io/github/commit-activity/m/rozhakxd/Tokenz">
    <img alt="Maintenance" src="https://img.shields.io/maintenance/no/2023">
  </p>
  <h4> Get Facebook Token Using Only Termux ! </h4>
</div>

##

### What is Tokenz?
[**Tokenz**](https://github.com/RozhakXD/Tokenz) is a program to get Facebook tokens which was created using the Python programming language.

The token you get is an eaab token which has fairly complete permissions.

### Termux command?
First you must have the [Termux](https://f-droid.org/repo/com.termux_118.apk) application to run this script and for how to use it can be seen on [**Youtube**](https://www.youtube.com/rozhakid). Then you enter some basic commands below!
```
$ apt update -y && apt upgrade -y
$ pkg install git python-pip
$ git clone https://github.com/RozhakXD/Tokenz
$ cd "Tokenz"
$ python -m pip install -r requirements.txt
$ python Run.py
```

```
$ cd "$HOME/Tokenz" && git pul
$ python Run.py
```

### No tokens appearing?

- Maybe your Facebook account is checkpointed or locked.
- The Facebook system has been repaired causing failure to get tokens.
- This program has been suspected by Facebook.

### Why login failed?

- Your Facebook account cookies are no longer valid or expired.
- Your Facebook account is logged out of the browser.
- Maybe your Facebook account has been checkpointed or temporarily locked.

### Making friends using Python?

```python
import requests, json

your_cookies, your_tokens, your_targets = ('c_user=...?', 'EAAB...?', '10009...?')
Dumps = []

def Friends(next_cursor):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
        'Host': 'graph.facebook.com',
        'Accept-Language': 'id,en;q=0.9',
    }
    params = {
        'access_token': your_tokens,
        'pretty': '1',
        'after': next_cursor,
    }
    response = requests.get('https://graph.facebook.com/v18.0/{}/friends?'.format(your_targets), params = params, headers = headers, cookies = {
        'cookie': cookies
    })
    json_data = json.loads(response.text)
    if '\'name\':' in str(json_data) and '\'id\':' in str(json_data):
        for z in json_data['data']:
            user_ids, name = z['id'], z['name']
            Dumps.append(f'{user_ids}|{name}')
        if '\'after\':' in str(json_data):
            next_cursor = json_data['paging']['cursors']['after']
            Friends(next_cursor)
        else:
            return ("Selesai")
    else:
        return ("Sukses")
```

### No friends collected?

- In essence, all the problems, if not in the fake account, are in the target you entered.
- Maybe your account is limited or blocked for 24 hours.
- The target you entered has no friends or is not visible to the public.
- You made an incorrect API request or the access token has expired.

### Get complete access on token?

To get complete access to the token, you can connect your Instagram account with your Facebook account. This method will add several access permissions to the token.

##
```python
print("Good luck hope it works!")
```
##

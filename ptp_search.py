import urllib
import requests
import inspect
import sys

h_user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'


def create_search_url(ss):
    urllib.
    return urllib.parse.quote(ss)


def main():
    url = 'https://passthepopcorn.me/ajax.php?action=login'
    login_data = {
        'username': 'blatsha92',
        'password': 'Mew9apr10',
        'passkey': 'qwmzz0rnvnpjpuf5j8ahm0swhq6cmpqy'
    }
    headers = {
        'user-agent': h_user_agent
    }
    s = requests.Session()
    s.post(url, data=login_data, headers=headers)
    search_string = input('Movie to search for: ')
    print('Searching for "' + search_string + '" .... ')
    # response = s.get(create_search_url(search_string))
    print(create_search_url(search_string))




if __name__ == '__main__':
    main()

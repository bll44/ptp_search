import urllib.parse
import requests
import json
import pprint

h_user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'


def parse_url(ss):
    return urllib.parse.quote(ss)


def main():
    url = 'https://passthepopcorn.me/ajax.php?action=login'
    login_data = {
        'username': '<username>',
        'password': '<password>',
        'passkey': '<passkey>'
    }
    headers = {
        'user-agent': h_user_agent
    }
    s = requests.Session()
    s.post(url, data=login_data, headers=headers)
    # search_string = input('Movie to search for: ')
    search_string = 'war dogs'  # for testing purposes
    print('Searching for "' + search_string + '" .... ')
    data = {
        'order_by': 'relevance',
        'searchstr': urllib.parse.quote(search_string),
        'json': 'noredirect'
    }
    search_url = 'https://passthepopcorn.me/torrents.php'
    # search_url = 'https://passthepopcorn.me/ajax.php?action=top10'
    response = s.get('https://passthepopcorn.me/torrents.php?order_by=relevance&searchstr=war%20dogs&json=noredirect')
    movies = json.loads(response.text)
    for m in movies['Movies']:
        print(m['Title'] + '\t' + m['Cover'] + ' :')
        for t in m['Torrents']:
            print('\t' + t['Resolution'] + ' - ' + t['Container'])
    exit()
    for m in movies['Movies']:
        t = m['Torrents'][0]
        if t['Resolution'].upper() == '720P' and t['Container'].upper() == 'MKV':
            torrent_id = t['Id']

    ptp_authkey = movies['AuthKey']
    ptp_passkey = movies['PassKey']
    query = {
        'action': 'download',
        'id': torrent_id,
        'authkey': ptp_authkey,
        'torrent_pass': ptp_passkey
    }
    download_url = 'https://passthepopcorn.me/torrents.php?' + urllib.parse.urlencode(query)
    pprint.pprint(download_url)
    exit()




if __name__ == '__main__':
    main()

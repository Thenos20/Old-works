import requests


headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

login_data = {
    'UserName': r'intra\username',
    'Password': 'password',
    'AuthMethod': 'FormsAuthentication'
}
params = {
    'id': 27,
    'org': 60
}
with requests.Session() as s:
    url = s.get("https://auth.vklass.se/grandid/initiate?id=27&org=60").url
    url2 = s.get(url, params=params)
    sessionid = url2.url.replace('https://login.grandid.com/?sessionid=', '')
    params2 = {'sid': sessionid}
    url2 = s.get('https://lundssp.grandid.com/', params=params2)
    url3 = url2.url
    print(url2.url)
    r = s.get(url3, headers=headers)
    r = s.post(url3, data=login_data, headers=headers)
    #print(r.content)

    with open('site.html', 'w') as f:
        f.write(r.text)
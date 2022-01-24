import requests

s = requests.session()

payload = {
    'usernames': 'LegoYodaDeathSound42',
    'passwords' : 'ReeHaw',
}

response = s.post("https://www.ytmonster.net/login?login=ok", data=payload)
print(response.content)



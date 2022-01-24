import requests

s = requests.session()

payload = {
    'UserName': '012507',
    'Password': '229361',
    'AuthMethod': 'FormsAuthentication'
}

response = s.post("https://fs.lund.se/adfs/ls/?wa=wsignin1.0&wtrealm=https%3a%2f%2flundssp.grandid.com%2f&wctx=rm%3d0%26id%3dpassive%26ru%3d%252f%253fsid%253d97aed474f509263e010ee7d322a90339&wct=2021-07-04T15%3a16%3a33Z&client-request-id=425c8ef9-bfb7-4ad5-6f25-0080010000d5", data=payload)
print(response.content)



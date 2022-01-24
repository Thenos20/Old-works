import requests
r = requests.get('https://www.aftonbladet.se/')

from bs4 import BeautifulSoup
soup = BeautifulSoup(r.text, "html.parser")
News = soup.find_all('div', {"class": "css-1p9ud9z"})

d = {}
a=0
for artcile in News:
    main = artcile.find_all('a')[0]
    link = main.get("href")
    if "nyheter" in link:
        a = a+1
        print("https://www.aftonbladet.se/" + link)
        d["link"+str(a)] = "https://www.aftonbladet.se/" + link
print(d)

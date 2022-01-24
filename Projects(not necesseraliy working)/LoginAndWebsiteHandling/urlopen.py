from urllib.request import urlopen

url = "https://www.vklass.se/default.aspx"

page = urlopen(url)

html_bytes = page.read()
html = html_bytes.decode("utf-8")

#print(html)


title_index = html.find("<title>")
print(title_index)

start_index = title_index + len("<title>")


end_index = html.find("</title>")
title = html[start_index:end_index]
print(title)
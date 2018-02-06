from bs4 import BeautifulSoup
url = 'https://www.apple.com/itunes/charts/songs/'


import urllib.request

data = urllib.request.urlopen(url).read()
html_content = data.decode("utf-8")

html_file = open ("itunes.html", "wb")
html_file.write(data)
html_file.close()

soup = BeautifulSoup(html_content, "html.parser")

print(soup.prettify())
div = soup.find_all('div', 'section-content')
li_list = div[1].find_all("li")


news_list = []

for li in li_list:


    Name = li.h3.string
    Artist = li.h4.string
    song = {
    'Name': Name,
    'Artist': Artist,
    }
    news_list.append(song)


import pyexcel
pyexcel.save_as(records= news_list, dest_file_name="itunes.xlsx")

from youtubedl import YoutubeDL

dl = YoutubeDL()

options = {
    'default_search': 'ytsearch',
    'max_downloads': 1,

}
dl = YoutubeDL(options)

dl.download([song])

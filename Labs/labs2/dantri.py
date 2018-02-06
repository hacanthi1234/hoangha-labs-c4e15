from bs4 import BeautifulSoup

url = "http://dantri.com.vn/"
output_file_name= "news.xlsx"



# import urllib.request
#
# opener = urllib.request.FancyURLopener({})
# url = "http://dantri.com.vn/"
# f = opener.open(url)
# content = f.read().decode("utf8") #decode để loại bỏ các thứ ko cần thiết, utf8 là dòng kí tự chuyên dụng.
#
# print(content)
# from urllib.request import urlopen
import urllib.request



data = urllib.request.urlopen(url).read()
html_content = data.decode("utf-8")

html_file = open ("dantri.html", "wb") #write
html_file.write(data)
html_file.close()


#2. extract ROI

soup = BeautifulSoup(html_content, "html.parser") #xml

print(soup.prettify())
ul = soup.find('ul', "ul1 ulnew") #class id ="" 1soup
li_list = ul.find_all("li")
# print(ul.prettyfy)
# print(li_list)

news_list = []

for li in li_list:
#     print(li)
#     print("*" * 20)

# li = li_list[0]
# h4 = li.h4 #walking
# a = h4.a
    h4 = li.h4
    a = li.h4.a #li.a di thang vào thư mục luôn

    href = url + a["href"]

    title = a.string
    news = {
        'title': title,
        'link': href

    }
    news_list.append(news)
    # print(href)
    # print(title)
    # print("*" *20)

import pyexcel
pyexcel.save_as(records= news_list, dest_file_name="dantri.xlsx")

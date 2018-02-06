url = 'http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2017/3/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn'
file_output = "VNM.xlsx"


from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel

data = urlopen(url).read()
html_content = data.decode('utf-8')

html_file = open('VNM.html', 'wb')
html_file.write(data)
html_file.close

soup = BeautifulSoup(html_content, 'html.parser')
table_form = soup.find('table', 'tableContent')
tr = table_form.find_all('tr')

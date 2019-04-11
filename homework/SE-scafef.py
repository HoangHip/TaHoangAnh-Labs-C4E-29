from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
url = "http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2017/3/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn"
conn = urlopen(url)
raw_data = conn.read()
html_content = raw_data.decode('utf8')

soup = BeautifulSoup(html_content, "html.parser")
div = soup.find("div", style="background-color:#e1e1e1;overflow:hidden")
tr = div.tr
td_list = tr.find_all('td')
data_list =[]
title_list = ['',]
for td in td_list:
    name = td.string
    if name != None:
        name = name.strip()
        if name != "Tăng trưởng":
            title_list.append(name)
div = soup.find("div", style="overflow:hidden;width:100%;border-bottom:solid 1px #cecece;")
tr_list = div.find_all('tr')
for tr in tr_list:
    td_list = tr.find_all('td')
    name_list = []
    dic = {}
    for td in td_list:
        name = td.string
        if name != None:
            name = name.strip()
            name_list.append(name)
    if len(name_list) == len(title_list):
        for i in range(len(name_list)):
            dic[title_list[i]] = name_list[i]
        data_list.append(dic)
    elif name_list != []:
        dic[title_list[0]] = name_list[0]
        data_list.append(dic)
pyexcel.save_as(records=data_list, dest_file_name="scafef.xlsx")
    

            
        
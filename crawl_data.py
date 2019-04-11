from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
from collections import OrderedDict
#1. Open connection
url = "https://dantri.com.vn"
conn = urlopen(url)
raw_data = conn.read()
html_content = raw_data.decode('utf8')

with open("dantri.html", "wb") as f:
    f.write(raw_data)
# print(html_content)

# 2. Find ROI

# soup = BeautifulSoup(html_content, "html.parser")
# # print(soup.prettify())
# ul = soup.find("ul", "ul1 ulnew")
# # riêng attribute class không cần ghi class = 

# #3. Extract ROI
# li_list = ul.find_all("li")
# # for li in li_list:
# #     print(li.prettify())
# #     print("**" * 20)
# news_list = []
# for li in li_list:
#     h4 = li.h4
#     a = h4.a
#     title = a.string.strip()
#     # a coi như 1 dictionary
#     link = url + a["href"]
#     news = OrderedDict({
#         "Title": title,
#         "Link": link
#     })
#     news_list.append(news)
# pyexcel.save_as(records=news_list, dest_file_name="dantri.xlsx")
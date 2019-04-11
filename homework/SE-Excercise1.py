from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
from youtube_dl import YoutubeDL

url = "https://www.apple.com/itunes/charts/songs/"
conn = urlopen(url)
raw_data = conn.read()
html_content = raw_data.decode("utf8")

soup = BeautifulSoup(html_content, "html.parser")

sec = soup.find("section", "section chart-grid")
ul = sec.div.ul

li_list = ul.find_all("li")
itunes_list = []
for li in li_list:
    a = li.h4.a
    a1 = li.h3.a
    artists = a.string.strip()    
    songs = a1.string.strip()
    
    name = {
        "Songs" : songs,
        "Artists" : artists
    }
    itunes_list.append(name)
    # Part 2

    options = {
        'default_search' : 'ytsearch',
        'max_downloads' : 1,
    }
    dl = YoutubeDL(options)
    dl.download(['songs' + 'name'])
    print(songs, artists)
pyexcel.save_as(records=itunes_list, dest_file_name="Itunes top song.xlsx")

    

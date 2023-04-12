import requests
import re
import datetime
import time
from email import utils
from bs4 import BeautifulSoup
from datetime import datetime
lista_linkow = []
odpowiedz = requests.get("https://www.lechpoznan.pl/aktualnosci,2.html?page=1&limit=10")
html_doc = odpowiedz.text
soup = BeautifulSoup(html_doc, 'html.parser')
for link in soup.find_all(class_="itemDefault"):
    #print("https://www.lechpoznan.pl/" + link.get('href'))
    lista_linkow.append("https://www.lechpoznan.pl/" + link.get('href'))
#print(lista_linkow)

baza_danychh = []
baza_danych_jedenar = []
baza_title = []
baza_lead = []
baza_link = []
baza_data = []

wynik_item = []

kuwa = []
#for i in range(len(lista_linkow)):
#    baza_danychh.append("a")
#for i in range(2):
for i in range(len(lista_linkow)):
    baza_danych_jedenar.clear()
    sprawdzany_link = lista_linkow[i]
    sprawdzany_link = re.sub(r'[^-_.~!*();:@&=+$,/?%#[A-z0-9]', r"_", sprawdzany_link)
    print(sprawdzany_link)
    sprawdzana_odpowiedz = requests.get(sprawdzany_link)
    sprawdzany_html = sprawdzana_odpowiedz.text
    sprawdzana_soup = BeautifulSoup(sprawdzany_html, 'html.parser')
    #sprawdzany_fragment = sprawdzana_soup.find(class_="Heading")
    #sprawdzana_title = sprawdzany_fragment.get_text()
    sprawdzany_fragment = sprawdzana_soup.find("meta", attrs={"name" : "title"})
    #print(sprawdzany_fragment)
    sprawdzana_title = sprawdzany_fragment["content"]
    print(sprawdzana_title)
    #sprawdzany_fragment = sprawdzana_soup.find(class_="Excerpt")
    #sprawdzana_lead = sprawdzany_fragment.get_text()
    sprawdzany_fragment = sprawdzana_soup.find("meta", attrs={"name" : "description"})
    sprawdzana_lead = sprawdzany_fragment["content"]
    sprawdzana_lead = re.sub(r'&nbsp;', r" ", sprawdzana_lead)
    sprawdzany_fragment = sprawdzana_soup.find("meta", attrs={"name" : "article:published_time"})
    sprawdzany_data = sprawdzany_fragment["content"]
    sprawdzany_data = datetime.strptime(sprawdzany_data, '%Y-%m-%d %H:%M:%S')
    nowdt = sprawdzany_data
    nowtuple = nowdt.timetuple()
    nowtimestamp = time.mktime(nowtuple)
    sprawdzany_data = utils.formatdate(nowtimestamp)
    ##baza_danych_jedenar.append(sprawdzana_title)
    ##baza_danych_jedenar.append(sprawdzany_link)
    ##baza_danych_jedenar.append(sprawdzana_lead)
    ##baza_danych_jedenar.append(sprawdzany_data)
    ##baza_danychh[i] = baza_danych_jedenar
    #baza_danychh.append(baza_danych_jedenar)
    #print(baza_danych)
    #print(sprawdzana_title + "\n" + sprawdzana_lead + "\n" + sprawdzany_data)
    baza_title.append(sprawdzana_title)
    baza_lead.append(sprawdzana_lead)
    baza_link.append(sprawdzany_link)
    baza_data.append(sprawdzany_data)
for j in range(len(baza_title)):
    #print(baza_title[j] + baza_lead[j] + baza_link[j] + "\n" + baza_data[j])
    #print("<item>\n<title>" + baza_title[j] + "</title>\n<link>" + baza_link[j] + "</link>\n<description>" + baza_lead[j] + "</description>\n<pubDate>" + baza_data[j] + "</pubDate>\n</item>")
    wynik_item.append("<item>\n<title>" + baza_title[j] + "</title>\n<link>" + baza_link[j] + "</link>\n<description>" + baza_lead[j] + "</description>\n<pubDate>" + baza_data[j] + "</pubDate>\n</item>")
wynik_intro = '''<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0">
    <channel>
        <link>https://www.lechpoznan.pl/</link>
        <description>Kanał RSS Lecha Poznań </description>
        <language>pl</language>
        <copyright>Lech Poznań</copyright>
        <pubDate>Wed, 06 May 2009 00:00:01 +0200</pubDate>
        <lastBuildDate>Sat, 28 Nov 2009 20:08:07 +0100</lastBuildDate>
        <title>Lech Poznań RSS</title>
'''
wynik_outro = '''
    </channel>
</rss>
'''
wynik_item2 = '\n'.join(wynik_item)
#print(wynik_intro + wynik_item2 + wynik_outro)
f = open("lechfeed.rss", "w", encoding="utf-8")
f.write(wynik_intro + wynik_item2 + wynik_outro)
f.close()

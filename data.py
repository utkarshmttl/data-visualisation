from bs4 import BeautifulSoup
import urllib.request as ur
from datetime import date, timedelta
import re

d1 = date(2017, 1, 1)  # start date
d2 = date(2017, 12, 31)  # end date

delta = d2 - d1         # timedelta
print(delta)

for i in range(delta.days + 1):
    print((d1 + timedelta(days=i)).strftime("%Y%m%d"))
    link = "https://www.timeanddate.com/scripts/cityajax.php?n=india/new-delhi&mode=historic&hd="+(d1 + timedelta(days=i)).strftime("%Y%m%d")+"&month="+(d1 + timedelta(days=i)).strftime("%-m")+"&year=2017"
    f = ur.urlopen(link)
    html = f.read()
    soup = BeautifulSoup(html,"lxml")

    for elem in soup(text=re.compile(r'(°C|\d\d\.\d\d)')):
        print(elem.parent)

    # print(soup)
    print("done ",i)

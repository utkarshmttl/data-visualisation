from bs4 import BeautifulSoup
import urllib.request as ur
from datetime import date, timedelta
import re
import sqlite3

d1 = date(2017, 1, 1)  # start date
d2 = date(2017, 12, 31)  # end date

city_airport = "VIDP" #IGI airport new delhi

delta = d2 - d1         # timedelta
print(delta)


for i in range(delta.days + 1):
    conn = sqlite3.connect('newDelhi_2017_temperature.db')
    currentDate = (d1 + timedelta(days=i)).strftime("%Y/%m/%d")
    print((d1 + timedelta(days=i)).strftime("%Y/%m/%d"))
    link = "https://www.wunderground.com/history/airport/"+city_airport+"/"+currentDate+"/DailyHistory.html"
    f = ur.urlopen(link)
    html = f.read()
    soup = BeautifulSoup(html,"lxml")
    div = soup.find_all("tr", {"class": "no-metars"})

    for elem in div:
        tds = elem.find_all("td")
        print(tds[0].text)
        if(tds[0].text[-5:-3] == "00" or tds[0].text[-5:-3] == "30"):
            print("***********","TRUEEEE","********")
            if tds[1].find("span",{"class": "wx-value"}) is not None:
                print(tds[1].find("span",{"class": "wx-value"}).text)
                conn.execute("UPDATE temperature set \'"+tds[0].text+"\' = "+tds[1].find("span",{"class": "wx-value"}).text+" where date = \'"+currentDate+"\'; ")
                conn.commit()


        # print('INSERT INTO or REPLACE questions (ID,query,solution) VALUES ('+ str(json_object["question_id"]) +', \''+str(json_object["query"])+'\', \'' + str(json_object["solution"]) +'\')')
        # conn.execute('INSERT or REPLACE INTO questions (ID,query,solution) VALUES ('+ str(json_object["question_id"]) +', \''+str(json_object["query"])+'\', \'' + str(json_object["solution"]) +'\')')
        # #conn.execute('INSERT INTO questions (ID,query,solution) VALUES ('+ str(json_object["question_id"]) +', '+str(json_object["query"])+', ' + str(json_object["solution"]) +')');
        # conn.commit()

    conn.close()
    print("done ",i," ",currentDate)

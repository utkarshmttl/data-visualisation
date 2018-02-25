from bs4 import BeautifulSoup
import urllib.request as ur
from datetime import date, timedelta
import re
import sqlite3

conn = sqlite3.connect('newDelhi_2017_temperature.db')

conn.execute("UPDATE temperature set '12:30 AM' = 15 where date = '2017/01/01'; ")
conn.commit()

conn.close()

print("DONE")

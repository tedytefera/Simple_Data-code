import requests
from bs4 import BeautifulSoup
import urllib.request
import sqlite3

conn = sqlite3.connect('project2.db')
cur = conn.cursor()

cur.execute('''
Drop table if exists mycode''')

cur.execute('''
create table count(Name Text, count Integer)''')


url = input("Enter: ")

html = urllib.request.urlopen(url).read()

soup = BeautifulSoup(html)

tags = soup('a')

for tag in tags:
    m = tag.get('href', None)
    print (m)
    
    cur.execute('''Insert into count(Name, count) Values(?, 1)''', (m, ))
    
    conn.commit()
    

    
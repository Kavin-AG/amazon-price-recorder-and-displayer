import requests
import urllib.request as rq
import csv
from datetime import date
import sqlite3
from bs4 import BeautifulSoup

#connect to/create database
conn = sqlite3.connect('amztracker.db')
c = conn.cursor()

#create the table once and uses the same all-time
try:
    c.execute('''CREATE TABLE prices(title TEXT, price FLOAT, asin TEXT,date DATE )''')
    print("creating new database\n")
except sqlite3.OperationalError :
    print("Database already available\n")

asins = []

#read csv to list
with open('asins.csv', 'r') as f:
    csv_reader = csv.reader(f)
    for row in csv_reader:
        asins.append(row[0])

#scrape data
for asin in asins:
    r = f'https://www.amazon.in/dp/{asin}'
    #get the header from "httpbin.org/get"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0", 
    "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", 
    "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

    page = requests.get(r, headers=headers)
    soup1 = BeautifulSoup(page.content, "html.parser")
    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")
    title = soup2.find(id='productTitle').text.strip()

    try:

        price = soup2.find(class_="a-price-whole").text.strip().replace(".","").replace(",","")
        
    except :
        price = None
    asin = asin
    date = date.today()
    c.execute('''INSERT INTO prices VALUES(?,?,?,?)''', (title, price,asin, date))
    print(f'Added data for {title}, of cost {price}')

conn.commit()
print('saved new entries to database')


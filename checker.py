import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from IPython.display import display

#connect to/create database
conn = sqlite3.connect('amztracker.db')

df = pd.read_sql_query('''SELECT * FROM prices''',conn)
title = [*set(list(df.title))]

#display(df)
def graph(i):
    tdf = pd.read_sql_query(f'''SELECT * FROM prices where title = "{i}"''',conn)
    display(tdf)
    tdf.plot(x='date', y='price', kind='line')
    plt.title(i)
    plt.show()

print("check the change in price of:")
for i in title:
    print(title.index(i)+1,". ",i)

h = int(input("\nenter your choice:"))
if h>len(title) or h <=0:
    print("enter a proper choice")
graph(title[h-1])
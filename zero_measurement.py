#!/bin/bash
from bs4 import BeautifulSoup
import requests
import datetime
import csv
import pandas as pd
import sqlite3
import os

x = datetime.datetime.now()
response = requests.get("https://www.doviz.com/")

web_html = response.text

soup = BeautifulSoup(web_html, "html.parser")

#List comprehension
investment_object = [each.get('data-socket-key') for each in soup.find_all(name="span", class_="value")]
investment_value  = [each.getText() for each in soup.find_all(name="span", class_="value")]

investment_object.insert(0, 'Date')
investment_value.insert(0, x)
list_to_convert = [investment_object, investment_value]

file_path = os.path.relpath("/mnt/c/grafana/grafana_project/insert_csv_list.csv")
with open(file_path, "w", newline='') as file:
    writer = csv.writer(file)
    writer.writerows(list_to_convert)
    file.close()

cmd = '/mnt/c/grafana/grafana_project/regex_insert_zero.sh'
os.system(cmd)

df = pd.read_csv(file_path, sep=',')
dbname = '/mnt/c/grafana/grafana_project/investment.db'
con = sqlite3.connect(dbname)
df.to_sql(name='invest', con=con, if_exists='append', index=False)
con.close()



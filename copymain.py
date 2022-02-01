#!/bin/bash
from bs4 import BeautifulSoup
import requests
import datetime
import csv
import os
import pandas as pd
import sqlite3

x = datetime.datetime.now()
response = requests.get("https://www.doviz.com/")

web_html = response.text

soup = BeautifulSoup(web_html, "html.parser")

#List comprehension
#investment_object = [each.get('data-socket-key') for each in soup.find_all(name="span", class_="value")]
investment_value = [each.getText() for each in soup.find_all(name="span", class_="value")]

#investment_object.insert(0, 'Date')
investment_value.insert(0, x)
list_to_convert = [investment_value]
#with open("insert_csv_list.csv","a",newline='') as file:

file_path = os.path.relpath("/mnt/c/grafana/grafana_project/test.csv_list.csv")
with open(file_path, "a", newline='') as file:
    writer = csv.writer(file)
    writer.writerows(list_to_convert)
    file.close()

#
# # Here in cmd we correct the numbering format. We replace ',' with '.' and also remove the $ sign from the data.
# cmd = '/mnt/c/grafana/grafana_project/regex_diff_csv.sh'
# os.system(cmd)





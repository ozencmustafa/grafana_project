import csv
import pandas as pd
import sqlite3
import os

dbname ='C:\\grafana\\grafana_project\\investment.db'
con = sqlite3.connect(dbname)
cur = con.cursor()

file_path = "C:\\grafana\\grafana_project\\diff_insert_csv_list.csv"
a_file = open(file_path)
rows = csv.reader(a_file)
cur.executemany("INSERT INTO invest VALUES (?,?,?,?,?,?,?,?,?)", rows)

con.commit()
con.close()

########################################################
# df = pd.read_csv("insert_csv_list.csv", sep=',')
# dbname ='C:\\grafana\\grafana_project\\investment.db'
# con = sqlite3.connect(dbname)
# df.to_sql(name='invest', con=con, if_exists='append', index=False)
# con.close()
#################################################
# file_path = "C:\\grafana\\grafana_project\\diff_insert_csv_list.csv"
# dbname = "C:\\grafana\\grafana_project\\investment1.db"
#
# #file_path = os.path.relpath("/mnt/c/grafana/grafana_project/diff_insert_csv_list.csv")
# df = pd.read_csv(file_path, sep=',')
# #dbname = '/mnt/c/grafana/grafana_project/investment.db'
# con = sqlite3.connect(dbname)
# df.to_sql(name='invest', con=con, if_exists='append', index=False)
# con.close()
#####################################################
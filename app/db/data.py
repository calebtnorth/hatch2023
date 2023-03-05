import pandas as pd
import sqlite3
from db import *
import matplotlib.pyplot as plt

#sqlfile.db is the .db file with data and the date they change things. Come back with mentor.
#usage = pd.read_db("hourlydata.db", index_col=0, parse_dates = True)
# # usage.plot.bar()
# # pi_usage = pd.read_db("totaldata.db", index_col=0, parse_dates = True)
# # pi_usage.plot.pie()
# # plt.show()

username = "justin"
username_data = get_activity(username)
print(username_data)

owner = "Caleb"
owner_data = get_business(owner)
print(owner_data)


plt.show()
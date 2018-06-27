import psycopg2
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn import datasets, linear_model
from numpy.matlib import randn



conn_string = "host='localhost' dbname='temp-2017' user='postgres' password='16a10a'"
conn = psycopg2.connect(conn_string)
res = pd.read_sql("SELECT indate, ntime FROM mvs100k.tasks",conn,index_col='indate',parse_dates=True)




res = res.resample('M').mean()
a = res.plot(kind='line', color = 'red')
dd = pd.rolling_mean(res,100, min_periods=1)
dd.plot(ax=a)
plt.show()

print(res)
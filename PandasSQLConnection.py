import psycopg2
import matplotlib.pyplot as plt
import pandas
from numpy.matlib import randn

conn_string = "host='localhost' dbname='temp-2017' user='postgres' password='16a10a'"
conn = psycopg2.connect(conn_string)
res = pandas.read_sql("SELECT tasks.indate,tasks.ntime FROM mvs100k.tasks",conn,index_col='indate')
res = res.resample('M',how='mean')
res.plot( )
plt.show()





print(res)
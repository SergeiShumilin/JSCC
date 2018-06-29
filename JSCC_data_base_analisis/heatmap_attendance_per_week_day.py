import psycopg2
import matplotlib.pyplot as plt
import pandas
import seaborn as sns; sns.set()
from numpy.matlib import randn

conn_string = "host='localhost' dbname='temp-2017' user='postgres' password='16a10a'"
conn = psycopg2.connect(conn_string)
df = pandas.read_sql("SELECT tasks.indate FROM mvs100k.tasks",conn)
df1 = df.resample('d', on='indate').size().reset_index(name='number of launchings')
df1['day'] = df1['indate'].dt.strftime('%a')
g = df1.resample('W', on='indate')['indate']
df1['week'] = g.transform('first').dt.strftime('%Y-%m-%d') + ' - ' + g.transform('last').dt.strftime('%Y-%m-%d')
pivot_table = df1.pivot('week','day',"number of launchings")
print(pivot_table.columns.tolist())
days = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']

ax = sns.heatmap(pivot_table[days])
plt.show()
#print(df1[df2])

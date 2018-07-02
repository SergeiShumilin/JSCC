# Author: Sergei Shumilin
# Organisation: Joint Super Computer Center of the Russian Academy of Sciences
# Copyright: This module has been placed in the public domain.

"""
This module makes analysis of PostgreSQL database containing information about using of supercomputers belonging to
Joint SuperComputer Center. It builds a heatmap of number of tasks included into the system by users per day of the week

It's aimed to get the  heat map depicting the number of tasks included in a system by users for every system of
(broadwell, haswell, mvs10p, mvs100k)


How To Use This Module
======================
(See the individual classes, methods, and attributes for details.)



"""

import psycopg2
import pandas
import seaborn as sns;

sns.set()
import matplotlib.pyplot as plt
import get_psql_table

df = get_psql_table.get_table()

df1 = df.resample('d', on='indate').size().reset_index(name='number of launchings')

df1['day'] = df1['indate'].dt.strftime('%a')

g = df1.resample('W', on='indate')['indate']

df1['week'] = g.transform('first').dt.strftime('%Y-%m-%d') + ' - ' + g.transform('last').dt.strftime('%Y-%m-%d')
pivot_table = df1.pivot('week', 'day', "number of launchings")

days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

ax = sns.heatmap(pivot_table[days])
plt.show()

import get_psql_table
import pandas as pd
import matplotlib.pyplot as plt

def get_queue_length_table():
    df = get_psql_table.get_table('tasks.indate, runs.rundate',
                                  'mvs100k.tasks join mvs100k.runs on tasks.tid = runs.tid')

    indates = pd.DataFrame()
    indates["time"] = df.indate
    indates["queue_length"] = 1

    rundates = pd.DataFrame()
    rundates["time"] = df.rundate
    rundates["queue_length"] = -1

    queue_length_table = pd.concat([indates, rundates])
    queue_length_table = queue_length_table.sort_values(by=['time'])
    queue_length_table = queue_length_table.groupby(['time']).sum()
    queue_length_table.queue_length = queue_length_table.queue_length.cumsum()

    return queue_length_table


get_queue_length_table().plot(kind='area')
plt.show()


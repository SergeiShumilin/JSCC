import get_psql_table
import pandas as pd
import matplotlib.pyplot as plt


def plot_queue_length_table():
    indate_table = get_psql_table.get_table('tasks.indate as time','mvs10p.tasks')
    indate_table["queue_length"] = 1
    print(indate_table)


    rundate_table = get_psql_table.get_table('runs.rundate as time, runs.exittype','mvs10p.runs')
    rundate_table["queue_length"] = -1
    print(rundate_table)
    rundate_table.loc[(rundate_table['exittype']==0) | (rundate_table['exittype']==5),'queue_length']=0
    print(rundate_table)
    rundate_table = rundate_table.drop(['exittype'],axis=1)
    print(rundate_table)
    queue_length_table = pd.concat([indate_table, rundate_table])
    queue_length_table = queue_length_table.sort_values(by=['time'])
    queue_length_table = queue_length_table.groupby(['time']).sum()
    queue_length_table.queue_length = queue_length_table.queue_length.cumsum()
    print(queue_length_table
          )

    queue_length_table.plot()
    plt.show()

plot_queue_length_table()
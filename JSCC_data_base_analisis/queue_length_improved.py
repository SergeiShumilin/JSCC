import get_psql_table
import pandas as pd
import matplotlib.pyplot as plt


def plot_queue_length_table(system_name,agreggate_by):
    indate_table = get_psql_table.get_table('tasks.indate as time',system_name+'.tasks')
    indate_table = add_queue_column(indate_table,1)



    rundate_table = get_psql_table.get_table('runs.rundate as time',system_name+'.runs')
    rundate_table = add_queue_column(rundate_table,-1)



    stopdate_table = get_psql_table.get_table('runs.stopdate as time, runs.exittype', system_name+'.runs')
    stopdate_table = add_queue_column(stopdate_table,0)
    stopdate_table = alter_exittype(stopdate_table,1)
    stopdate_table = drop_exittype_column(stopdate_table)
    print(stopdate_table)

    queue_length_table = concatenate_tables(indate_table,rundate_table,stopdate_table)
    queue_length_table = queue_length_table.sort_values(by=['time'])
    queue_length_table = queue_length_table.groupby(['time']).sum()
    queue_length_table = queue_length_table.resample(agreggate_by).sum()
 #   queue_length_table.queue_length = queue_length_table.queue_length.cumsum()

    queue_length_table.plot()
    plt.show()

def alter_exittype(table,for_what_number):
    table.loc[(table['exittype'] == 0) | (table['exittype'] == 5), 'queue_length'] = for_what_number
    return table

def add_queue_column(table,default_value):
    table["queue_length"] = default_value
    return table

def drop_exittype_column(table):

    return table.drop('exittype',axis=1)

def concatenate_tables(table_1,table_2,table_3):
    supertable = pd.concat([table_1, table_2])
    supertable = pd.concat([supertable, table_3])
    return supertable


plot_queue_length_table('mvs10p','W')
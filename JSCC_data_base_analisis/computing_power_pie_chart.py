import get_psql_table
import pandas as pd
import matplotlib.pyplot as plt


def plot_computer_power_pie_chart():
    table = get_psql_table.get_table('runs.tid,runs.rundate,runs.stopdate,tasks.nproc','mvs10p.runs left join'
                                     ' mvs10p.tasks on runs.tid = tasks.tid')
    table['nodes_per_hour']=table.apply(lambda row: ((pd.Timedelta(row.stopdate - row.rundate).seconds)/3600)*row.nproc, axis=1)
    table = table.drop(['rundate','stopdate','nproc'],axis = 1)
    table = table.groupby(['tid']).sum()
    table = table.reset_index()


    nproc_table = get_psql_table.get_table('tasks.tid,tasks.nproc','mvs10p.tasks')

    table = table.merge(nproc_table,how='left')

    total_nodes_per_hour_power = table['nodes_per_hour'].sum()
    print(total_nodes_per_hour_power)
    labels = '0-16','16-32','32-64','64-128','128-256','256-512','512-1024','1024-2048'
    tuple = [(0,16),(16,32),(32,64),(64,128),(128,256),(256,512),(512,1024),(1024,2048)]

    statistics = [count_partial_power(table,pair[0],pair[1]) for pair in tuple]
    statistics = (statistics/total_nodes_per_hour_power)
    print(statistics)

    fig1, ax1 = plt.subplots()
    ax1.pie(statistics, autopct='%1.1f%%', labels=labels,
            shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    plt.show()


def select_rows(table, low, high):
    table = table[(table['nproc']>=low) & (table['nproc']<= high)]
    return table

def count_partial_power(table,low,high):
    table = select_rows(table,low+1,high)

    partial_power=table['nodes_per_hour'].sum()
    return partial_power



plot_computer_power_pie_chart()
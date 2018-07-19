import get_psql_table
import pandas as pd
import matplotlib.pyplot as plt
import seaborn

def plot_computer_power_pie_chart(tuple):
    table = get_psql_table.get_table('runs.tid,runs.rundate,runs.stopdate,tasks.nproc','mvs10p.runs left join'
                                     ' mvs10p.tasks on runs.tid = tasks.tid')
    add_nodes_per_hour_column(table)
    table = drop_columns(table)

    table = table.groupby(['tid']).sum()

    table = table.reset_index()

    nproc_table = get_psql_table.get_table('tasks.tid,tasks.nproc','mvs10p.tasks')

    table = table.merge(nproc_table,how='left')

    seaborn.set()

    fig1, ax1 = plt.subplots()

    ax1.pie(get_percentage_list(table,tuple)[0], autopct='%1.1f%%', labels=get_percentage_list(table,tuple)[1],
            shadow=False, startangle=80,pctdistance=0.75,textprops={'fontsize': 14},wedgeprops=dict(width=0.5))

    ax1.set_title('Power distribution',fontsize=16)

    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    plt.show()


def drop_columns(table):
    table = table.drop(['rundate','stopdate','nproc'],axis = 1)
    return table

def add_nodes_per_hour_column(table):
    table['nodes_per_hour']=table.apply(lambda row: ((pd.Timedelta(row.stopdate - row.rundate).seconds)/3600)*row.nproc, axis=1)
    return table

def select_rows(table, low, high):
    table = table[(table['nproc']>=low) & (table['nproc']<= high)]
    return table

def count_partial_power(table,low,high):
    table = select_rows(table,low+1,high)

    partial_power=table['nodes_per_hour'].sum()
    return partial_power

def get_labels(tuple):
    labels = [str(pair[0])+'-'+str(pair[1]) for pair in tuple]
    return labels

def get_percentage_list(table, tuple):
    total_nodes_per_hour_power = table['nodes_per_hour'].sum()
    list_of_percentage = [count_partial_power(table, pair[0], pair[1]) for pair in tuple]
    list_of_percentage = (list_of_percentage / total_nodes_per_hour_power)
    print(list_of_percentage)
    labels = get_labels(tuple)
    if (sum(list_of_percentage)<1):
       return add_others_wedge(list_of_percentage,labels)
    return list_of_percentage,labels

def add_others_wedge(list_of_percentage,labels):
    others_percent = 1 - sum(list_of_percentage)
    if (others_percent)<1:
        return list_of_percentage,labels
    list_of_percentage = list_of_percentage.tolist()
    list_of_percentage.append(others_percent)
    labels.append('Others')
    return list_of_percentage,labels

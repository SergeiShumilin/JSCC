import get_psql_table
import pandas as pd
import matplotlib.pyplot as plt


def plot_computer_power_pie_chart():
    table = get_psql_table.get_table('runs.tid,runs.rundate,runs.stopdate,tasks.nproc','mvs10p.runs left join'
                                     ' mvs10p.tasks on runs.tid = tasks.tid')
    table['nodes_per_hour']=table.apply(lambda row: (pd.Timedelta(row.rundate - row.stopdate).seconds)/3600, axis=1)
    # как в DF преобразовать рахницу дат в часы


    print(table)










plot_computer_power_pie_chart()
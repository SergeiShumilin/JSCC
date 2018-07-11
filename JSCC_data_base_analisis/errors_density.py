import get_psql_table
import pandas as pd
import matplotlib.pyplot as plt


def errors_density():

    errors_table = get_psql_table.get_table('runs.stopdate as time, runs.exittype', 'mvs10p.runs')
    errors_table = errors_table.sort_values(by=['time'])
    errors_table.plot()
    plt.show()




errors_density()
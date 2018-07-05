"""
# Author: Sergei Shumilin
# Organisation: Joint Super Computer Center of the Russian Academy of Sciences
# Copyright: This module has been placed in the public domain.

This module analyses the database containing information about usage of supercomputer and plots a graph representing
dependency between length of queue of systems waiting to be launched.

How To Use This Module
======================
(See the individual classes, methods, and attributes for details.)

1. import this module and launch ``plot_queue_length_table()``.

"""
import get_psql_table
import pandas as pd
import matplotlib.pyplot as plt

def get_queue_length_table():
    """
    Retrieve data from database and transform it to the form convenient for plotting.

    Function uses Pandas and manipulates the dataframe's structure.

    """
    # Compose a query for database and get a table
    df = get_psql_table.get_table('tasks.indate, runs.rundate',
                                  'mvs100k.tasks join mvs100k.runs on tasks.tid = runs.tid')

    # Create new dataframe with new ``queue_length`` column with all 1 values.
    indates = pd.DataFrame()
    indates["time"] = df.indate
    indates["queue_length"] = 1

    # Create new dataframe with new ``queue_length`` column with all -1 values.
    rundates = pd.DataFrame()
    rundates["time"] = df.rundate
    rundates["queue_length"] = -1

    # Concatenate two dataframes
    queue_length_table = pd.concat([indates, rundates])

    # Sort by date
    queue_length_table = queue_length_table.sort_values(by=['time'])

    # Exclude repetitive rows
    queue_length_table = queue_length_table.groupby(['time']).sum()

    # Summarize all 1 and -1 values and get the total number for every date in the table
    queue_length_table.queue_length = queue_length_table.queue_length.cumsum()

    return queue_length_table


def plot_queue_length_table():
    """Plot the time - queue_length graph."""
    get_queue_length_table().plot()
    plt.show()


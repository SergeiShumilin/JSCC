# Author: Sergei Shumilin
# Organisation: Joint Super Computer Center of the Russian Academy of Sciences
# Copyright: This module has been placed in the public domain.

"""
This module makes analysis of PostgreSQL database containing information about using of supercomputers belonging to
Joint SuperComputer Center. It builds a heatmap of some parameter frequency per day of the week.

It's aimed to get the  heat map depicting the number of tasks included in a system by users for every system of
(broadwell, haswell, mvs10p, mvs100k).

It uses ``pandas`` to retrieve information from PostgreSQL database.
It uses ``seaborn`` to plot the heatmap and it's default colormap.

For example:

You've got this:
     +-------------------+
     |      indate       |
     +===================+
     |2016-12-19 12:16:00|
     |2016-12-19 12:21:00|
     |2016-12-20 12:32:00|
     |2016-12-20 12:34:00|
     +-------------------+

You can aggregate it this way and calculate the number of rows put together:
      ===========  ======================
           indate  number of launchings
      ===========  ======================
      2016-12-19             2
      2016-12-20             3
      2016-12-21             4
      2016-12-22             5
                ...
      ===================================

Finally the function ``make_heatmap`` plots a heatmap based on this table:
    =======================  =========  =====================
              week           day        number of launchings
    =======================  =========  =====================
    2016-12-19 - 2016-12-25   Mo                2
    2016-12-19 - 2016-12-25   Tu                3
    2016-12-19 - 2016-12-25   We                4
    2016-12-19 - 2016-12-25   Th                5
                            ...
    =======================  ========  ======================

How To Use This Module
======================
(See the individual classes, methods, and attributes for details.)

1. Use ``make_heatmap(what, from_table)`` to plot a heatmap.

2. Define the query to the database in the ``make_heatmap`` arguments.
    If you need to change the connection parameters - see  ``get_psql_table`` module.

"""

__docformat__ = 'restructuredtext'

import seaborn as sns
import matplotlib.pyplot as plt
import get_psql_table


def make_heatmap(what='tasks.indate', from_table='mvs100k.tasks'):
    """
    Plot a heatmap basing on a single time row as a column.

    See the example in the module description.

    :param what: the information you need to get from the table
    :param from_table: the table you need to get info from
    """
    df = get_psql_table.get_table(what=what, from_table=from_table)
    df = add_number_of_launchings_column(df)
    df = add_day_of_week_column(df)
    df = transform_week_column(df)
    sns.heatmap(pivot_the_dataframe(df))
    plt.show()


def add_number_of_launchings_column(dataframe):
    """
    Add number of launchings column. The function aggregates original time row and calculates how many rows
    were aggregated into every new one.

    :param dataframe: pandas dataframe
    :return: dataframe with added number_of_launching column
    """
    dataframe = dataframe.resample('d', on='indate').size().reset_index(name='number of launchings')
    return dataframe


def add_day_of_week_column(dataframe):
    """
    Add `day` column to the table.

    :param dataframe: pandas dataframe
    :return: pandas dataframe
    """
    dataframe['day'] = dataframe['indate'].dt.strftime('%a')
    return dataframe


def transform_week_column(dataframe):
    """
    Alter the ``week`` column into the  `2016-12-19 - 2016-12-25` view

    :param dataframe: pandas dataframe
    :return: pandas dataframe
    """
    g = dataframe.resample('W', on='indate')['indate']
    dataframe['week'] = g.transform('first').dt.strftime('%Y-%m-%d') + ' - ' + \
                        g.transform('last').dt.strftime('%Y-%m-%d')
    return dataframe


def pivot_the_dataframe(dataframe):
    """
    Alter the dataframe to make it suitable for plotting heatmap.

    The method description:
    https://pandas.pydata.org/pandas-docs/stable/reshaping.html

    The ``days`` array defines the sequence of day of the week plotted on the heatmap.

    :param dataframe:
    :return: pivoted table
    """
    sns.set()
    pivot_table = dataframe.pivot('week', 'day', "number of launchings")
    days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    return pivot_table[days]

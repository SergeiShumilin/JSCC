# Author: Sergei Shumilin
# Organisation: Joint Super Computer Center of the Russian Academy of Sciences
# Copyright: This module has been placed in the public domain.

"""
This module returns a DataFrame retrieved from PostgreSQL database.
It's aimed to get the table composing a query to the database.
The connection closes by the using of the `with as` construction.

How To Use This Module
======================
(See the individual classes, methods, and attributes for details.)

1) Use get_table function to get a table from a database.

2) Change or leave default the connection parameters in the get_table signature.

3) Set the `what` param. to indicate what you need to retrieve from the table.

4) Set the `from_table` to indicate from what table you need to get the info from.

For example: `what`== 'tasks.indate', `from_table` == 'mvs100k.tasks' gives:
"SELECT tasks.indate FROM mvs100k.tasks"


"""

import psycopg2
import pandas


def get_table(what ='tasks.indate', from_table='mvs100k.tasks', host='localhost', dbname='temp-2017', user='postgres',
              password='16a10a'):
    """
    Return a pandas DataFrame from the PostgreSQL database.

    Composes a query to the database. And returns it in the form of a pandas DataFrame.

    :param what: info to retrieve from the table
    :param from_table: the table you need to get info from
    :param host: hostname
    :param dbname: database name
    :param user: user name
    :param password: user's password for the database
    :return: DataFrame with information retrieved from the database
    :rtype: pandas DataFrame
    """
    conn_string = "host=" + host + " dbname=" + dbname + " user=" + user + " password=" + password
    with psycopg2.connect(conn_string) as conn:
        df = pandas.read_sql("SELECT " + what + " FROM " + from_table, conn)
    return df

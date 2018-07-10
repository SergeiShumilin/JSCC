"""
# Author: Sergei Shumilin
# Organisation: Joint Super Computer Center of the Russian Academy of Sciences
# Copyright: This module has been placed in the public domain.

This module analyses the database containing information about completion codes of tasks launched on two supercomputer
systems.

How To Use This Module
======================
(See the individual classes, methods, and attributes for details.)

1. import this module and launch ``plot_error_codes_bar(system_name_1, system_name_2)``.
"""

import get_psql_table
import matplotlib.pyplot as plt


def get_error_codes_dict(system):
    """
    Return a dictionary representing number of completion codes in the database.

    :param system: name of supercomputer system in the database.
    """

    # Compose an sql query to the database and return a dataframe
    number_of_errors = [get_psql_table.get_table('runs.exittype',
                                                 '{0}.runs where runs.exittype = {1}'.format(system, i))[
                                                 'exittype'].count() for i in range(-1, 6)]
    result_dict = dict(enumerate(number_of_errors, start=-1))
    return result_dict


def plot_error_codes_bar(system_name_1, system_name_2):
    """
    Plot a bar graph to represent the number of completion codes in the table of running sessions.

    :param system_name_1: name of system1 to compare
    :param system_name_2: name of system2 to compare
    """
    fig = plt.subplot()

    sys1_total_num_of_launches = sum(get_error_codes_dict(system_name_1).values())
    sys2_total_num_of_launches = sum(get_error_codes_dict(system_name_2).values())

    fig.bar(get_error_codes_dict(system_name_1).keys(), get_error_codes_dict(system_name_1).values(),
            label=system_name_1 + ', total = ' + str(sys1_total_num_of_launches) + ' launches',
            alpha=0.8,
            align='edge',
            width=-0.4)
    fig.bar(get_error_codes_dict(system_name_2).keys(), get_error_codes_dict(system_name_2).values(),
            label=system_name_2 + ', total = ' + str(sys2_total_num_of_launches) + ' launches',
            alpha=0.8,
            align='edge',
            width=0.4)

    fig.set_title('Number of completion codes', size=14)
    plt.legend(loc='upper right')
    plt.show()

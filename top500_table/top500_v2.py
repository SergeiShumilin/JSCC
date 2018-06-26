# Author: Sergei Shumilin
# Organisation: Joint Super Computer Center of the Russian Academy of Sciences
# Copyright: This module has been placed in the public domain.

"""
This module retrieves information from the top500 supercomputers (SC) table
from top500.org and defines the following indicators:

a) The total peak performance (Rpeak [TFlop/s]) of the SC in a given country;

б) The ratio of peak performance of SCs based on accelerators to the entire
performance of all SC in the given country.

How To Use This Module
======================
(See the individual classes, methods, and attributes for details.)

1. Download the TOP500 exel file on your computer.

2. Convert it to the .csv format (Use comma separation, pay attention to encoding)

3. In the get_the_full_table() function define the path to the .csv table.

4. Use get_the_countrys_total_peak_perfomance(region) function to get the total peak performance (Rpeak [TFlop/s]) of
the SCs in the given country.
    The countries you can get the info about (The :arg region must be exactly similar as shown down:
        a) 'China'
        b) 'United States'
        c) 'EU' (European Union)
        d) 'Russia'
        e) 'Others'

5. Use get_accelerators_to_entire_performance_ratio(region) function to get the ratio of peak performance of SCs based
 on accelerators to the entire performance of all SCs in the given country.
    The countries you can get the info about (The :arg region must be exactly similar as shown down:
        a) 'China'
        b) 'United States'
        c) 'EU' (European Union)
        d) 'Russia'
        e) 'Others'

"""

__docformat__ = 'restructuredtext'

import pandas as pd


def make_notnull_table(full_table):
    table_without_notnull_values = full_table[full_table['Accelerator/Co-Processor Cores'].notnull()]
    return table_without_notnull_values

def get_the_full_table():
    top500_table = pd.read_csv('TOP500_201806.csv', sep=',')
    top500_table.set_index(['Rank'], inplace=True)
    return top500_table

def get_total_peak_performance():
    table = get_the_full_table()
    return 'The total peak performance is ' + str(table['Rpeak [TFlop/s]'].sum())

def get_euro_countries_table():
    table = get_the_full_table()
    euro_countries_table = table[(table['Region']=='Northern Europe') |
                                 (table['Region']=='Western Europe')|
                                 (table['Region']=='Southern Europe')|
                                 (table['Region']=='Eastern Europe')& (table['Country']!='Russia')
                                 & (table['Country'] != 'Switzerland')]
    return euro_countries_table

def get_accelerators_to_entire_performance_ratio(region):
    table = get_region_table(region)
    summary_peak_performance = table['Rpeak [TFlop/s]'].sum()
    table = make_notnull_table(table)
    summary_country_peak_performance = table['Rpeak [TFlop/s]'].sum()
    return "The ratio of peak performance of SCs based on accelerators to the " + region + \
           "'s summary peak performance" + " is " + str(
        summary_country_peak_performance / summary_peak_performance)

def get_region_table(region):
    if region == 'EU':
        table = get_euro_countries_table()
    elif region == 'Others':
        table = get_other_countries_table()
    else:
        table = get_the_countrys_table(region)
    return table

def get_other_countries_table():
    table = get_the_full_table()
    other_countries_table = table[(table['Region']!='Northern Europe')&
                                 (table['Region']!='Western Europe')&
                                 (table['Region']!='Southern Europe')&
                                 (table['Region']!='Eastern Europe')
                                  &(table['Country']!='Russia')
                                  & (table['Country']!='United States')
                                  & (table['Country']!='China')]
    return other_countries_table

def get_the_countrys_table(country):
    table = get_the_full_table()
    country_table = table[table['Country'] == country]
    return country_table

def get_the_countrys_total_peak_perfomance(region):
    region_table = get_region_table(region)
    summary__country_peak_performance = region_table['Rpeak [TFlop/s]'].sum()
    return 'The total performance of ' + region + ' is ' + str(summary__country_peak_performance)

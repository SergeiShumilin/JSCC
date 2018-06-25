import pandas as pd
import urllib
import html5lib
import bs4
import re

myurl100 = urllib.request.urlopen('https://www.top500.org/list/2018/06/?page=1')
myurl200 = urllib.request.urlopen('https://www.top500.org/list/2018/06/?page=2')
myurl300 = urllib.request.urlopen('https://www.top500.org/list/2018/06/?page=3')
myurl400 = urllib.request.urlopen('https://www.top500.org/list/2018/06/?page=4')
myurl500 = urllib.request.urlopen('https://www.top500.org/list/2018/06/?page=5')
top500_table100 = pd.read_html(myurl100, flavor='bs4',keep_default_na = False)
top500_table200 = pd.read_html(myurl200, flavor='bs4',keep_default_na = False)
top500_table300 = pd.read_html(myurl300, flavor='bs4',keep_default_na = False)
top500_table400 = pd.read_html(myurl400, flavor='bs4',keep_default_na = False)
top500_table500 = pd.read_html(myurl500, flavor='bs4',keep_default_na = False)
top100 = pd.concat(top500_table100)
top200 = pd.concat(top500_table200)
top300 = pd.concat(top500_table300)
top400 = pd.concat(top500_table400)
top500 = pd.concat(top500_table500)
top_500_full = top100.append(top200, ignore_index=True). \
    append(top300, ignore_index=True). \
    append(top400, ignore_index=True). \
    append(top500, ignore_index=True)
top_500_full.set_index(['Rank'], inplace=True)
#smth = top_500_full['System'].str.contains(r'\b\d+C\b', na = False)
#print(smth)
#print('----------------------------------------------------------------')
#print((smth==True).sum())
#print('----------------------------------------------------------------')
#print(type(top_500_full['Rpeak (TFlop/s)']))
#print(top_500_full['Rpeak (TFlop/s)'].cumsum())
#top_500_full.to_csv('top500.csv',sep=',',index_label='Rank')
#'----------------------------------------------------------------')
"""true_false_table = table_with_notnull_values['System'].str.contains(r'\b\d+C\b')
    return (true_false_table == True).sum()"""

def get_the_number_of_inclusions(country):
    country_table = top_500_full[top_500_full['Site'].str.contains(country)& top_500_full['System'].str.contains(r'\b\d+C\b')]
    summary_peak_performance = top_500_full['Rpeak (TFlop/s)'].sum()
    print(summary_peak_performance)
    summary__country_peak_performance = country_table['Rpeak (TFlop/s)'].sum()
    print(summary__country_peak_performance)
    return 'The relation of peak performance to the summary world one of '+country+' is ' + str(summary__country_peak_performance/summary_peak_performance)


print(get_the_number_of_inclusions('United States'))
print(get_the_number_of_inclusions('China'))
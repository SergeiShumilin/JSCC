import pandas as pd


def get_the_csv_notnull_table():
    top500_table = pd.read_csv('TOP500_201806.csv', sep=',')
    top500_table.set_index(['Rank'], inplace=True)
    # print('The total peak performance is ' + str(top500_table['Rpeak [TFlop/s]'].sum()))
    table_with_notnull_values = top500_table[top500_table['Accelerator/Co-Processor Cores'].notnull()]
    return table_with_notnull_values

def get_the_csv_full_table():
    top500_table = pd.read_csv('TOP500_201806.csv', sep=',')
    top500_table.set_index(['Rank'], inplace=True)
    print('The total peak performance is ' + str(top500_table['Rpeak [TFlop/s]'].sum()))
    return top500_table

def get_the_ratio1(country):
    country_table = get_the_csv_notnull_table[get_the_csv_notnull_table['Country'] == country]
    summary_peak_performance = get_the_csv_notnull_table['Rpeak [TFlop/s]'].sum()
    summary__country_peak_performance = country_table['Rpeak [TFlop/s]'].sum()
    return 'The relation of peak performance to the summary world one of '+country+' is ' + str(summary__country_peak_performance/summary_peak_performance)

def get_the_ratio2(country):
    table = get_the_csv_full_table()
    country_table = table[table['Country'] == country]
    summary_peak_performance = country_table['Rpeak [TFlop/s]'].sum()
    country_table = country_table[country_table['Accelerator/Co-Processor Cores'].notnull()]
    summary_country_peak_performance = country_table['Rpeak [TFlop/s]'].sum()
    return "The relation of peak performance to the country's summary one of " + country + ' is ' + str(
        summary_country_peak_performance / summary_peak_performance)



def get_euro_countries_table():
    table = get_the_csv_full_table()
    euro_countries_table = table[(table['Region']=='Northern Europe') |
                                 (table['Region']=='Western Europe')|
                                 (table['Region']=='Southern Europe')|
                                 (table['Region']=='Eastern Europe')& (table['Country']!='Russia')]
    return euro_countries_table


def get_euro_countries_ratio(region,table):
    table = table
    summary_peak_performance = table['Rpeak [TFlop/s]'].sum()
    table = table[table['Accelerator/Co-Processor Cores'].notnull()]
    summary_country_peak_performance = table['Rpeak [TFlop/s]'].sum()
    return "The relation of peak performance to the country's summary one of" +region + "is " + str(
        summary_country_peak_performance / summary_peak_performance)


def get_other_countries_table():
    table = get_the_csv_full_table()
    other_countries_table = table[(table['Region']!='Northern Europe')&
                                 (table['Region']!='Western Europe')&
                                 (table['Region']!='Southern Europe')&
                                 (table['Region']!='Eastern Europe')
                                  &(table['Country']!='Russia')
                                  & (table['Country']!='United States')
                                  & (table['Country']!='China')]
    return other_countries_table

print(get_the_ratio2('China'))
print(get_the_ratio2('United States'))
print(get_the_ratio2('Russia'))
print(get_euro_countries_ratio('European Union',get_euro_countries_table()))
print(get_euro_countries_ratio('other countries',get_other_countries_table()))
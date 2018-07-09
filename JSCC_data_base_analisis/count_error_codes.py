import get_psql_table
import pandas as pd
import matplotlib.pyplot as plt

def get_error_codes_dict(system):

    number_of_errors = [get_psql_table.get_table('runs.exittype',
                        '{1}.runs where runs.exittype = {0}'.format(i,system))['exittype'].count() for i in range(-1,6)]
    result_dict = dict(enumerate(number_of_errors,start = -1))
    return result_dict


def plot_bar(dict1,dict2):
    fig = plt.subplot()
    fig.bar(dict1.keys(), dict1.values(),label='mvp10p, total = 77135',alpha= 0.8)
    fig.bar(dict2.keys(), dict2.values(),label='mvp100k, total = 24934',alpha= 0.8)
    fig.set_title('Number of error codes. Total amount = 77135')
    plt.legend(loc='upper right')
    plt.show()



plot_bar(get_error_codes_dict('mvs10p'),get_error_codes_dict('mvs100k'))
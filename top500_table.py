import pandas as pd
import urllib
import html5lib
import bs4

myurl100 = urllib.request.urlopen('https://www.top500.org/list/2017/11/?page=1')
myurl200 = urllib.request.urlopen('https://www.top500.org/list/2017/11/?page=2')
myurl300 = urllib.request.urlopen('https://www.top500.org/list/2017/11/?page=3')
myurl400 = urllib.request.urlopen('https://www.top500.org/list/2017/11/?page=4')
myurl500 = urllib.request.urlopen('https://www.top500.org/list/2017/11/?page=5')
top500_table100 = pd.read_html(myurl100, flavor='bs4')
top500_table200 = pd.read_html(myurl200, flavor='bs4')
top500_table300 = pd.read_html(myurl300, flavor='bs4')
top500_table400 = pd.read_html(myurl400, flavor='bs4')
top500_table500 = pd.read_html(myurl500, flavor='bs4')
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
smth = top_500_full[top_500_full['System'].str.contains('Phi', na = False)]
print(smth)
print('----------------------------------------------------------------')
#print((smth==True).sum())
# top_500_full.to_csv('top500.csv',sep=';')

def get_the_top500_table(year,month):
    """

    :param year:
    :param month:
    :return:
    """
    for i in range(0,5):
        myurl100 = urllib.request.urlopen('https://www.top500.org/list/{}/{}/?page={}'.format(year,month,i))
        myurl200 = urllib.request.urlopen('https://www.top500.org/list/2017/11/?page=2')
        myurl300 = urllib.request.urlopen('https://www.top500.org/list/2017/11/?page=3')
        myurl400 = urllib.request.urlopen('https://www.top500.org/list/2017/11/?page=4')
        myurl500 = urllib.request.urlopen('https://www.top500.org/list/2017/11/?page=5')
        top500_table100 = pd.read_html(myurl100, flavor='bs4')
        top500_table200 = pd.read_html(myurl200, flavor='bs4')
        top500_table300 = pd.read_html(myurl300, flavor='bs4')
        top500_table400 = pd.read_html(myurl400, flavor='bs4')
        top500_table500 = pd.read_html(myurl500, flavor='bs4')
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
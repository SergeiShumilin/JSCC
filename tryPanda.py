import pandas
import numpy as np

sdata = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}
states = ['California', 'Ohio', 'Oregon', 'Texas']
obj1 = pandas.Series(sdata)
obj2 = pandas.Series(sdata, index=states)

data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada', ], 'year': [2000, 2001, 2002, 2001, 2002],
        'pop': [1.5, 1.7, 3.6, 2.4, 2.9]}
frame = pandas.DataFrame(data)

# Автоматическое заполнение объекта Series
col = pandas.Series(['blue', 'purple', 'yellow'], index=[0, 2, 4])
print(col.reindex(range(3), method='ffill'))

# Составление простого DataFrame (прим. метод reshape)
data = pandas.DataFrame(np.arange(16).reshape((4, 4)), index=['Ohio', 'Colorado', 'Utah', 'New York'],
                        columns=['one', 'two', 'three', 'four'])
print(data.drop(['Ohio'])) 

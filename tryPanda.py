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
# print(col.reindex(range(3), method='ffill'))

# Составление простого DataFrame (прим. метод reshape)
data = pandas.DataFrame(np.arange(16).reshape((4, 4)), index=['Ohio', 'Colorado', 'Utah', 'New York'],
                        columns=['one', 'two', 'three', 'four'])
# print(data.drop(['Ohio']))

# Составление временного ряда через заданный промежуток
arr = pandas.date_range('1/1/2000', '1/3/2000 23:59', freq='4h')
# print(arr)

rng = pandas.period_range('1/1/2000', '6/30/2000', freq='M')
# print(rng)
# print(pandas.Series(np.random.randn(6),index=rng))


# Агрегирование данных (среднее значение) при понижении частоты временного промежутка
rng = pandas.date_range('1/1/2000', periods=100, freq='D')
ts = pandas.Series(np.random.randn(len(rng)), index=rng)
print(ts)
print(ts.resample('M').mean())

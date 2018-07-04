import get_psql_table
import pandas as pd

def plot_queue_length():
    pass

#df = get_psql_table.get_table('tasks.tid, tasks.indate, runs.rundate','mvs100k.tasks join mvs100k.runs on tasks.tid = runs.tid')

df = pd.DataFrame([["2018-01-01 12:00", "2018-01-01 15:00"], ["2018-01-01 16:00", "2018-01-01 20:00"], ["2018-01-01 16:30", "2018-01-01 20:00"], ["2018-01-01 17:00", "2018-01-01 21:00"]])
df.columns = ["starts", "finishes"]
print(df)
print('===========================================================================')
starts = pd.DataFrame()
starts["time"] = df.starts
starts["number_of_conc_progs"] = 1
print(starts)
print('===========================================================================')
finishes = pd.DataFrame()
finishes["time"] = df.finishes
finishes["number_of_conc_progs"] = -1
print(finishes)
print('===========================================================================')
result = pd.DataFrame()
result = pd.concat([starts,finishes])
print(result)
print('===========================================================================')
result = result.sort_values(by=['time'])
print(result)
print('===========================================================================')
result = result.groupby(['time']).sum()
print(result)
print('===========================================================================')
result.number_of_conc_progs = result.number_of_conc_progs.cumsum()


print(result)
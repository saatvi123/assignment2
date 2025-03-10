import pandas as pd

df = pd.read_csv("wdwM-military-23.csv", delimiter=";")

df['clock time'] = pd.to_datetime(df['clock time'], format='%H:%M:%S')

df['net time'] = pd.to_datetime(df['net time'], format='%H:%M:%S')

df['wait_time'] = (df['clock time'] - df['net time']).dt.total_seconds()

waittime = df.sort_values(by='wait_time', ascending=False).head(10)

waittime.to_csv("waittime.txt", index=False, sep='\t')

print(waittime)

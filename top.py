import pandas as pd
df = pd.read_csv("wdwM-military-23.csv", delimiter=";")

df['net time'] = pd.to_datetime(df['net time'], format='%H:%M:%S')

df['clock time'] = pd.to_datetime(df['clock time'], format='%H:%M:%S')

df['net_time_seconds'] = df['net time'].dt.hour * 3600 + df['net time'].dt.minute * 60 + df['net time'].dt.second

df['race_distance'] = 0 

df.loc[df['distance'].str.contains('marathon', case=False, na=False), 'race_distance'] = 26.2

df['minutes_per_mile'] = df['net_time_seconds'] / 60 / df['race_distance']

top = df.sort_values(by='minutes_per_mile').head(10)

top.to_csv("top.txt", index=False, sep='\t')

print(top)


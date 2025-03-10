import pandas as pd

df = pd.read_csv("wdwM-military-23.csv", delimiter=";")

df['net time'] = pd.to_datetime(df['net time'], format='%H:%M:%S')

women = df[df['gender'] == 'F'].sort_values(by='net time').head(10)

women.to_csv("women.txt", index=False, sep='\t')

print(women)

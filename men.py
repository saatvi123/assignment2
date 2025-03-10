import pandas as pd

df = pd.read_csv("wdwM-military-23.csv", delimiter=";")

df['net time'] = pd.to_datetime(df['net time'], format='%H:%M:%S')

men = df[df['gender'] == 'M'].sort_values(by='net time').head(10)

men.to_csv("men.txt", index=False, sep='\t')

print(men)

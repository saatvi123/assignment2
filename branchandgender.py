import pandas as pd

df = pd.read_csv("wdwM-military-23.csv", delimiter=";")

df['net time'] = pd.to_datetime(df['net time'], format='%H:%M:%S')

branches = df['branch'].unique()

result = []

for branch in branches:
    for gender in ['M','F']:
        top = df[(df['branch'] == branch) & (df['gender'] == gender)].sort_values(by='net time').head(5)
        result.append(top)

branchandgender = pd.concat(result)

branchandgender.to_csv("branchandgender.txt", index=False, sep='\t')

print(branchandgender)

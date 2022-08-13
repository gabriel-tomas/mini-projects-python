import pandas as pd
with open('project10/data.csv', 'a+') as a:
    a.read()
df = pd.read_csv('project10/data.csv')

print(df.to_string())
import pandas as pd
from statistics import mean
import numpy as np

positions = ('k', 'qb', 'rb', 'wr', 'te', 'def')
numTeams = 12
numStarters = {'k': 1, 
               'qb': 1, 
               'rb': 2, 
               'wr': 2, 
               'te': 1, 
               'def': 1}
data = []

for pos in positions:
    df = pd.read_csv('resources/{}.csv'.format(pos))
    df.dropna(inplace=True)
    benchmark = mean(df['FPTS'][:numStarters[pos] * numTeams])
    df['value'] = df['FPTS'] - benchmark
    df['pos'] = pos
    
    df = df[['Player', 'FPTS', 'value', 'pos']]
    df.set_index(df['Player'])
    print(df.head())
    
    data.append(df)
    
merged = pd.concat(data)
print(merged)
merged.sort_values('value', ascending=False, inplace=True)
merged.reset_index()
merged.to_csv('playerValues.csv')

import pandas as pd
from statistics import mean, stdev
import numpy as np

def analyze(numStarters, numTeams=12, how='mean'):
    data = []
    for pos in numStarters:
        df = pd.read_csv('resources/{}.csv'.format(pos))
        df.dropna(inplace=True)
        if how == 'mean':
            benchmark = mean(df['FPTS'][:numStarters[pos] * numTeams])
            df['value'] = df['FPTS'] - benchmark
        elif how == 'z':
            dev = stdev(df['FPTS'][:numStarters[pos] * numTeams])
            avg = mean(df['FPTS'][:numStarters[pos] * numTeams])
            df['value'] = (df['FPTS'] - avg) / dev
        
        df['pos'] = pos
        df = df[['Player', 'FPTS', 'value', 'pos']]
        df.set_index(df['Player'])
        
        data.append(df)
    return pd.concat(data)
    
numStarters = {'qb': 1, 
               'rb': 2, 
               'wr': 2, 
               #'def': 1,
               #'k': 1, 
               #'te': 1
               }

merged = analyze(how='mean', numStarters=numStarters, numTeams=12)
merged.sort_values('value', ascending=False, inplace=True)
merged.reset_index(inplace=True, drop=True)
merged.index += 1
merged.to_csv('playerValues.csv')

print(merged.head(25))

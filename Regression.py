#! python3

'''
 Notes
 - Feature:
 - Label:
 - Classifier:


'''

import pandas as pd
import quandl
import math
import numpy as np
from sklearn import preprocessing, cross_validation, svm

df = quandl.get('WIKI/GOOGL')

df = df[['Adj. Open', 'Adj. High','Adj. Low', 'Adj. Close','Adj. Volume',]]
df['HL_PCT'] = (df['Adj. High'] - df['Adj. Close']) / df['Adj. Close'] *100
df['PCT_Change'] = (df['Adj. Close'] - df['Adj. Open']) / df['Adj. Open'] *100

df = df[['Adj. Close','HL_PCT','PCT_Change','Adj. Volume',]]

forcast_col = 'Adj. Close'
df.fillna(-99999, inplace=True)

forcast_out = int(math.ceil(0.01*len(df)))

df['label'] = df[forcast_col].shift(-forcast_out)

print(df.head())

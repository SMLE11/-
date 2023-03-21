import pandas as pd
import numpy as np
from scipy.stats import pearsonr
from sklearn.preprocessing import StandardScaler
from  sklearn.linear_model import  LinearRegression
data = pd.read_csv('AAPL.csv',index_col=[0])
data.drop("Name",axis=1,inplace=True)
data['diff_high_low'] = data['High'] - data['Low']
data['diff_open_close'] = data['Open'] - data['Close']
data['ave'] = (data['Open']+data['Close']+data['High']+data['Low'])/4

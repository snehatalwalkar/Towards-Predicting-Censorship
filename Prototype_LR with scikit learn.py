            #Identifying Correlations between Google Trends Interest over Time Peaks and Censorship

import numpy as np
import pandas as pd
from datetime import datetime
import datetime as dt
import time
from matplotlib import pyplot as plt
import matplotlib as mpl
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error


#Fetch dataset : OONI + CitizenLab + Censoredplanet : Confirmed/Blockpage censorship measurements only!
path="C:\\zzz.csv"
df = pd.read_csv(path)

#datetime to float
df['Tfirst spike in trending'] = df['Tfirst spike in trending'].astype('datetime64[ns]')
df['Tfirst confirmed censorship'] = df['Tfirst confirmed censorship'].astype('datetime64[ns]')
def dt64_to_float(dt64):
    year = dt64.astype('M8[Y]')
    days = (dt64 - year).astype('timedelta64[D]')
    year_next = year + np.timedelta64(1, 'Y')
    days_of_year = (year_next.astype('M8[D]') - year.astype('M8[D]')
                    ).astype('timedelta64[D]')
    dt_float = 1970 + year.astype(float) + days / (days_of_year)
    return dt_float
df['Tfirst spike in trending'] = dt64_to_float(df['Tfirst spike in trending'].to_numpy())
df['Tfirst confirmed censorship'] = dt64_to_float(df['Tfirst confirmed censorship'].to_numpy())



#************************  LINEAR REGRESSION MODEL WITH SCIKIT   ***********************#

x = df['Tfirst spike in trending']
y = df['Tfirst confirmed censorship']

#Correlations between Tspike and Tcensorship
print(df.corr())
print(df.describe())
y = df['Tfirst spike in trending'].values.reshape(-1, 1)
X = df['Tfirst confirmed censorship'].values.reshape(-1, 1)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2)

SEED = 52

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = SEED)
regressor = LinearRegression()
regressor.fit(X_train, y_train)
print(regressor.intercept_)
print(regressor.coef_)
def calc(slope, intercept, spike):
    return slope*spike+intercept

#Prediction
#Let random spike date be 2020-09-01, float value is 1598932800.0 for time =0
censorship = calc(regressor.coef_, regressor.intercept_, 1598932800.0 )
print('Result: ',censorship)
censorship = regressor.predict([[1598932800.0 ]])

y_pred = regressor.predict(X_test)
df_preds = pd.DataFrame({'Actual': y_test.squeeze(), 'Predicted': y_pred.squeeze()})
print(df_preds)


#Model Evaluation
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
print(f'Mean absolute error: {mae:.2f}')
print(f'Mean squared error: {mse:.2f}')
print(f'Root mean squared error: {rmse:.2f}')





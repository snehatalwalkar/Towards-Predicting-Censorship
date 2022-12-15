            #Identifying Correlations between Google Trends Interest over Time Peaks and Censorship

import numpy as np
import pandas as pd
from datetime import datetime
import datetime as dt
import time
from matplotlib import pyplot as plt
import matplotlib as mpl


#Fetch dataset : OONI + CitizenLab + Censoredplanet : Confirmed/Blockpage censorship measurements only!
path="C:\\Data.csv"
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



#************************  LINEAR REGRESSION MODEL   ***********************#

x = df['Tfirst spike in trending']
y = df['Tfirst confirmed censorship']
def linear_regression(x, y):     
    N = len(x)
    x_mean = x.mean()
    y_mean = y.mean()
    B1_num = ((x - x_mean) * (y - y_mean)).sum()
    B1_den = ((x - x_mean)**2).sum()
    B1 = B1_num / B1_den
    B0 = y_mean - (B1*x_mean)
    reg_line = 'y = {} + {}β'.format(B0, round(B1, 3))
    return (B0, B1, reg_line)

#Supporting functions
#Correlation b/w Tfirst spike in trending & Tfirst confirmed censorship
def corr_coef(x, y):
    N = len(x)
    num = (N * (x*y).sum()) - (x.sum() * y.sum())
    den = np.sqrt((N * (x**2).sum() - x.sum()**2) * (N * (y**2).sum() - y.sum()**2))
    R = num / den
    return R



#RESULTS & MODEL EVALUATION
B0, B1, reg_line = linear_regression(x, y)
R = corr_coef(x, y)
print('\n\nRegression Line: ', reg_line)
print('\ny-intercept is :',B0,'Slope is:',B1)
print('\nLinear regression model Evaluation')
print('Correlation Coefficient: ', R)
print('Goodness of Fit: ', R**2)



#PLOT
plt.title("Correlations between Google Trends and Censorship")
plt.xlabel('Tspike')
plt.ylabel('Tcensorship')
plt.plot(range(100))
plt.xlim(2020, 2023)
plt.ylim(2020, 2023)
ax = plt.gca()
ax.set_aspect('equal')
ax.xaxis.set_major_locator(mpl.ticker.MaxNLocator(integer=True))
ax.yaxis.set_major_locator(mpl.ticker.MaxNLocator(integer=True))
plt.scatter(x,y,c="Blue")
plt.show()

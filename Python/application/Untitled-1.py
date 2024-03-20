# %%
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns
import warnings 

# %%

warnings.filterwarnings('ignore') 

# %%

%matplotlib

# %%
matplotlib.get_backend()

# %%
import matplotlib

# %%
matplotlib.get_backend()

# %%
%matplotlib

# %%
matplotlib.use('TkAgg')

# %%
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns
import warnings 

# %%
url = 'https://raw.githubusercontent.com/yangsbin/Meteo_data_analysis/master/data/wind_data.txt'

# %%

wind_data = pd.read_csv(url, sep = r'\s+', header = None, names = ['Year','Month','Day','Hour', 'WD','WS'])

# %%

wind_data.WS = wind_data.WS/10.0    

# %%

wind_data.head()   

# %%

from datetime import datetime   

# %%

datetimes = []

# %%

year_v = wind_data['Year'].values 

# %%

month_v = wind_data['Month'].values   

# %%

day_v = wind_data['Day'].values   

# %%

hour_v = wind_data['Hour'].values  

# %%
i in range(0, len(year_v)):
    datetimes.append(datetime(year_v[i], month_v[i], day_v[i], hour_v[i]))       

# %%

for i in range(0, len(year_v)):
    datetimes.append(datetime(year_v[i], month_v[i], day_v[i], hour_v[i]))     

# %%

wind_data.index = pd.Series(datetimes) 

# %%

wind_data.index.name = 'Datetime' 

# %%

wind_data.head()

# %%

wind_data[['Year','Month','WD', 'WS']].groupby(['Year', 'Month']).describe().head()

# %%

fg = plt.figure()

# %%

plt.subplot(121)
plt.plot(wind_data.WD)
plt.ylabel('Values')
plt.title('WD')

# %%

plt.subplot(122)
plt.plot(wind_data.WS)
plt.ylabel('Values')
plt.title('WS')

# %%

plt.subplots_adjust(top=0.92, bottom=0.41, left=0.10, right=0.95, hspace=0.25, wspace=0.55)

# %%
from windrose import WindroseAxes
import matplotlib.cm as cm

# %%
from windrose import WindroseAxes
import matplotlib.cm as cm

# %%

ax = WindroseAxes.from_ax()
ax.bar(wd_Jan.WD, ws_Jan.WS, normed=True, opening=0.8, edgecolor='black')
ax.set_legend()

# %%

ax = WindroseAxes.from_ax()
ax.contourf(wd_Jan.WD, ws_Jan.WS, bins=np.arange(0,9,1), cmap=cm.hot)
ax.contour(wd_Jan.WD, ws_Jan.WS, bins=np.arange(0,9,1), colors = 'black', lw=1)
ax.set_title('January')
ax.set_legend()

# %%

fg = plt.figure()

wd_Jan = wind_2012.loc[wind_2012['Month'] == 1, ['Month','WD']]
wd_Jul = wind_2012.loc[wind_2012['Month'] == 7, ['Month','WD']]

plt.subplot(121)
sns.distplot(wd_Jan.WD)
sns.distplot(wd_Jul.WD)
plt.ylabel('Probability')
plt.grid()
plt.legend(['Jan','Jul'], frameon = False)

ws_Jan = wind_2012.loc[wind_2012['Month'] == 1, ['Month','WS']]
ws_Jul = wind_2012.loc[wind_2012['Month'] == 7, ['Month','WS']]

plt.subplot(122)
sns.distplot(ws_Jan.WS)
sns.distplot(ws_Jul.WS)
plt.ylabel('Probability')
plt.xlabel('WS (m/s)')
plt.grid()
plt.legend(['Jan','Jul'], frameon = False)

plt.subplots_adjust(top=0.92, bottom=0.21, left=0.10, right=1.0, hspace=0.25, wspace=0.45)

# %%

outlier_index = np.logical_or(wind_data['WD'] > 360, wind_data['WS'] > 1000)
wind_data = wind_data.loc[~outlier_index, :]
print("{0} rows of data were removed".format(len(outlier_index)) )

# %%

wind_data[['Year','Month','WD', 'WS']].groupby(['Year', 'Month']).describe().head()

# %%

fg = plt.figure()

plt.subplot(121)
plt.plot(wind_data['WD'], linewidth=0.2)
plt.ylabel('Values')
plt.title('WD')

plt.subplot(122)
plt.plot(wind_data['WS'])
plt.ylabel('Values')
plt.title('WS')

plt.subplots_adjust(top=0.92, bottom=0.41, left=0.10, right=0.95, hspace=0.25, wspace=0.55)

# %%

wind_2012 = wind_data.loc[wind_data['Year']==2012, ['Month','Day','Hour', 'WD', 'WS']]

# %%

from windrose import WindroseAxes
import matplotlib.cm as cm

# %%

ax = WindroseAxes.from_ax()
ax.bar(wd_Jan.WD, ws_Jan.WS, normed=True, opening=0.8, edgecolor='black')
ax.set_legend()

# %%
fg = plt.figure()

plt.subplot(121)
ax = sns.distplot(wind_2012.WD)
plt.ylabel('Probability')
plt.grid()

plt.subplot(122)
ax = sns.distplot(wind_2012.WS)
plt.ylabel('Probability')
plt.xlabel('WS (m/s)')
plt.grid()

plt.subplots_adjust(top=0.92, bottom=0.21, left=0.10, right=1.0, hspace=0.25, wspace=0.45)

# %%
fg = plt.figure()

plt.subplot(121)
wd_2012 = wind_data[['Month','WD']]
sns.boxplot(x = 'WD', y = 'Month', data = wd_2012, orient = 'h', fliersize=0.5, linewidth = 0.7)

plt.subplot(122)
ws_2012 = wind_data[['Month','WS']]
ax = sns.boxplot(x = 'WS', y = 'Month', data = ws_2012, orient = 'h', fliersize=0.5, linewidth = 0.7)
ax.set_xlabel('WS (m/s)')

plt.subplots_adjust(top=0.92, bottom=0.21, left=0.10, right=1.0, hspace=0.25, wspace=0.45)

# %%

fg = plt.figure()

wd_Jan = wind_2012.loc[wind_2012['Month'] == 1, ['Month','WD']]
wd_Jul = wind_2012.loc[wind_2012['Month'] == 7, ['Month','WD']]

plt.subplot(121)
sns.distplot(wd_Jan.WD)
sns.distplot(wd_Jul.WD)
plt.ylabel('Probability')
plt.grid()
plt.legend(['Jan','Jul'], frameon = False)

ws_Jan = wind_2012.loc[wind_2012['Month'] == 1, ['Month','WS']]
ws_Jul = wind_2012.loc[wind_2012['Month'] == 7, ['Month','WS']]

plt.subplot(122)
sns.distplot(ws_Jan.WS)
sns.distplot(ws_Jul.WS)
plt.ylabel('Probability')
plt.xlabel('WS (m/s)')
plt.grid()
plt.legend(['Jan','Jul'], frameon = False)

plt.subplots_adjust(top=0.92, bottom=0.21, left=0.10, right=1.0, hspace=0.25, wspace=0.45)

# %%

from windrose import WindroseAxes
import matplotlib.cm as cm

# %%

ax = WindroseAxes.from_ax()
ax.bar(wd_Jan.WD, ws_Jan.WS, normed=True, opening=0.8, edgecolor='black')
ax.set_legend()

# %%

ax = WindroseAxes.from_ax()
ax.bar(wd_Jan.WD, ws_Jan.WS, normed=True, opening=0.8, edgecolor='blue')
ax.set_legend()

# %%

ax = WindroseAxes.from_ax()
ax.contourf(wd_Jan.WD, ws_Jan.WS, bins=np.arange(0,9,1), cmap=cm.hot)
ax.contour(wd_Jan.WD, ws_Jan.WS, bins=np.arange(0,9,1), colors = 'black', lw=1)
ax.set_title('January')
ax.set_legend()

# %%

df = pd.DataFrame({'speed':ws_Jul.WS.values, 'direction':wd_Jul.WD.values})
ax = plot_windrose(df, kind = 'contour', bins=np.arange(0, 9, 1), cmap=cm.jet, lw=1)
ax.set_title('July')

# %%

df = pd.DataFrame({'speed':ws_Jul.WS.values, 'direction':wd_Jul.WD.values})
ax = windrose.plot_windrose(df, kind = 'contour', bins=np.arange(0, 9, 1), cmap=cm.jet, lw=1)
ax.set_title('July')

# %%
import windrose

# %%

df = pd.DataFrame({'speed':ws_Jul.WS.values, 'direction':wd_Jul.WD.values})
ax = windrose.plot_windrose(df, kind = 'contour', bins=np.arange(0, 9, 1), cmap=cm.jet, lw=1)
ax.set_title('July')



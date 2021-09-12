from pandas import read_csv
from pandas import to_datetime
from pandas import DataFrame
from fbprophet import Prophet
from matplotlib import pyplot
from pandas.core.indexes.datetimes import DatetimeIndex

path = input('Enter the path to csv file: ')
df = read_csv(path, header=0)

n = int(input('Enter number of years to predict: '))

df.columns = ['ds', 'y']
df['ds'] = to_datetime(df['ds'],format='%Y')

model = Prophet()
model.fit(df)

future = list()
for i in range(1, n+1):
    date = df.iloc[-1]['ds'].year + i
    future.append([date])
future = DataFrame(future)
future.columns = ['ds']

forecast = model.predict(future)

model.plot(forecast)

df_ = DataFrame(forecast[['ds', 'yhat']])
df_['ds'] = DatetimeIndex(df_['ds']).year
df_.columns = ['Year','Waste generated in tonnes']
df_.to_csv('out.csv',index=False)

pyplot.show()

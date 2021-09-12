from pandas import read_csv
from pandas import to_datetime
from pandas import DataFrame
from sklearn.metrics import mean_absolute_error
from fbprophet import Prophet
from matplotlib import pyplot

path = 'https://raw.githubusercontent.com/jbrownlee/Datasets/master/monthly-car-sales.csv'
df = read_csv(path, header=0)

df.columns = ['ds', 'y']
df['ds']= to_datetime(df['ds'])

train = df.drop(df.index[-12:])
print(train.tail())

model = Prophet()
model.fit(train)


future = list()
for i in range(1, 13):
	date = '1969-%02d' % i
	future.append([date])
future = DataFrame(future)
future.columns = ['ds']
future['ds']= to_datetime(future['ds'])

forecast = model.predict(future)


y_true = df['y'][-12:].values
y_pred = forecast['yhat'].values

mae = mean_absolute_error(y_true,y_pred)
print('MAE: %.3f' % mae)

pyplot.plot(y_true, label='Actual')
pyplot.plot(y_pred, label='Predicted')
pyplot.legend()
pyplot.show()

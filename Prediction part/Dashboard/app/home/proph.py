import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from fbprophet import Prophet
from datetime import date, datetime, timedelta



prediction =object()

def datetime_range(start, end, delta):
    current = start
    if not isinstance(delta, timedelta):
        delta = timedelta(**delta)
    while current < end:
        yield current
        current += delta

def training():
	data=pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vQVtdpXMHB4g9h75a0jw8CsrqSuQmP5eMIB2adpKR5hkRggwMwzFy5kB-AIThodhVHNLxlZYm8fuoWj/pub?gid=2105854808&single=true&output=csv', sep = ',', encoding= 'utf_8')
	del data['Unnamed: 4']
	del data['Remarque']
	dataset=data.dropna()
	dataset['Date']= pd.to_datetime(dataset.iloc[:, 0]+ ' ' + dataset.iloc[:, 1], format="%d/%m/%Y %H:%M:%S")
	dataset=dataset.drop(dataset.columns[1],axis=1)
	dataset_traitement=dataset
	dataset_traitement.columns
	data_train=dataset_traitement[["Date","Vélos ce jour / Today\'s total"]]
	data_train.rename(columns={ "Vélos ce jour / Today\'s total": "y"})
	data_train.sort_values(by=['Date'], inplace=True, ascending=True)
	min_df = data_train.resample('1min', on='Date').mean()
	w_df = min_df.reset_index().dropna()
	w_df.columns = ['ds', 'y']
	w_df["y"]=np.log(w_df["y"])
	w_df["y"]=w_df["y"].replace([np.inf, -np.inf], np.nan)
	P=Prophet()
	P.add_country_holidays(country_name='France')
	P.fit(w_df)
	global prediction
	prediction=P
	return prediction


def predict():
	future = list()
	for dt in datetime_range(datetime.now(),datetime.now()+timedelta(30), {'hours':1}):
		future.append([dt])
	future = pd.DataFrame(future)
	future.columns = ['ds']
	future['ds']= pd.to_datetime(future['ds'])
	# use the model to make a forecast
	forecast = prediction.predict(future)
	# summarize the forecast
	forecast['yhat'] = np.exp(forecast['yhat']).astype(int)
	return forecast[['ds', 'yhat']]

def data_prevision_week():
	data=predict()
	tmp=data.resample('W', on='ds').yhat.sum().index.to_pydatetime()
	return ([str(date.replace(microsecond=0)) for date in tmp],list(data.resample('W', on='ds').yhat.sum().iloc[:]))

def data_prevision_hour():
	data=predict()
	tmp=data.resample('h', on='ds').yhat.sum().index.to_pydatetime()
	return ([str(date.replace(microsecond=0)) for date in tmp],list(data.resample('h', on='ds').yhat.sum().iloc[:]))

def data_prevision_day():
	data=predict()
	tmp=data.resample('D', on='ds').yhat.sum().index.to_pydatetime()
	return ([str(date.replace(microsecond=0)) for date in tmp],list(data.resample('D', on='ds').yhat.sum().iloc[:]))

def data_prevision_month():
	data=predict()
	tmp=data.resample('M', on='ds').yhat.sum().index.to_pydatetime()
	return ([str(date.replace(microsecond=0)) for date in tmp],list(data.resample('M', on='ds').yhat.sum().iloc[:]))

def data_prevision_year():
	data=predict()
	tmp=data.resample('Y', on='ds').yhat.sum().index.to_pydatetime()
	return ([str(date.replace(microsecond=0)) for date in tmp],list(data.resample('Y', on='ds').yhat.sum().iloc[:]))


training()

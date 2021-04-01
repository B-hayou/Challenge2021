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
	dataset['Date']= pd.to_datetime(dataset['Date'] + ' ' + dataset.iloc[:, 1], format="%d/%m/%Y %H:%M:%S")
	dataset=dataset.drop(dataset.columns[1],axis=1)
	dataset_traitement=dataset
	dataset_traitement.columns
	data_train=dataset_traitement[["Date","Vélos ce jour / Today\'s total"]]
	data_train.rename(columns={ "Vélos ce jour / Today\'s total": "y"})
	data_train.sort_values(by=['Date'], inplace=True, ascending=True)
	hour_df = data_train.resample('1min', on='Date').sum()
	w_df = hour_df.reset_index().dropna()
	w_df.columns = ['ds', 'y']
	P=Prophet()
	P.add_country_holidays(country_name='France')
	P.fit(w_df)
	global prediction
	prediction=P
	return prediction


def predict(start_date,end_date):
	future = list()
	for dt in datetime_range(start_date, end_date, {'hours':1}):
		future.append([date])
	future = pd.DataFrame(future)
	future.columns = ['ds']
	future['ds']= pd.to_datetime(future['ds'])
	# use the model to make a forecast
	forecast = prediction.predict(future)
	# summarize the forecast
	forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']]
	return forecast.yhat.sum()



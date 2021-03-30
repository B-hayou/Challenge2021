import  pandas as pd 
import datetime as dt
url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQVtdpXMHB4g9h75a0jw8CsrqSuQmP5eMIB2adpKR5hkRggwMwzFy5kB-AIThodhVHNLxlZYm8fuoWj/pub?gid=2105854808&single=true&output=csv"
  
def data_per_week():
    data_file = pd.read_csv(url)
    data_file = data_file.drop(['Unnamed: 4','Remarque'],axis=1)
    data_file=data_file.dropna()
    data_file['Date']= pd.to_datetime(data_file['Date'] + ' ' + data_file.iloc[:, 1], format="%d/%m/%Y %H:%M:%S")
    data_file=data_file.drop(data_file.columns[1],axis=1)
    data_file.columns= ["Date","TotalPerYear","TotalPerDay"]
    data=data_file.resample('W', on='Date').TotalPerDay.sum()
    tmp=data_file.resample('W', on='Date').TotalPerDay.sum().index.to_pydatetime()
    return ([str(date.replace(microsecond=0)) for date in tmp],list(data.iloc[:]))

def data_per_hour():
    data_file = pd.read_csv(url)
    data_file = data_file.drop(['Unnamed: 4','Remarque'],axis=1)
    data_file=data_file.dropna()
    data_file['Date']= pd.to_datetime(data_file['Date'] + ' ' + data_file.iloc[:, 1], format="%d/%m/%Y %H:%M:%S")
    data_file=data_file.drop(data_file.columns[1],axis=1)
    data_file.columns= ["Date","TotalPerYear","TotalPerDay"]
    data_file.columns= ["Date","TotalPerYear","TotalPerDay"]
    data=data_file.resample('h', on='Date').TotalPerDay.sum()
    tmp=data_file.resample('h', on='Date').TotalPerDay.sum().index.to_pydatetime()
    return ([str(date.replace(microsecond=0)) for date in tmp],list(data.iloc[:]))

def data_per_day():
    data_file = pd.read_csv(url)
    data_file = data_file.drop(['Unnamed: 4','Remarque'],axis=1)
    data_file=data_file.dropna()
    data_file['Date']= pd.to_datetime(data_file['Date'] + ' ' + data_file.iloc[:, 1], format="%d/%m/%Y %H:%M:%S")
    data_file=data_file.drop(data_file.columns[1],axis=1)
    data_file.columns= ["Date","TotalPerYear","TotalPerDay"]
    data=data_file.resample('D', on='Date').TotalPerDay.sum()
    tmp=data_file.resample('D', on='Date').TotalPerDay.sum().index.to_pydatetime()
    return ([str(date.replace(microsecond=0)) for date in tmp],list(data.iloc[:]))

def data_per_month():
    data_file = pd.read_csv(url)
    data_file = data_file.drop(['Unnamed: 4','Remarque'],axis=1)
    data_file=data_file.dropna()
    data_file['Date']= pd.to_datetime(data_file['Date'] + ' ' + data_file.iloc[:, 1], format="%d/%m/%Y %H:%M:%S")
    data_file=data_file.drop(data_file.columns[1],axis=1)
    data_file.columns= ["Date","TotalPerYear","TotalPerDay"]
    data=data_file.resample('M', on='Date').TotalPerDay.sum()
    tmp=data_file.resample('M', on='Date').TotalPerDay.sum().index.to_pydatetime()
    return ([str(date.replace(microsecond=0)) for date in tmp],list(data.iloc[:]))


def data_per_year():
    data_file = pd.read_csv(url)
    data_file = data_file.drop(['Unnamed: 4','Remarque'],axis=1)
    data_file=data_file.dropna()
    data_file['Date']= pd.to_datetime(data_file['Date'] + ' ' + data_file.iloc[:, 1], format="%d/%m/%Y %H:%M:%S")
    data_file=data_file.drop(data_file.columns[1],axis=1)
    data_file.columns= ["Date","TotalPerYear","TotalPerDay"]
    data=data_file.resample('Y', on='Date').TotalPerDay.sum()
    tmp=data_file.resample('Y', on='Date').TotalPerDay.sum().index.to_pydatetime()
    return ([str(date.replace(microsecond=0)) for date in tmp],list(data.iloc[:]))

import  pandas as pd 
import datetime as dt
url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQVtdpXMHB4g9h75a0jw8CsrqSuQmP5eMIB2adpKR5hkRggwMwzFy5kB-AIThodhVHNLxlZYm8fuoWj/pub?gid=2105854808&single=true&output=csv"
stations="https://data.montpellier3m.fr/sites/default/files/ressources/MMM_MMM_GeolocCompteurs.csv"
import requests
import json
import pandas as pd 
import ast
import folium


def data_stats(data_file,unity):
    data_file['dateObserved']= pd.to_datetime(data_file["dateObserved"], format="%Y-%m-%dT%H:%M:%S")
    data=data_file.resample(unity, on='dateObserved').intensity.sum()
    tmp=data_file.resample(unity, on='dateObserved').intensity.sum().index.to_pydatetime()
    return [str(date.replace(microsecond=0)) for date in tmp],list(data.iloc[:])


def stations_name():
    return pd.read_csv(stations,encoding= 'unicode_escape').iloc[:,0].to_list()

def data_maps(data,hours,station_name):
    lat = data.iloc[:,3].to_list()[0]
    lng = data.iloc[:,4].to_list()[0]
    map = folium.Map(location=[lat, lng], zoom_start=100)
    folium.CircleMarker(location = [lat, lng], radius = 50, popup = str(hours[1][-1]) +" Bikes counted " +str(hours[0][-1])+ " in "+ station_name+"station",fill=True,
    fill_color="#3186cc",).add_to(map)
    folium.Marker(location = [lat, lng], radius = 70, popup =  str(hours[1][-1]) +" Bikes counted " +str(hours[0][-1])+ " in "+ station_name+" station",icon=folium.Icon(color="blue", icon="info-sign"),).add_to(map)
    
    map.save(outfile='app/home/templates/map.html')


def visualisation_function(station):
    data_stations=pd.read_csv(stations,encoding= 'unicode_escape')
    station_name=station
    maps=data_stations[data_stations.iloc[:,0]==station]
    station=data_stations[data_stations.iloc[:,0]==station].iloc[:,2].to_list()[0]
    
    url ='https://data.montpellier3m.fr/sites/default/files/ressources/MMM_EcoCompt_'+station+'_archive.json'
    r = requests.get(url)
    k=r.content.decode("utf-8")
    open('test.json', 'w').write(str(k))
    file1 = open('test.json', 'r')
    Lines = file1.readlines()
    count = 0
    data=[]
    for i in range(len(Lines)):
        Lines[i]= Lines[i].replace("{\"intensity\"",",-{\"intensity\"")
    for line in Lines:
        data.append(line.split(",-"))
    flat_list = [item for sublist in data for item in sublist]
    file=[]
    for i in flat_list:
        try:
                file.append(i)
        except:
                pass
    file=[x for x in file if x != ' \n']
    file=[x for x in file if x != '']
    jsons=[]
    for d in file:
        d=d.replace("false","False")
        jsons.append(eval(d))

    with open('final_'+station+'.json', 'w') as fout:
        json.dump(jsons , fout)

    data=pd.read_json("final_"+station+".json")
    data["dateObserved"]=data["dateObserved"].astype(str)
    data["dateObserved"]=data["dateObserved"].str.split("/").str[0]
    hours=data_stats(data[["intensity","dateObserved"]],'h')
    days=data_stats(data[["intensity","dateObserved"]],'d')
    weeks=data_stats(data[["intensity","dateObserved"]],'W')
    months=data_stats(data[["intensity","dateObserved"]],'M')
    years=data_stats(data[["intensity","dateObserved"]],'Y')
    data_maps(maps,hours,station_name)
    return (hours,days,weeks,months,years)


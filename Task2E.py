from floodsystem.stationdata import build_station_list
from floodsystem.datafetcher import fetch_measure_levels
import datetime
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.station import MonitoringStation

def run():
    """Requirements for Task 2E"""

#Build list of stations and updates water level data
station = build_station_list()
update_water_levels(station)

#List of 5 station names with highest current relative water levels
at_risk_names = []
for i in stations_highest_rel_level(station, 5):
    at_risk_names.append(i[0])
print(at_risk_names)

#Station data for these 5 at risk stations
station_data = []
for i in station:
    for k in range (len(at_risk_names)):
        if i.name == at_risk_names[k]:
            station_data.append(i) 
print(station_data)


#Fetching data over the past 10 days for each at risk station
dt = 10
for i in range (5):
    dates[i], levels[i] = fetch_measure_levels(at_risk_names[i].measure_id, dt=datetime.timedelta(days=dt))



if __name__ == "__main__":
    print("*** Task 2E: CUED Part IA Flood Warning System ***")
    run()

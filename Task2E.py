from floodsystem.stationdata import build_station_list
from floodsystem.datafetcher import fetch_measure_levels
import datetime
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.station import MonitoringStation
from floodsystem.plot import plot_water_levels
import floodsystem.plot as plot

def run():
    """Requirements for Task 2E"""

    #Build list of stations and updates water level data
    station = build_station_list()
    update_water_levels(station)

    #List of 5 station names with highest current relative water levels
    at_risk_names = []
    for i in stations_highest_rel_level(station, 5):
        at_risk_names.append(i[0].name)
    
    print('Stations with a relative water level above 100 have been removed')


    #Station data for these 5 at risk stations
    station_data = []
    for i in station:
        for k in range (len(at_risk_names)):
            if i.name == at_risk_names[k]:
                station_data.append(i) 

   
    #Fetching data over the past 10 days for each at risk station
    for i in station_data:
        dates, levels = fetch_measure_levels(i.measure_id, dt = datetime.timedelta(days = 10))

        #Plotting graph for each station (5 different graphs)
        plot_water_levels(i, dates, levels)
      
    

if __name__ == "__main__":
    print("*** Task 2E: CUED Part IA Flood Warning System ***")
    run()

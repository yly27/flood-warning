from floodsystem.geo import rivers_with_station, stations_by_river
from floodsystem.utils import sorted_by_key  # noqa
from haversine import haversine, Unit
from floodsystem.station import MonitoringStation
from floodsystem.stationdata import build_station_list
from collections import defaultdict   



def run():
    """Requirements for Task 1D Part A"""

    # Build list of stations
    stations = build_station_list()
    
    river_stations_list = (rivers_with_station(stations))

    #Prints number of rivers with at least one monitoring stations
   # print(len(river_stations_list))

    #Prints first 10 of this list
    #print(list(river_stations_list)[:10])

    

    '''Requirements for Task 1D Part B'''
    river_dict = stations_by_river(stations)
    print('River Aire has the following stations...',sorted(river_dict['River Aire']))
    print('River Cam has the following stations...',sorted(river_dict['River Cam']))
    print('River Thames has the following stations...',sorted(river_dict['River Thames']))

if __name__ == "__main__":
    print("*** Task 1D: CUED Part IA Flood Warning System ***")
    run()
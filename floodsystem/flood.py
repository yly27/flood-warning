from floodsystem.station import MonitoringStation
from floodsystem.stationdata import build_station_list, update_water_levels
from .utils import sorted_by_key 


'''Task 2B part b'''

stations = build_station_list()
def station_level_over_threshold(stations, tol):
    big_list = []
    #Locates stations with relative water level is over tol and adds to a list
    for i in stations:
        if i.relative_water_level > tol:
            big_list.append(i,i.relative_water_level)


    big_list.sort(reverse=True)
    return big_list
  

'''Task 2C'''
def stations_highest_rel_level(stations, N):
    station_names = [], relative_levels = []
    for i in stations:
        if i.relative_water_level() == False:
            pass
        else:
            #list of all stations and their relative water level
            station_names.append(i.name)
            relative_levels.append(i.relative_water_level)

    #combining the two lists into a list of tuples
    station_biglist = list(zip(station_names, relative_levels))

    #sort list biggest to smallest
    station_biglist = sorted_by_key(station_biglist, 1, reverse = False)  

    return station_biglist[:N]
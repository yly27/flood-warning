from .utils import sorted_by_key  # noqa
from .station import MonitoringStation
from floodsystem.geo import stations_by_river
from floodsystem.stationdata import build_station_list, update_water_levels
from .utils import sorted_by_key 

'''Task 2B part b'''
stations = build_station_list()

def stations_level_over_threshold(stations, tol):
    big_list = []
    #Locates stations with relative water level is over tol and adds to a list
    for i in stations:
        if (i.relative_water_level() != None) and (i.relative_water_level() > tol):
            if i.relative_water_level() < 100:
                big_list.append((i, i.relative_water_level()))

        big_list = sorted(big_list, key = lambda x:-x[1])

    return big_list



  

'''Task 2C'''
def stations_highest_rel_level(stations, N):
    high_water_levels = []
    
    for i in stations:
        if (i.relative_water_level() == None) or (i.relative_water_level() > 100 ):
            pass
        else:
            #list of all stations and their relative water level
            high_water_levels.append((i.name, i.relative_water_level()))

    
    #sort list biggest to smallest
    high_water_levels = sorted_by_key(high_water_levels, 1, reverse = True)  

    return high_water_levels[:N]

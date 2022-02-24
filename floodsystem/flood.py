from floodsystem.station import MonitoringStation
from floodsystem.stationdata import build_station_list, update_water_levels


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
  
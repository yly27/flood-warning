from floodsystem.station import MonitoringStation
from floodsystem.stationdata import build_station_list, update_water_levels


'''Task 2B part b'''

stations = build_station_list()
def station_level_over_threshold(stations, tol):

    #Locates stations with relative water level is over tol and adds to a list
    for i in stations:
        if i.relative_water_level > tol:
            print('Bigger than tol')






  #  distances = []
   # names = []
    #towns = []

    #for i in stations:
     #   distances.append(haversine(p, i.coord)) 
      #  names.append(i.name)
       # towns.append(i.town) 

    #big_list = list(zip(names,towns,distances))
    #return(sorted_by_key((big_list),2))

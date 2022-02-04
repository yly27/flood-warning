from floodsystem.geo import rivers_with_station
from sympy import stationary_points
from floodsystem.utils import sorted_by_key  # noqa
from haversine import haversine, Unit
from floodsystem.station import MonitoringStation
from floodsystem.stationdata import build_station_list



def run():
    """Requirements for Task 1D"""

    # Build list of stations
    stations = build_station_list()
    
    river_stations_list = (rivers_with_station(stations))

    #Prints number of rivers with at least one monitoring stations
    print(len(river_stations_list))

    #Prints first 10 of this list
    print(list(river_stations_list)[:10])


if __name__ == "__main__":
    print("*** Task 1D: CUED Part IA Flood Warning System ***")
    run()
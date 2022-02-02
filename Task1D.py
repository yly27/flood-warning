from floodsystem.geo import stations_by_distance
from sympy import stationary_points
from floodsystem.utils import sorted_by_key  # noqa
from haversine import haversine, Unit
from floodsystem.station import MonitoringStation
from floodsystem.stationdata import build_station_list



def run():
    """Requirements for Task 1D"""

    # Build list of stations
    stations = build_station_list()
    
    def rivers_with_station(stations):
        print('hi')
  

if __name__ == "__main__":
    print("*** Task 1D: CUED Part IA Flood Warning System ***")
    run()
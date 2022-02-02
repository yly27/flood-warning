from floodsystem.geo import stations_within_radius
from sympy import stationary_points
from floodsystem.utils import sorted_by_key  # noqa
from haversine import haversine, Unit
from floodsystem.station import MonitoringStation
from floodsystem.stationdata import build_station_list

def run():
    """Requirements for Task 1C"""

    # Build list of stations
    stations = build_station_list()

    #Stations within radius 10 km of the Cambridge city centre, in alphabetical order
    stationsinRadius = stations_within_radius(stations,(52.2053,0.1218),10)
    print(sorted(stationsinRadius))

if __name__ == "__main__":
    print("*** Task 1C: CUED Part IA Flood Warning System ***")
    run()

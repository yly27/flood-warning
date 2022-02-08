from floodsystem.geo import stations_by_distance
from floodsystem.utils import sorted_by_key  # noqa
from haversine import haversine, Unit
from floodsystem.station import MonitoringStation
from floodsystem.stationdata import build_station_list

def run():
    """Requirements for Task 1B"""

    # Build list of stations
    stations = build_station_list()

    big_list = stations_by_distance(stations,(52.2053,0.1218))
    print(big_list[:10])
    print(big_list[-10:])

if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    run()


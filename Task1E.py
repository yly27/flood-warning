from floodsystem.geo import rivers_by_station_number
from floodsystem.utils import sorted_by_key  # noqa
from floodsystem.station import MonitoringStation
from floodsystem.stationdata import build_station_list

def run():
    """Requirements for Task 1C"""

    # Build list of stations
    stations = build_station_list()

    # Determines the N rivers with the greatest number of monitoring stations
    topNrivers = rivers_by_station_number(stations, 9)
    print(topNrivers)

if __name__ == "__main__":
    print("*** Task 1C: CUED Part IA Flood Warning System ***")
    run()


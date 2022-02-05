from floodsystem.stationdata import build_station_list
from floodsystem.station import typical_range_inconsistent


def run():
    """Requirements for Task 1F"""

    # Build list of stations
    stations = build_station_list()

    # make a list of inconsistent stations
    inconsistent_stations = typical_range_inconsistent(stations)

if __name__ == "__main__":
    print("*** Task 1C: CUED Part IA Flood Warning System ***")
    run()

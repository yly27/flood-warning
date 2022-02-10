from floodsystem.stationdata import build_station_list
from floodsystem.station import MonitoringStation, inconsistent_typical_range_stations
def run():
    """Requirements for Task 2B"""

    stations = build_station_list(0)
    i=0
    while i < 3:
        if stations[i].latest_level != None:
            print(stations[i].latest_level)
           
            i += 1
            print(stations[i].typical_range)
        

if __name__ == "__main__":
    print("*** Task 2B: CUED Part IA Flood Warning System ***")
    run()

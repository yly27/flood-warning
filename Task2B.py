from floodsystem.flood import stations_level_over_threshold
from floodsystem.stationdata import build_station_list, update_water_levels

def run():
    """Requirements for Task 2B"""

    stations = build_station_list()

    # Update latest level data for all stations
    update_water_levels(stations)

    stations_over_tol = station_level_over_threshold(stations, 0.8)
    print(stations_over_tol)



    
if __name__ == "__main__":
    print("*** Task 2B: CUED Part IA Flood Warning System ***")
    run()

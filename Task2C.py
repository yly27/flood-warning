from floodsystem.flood import stations_highest_rel_level
from floodsystem.stationdata import build_station_list, update_water_levels


def run():
    """Requirements for Task 2C"""

#build list of stations and update
stations = build_station_list()
update_water_levels(stations)

#find top 10 most at risk
print(stations_highest_rel_level(stations, 10))

if __name__ == "__main__":
    print("*** Task 1F: CUED Part IA Flood Warning System ***")
    run()

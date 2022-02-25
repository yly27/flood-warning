from floodsystem.flood import stations_highest_rel_level
from floodsystem.stationdata import build_station_list, update_water_levels


def run():
    """Requirements for Task 2C"""

#build list of stations and update
stations = build_station_list()
update_water_levels(stations)

#find top 10 most at risk
for i in stations_highest_rel_level(stations, 10):
    print("{}  {}".format(i[0], i[1]))

if __name__ == "__main__":
    print("*** Task 1F: CUED Part IA Flood Warning System ***")
    run()

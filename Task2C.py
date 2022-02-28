from floodsystem.flood import stations_highest_rel_level
from floodsystem.stationdata import build_station_list, update_water_levels


def run():
    """Requirements for Task 2C"""

    #build list of stations and update
    stations = build_station_list()
    update_water_levels(stations)

    high_ten = stations_highest_rel_level(stations, 10)
   
    #find top 10 most at risk
    for station in high_ten:
        print("{} {}".format((station[0]).name, station[1]))

    print('Stations with a relative water level above 100 have been removed')

if __name__ == "__main__":
    print("*** Task 2C: CUED Part IA Flood Warning System ***")
    run()

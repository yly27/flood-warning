import datetime
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.plot import plot_water_level_with_fit

def run():
    """Requirements for Task 2F"""
    
     #build list of stations and update
    stations = build_station_list()
    update_water_levels(stations)

    high_five = stations_highest_rel_level(stations, 5)

    for i in high_five:
        station = i[0]

        dt = 2
        dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
        plot_water_level_with_fit(station, dates, levels, 4) 


if __name__ == "__main__":
    print("*** Task 2F: CUED Part IA Flood Warning System ***")
    run()

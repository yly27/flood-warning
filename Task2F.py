import datetime
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from floodsystem.analysis import polyfit
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level

def run():
    """Requirements for Task 2F"""
    
     #build list of stations and update
    stations = build_station_list()
    update_water_levels(stations)

    high_five = stations_highest_rel_level(stations, 5)



if __name__ == "__main__":
    print("*** Task 1F: CUED Part IA Flood Warning System ***")
    run()

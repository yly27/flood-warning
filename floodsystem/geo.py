# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""
from sympy import stationary_points
from .utils import sorted_by_key  # noqa
from haversine import haversine, Unit
from .station import MonitoringStation
from .stationdata import build_station_list
import numpy as np
from floodsystem.datafetcher import fetch_station_data


'''Task 1B'''
stations = build_station_list
def stations_by_distance(stations, p):
    # stations is a list of MonitoringStation objects and p is a coordinate
    # the function returns the name, town and distance from the coordinate to that particular station

    #this creates a list with the distances, names and town 
    distances = []
    names = []
    towns = []

    for i in stations:
        distances.append(haversine(p, i.coord)) 
        names.append(i.name)
        towns.append(i.town) 

    big_list = list(zip(names,towns,distances))
    return(sorted_by_key((big_list),2))

'''Task 1C'''
stations = build_station_list
def stations_within_radius(stations, centre, r):
    # stations is a list of MonitoringStation objects, centre is the coordinate x and r is the radius
    # the function builds a list of stations within a given radius of a given coordinate

    

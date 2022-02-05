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
from collections import defaultdict   

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
    stationsinRadius = []
    big_list2 = stations_by_distance(stations, centre)
    
    #checking if radius < r
    for j, station in enumerate(big_list2):
        if big_list2[j][2] < r:
            stationsinRadius.append(big_list2[j][0])
        
        else:
            break
    
    return stationsinRadius


'''Task 1D'''
def rivers_with_station(stations):

    #Builds a set with the name of every river witha monitoring station
    river_stations_list = set()
    for i in stations:
        river_stations_list.add(i.river)

    #Alphabetically sorted set  
    return sorted(river_stations_list)


#Task 1D Part 2
def stations_by_river(stations):
    river_dict = defaultdict(list)
    for i in stations:
        river_dict[i.river].append(i.name)
    return(river_dict)

    
'''Task 1E'''
def rivers_by_station_number(stations, N):
    stationsbyRiver = stations_by_river(stations)

#list of rivers and how many stations they have 
    numberofStations = []

    for key, value in stationsbyRiver.items():
        numberofStations.append((key, len(value)))
    
#sort list largest to smallest
    numberofStations = sorted_by_key(numberofStations, 1, reverse = True)
    
#checking for the case where  there are more rivers with the same number of stations as the Nth entr
    count = 0
    n = N
    for item in range(0,n):
        if numberofStations[item][1] == numberofStations[(item+1)][1]:
            count += 1
            n += 1
                
    return numberofStations[:N+count]

    

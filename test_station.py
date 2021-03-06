# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""Unit test for the station module"""

from floodsystem.station import MonitoringStation
from floodsystem.stationdata import build_station_list

#Import test data
from test_geo import tester_station


'''Task 1F Test'''
def test_typical_range_consistent():
    assert tester_station[0].typical_range_consistent() == False
    assert tester_station[1].typical_range_consistent() == True

'''Task 2B Test (Part 1)'''
def test_relative_water_level():
    #Typical range for test_station_2 is 10 to 20
    #Check that the relative water level calculation is correct if the current water level is 20
    tester_station[1].latest_level = 20
    assert tester_station[1].relative_water_level() == 1
    assert tester_station[0].relative_water_level() == None


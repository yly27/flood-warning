#Import test data
from floodsystem.stationdata import build_station_list
from test_geo import tester_station
from floodsystem.flood import stations_level_over_threshold
from floodsystem.station import MonitoringStation

stations = build_station_list

'''Task 2B Test (Part 2)'''
def test_stations_level_over_threshold():
    test_list = stations_level_over_threshold(stations, 0.5)

    for i in range (len(test_list)):
        assert test_list[i][1] > 0.5
        assert test_list[i][1] != None
        assert test_list[i+1][1] < test_list[i][1]
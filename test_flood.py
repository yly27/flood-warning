#Import test data
from floodsystem.stationdata import build_station_list
from test_geo import tester_station
from floodsystem.flood import stations_level_over_threshold
from floodsystem.station import MonitoringStation

stations = build_station_list

'''Task 2B Test (Part 2)'''
def test_stations_level_over_threshold():
    for i in stations_level_over_threshold(stations, 0.8):
        assert i[1] > 0.5
        assert i[1] != None
        assert i[1] > (i+1)[1]
from floodsystem.flood import stations_level_over_threshold, stations_highest_rel_level
from floodsystem.station import MonitoringStation
import random 
from floodsystem.stationdata import build_station_list, update_water_levels

stations = build_station_list()
tester_stations = [MonitoringStation(
        station_id=1,
        measure_id=15,
        label='Station 1',
        coord=(float(0.5), float(1)),
        typical_range=(1.2, 1.5),
        river='Test River',
        town='Town 1'),
        MonitoringStation(
        station_id=2,
        measure_id=20,
        label='Station 2',
        coord=(float(10), float(50)),
        typical_range=(2, 5),
        river='Test River',
        town='Town 2'),
        MonitoringStation(
        station_id=3,
        measure_id=50,
        label='Station 3',
        coord=(float(25), float(35)),
        typical_range=(1, 19),
        river='Test River',
        town='Town 3')]


'''Task 2B Test (Part 2)'''
def test_stations_level_over_threshold():
    #Assign each station a current water level
    tester_stations[0].latest_level = 1.5
    tester_stations[1].latest_level = 10
    tester_stations[2].latest_level = 25

    test_list = stations_level_over_threshold(tester_stations,0.5)
    assert test_list[0][1] > test_list[1][1]
    
    for i in range (len(test_list)):
        #Check every station in the list is over threshold
        assert test_list[i][1] > 0.5

        #Check list is sorted with highest first
        if i < ((len(test_list)) - 1):
            assert test_list[i][1] > test_list[i+1][1]


'''Task 2C Test'''

def test_stations_highest_rel_level():
    update_water_levels(stations)

    highest_level_list = stations_highest_rel_level(stations, 20)
    for i in range (len(highest_level_list)):
        #Check list is sorted with highest first
        if i < ((len(highest_level_list)) - 1):
            assert highest_level_list[i][1] > highest_level_list[i+1][1]
    
    #Check there are 20 stations in the list as required
    assert (len(highest_level_list)) == 20

    #Check relative water levels and corresponding station is correct using test data
    tester_stations[0].latest_level = 1.5
    tester_stations[1].latest_level = 12
    test_list = stations_highest_rel_level(tester_stations, 1)
    assert round(test_list[0][1]) == 3
    assert test_list[0][0].name == 'Station 2' 
    
    
        
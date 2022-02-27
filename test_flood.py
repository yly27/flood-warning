from floodsystem.flood import stations_level_over_threshold
from floodsystem.station import MonitoringStation

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
        assert test_list[i][1] > 0.5
        if i < ((len(test_list)) - 1):
            assert test_list[i][1] > test_list[i+1][1]
    
        
import floodsystem.geo as geo
from floodsystem.stationdata import build_station_list
from test_station import test_create_monitoring_station

stations = build_station_list()
tester_station = test_create_monitoring_station()

'''Task 1B Test'''
def test_stations_by_distance():
    big_list = geo.stations_by_distance(stations(0,0))

    #Checks if distances have been sorted.
    for i in big_list:
        if big_list[i][2] > big_list[i+1][2]:
            raise ValueError('The list should be in order of increasing distance.')
    
    #Checks if distance from (0,0) to tester station (-2,4) is correct
    assert round(geo.stations_by_distance(tester_station, (0, 0))[0][2]) == 4
            





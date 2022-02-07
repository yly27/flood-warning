from floodsystem.geo import stations_by_distance
from floodsystem.stationdata import build_station_list
from test_station import test_create_monitoring_station


stations = build_station_list()
tester_station = test_create_monitoring_station()

'''Task 1B Test'''
def test_stations_by_distance():
    assert round(stations_by_distance(tester_station, (0, 0))[0][2]) == 497
    assert len(stations_by_distance(stations, (0, 0))) > 0




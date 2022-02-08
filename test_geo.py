import floodsystem.geo as geo
from floodsystem.stationdata import build_station_list
from test_station import test_create_monitoring_station


stations = build_station_list()
tester_station = test_create_monitoring_station()

'''Task 1B Test'''
def test_stations_by_distance():
    assert len(geo.stations_by_distance(stations, (0, 0))) >0
    assert round(geo.stations_by_distance(tester_station, (0,0)) [0][1]) == 497

'''Task 1C Test'''
def test_stations_within_radius():
    x = geo.stations_within_radius(stations, (52.2053, 0.1218), 10)
    assert len(x) == 11
    assert type(x) == list
    assert len(geo.stations_within_radius(stations, (52.2053, 0.1218), 1))<len(geo.stations_within_radius(stations, (52.2053, 0.1218),2))
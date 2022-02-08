import floodsystem.geo as geo
from floodsystem.stationdata import build_station_list
from test_station import test_create_monitoring_station


stations = build_station_list()
tester_station = test_create_monitoring_station()


'''Task 1C Test'''
def test_stations_within_radius():
    assert len(geo.stations_within_radius(stations, (52.2053, 0.1218), 0)) == 0
    assert len(geo.stations_within_radius(stations, (52.2053, 0.1218), 10)) > 0
    assert len(geo.stations_within_radius(stations, (52.2053, 0.1218), 5)) > len(geo.stations_within_radius(stations, (52.2053, 0.1218), 1))


'''Task 1D Test'''
def test_rivers_with_station():
    assert len(geo.rivers_with_station(stations)) > 0
    assert geo.rivers_with_station(tester_station) == ['River X']

def test_stations_by_river():
    assert type(geo.stations_by_river) == dict
    assert len(geo.stations_by_river(stations)['River Cam']) > 5




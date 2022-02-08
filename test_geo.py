import floodsystem.geo as geo
from floodsystem.stationdata import build_station_list
from floodsystem.station import MonitoringStation

stations = build_station_list()
tester_station = [MonitoringStation(
        station_id=1,
        measure_id=10,
        label='Test_Station_1',
        coord=(float(0.1), float(0.1)),
        typical_range=(1, 1.5),
        river='Test_River_1',
        town='Test_Town_1'),MonitoringStation(
        station_id=2,
        measure_id=20,
        label='Test_Station_2',
        coord=(float(50), float(0)),
        typical_range=(10, 20),
        river='River_Test_2',
        town='Test_Town_2')]

'''Task 1B Test'''
def test_stations_by_distance():
    assert len(geo.stations_by_distance(stations, (0, 0))) >0
    assert round(geo.stations_by_distance(tester_station, (0, 0))[0][2]) == 16

'''Task 1C Test'''
def test_stations_within_radius():
    assert len(geo.stations_within_radius(stations, (52.2053, 0.1218), 0)) == 0
    assert len(geo.stations_within_radius(stations, (52.2053, 0.1218), 10)) > 0
    assert len(geo.stations_within_radius(stations, (52.2053, 0.1218), 5)) > len(geo.stations_within_radius(stations, (52.2053, 0.1218), 1))


'''Task 1D Test'''
def test_rivers_with_station():
    assert len(geo.rivers_with_station(stations)) > 0
    assert geo.rivers_with_station(tester_station)[0] == ['River_Test_1']

def test_stations_by_river():
    assert len(geo.stations_by_river(stations)['River Cam']) > 5
    



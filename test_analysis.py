from floodsystem.stationdata import build_station_list, update_water_levels
import random
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.analysis import polyfit
import numpy
import datetime

def test_risk_analysis():
    print('DUNNO')



def test_polyfit():
    stations = build_station_list()
    update_water_levels(stations)

    #random station
    n = random.randint(1,50)
    test_station = stations[n]

    dates, levels = fetch_measure_levels(test_station.measure_id, dt=datetime.timedelta(days=4))
    poly, d0 = polyfit(dates, levels, 5)


    assert len(poly) != 0
    assert type(poly) == numpy.poly1d
    
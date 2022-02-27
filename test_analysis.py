from floodsystem.analysis import risk_analysis, risk_rater
from floodsystem.stationdata import build_station_list
from floodsystem.flood import update_water_levels
from floodsystem.stationdata import build_station_list, update_water_levels
import random
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.analysis import polyfit
import numpy
import datetime

def test_risk_rater():
    #Test risk values and checking they come out with the correct risk level
    risk = 0.4
    assert risk_rater(risk) == 'Severe'
    risk = 0.25
    assert risk_rater(risk) == 'High'
    risk = 0.15
    assert risk_rater(risk) == 'Moderate'
    risk = 0.05
    assert risk_rater(risk) == 'Low'

def test_risk_analysis():
    stations = build_station_list()
    update_water_levels(stations)
    assert (len(risk_analysis(stations))) > 0
    assert (type(risk_analysis(stations))) == dict

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
    

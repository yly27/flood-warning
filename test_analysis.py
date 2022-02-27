from floodsystem.analysis import risk_analysis, risk_rater
from floodsystem.stationdata import build_station_list
from floodsystem.flood import update_water_levels

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
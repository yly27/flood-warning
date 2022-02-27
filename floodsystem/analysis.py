from pickle import HIGHEST_PROTOCOL
from re import X
from unicodedata import name
import numpy as np
import matplotlib
from .stationdata import build_station_list
from floodsystem.station import MonitoringStation, inconsistent_typical_range_stations
from floodsystem.stationdata import update_water_levels
import datetime
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.flood import stations_highest_rel_level
from .utils import sorted_by_key


def polyfit(dates, levels, p):
    # Create set of data points
    x = matplotlib.dates.date2num(dates)
    y = levels

    #The amount we shifted the dates by
    d0 = x[0]

    # Find coefficients of best-fit polynomial f(x) of degree p. We use x-x[0] to shift the date values
    p_coeff = np.polyfit(x-x[0], y, p)

    # Convert coefficient into a polynomial that can be evaluated
    poly = np.poly1d(p_coeff)

    return poly, d0


def risk_analysis(stations):

    #Check is typical ranges are consistent and build a list of only consistent stations
    inconsistent_station_names = inconsistent_typical_range_stations(stations)
    consistent_stations = []
    for i in stations:
        if i.name not in inconsistent_station_names:
            consistent_stations.append(i)

    #Take the relative water level of every consistent station
    update_water_levels(stations)

    list_risk_scores = []
    temp_list = consistent_stations[:50]        #takes too long to check all so just checks 50

    for station in temp_list:
        dt = 2
        dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
        
        if dates == None or levels == None:
            pass
        else:
            x = matplotlib.dates.date2num(dates)
            try:
                poly, d0 = polyfit(dates, levels, 4)
            except (IndexError):
                pass

            day_today = max(x - d0)

        #take first derivative
            d1_poly = poly.deriv()
            current_increase_rate = d1_poly(day_today)

        #create weighted risk score
            current_rel_level_weight = 0.6
            current_increase_rate_weight = 0.4
            risk_score = ((current_rel_level_weight*station.relative_water_level()) +  (current_increase_rate_weight*current_increase_rate))
            list_risk_scores.append(risk_score)


    risky_list = zip(temp_list,list_risk_scores)

    risk_dictionary = {}

    #the risk level for a town is that of the station recording highest relative water levels for that town
    for station in risky_list:
        if ((station[0]).town not in risk_dictionary.keys()) or station[1] > risk_dictionary[(station[1]).town]:
            risk_dictionary[(station[0]).town] = station[1]
        
        else:
            pass

    return risk_dictionary



def risk_rater(risk):
    severe_tol = 0.3
    high_tol = 0.2
    moderate_tol = 0.1

    if risk >= severe_tol:
        return "Severe"

    elif high_tol <= risk < severe_tol:
        return "High"
    
    elif moderate_tol <= risk < high_tol:
        return "Moderate"

    elif risk < moderate_tol:
        return "Low"
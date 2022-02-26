from unicodedata import name
import numpy as np
import matplotlib
from .stationdata import build_station_list
from floodsystem.station import MonitoringStation, inconsistent_typical_range_stations
from floodsystem.stationdata import update_water_levels
import datetime
from floodsystem.datafetcher import fetch_measure_levels

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
        for k in range (len(inconsistent_station_names)):
            if i.name != inconsistent_station_names[k]:
                consistent_stations.append(i)

    #Take the relative water level of every consistent station
    current_rel_water_levels = []
    update_water_levels(stations)
    
    for i in consistent_stations:
        
        current_rel_water_levels.append(i.relative_water_level())

    #Take the predicted water levels for the next day 
        # Fetch data over past 2 days
        dt = 2
        dates, levels = fetch_measure_levels(i.measure_id, dt=datetime.timedelta(days=dt))
        poly, d0 = polyfit(dates, levels, 4)
        day_today = max(matplotlib.dates.dates2num(dates) - d0)

        #predict tomorrow
        predicted = poly(day_today + 1)
        rel_predicted = ((predicted - i.typical_range[0])/i.typical_range[1] - i.typical_range[0])

        return rel_predicted[:5]


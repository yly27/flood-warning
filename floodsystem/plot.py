import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import matplotlib
from floodsystem.analysis import polyfit
from floodsystem.flood import stations_highest_rel_level
import numpy as np

def plot_water_levels(station, dates, levels):

    plt.plot(dates, levels)

    #Labelling 
    plt.title('S')
    plt.xlabel('Date')
    plt.ylabel('Water Level (m)')
    plt.xticks(rotation=45)
    plt.title(station.name)

    #Plotting typical ranges 
    plt.axhline(y=station.typical_range[0], linestyle = ':')
    plt.axhline(y=station.typical_range[1], linestyle = ':')

    plt.tight_layout()
    plt.show()



def plot_water_level_with_fit(station, dates, levels, p):
    if dates == None or levels == None:
        pass

    else:
        poly, d0 = polyfit(dates, levels, p)
        dates = matplotlib.dates.date2num(dates) - d0
        x = np.linspace(dates[0],dates[-1],30)
        
        plt.plot(dates, levels, '.')
        plt.plot(x, poly(x), label = "Best-fit polynomial")
        plt.plot(x, np.linspace(station.typical_range[0],station.typical_range[0],30), '-b', label = "Typical relative low value")
        plt.plot(x, np.linspace(station.typical_range[1],station.typical_range[1],30), '-g', label = "Typical relative high value")
        plt.legend(loc = 'best')

        plt.xlabel("Number of days ago")
        plt.ylabel("Relative water level")
        plt.title(station.name)
        plt.tight_layout()

    plt.show()


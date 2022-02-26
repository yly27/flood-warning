import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import matplotlib

def plot_water_levels(station, dates, levels):

    plt.plot(dates, levels)

    #Labelling 
    plt.title('S')
    plt.xlabel('Date')
    plt.ylabel('Water Level (m)')
    plt.xticks(rotation=45)
    plt.title(station.name)

    plt.tight_layout

    

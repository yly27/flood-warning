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

    #Plotting typical ranges 
    plt.axhline(y=station.typical_range[0], linestyle = ':')
    plt.axhline(y=station.typical_range[1], linestyle = ':')

    plt.tight_layout()
    plt.show()

    

import numpy as np
import matplotlib

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

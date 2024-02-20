import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit

    x = range(df['Year'].min(), 2051)
    slope, intercept, r, p, se = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    plt.plot(x, intercept + slope*x, 'r', label='fitted line')

    # Create second line of best fit

    df_f = df[df['Year'] >= 2000]
    x = range(2000, 2051)
    slope, intercept, r, p, se = linregress(df_f['Year'], df_f['CSIRO Adjusted Sea Level'])    

    # Add labels and title
    plt.plot(x, intercept + slope*x, 'g', label='fitted line')
    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
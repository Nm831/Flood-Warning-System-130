import matplotlib.pyplot as plt
from datetime import datetime, timedelta


def plot_water_levels(station, dates, levels):
    

    t = dates
    level = levels

    # Plot
    plt.plot(t, level)

    # Add axis labels, rotate date labels and add plot title
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45);
    plt.title("Stations {}".format(station.name))

    plt.axhline(y=station.typical_range[0],linestyle ='--')
    plt.axhline(y=station.typical_range[1],linestyle ='--')

    # Display plot
    plt.tight_layout()  # This makes sure plot does not cut off date labels

    plt.show()
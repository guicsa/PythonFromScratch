import pandas as pd
import matplotlib.pyplot as plt

air_quality = pd.read_csv("../99 - Data/air_quality_no2.csv", index_col=0, parse_dates=True)

print(air_quality.head(3))

air_quality.plot.scatter(x="station_london",y="station_paris", alpha=0.5)
plt.show()


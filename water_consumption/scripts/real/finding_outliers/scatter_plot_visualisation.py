#!/bin/python3
import sys
sys.path.append("/home/krizondr/school/past/stat_projekt/water_consumption/scripts")
from input_data_parse.input_data_parser import WaterConsumption
from scipy import stats
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns

matplotlib.use("WebAgg")

# We load all the original data with all the outliers.
watCons = WaterConsumption('water_consumption_september_2022.csv')

dataA = watCons.get_consumptions_in_block("A")
dataB = watCons.get_consumptions_in_block("B")
dataC = watCons.get_consumptions_in_block("C")


# Calculate the total water consumption for each apartment over the month.
total_consumptionA = np.sum(dataA, axis=1)
total_consumptionB = np.sum(dataB, axis=1)
total_consumptionC = np.sum(dataC, axis=1)

print(dataA)
print(total_consumptionA)
# Total water consumption by entrances

plt.figure(figsize=(8, 6))
plt.scatter(watCons.get_flat_in_block("A"), total_consumptionA, color='red', marker='+', label='Data Points')
plt.scatter(watCons.get_flat_in_block("B"), total_consumptionB, color='blue', marker='+', label='Data Points')
plt.scatter(watCons.get_flat_in_block("C"), total_consumptionC, color='green', marker='+', label='Data Points')

# Add labels and title.
plt.xlabel('X-axis Label')
plt.ylabel('Y-axis Label')
plt.title('Scatter Plot Example')

# Add a legend (if needed).
plt.legend()

plt.grid(True)  # Add grid lines (optional).
plt.show()

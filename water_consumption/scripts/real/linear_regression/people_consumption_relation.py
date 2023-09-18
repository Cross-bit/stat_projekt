#!/bin/python3
import sys
sys.path.append("/home/krizondr/school/past/stat_projekt/water_consumption/scripts")
from input_data_parse.input_data_parser import WaterConsumption
from scipy import stats
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

matplotlib.use("WebAgg")


df = pd.read_csv('../../input_data/water_consumption_september_2022_no_outliers.csv', decimal=",")

# this is the X (independent)
people_count = df['#osob'].values.reshape(-1, 1)
# this is the Y (dependent)
total_water_consumption = df.loc[:, "1":"30"].sum(axis=1).values.reshape(-1, 1)


model = LinearRegression()
model.fit(people_count, total_water_consumption)

r_score = np.corrcoef(people_count.flatten(), total_water_consumption.flatten())[0,1]
r_squared = model.score(people_count, total_water_consumption)

y_pred = model.predict(people_count)

residuals = total_water_consumption - y_pred
print(residuals.flatten())
print("R-squared:", r_squared)
print("R:", r_score)

plt.figure(figsize=(8, 6))

# Plot the data points and the regression line
plt.scatter(people_count, total_water_consumption, label='Hodnoty')
plt.plot(people_count, y_pred, color='red', label='Regresní přímka')
plt.xlabel('Počet lidí v jednotce')
plt.ylabel('Celková spotřeba vody jednotky')
plt.legend()




plt.figure(figsize=(12, 6))

values, bins, bars = plt.hist(np.round(residuals, 3), edgecolor='k', density=True, bins=30, alpha=0.5)

plt.xlabel('Hodnota')
plt.ylabel('Četnost')
plt.title('Histogram chyb')
print(stats.shapiro(residuals))


plt.figure(figsize=(8, 6))
quantiles, values = stats.probplot(residuals.flatten(), dist=stats.norm, plot=plt)
plt.title("Q-Q Plot pro normální rozdělení")
plt.xlabel("Teoretické kvantily")
plt.ylabel("Kvantily vzorku")

plt.figure(figsize=(8, 6))
sns.scatterplot(x=y_pred.flatten(), y=residuals.flatten())
plt.xlabel("Fitted Values")
plt.ylabel("Residuals")
plt.title("Residuals vs. Fitted Values Plot")

# Add a horizontal line at y=0 for reference
plt.axhline(y=0, color='red', linestyle='--')

plt.show()
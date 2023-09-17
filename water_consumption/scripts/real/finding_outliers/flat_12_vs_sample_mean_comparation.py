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

# NOTE: Using webAgg here, need to set DISPLAY=:0 and the underlying render api as needed !!!!
matplotlib.use("WebAgg")

df = pd.read_csv('../../input_data/water_consumption_september_2022.csv', decimal=",")

all_data_without_12 = df.set_index('id').drop(12).loc[:, "1":"30"]

all_data_mean = all_data_without_12.mean().mean()
print(all_data_mean)

row_12_days = df.set_index('id').loc[12,"1":]

#print(all_data_mean)

#plt.figure(figsize=(8,6))
fig, ax = plt.subplots()
fig.set_size_inches(12, 5)
sns.set_style("darkgrid")

sns.lineplot(data=row_12_days)

#sns.lineplot(data=all_data_without_12)

ax.axhline(y=all_data_mean, color='red', label='Constant Value')

plt.ylabel("Spotřeba za jednotku [$m^3$]")
plt.xlabel("Den v měsíci")

plt.title('Porovnání spotřeby 12. bytu oproti ostatním', fontsize=15, pad=10)

plt.show()
#!/bin/python3
from scipy import stats
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns

# NOTE: Using webAgg here, need to set DISPLAY=:0 and the underlying render api as needed !!!!
matplotlib.use("WebAgg")

df = pd.read_csv('../input_data/water_consumption_september_2022.csv', decimal=",")

df_no_outliers = pd.read_csv('../input_data/water_consumption_september_2022_no_outliers.csv', decimal=",") ## these are already completly cleaned data

#all_data_without_12 = df.set_index('id').drop(12).loc[:, "1":"30"]
all_data_no_outliers = df_no_outliers.loc[:, "1":"30"]

all_data_mean = all_data_no_outliers.mean().mean() #all_data_without_12.mean().mean()

print(f"Mean without outliers: {all_data_mean}")

row_12_days = df.set_index('id').loc[12,"1":]

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
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

matplotlib.use("WebAgg")

plt.figure(figsize=(8, 6))

df = pd.read_csv('../../input_data/water_consumption_september_2022_no_outliers.csv', decimal=",")


all_vals_flat_no_outliers = df.loc[:, "1":"30"].stack()
#print(all_vals_flat)

all_mean = np.mean(all_vals_flat_no_outliers)
lambda_hat = 1/all_mean
print("mean of all values " + str(all_mean))
rv = stats.expon(scale=1/lambda_hat)


values, bins, bars = plt.hist(all_vals_flat_no_outliers, edgecolor='k', density=True, bins='auto', alpha=0.5)
plt.bar_label(bars, fontsize=10, color='navy')
x = np.linspace(np.min(all_vals_flat_no_outliers), np.max(all_vals_flat_no_outliers))

plt.plot(x, rv.pdf(x), alpha=0.4);


plt.figure(figsize=(8, 6))


plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram of all Data')


quantiles, values = stats.probplot(all_vals_flat_no_outliers, dist=stats.expon, plot=plt)
plt.title("Q-Q Plot")

plt.figure(figsize=(8, 6))
quantiles, values = stats.probplot(all_vals_flat_no_outliers, dist=stats.gamma(2, scale=2), plot=plt)
plt.title("Q-Q Plot for Gamma Distribution")


plt.show();


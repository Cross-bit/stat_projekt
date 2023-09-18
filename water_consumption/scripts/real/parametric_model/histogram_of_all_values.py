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

df = pd.read_csv('../../input_data/water_consumption_september_2022_no_outliers.csv', decimal=",")

plot_estimated_pdf = True

# Data load

all_vals_flat_no_outliers = df.loc[:, "1":"30"].stack()

# MLE estimator calculation

sample_mean = np.mean(all_vals_flat_no_outliers)

mle = 1 / sample_mean

print("Lambda estimate:")
print(mle)


expon_estimated = stats.expon(scale=1/mle)

plt.figure(figsize=(12, 6))

values, bins, bars = plt.hist(np.round(all_vals_flat_no_outliers, 3), edgecolor='k', density=True, bins=50, alpha=0.5)

#plt.bar_label(bars, fontsize=5, color='navy')

if plot_estimated_pdf:
    x = np.linspace(np.min(all_vals_flat_no_outliers), np.max(all_vals_flat_no_outliers))
    plt.plot(x, expon_estimated.pdf(x), alpha=0.7);

plt.xlabel('Hodnota')
plt.ylabel('Četnost')
plt.title('Histogram hodnot denní spotřeby')

plt.show()
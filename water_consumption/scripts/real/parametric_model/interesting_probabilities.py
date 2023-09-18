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


# Data load

all_vals_flat_no_outliers = df.loc[:, "1":"30"].stack()

# MLE estimator calculation

sample_mean = np.mean(all_vals_flat_no_outliers)

mle = 1 / sample_mean

print("Lambda estimate:")
print(mle)

expon_estimated = stats.expon(scale=1/mle)

generated_values = expon_estimated.rvs(size=630)
print(all_vals_flat_no_outliers)


exit()
num_of_tests = 50
p_vals = []
for x in range(0, 80):
    # Divide your data into bins
    bins = np.linspace(np.min(all_vals_flat_no_outliers), np.max(all_vals_flat_no_outliers), 5)

    observed_frequencies = np.histogram(all_vals_flat_no_outliers, bins)[0]

    generated_values = expon_estimated.rvs(size=630)

    generated_frequencies = np.histogram(generated_values, bins)[0]

    if (np.sum(generated_frequencies) == 629):
        generated_frequencies[0] = generated_frequencies[0] + 1

    if(np.sum(observed_frequencies) == 629):
        observed_frequencies[0] = observed_frequencies[0] + 1

    generated_frequencies = (np.array(generated_frequencies) + 1).tolist()
    observed_frequencies = (np.array(observed_frequencies) + 1).tolist()
    
    chi_square_statistic, p_value = stats.chisquare(f_obs=observed_frequencies, f_exp=generated_frequencies, ddof=1)
    p_vals.append(p_value)



values, bins, bars = plt.hist(np.round(p_vals, 3), edgecolor='k', density=True, bins=50, alpha=0.5)
print(np.mean(p_vals))

plt.xlabel('Hodnota')
plt.ylabel('Četnost')
plt.title('Histogram hodnot denní spotřeby')

plt.show()




print("p-value")
print(p_value)

print("KS")
print("p-value")
#print(all_vals_flat_no_outliers)
ks_statistic, ks_p_value = stats.kstest(all_vals_flat_no_outliers, cdf=generated_values);
print(ks_p_value)
exit();
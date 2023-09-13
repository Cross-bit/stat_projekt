#!/bin/python3
from input_data_parse.input_data_parser import PersonalHearthPressureData
from scipy import stats
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm
matplotlib.use("WebAgg")

hearth_pressure = PersonalHearthPressureData();

systolic_pressuers = hearth_pressure.get_systolic_pressures(True);
diastolic_pressuers = hearth_pressure.get_dyastolic_pressures(True);

distribution = stats.norm

data = systolic_pressuers

num_resamples = 500

# Create an array to store bootstrap sample means
bootstrap_means = []

# Perform bootstrapping
for _ in range(num_resamples):
    # Randomly sample with replacement from the original data
    bootstrap_sample = np.random.choice(data, size=len(data), replace=True)
    
    # Calculate the mean of the bootstrap sample
    bootstrap_mean = np.mean(bootstrap_sample)
    
    # Store the bootstrap sample mean
    bootstrap_means.append(bootstrap_mean)



#ks_statistic, p_value = stats.kstest(bootstrap_means, distribution.cdf)
statistic, p_value = stats.shapiro(systolic_pressuers)
print("systolic: ");
print(p_value);
statistic, p_value = stats.shapiro(diastolic_pressuers)
print("diastolic: ");
print(p_value);


data = systolic_pressuers

std_dev = np.std(data)
mean = np.mean(data)



#plt.hist(diastolic_pressuers, bins=40, edgecolor='k')
print(data)

x = np.linspace(np.min(data), np.max(data), 100)
pdf = norm.pdf(x, mean, std_dev)
plt.hist(data, edgecolor='k', density=True, alpha=0.5, bins=25)

plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram of Data')

plt.show()






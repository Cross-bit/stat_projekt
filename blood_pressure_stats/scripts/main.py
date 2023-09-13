#!/bin/python3

from input_data_parse.input_data_parser import PersonalHearthPressureData
from scipy import stats
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

matplotlib.use("WebAgg")

hearth_pressure = PersonalHearthPressureData();

systolic_pressuers = hearth_pressure.get_systolic_pressures(True);
diastolic_pressuers = hearth_pressure.get_dyastolic_pressures(True);

#statistic, p_value = stats.shapiro(dyastolic_pressuers)

#print(stats.shapiro(systolic_pressuers))
data = systolic_pressuers
# Number of bootstrap resamples
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

print(stats.shapiro(bootstrap_means));

plt.hist(bootstrap_means, bins=100, edgecolor='k')  # Adjust the number of bins as needed
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram of Data')
plt.show()
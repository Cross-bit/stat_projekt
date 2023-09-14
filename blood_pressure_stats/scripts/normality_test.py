#!/bin/python3
from input_data_parse.input_data_parser import PersonalHearthPressureData
from scipy import stats
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pingouin as pg
from scipy.stats import norm

matplotlib.use("WebAgg")

hearth_pressure = PersonalHearthPressureData();

systolic_pressuers = hearth_pressure.get_systolic_pressures(True);
diastolic_pressuers = hearth_pressure.get_dyastolic_pressures(True);

distribution = stats.norm

data = diastolic_pressuers

statistic, p_value = stats.shapiro(systolic_pressuers)
print("systolic: ");
print(p_value);
statistic, p_value = stats.shapiro(diastolic_pressuers)
print("diastolic: ");
print(p_value);


data = diastolic_pressuers

std_dev = np.std(data)
mean = np.mean(data)

print(data)

x = np.linspace(np.min(data), np.max(data), 1000)
pdf = norm.pdf(x, mean, std_dev)
plt.hist(data, edgecolor='k', density=True, alpha=0.5, bins=25)

plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram of Data')



plt.figure(figsize=(8, 6))
#pg.qqplot(data, dist='norm', confidence=.95)
quantiles, values = stats.probplot(data, dist='norm', plot=plt)
plt.title("Q-Q Plot for Normal Distribution")

plt.show()






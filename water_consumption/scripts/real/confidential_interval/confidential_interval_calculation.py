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

# Data load

df = pd.read_csv('../../input_data/water_consumption_september_2022_no_outliers.csv', decimal=",")


# Calculation of confidentional interval
all_data = df.loc[:, "1":"30"]
sample_mean = all_data.mean().mean();
z_score = 1.96
population_std = 0.0554 #all_data.std().std()

sample_size = all_data.size;
print(all_data.std().std())

upper_bound = sample_mean + (z_score * (population_std/np.sqrt(sample_size)))
lower_bound = sample_mean - (z_score * (population_std/np.sqrt(sample_size)))

print("Upper boundary:")
print(upper_bound)
print("Lower boundary:")
print(lower_bound)

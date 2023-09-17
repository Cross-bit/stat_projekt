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

df = pd.read_csv('../../input_data/water_consumption_population_2022.csv', decimal=",")

consumption_only = df.iloc[:, 1:]

population_variance = consumption_only.var().var()
# Calculation method (uses n-1 normalisation) https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.var.html

population_mean  = consumption_only.mean().mean()


print("Population variance:")
print(population_variance)
print("Standard deviation:")
print(np.sqrt(population_variance))
print("Population mean:")
print(population_mean)









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
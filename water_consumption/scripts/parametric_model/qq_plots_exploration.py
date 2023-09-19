#!/bin/python3
from scipy import stats
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns

matplotlib.use("WebAgg")


# Data load

df = pd.read_csv('../../input_data/water_consumption_september_2022_no_outliers.csv', decimal=",")

all_vals_flat_no_outliers = df.loc[:, "1":"30"].stack()

# Distribution comparision testing

## Poison
plt.figure(figsize=(8, 6))
quantiles, values = stats.probplot(all_vals_flat_no_outliers, dist=stats.poisson, sparams=(all_vals_flat_no_outliers.mean() ), plot=plt)
plt.title("Q-Q Plot pro Poissonovskou distribuci")
plt.xlabel("Teoretické kvantily")
plt.ylabel("Kvantily vzorku")

## Normal
plt.figure(figsize=(8, 6))
quantiles, values = stats.probplot(all_vals_flat_no_outliers, dist=stats.norm, plot=plt)
plt.title("Q-Q Plot pro normální rozdělení")
plt.xlabel("Teoretické kvantily")
plt.ylabel("Kvantily vzorku")

## Uniform
plt.figure(figsize=(8, 6))
quantiles, values = stats.probplot(all_vals_flat_no_outliers, dist=stats.uniform(2, scale=2), plot=plt)
plt.title("Q-Q Plot pro uniformní rozdělení")
plt.xlabel("Teoretické kvantily")
plt.ylabel("Kvantily vzorku")

## Exponential
plt.figure(figsize=(8, 6))
quantiles, values = stats.probplot(all_vals_flat_no_outliers, dist=stats.expon, plot=plt)
plt.title("Q-Q Plot pro exponencionální rozdělení")
plt.xlabel("Teoretické kvantily")
plt.ylabel("Kvantily vzorku")

## Gamma
plt.figure(figsize=(8, 6))
quantiles, values = stats.probplot(all_vals_flat_no_outliers, dist=stats.gamma(2, scale=2), plot=plt)
plt.title("Q-Q Plot pro gamma rozdělení")
plt.xlabel("Teoretické kvantily")
plt.ylabel("Kvantily vzorku")

plt.show();


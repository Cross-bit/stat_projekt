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


df = pd.read_csv('../../input_data/water_consumption_september_2022_no_outliers.csv', decimal=",")

# we sum values in the rows (of each flat)
summed_rows = df.loc[: , "1":"30"].sum(axis=1)
summed_rows.name = "sum"

rows_with_entrances = pd.concat([df['vchod'], summed_rows], axis=1)

sums_a = rows_with_entrances[rows_with_entrances['vchod'] == 'A'];
sums_b = rows_with_entrances[rows_with_entrances['vchod'] == 'B'];
sums_c = rows_with_entrances[rows_with_entrances['vchod'] == 'C'];

data_result = pd.DataFrame({ 'vchod': [], 'min': [], 'max': [], 'mean': [], 'Q1': [], 'Q3': [], 'median': [], 'upper whisker': [], 'lower whisker': [] })

for entrance_data in [sums_a, sums_b, sums_c]:
    summary_stats = entrance_data.describe()

    # calculating the IQR using Tukey method
    Q1 = summary_stats.loc['25%', 'sum']
    Q3 = summary_stats.loc['75%', 'sum']
    median = summary_stats.loc['50%', 'sum']

    IQR = Q3 - Q1

    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    outliers = summary_stats[(summary_stats['sum'] < lower_bound) | (summary_stats['sum'] > upper_bound)]

    min_value = summary_stats.loc['min', 'sum']
    max_value = summary_stats.loc['max', 'sum']
    mean_value = summary_stats.loc['mean', 'sum']
    
    entrance = entrance_data.iloc[0]['vchod']
    new_data = {'vchod': [entrance], 'min': [min_value], 'max': [max_value], 'mean': [mean_value], 
                'Q1': [Q1], 'Q3': [Q3], 'median': [median], 'upper whisker': [upper_bound], 'lower whisker': [lower_bound] }
    
    new_df = pd.DataFrame(new_data)
    data_result = pd.concat([data_result, new_df], ignore_index=True)


# Print the stats
print(data_result)

# save the table
with open('../../../assets/html/boxplot_with_outliers_table.html', 'w') as f:
    f.write(data_result.to_html())


# Print final box plot
plt.figure(figsize=(8,6))
sns.set_style("darkgrid")

sns.boxplot(x="vchod", y="sum", data=rows_with_entrances, whis=1.5)
sns.swarmplot(x="vchod", y="sum", data=rows_with_entrances, marker="o", color="red", alpha=0.5)

data_result.set_index('vchod')
# plot explicitly means
plt.scatter([0], [data_result.set_index('vchod').loc['A', 'mean']], color='black', marker='+', label='Mean')
plt.scatter([1], [data_result.set_index('vchod').loc['B', 'mean']], color='black', marker='+', label='Mean')
plt.scatter([2], [data_result.set_index('vchod').loc['C', 'mean']], color='black', marker='+', label='Mean')

plt.ylabel("Celková spotřeba za jednotku [$m^3$]")
plt.xlabel("Jednotlivé vchody")
plt.title('Box plot celkové spotřeby bytů dle jednotlivých vchodů', fontsize=15, pad=10)

plt.show()
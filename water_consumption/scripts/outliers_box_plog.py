#!/bin/python3
from input_data_parse.input_data_parser import WaterConsumption
from scipy import stats
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
matplotlib.use("WebAgg")



watCons = WaterConsumption()

dataA = watCons.get_consumptions_in_block("A")
dataB = watCons.get_consumptions_in_block("B")
dataC = watCons.get_consumptions_in_block("C")



print();
# Calculate the total water consumption for each apartment over the month.
total_consumptionA = np.sum(dataA, axis=1)
total_consumptionB = np.sum(dataB, axis=1)
total_consumptionC = np.sum(dataC, axis=1)

new_vals = np.concatenate((total_consumptionA, total_consumptionB, total_consumptionC))
all_vals = watCons.get_all_consumption_matrix()
all_vals_flat = np.array(all_vals).flatten()


rnds =[]
for val in all_vals_flat:
    if(val > 0.05):
        rnds.append(int(np.round(val*1000)));


print(rnds)
statistic, p_value = stats.shapiro(rnds)
print("p-value: ");
print(p_value);

fit_params = stats.expon.fit(rnds)

ks_statistic_e, p_value_e = stats.kstest(rnds, 'expon', args=fit_params)

print("P-value:", p_value_e)


mean = np.mean(rnds)
poisson_dist = stats.poisson(mean)

# Generate the cumulative distribution function (CDF) for your data.
data_cdf = np.arange(0, max(rnds) + 1) / len(rnds)

# Generate the CDF for the Poisson distribution.
poisson_cdf = poisson_dist.cdf(np.arange(0, max(rnds) + 1))

# Perform the KS test to compare the two CDFs.
ks_statistic, p_value_p = stats.kstest(data_cdf, poisson_cdf)

# Print the chi-square statistic and p-value.
print("P-value po:", p_value_p)



plt.hist(rnds, edgecolor='k', density=True, alpha=0.5, bins=100)

plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram of Data')

# Create a box plot of the total consumption for all apartments.
plt.figure(figsize=(8, 6))

boxplot = plt.boxplot(total_consumptionA, vert=True)

plt.xlabel('Total Monthly Water Consumption')
plt.title('Box Plot of Total Monthly Water Consumption for All Apartments')

apartment_labels = [f'Apartment {i+1}' for i in range(len(total_consumptionA))]
#plt.xticks(range(1, len(total_consumptionA) + 1), labels=apartment_labels)



# Create a box plot of the total consumption for all apartments.
plt.figure(figsize=(8, 6))
blotB = plt.boxplot(total_consumptionB, vert=True)

# Get the outlier positions and values.
outliers = blotB['fliers'][0].get_data()
outlier_x_positions = outliers[0]
outlier_y_values = outliers[1]

# Add labels for the outliers.
for x, y in zip(outlier_x_positions, outlier_y_values):
    plt.annotate(f'{y:.2f}', (x, y), textcoords='offset points', xytext=(0, 10), ha='center')


zero_outliers = [x for x in total_consumptionB if x < 0.05]
plt.scatter(zero_outliers, [1] * len(zero_outliers), c='red', marker='o', label='Zero Outliers')



print(blotB['fliers'][0].get_data()[1])

plt.xlabel('Total Monthly Water Consumption')
plt.title('Box Plot of Total Monthly Water Consumption for All Apartments')


#apartment_labels = [f'Apartment {i+1}' for i in range(len(total_consumptionB))]
#plt.yticks(range(1, len(total_consumptionB) + 1), labels=apartment_labels)



plt.figure(figsize=(8, 6))

blotB = plt.boxplot(total_consumptionC, vert=True)

print(blotB['fliers'][0].get_data()[1])

plt.xlabel('Total Monthly Water Consumption')
plt.title('Box Plot of Total Monthly Water Consumption for All Apartments')

#apartment_labels = [f'Apartment {i+1}' for i in range(len(total_consumptionC))]
#plt.yticks(range(1, len(total_consumptionC) + 1), labels=apartment_labels)


# Create a violin plot using Seaborn.
plt.figure(figsize=(8, 6))
sns.violinplot(x=total_consumptionA, orient='h', color='skyblue')

plt.xlabel('Total Monthly Water Consumption')
plt.title('Violin Plot of Total Monthly Water Consumption for All Apartments')


plt.figure(figsize=(8, 6))
sns.kdeplot(total_consumptionC, shade=True, color='skyblue')

plt.xlabel('Data Values')
plt.ylabel('Density')
plt.title('Kernel Density Plot')


plt.figure(figsize=(8, 6))
plt.scatter(watCons.get_flat_in_block("A"), total_consumptionA, color='blue', marker='o', label='Data Points')

# Add labels and title.
plt.xlabel('X-axis Label')
plt.ylabel('Y-axis Label')
plt.title('Scatter Plot Example')

# Add a legend (if needed).
plt.legend()

# Show the plot.
plt.grid(True)  # Add grid lines (optional).


plt.figure(figsize=(8, 6))
plt.scatter(watCons.get_flat_in_block("B"), total_consumptionB, color='blue', marker='o', label='Data Points')

# Add labels and title.
plt.xlabel('X-axis Label')
plt.ylabel('Y-axis Label')
plt.title('Scatter Plot Example')

# Add a legend (if needed).
plt.legend()

# Show the plot.
plt.grid(True)  # Add grid lines (optional).


# Add a legend (if needed).
plt.legend()

# Show the plot.
plt.grid(True)  # Add grid lines (optional).


plt.figure(figsize=(8, 6))
plt.scatter(watCons.get_flat_in_block("C"), total_consumptionC, color='blue', marker='o', label='Data Points')

# Add labels and title.
plt.xlabel('X-axis Label')
plt.ylabel('Y-axis Label')
plt.title('Scatter Plot Example')

# Add a legend (if needed).
plt.legend()

# Show the plot.
plt.grid(True)  # Add grid lines (optional).


plt.figure(figsize=(8, 6))
#plt.scatter(watCons.get_flat_in_block(), np.concatenate((total_consumptionA, total_consumptionB, total_consumptionC)), color='blue', marker='o', label='Data Points')
plt.scatter(watCons.get_flat_in_block("A"), total_consumptionA, color='red', marker='o', label='Data Points')
plt.scatter(watCons.get_flat_in_block("B"), total_consumptionB, color='blue', marker='o', label='Data Points')
plt.scatter(watCons.get_flat_in_block("C"), total_consumptionC, color='green', marker='o', label='Data Points')

# Add labels and title.
plt.xlabel('X-axis Label')
plt.ylabel('Y-axis Label')
plt.title('Scatter Plot Example')

# Add a legend (if needed).
plt.legend()



plt.grid(True)  # Add grid lines (optional).




plt.show()


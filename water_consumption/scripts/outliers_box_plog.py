#!/bin/python3
from input_data_parse.input_data_parser import WaterConsumption
from scipy import stats
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
matplotlib.use("WebAgg")



watCons = WaterConsumption('water_consumption_9_12_2022.csv')

dataA = watCons.get_consumptions_in_block("A")
dataB = watCons.get_consumptions_in_block("B")
dataC = watCons.get_consumptions_in_block("C")


# Calculate the total water consumption for each apartment over the month.
total_consumptionA = np.sum(dataA, axis=1)
total_consumptionB = np.sum(dataB, axis=1)
total_consumptionC = np.sum(dataC, axis=1)


plt.figure(figsize=(8, 6))

values, bins, bars = plt.hist(dataA[0], edgecolor='k', density=True, bins='auto', alpha=0.5)
plt.title('A')

plt.figure(figsize=(8, 6))
values, bins, bars = plt.hist(dataB[0], edgecolor='k', density=True, bins='auto', alpha=0.5)
plt.title('B')

plt.figure(figsize=(8, 6))
values, bins, bars = plt.hist(dataC[0], edgecolor='k', density=True, bins='auto', alpha=0.5)
plt.title('C')

plt.figure(figsize=(8, 6))
#print(dataC)

all_vals = watCons.get_all_consumption_matrix()
all_vals_flat = np.array(all_vals).flatten()

quantiles, values = stats.probplot(all_vals_flat, dist=stats.norm, plot=plt)
plt.title("Q-Q Plot for expon entrance Distribution")


total_flat_18 = watCons.get_consumption_in_day_flat(24);

plt.figure(figsize=(8, 6))

#print(total_flat_18)
valuesaa, binsaa, barsaa = plt.hist(total_flat_18, edgecolor='k', density=True, bins=10, alpha=0.5)
plt.title('f 18')

plt.figure(figsize=(8, 6))
valuesa, binsa, barsa = plt.hist(total_consumptionA, edgecolor='k', density=True, bins=50, alpha=0.5)
plt.title('f A')

plt.figure(figsize=(8, 6))
valuesa, binsa, barsa = plt.hist(total_consumptionB, edgecolor='k', density=True, bins=50, alpha=0.5)
plt.title('f B')
plt.figure(figsize=(8, 6))
valuesa, binsa, barsa = plt.hist(total_consumptionC, edgecolor='k', density=True, bins=50, alpha=0.5)
plt.title('f C')

plt.bar_label(barsa, fontsize=10, color='navy')


new_vals = np.concatenate((total_consumptionA, total_consumptionB, total_consumptionC))

all_vals = watCons.get_all_consumption_matrix()
all_vals_flat = np.array(all_vals).flatten()

print(all_vals_flat);

rnds =[]
for val in all_vals_flat:
    if(val > 0.05 and val < 1):
        rnds.append(int(np.round(val*1000)));

all_vals_flat_no_outliers = []
for val in all_vals_flat:
    if(val > 0.05 and val < 1):
        all_vals_flat_no_outliers.append(val);


#print(rnds)
statistic, p_value = stats.shapiro(rnds)
print("p-value: ");
print(p_value);

fit_params = stats.expon.fit(all_vals_flat_no_outliers, floc=0.004)
print(fit_params)

#ks_statistic_e, p_value_e = stats.kstest(all_vals_flat_no_outliers, 'expon', args=fit_params)
all_mean = np.mean(all_vals_flat_no_outliers)
lambda_hat = 1/all_mean
print("mean of all values " + str(all_mean))
rv = stats.expon(scale=1/lambda_hat)



desired_value = 0.03 # Replace with the desired total value

# Calculate the cumulative probability for the desired total value using the exponential distribution CDF

cumulative_probability_less_than = 1 - np.exp(-lambda_hat * desired_value)

# Calculate the predicted probability that the total water consumption will be less than or equal to the desired value
predicted_probability = cumulative_probability_less_than

print(f"Predicted probability of total water consumption ≤ {desired_value} in the 1st week of the next month: {predicted_probability:.4f}")


mean = np.mean(rnds)
poisson_dist = stats.poisson(mean)

# Generate the cumulative distribution function (CDF) for your data.
data_cdf = np.arange(0, max(rnds) + 1) / len(rnds)

# Generate the CDF for the Poisson distribution.
poisson_cdf = poisson_dist.cdf(np.arange(0, max(rnds) + 1))

# Perform the KS test to compare the two CDFs.
ks_statistic, p_value_p = stats.kstest(data_cdf, poisson_cdf)

# Print the chi-square statistic and p-value.
#print("P-value po:", p_value_p)


plt.figure(figsize=(8, 6))



values, bins, bars = plt.hist(all_vals_flat_no_outliers, edgecolor='k', density=True, bins='auto', alpha=0.5)

plt.bar_label(bars, fontsize=10, color='navy')

x = np.linspace(np.min(all_vals_flat_no_outliers), np.max(all_vals_flat_no_outliers))

plt.plot(x, rv.pdf(x), alpha=0.4);
plt.plot(x, stats.expon.pdf(x, fit_params[0], fit_params[1]), color="green", alpha=0.5)

plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram of all Data')

plt.figure(figsize=(8, 6))


quantiles, values = stats.probplot(all_vals_flat_no_outliers, dist=stats.expon, plot=plt)
plt.title("Q-Q Plot")
#print(quantiles);
# Calculate residuals
residuals = np.array(quantiles[1]) - np.array(values[1])

# Define a tolerance threshold (e.g., within +/- 0.1)
tolerance = 0.4

# Count the number of points closely following the line
num_closely_following = np.sum(np.abs(residuals) <= tolerance)

print(f"Number of points closely following the line: {num_closely_following} out of {len(all_vals_flat_no_outliers)}")




# Create a box plot of the total consumption for all apartments.
plt.figure(figsize=(8, 6))

quantiles, values = stats.probplot(all_vals_flat_no_outliers, dist=stats.norm, plot=plt)
plt.title("Q-Q Plot for Normal Distribution")

plt.figure(figsize=(8, 6))
quantiles, values = stats.probplot(all_vals_flat_no_outliers, dist=stats.uniform, plot=plt)
plt.title("Q-Q Plot for Uniform Distribution")

plt.figure(figsize=(8, 6))
quantiles, values = stats.probplot(all_vals_flat_no_outliers, dist=stats.gamma(2, scale=2), plot=plt)
plt.title("Q-Q Plot for Gamma Distribution")


plt.figure(figsize=(8, 6))
quantiles, values = stats.probplot(all_vals_flat_no_outliers, dist=stats.lognorm(s=1), plot=plt)
plt.title("Q-Q Plot for Log-Normal Distribution")


plt.figure(figsize=(8, 6))
#quantiles, values = stats.probplot(all_vals_flat_no_outliers, dist=stats.poisson, plot=plt)
stats.probplot(all_vals_flat_no_outliers, dist='poisson', sparams=(2.5,), plot=plt)
plt.title("Q-Q Plot for poisson")


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


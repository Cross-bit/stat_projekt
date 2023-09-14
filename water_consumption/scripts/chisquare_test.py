#!/bin/python3
from input_data_parse.input_data_parser import WaterConsumption
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

from scipy import stats
matplotlib.use("WebAgg")

watCons = WaterConsumption("water_consumption_september_2022_no_outliers.csv")

total_consumptions = watCons.get_total_consumptions()

total_monthly_consumption = np.sum(total_consumptions)

all_people = watCons.get_all_people_array()
group_sizes_aggregated = sorted(list(set(all_people)))[0: -1]

all_people_count = np.sum(watCons.get_all_people_array())



all_groups_means = [] # will be correctly sorted from definition
for group_size in group_sizes_aggregated:
    all_groups_means.append(watCons.get_mean_by_people_count_array(group_size))


# we take the consumption of single person group and linearly scale  
expected_groups_means = []
for group_size in group_sizes_aggregated:
    expected_group_mean = all_groups_means[0] * group_size
    expected_groups_means.append(expected_group_mean)


# since p. chi-square test needs expected and real "frequencies" to have the same sum
# we scale the expected values first
groups_means_sum = sum(all_groups_means)
expected_groups_means_sum = sum(expected_groups_means)

expected_groups_means_normalized = []
for expected_group_mean in expected_groups_means:
    expected_group_mean_normalized = (expected_group_mean / expected_groups_means_sum) * groups_means_sum
    expected_groups_means_normalized.append(expected_group_mean_normalized)

print(expected_groups_means_normalized)

pvalue = stats.chisquare(all_groups_means, expected_groups_means_normalized)
print(pvalue)

print(expected_groups_means)
print(expected_groups_means_normalized)
MSE = np.square(np.subtract(expected_groups_means,expected_groups_means_normalized)).mean()
print("MSE " + str(MSE))

plt.figure(figsize=(10, 8))
plt.scatter(group_sizes_aggregated, all_groups_means, color="blue")
plt.plot(group_sizes_aggregated, all_groups_means,linewidth=0.5, color="blue")

#plt.scatter(group_sizes_aggregated, expected_groups_means, color="green")
#plt.plot(group_sizes_aggregated, expected_groups_means, linewidth=0.5, color="green")

plt.scatter(group_sizes_aggregated, expected_groups_means_normalized, color="red")
plt.plot(group_sizes_aggregated, expected_groups_means_normalized, linewidth=0.5, color="red")

plt.show()
exit()



total_consumptions_expected = []


# we expect that water consumption will grow lineary
total_consumptiosn_by_people_count = {}
for people_count in all_people:
    expected_consumption = total_monthly_consumption * (people_count/all_people_count)
    total_consumptiosn_by_people_count[people_count] = expected_consumption

total_consumptiosn_by_people_count_tuples = sorted(total_consumptiosn_by_people_count.items(), key=lambda x: x[0])


total_consumptions_means = {}

for people_count in all_people:
    total_consumptions_means[people_count] = watCons.get_mean_by_people_count_array(int(people_count))

print("here")
total_consumptions_means_tuples =  sorted(total_consumptions_means.items(), key=lambda x: x[0])
total_consumptions_means_arr = [item[1] for item in total_consumptions_means_tuples]
print(total_consumptions_means)


all_people_aggregated = [item[0] for item in total_consumptiosn_by_people_count_tuples]
total_consumptions_expected_aggregated = [item[1] for item in total_consumptiosn_by_people_count_tuples]

print(all_people_aggregated)

plt.figure(figsize=(10, 8))
plt.scatter(all_people, total_consumptions, color="blue")
plt.scatter(all_people_aggregated, total_consumptions_expected_aggregated, color="red")
plt.scatter(all_people_aggregated, total_consumptions_means_arr, color="green")
#plt.plot(all_people_count, expected_consumptions)

# Add labels and a title
plt.xlabel('People count real(blue)/expected(red)')
plt.ylabel('Consumption in month')
#plt.title('')

print(np.sum(total_consumptions_expected_aggregated))
print(np.sum(total_consumptions_means_arr))
chisq, pvalue = stats.chisquare(total_consumptions_expected_aggregated, total_consumptions_means_arr)

print("Chi-Square Statistic:", chisq)
#print("Degrees of Freedom:", dof)
print("p-value:", pvalue)

# Display the plot (optional)
plt.show()




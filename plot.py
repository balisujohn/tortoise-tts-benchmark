import pandas as pd
import numpy as np
from scipy.stats import t
import matplotlib.pyplot as plt

# Load data from CSV files
df1 = pd.read_csv('time_results_tortoise-tts.csv')
df2 = pd.read_csv('time_results_tortoise-cpp.csv')

# Assuming "Real_time" is a column in both dataframes
data1 = df1['Real_time']
data2 = df2['Real_time']

# Calculate sample statistics
mean1 = np.mean(data1)
mean2 = np.mean(data2)
std1 = np.std(data1, ddof=1)  # ddof=1 for sample standard deviation
std2 = np.std(data2, ddof=1)
n1 = len(data1)
n2 = len(data2)

# Calculate standard error of the mean
SE1 = std1 / np.sqrt(n1)
SE2 = std2 / np.sqrt(n2)

# Plotting the means with error bars as a bar chart
plt.figure(figsize=(8, 6))

bar_width = 0.35
index = np.arange(2)/2

plt.bar(index, [mean1, mean2], bar_width, yerr=[SE1, SE2], color='blue', ecolor='black', capsize=10, label='Standard Error')

# Adding labels and title
plt.xlabel('model')
plt.ylabel('Seconds wallclock time on 1070ti')
plt.title('Time to generate the phrase "Based... Dr. Freeman?"(case insensitive)')
plt.xticks(index, ['tortoise-tts', 'tortoise.cpp'])
plt.legend()

# Show plot
plt.tight_layout()
plt.show()
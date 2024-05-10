import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import os

baseline_folder = "analysis\empatica_bvp_baseline"
task_folder = "analysis\empatica_bvp_task"

# Initialize lists to store results
baseline_means = []
task_means = []
t_statistics = []
p_values = []

# Initialize lists to store data for visualization
baseline_bvp_all = []
task_bvp_all = []

# Clean up outliers using IQR method
def remove_outliers(data):
    Q1 = np.percentile(data, 25)
    Q3 = np.percentile(data, 75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    clean_data = data[(data >= lower_bound) & (data <= upper_bound)]
    return clean_data

# Iterate over each patient's data
for patient_file in os.listdir(baseline_folder):
    if patient_file.endswith(".csv"):
        # Load the Data
        baseline_data = pd.read_csv(os.path.join(baseline_folder, patient_file))
        task_data = pd.read_csv(os.path.join(task_folder, patient_file))
        
        # Store data for visualization
        baseline_bvp_all.append(baseline_data['bvp'])
        task_bvp_all.append(task_data['bvp'])

        # Clean up outliers in baseline and task data
        baseline_clean = remove_outliers(baseline_data['bvp'])
        task_clean = remove_outliers(task_data['bvp'])

        # Calculate means after cleanup
        baseline_mean = baseline_clean.mean()
        task_mean = task_clean.mean()

        # Statistical Analysis
        t_statistic, p_value = stats.ttest_ind(baseline_clean, task_clean)

        # Store results
        baseline_means.append(baseline_mean)
        task_means.append(task_mean)
        t_statistics.append(t_statistic)
        p_values.append(p_value)

        # Print the results
        print(f"Patient {len(baseline_means)-1}:")
        print("Mean of baseline data:", baseline_mean)
        print("Mean of task data:", task_mean)
        print("T-statistic:", t_statistic)
        print("P-value:", p_value)
        print()

        # Visualization (box plot and histogram)
        fig, axs = plt.subplots(1, 2, figsize=(14, 6))

        axs[0].boxplot([baseline_clean, task_clean], labels=['Baseline', 'Task'])
        axs[0].set_title(f'Patient {len(baseline_means)-1}: Blood Volume Pulse Distribution (Outliers Removed)')
        axs[0].set_ylabel('Blood Volume Pulse')
        axs[0].set_xlabel('Condition')
        axs[0].grid(True)

        axs[1].hist(baseline_clean, bins=20, alpha=0.5, label='Baseline')
        axs[1].hist(task_clean, bins=20, alpha=0.5, label='Task')
        axs[1].set_title(f'Patient {len(baseline_means)-1}: Blood Volume Pulse Distribution (Outliers Removed)')
        axs[1].set_xlabel('Blood Volume Pulse')
        axs[1].set_ylabel('Frequency')
        axs[1].legend()

        plt.show()

# Calculate average t-statistic and average p-value after cleanup
avg_t_statistic = np.mean(t_statistics)
avg_p_value = np.mean(p_values)

print("Average T-statistic after cleanup:", avg_t_statistic)
print("Average P-value after cleanup:", avg_p_value)

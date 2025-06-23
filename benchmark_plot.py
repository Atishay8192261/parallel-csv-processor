import matplotlib.pyplot as plt

# Bar data
labels = ['Pandas', 'Dask', 'Dask Optimized']
colors = ['#4CAF50', '#2196F3', '#FFC107']  # Green, Blue, Amber

# 1. Execution Time
exec_times = [10.76, 15.18, 11.29]
plt.figure()
bars = plt.bar(labels, exec_times, color=colors)
plt.ylabel("Execution Time (s)")
plt.title("Execution Time Comparison")
for bar, val in zip(bars, exec_times):
    plt.text(bar.get_x() + bar.get_width()/2, val + 0.5, f"{val:.2f}", ha='center')
plt.savefig("output/execution_time_colored.png")
plt.close()

# 2. Memory Usage
mem_usage = [694.26, 465.27, 733.65]
plt.figure()
bars = plt.bar(labels, mem_usage, color=colors)
plt.ylabel("Memory Usage (MB)")
plt.title("Memory Usage Comparison")
for bar, val in zip(bars, mem_usage):
    plt.text(bar.get_x() + bar.get_width()/2, val + 20, f"{val:.2f}", ha='center')
plt.savefig("output/memory_usage_colored.png")
plt.close()

# 3. CPU Usage
cpu_usage = [46.8, 77.5, 71.2]
plt.figure()
bars = plt.bar(labels, cpu_usage, color=colors)
plt.ylabel("CPU Usage (%)")
plt.title("CPU Usage Comparison")
for bar, val in zip(bars, cpu_usage):
    plt.text(bar.get_x() + bar.get_width()/2, val + 2, f"{val:.2f}", ha='center')
plt.savefig("output/cpu_usage_colored.png")
plt.close()


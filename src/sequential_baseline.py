import pandas as pd
import time
import psutil

# Start measuring total execution time
start_time = time.time()

# Track memory and CPU usage at the start
process = psutil.Process()
start_mem = process.memory_info().rss / 1024 / 1024  # in MB
start_cpu = psutil.cpu_percent(interval=None)

print("Reading CSV...")
csv_start = time.time()
df = pd.read_csv('data/large_data.csv')
csv_end = time.time()
print(f"CSV loaded in {csv_end - csv_start:.2f} seconds")

print("\nPerforming basic analysis...")
analysis_start = time.time()
means = df.mean(numeric_only=True)
stds = df.std(numeric_only=True)
analysis_end = time.time()

print(f"Analysis done in {analysis_end - analysis_start:.2f} seconds")

print("\nColumn-wise Mean:\n", means)
print("\nColumn-wise Standard Deviation:\n", stds)

# End time and memory
end_time = time.time()
end_mem = process.memory_info().rss / 1024 / 1024  # in MB
end_cpu = psutil.cpu_percent(interval=None)

# Execution summary
print("\n--- Execution Summary ---")
print(f"Total execution time: {end_time - start_time:.2f} seconds")
print(f"Memory used: {end_mem - start_mem:.2f} MB")
print(f"CPU usage snapshot: {end_cpu}%")


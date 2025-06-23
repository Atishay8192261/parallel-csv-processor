import dask.dataframe as dd
import time
import psutil

# Start time tracking
start_time = time.time()

# Track system resource usage
process = psutil.Process()
start_mem = process.memory_info().rss / 1024 / 1024  # in MB
start_cpu = psutil.cpu_percent(interval=None)

print("Reading CSV with Dask (parallel, optimized)...")
csv_start = time.time()

# Optimization: use assume_missing and custom blocksize
df = dd.read_csv('data/large_data.csv', assume_missing=True, blocksize="64MB")

# Optimization: persist the data in memory
df = df.persist()

csv_end = time.time()
print(f"CSV loaded (parallel) in {csv_end - csv_start:.2f} seconds")

print("\nPerforming basic analysis (parallel, optimized)...")
analysis_start = time.time()

# Only use numeric columns
numeric_df = df.select_dtypes(include=['number'])

# Compute mean and std
means = numeric_df.mean().compute()
stds = numeric_df.std().compute()

analysis_end = time.time()
print(f"Analysis done in {analysis_end - analysis_start:.2f} seconds")

# Display stats
print("\nColumn-wise Mean (Dask Optimized):\n", means)
print("\nColumn-wise Std Dev (Dask Optimized):\n", stds)

# Total execution time
end_time = time.time()
end_mem = process.memory_info().rss / 1024 / 1024
end_cpu = psutil.cpu_percent(interval=None)

print("\n--- Execution Summary (Dask Optimized) ---")
print(f"Total execution time: {end_time - start_time:.2f} seconds")
print(f"Memory used: {end_mem - start_mem:.2f} MB")
print(f"CPU usage snapshot: {end_cpu}%")


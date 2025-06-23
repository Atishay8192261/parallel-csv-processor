# Parallel CSV Processing and Benchmarking System

A modular, high-performance CSV data processing tool that explores how parallelism impacts system efficiency. This project compares sequential and parallel processing approaches using `pandas` and `dask`, highlighting core systems concepts such as data parallelism, lazy evaluation, and DAG scheduling.

---

## About the Project

As data volumes continue to grow, the performance limitations of traditional single-threaded CSV processing tools like `pandas` become apparent. This project introduces a parallel processing pipeline that addresses these limitations and provides a comparative framework for evaluating different execution strategies.

Key goals include:

- Designing a system that supports multiple execution backends (sequential and parallel)
- Implementing performance-aware processing using modern Python libraries
- Demonstrating key systems concepts in action such as task graph evaluation, persistence, and parallel load balancing
- Visualizing execution behavior through system-level metrics and architecture schematics

---

## Core Features

- Multi-mode execution engine:
  - Sequential: traditional `pandas` pipeline
  - Parallel: scalable `dask.dataframe` engine
  - Optimized: `dask` with persistence and chunking

- Modular performance monitoring system:
  - Time tracking using Python’s `time` module
  - Memory and CPU usage via `psutil` and `htop`

- Lazy evaluation and DAG-based task orchestration

- Visual dashboards and code-generated charts for deeper insights

---

## Tech Stack

| Layer               | Technologies Used       |
|--------------------|-------------------------|
| Language            | Python 3.10             |
| Data Processing     | pandas, dask            |
| Benchmarking Tools  | psutil, time, htop      |
| Visualization       | matplotlib, seaborn     |
| Platform            | macOS (Intel CPU)       |

---

## Architecture

The system consists of the following pipeline stages:

1. **Data Loader**  
   - Loads CSV using `pandas` or `dask`, depending on execution mode

2. **Execution Engine**  
   - Performs column-wise and aggregated operations across the dataset  
   - Uses parallel workers in `dask` for partitioned execution

3. **Resource Monitoring Module**  
   - Tracks runtime performance without interfering with workload execution

4. **Results Aggregator**  
   - Collects raw execution metrics and feeds them into visualization scripts

5. **Visualization Layer**  
   - Produces comparative bar charts and system usage snapshots

---

## Systems Concepts Implemented

- **Amdahl’s Law**  
  Analyzed theoretical speedup limits of parallel execution and how overhead affects real-world gains.

- **Directed Acyclic Graph (DAG) Scheduling**  
  `dask` constructs a task graph of operations, allowing lazy execution and task parallelism.

- **Lazy Evaluation**  
  Ensures operations are only executed when necessary, improving memory and CPU efficiency.

- **Concurrency Safety**  
  All operations are stateless and isolated across partitions, preventing race conditions and deadlocks.

---

## File Structure

```bash
project-root/
│
├── data/
│   └── large_data.csv
│
├── sequential_baseline.py
├── dask_parallel.py
├── dask_optimized.py
│
├── benchmark_utils.py
├── visualizations/
│   ├── cpu_usage.png
│   ├── memory_usage.png
│   └── execution_time.png
│
├── README.md
└── requirements.txt

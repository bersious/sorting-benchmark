# sorting-benchmark
"Benchmarking QuickSort, HeapSort, MergeSort, and NumPy Sort on 1,000,000 elements — TTNT2025"
# 📊 Sorting Benchmark

A performance comparison of classic sorting algorithms on datasets of 1,000,000 elements.

## 📌 Overview

This project benchmarks 4 sorting algorithms across multiple data types and orderings:

- **QuickSort** – iterative, median-of-three pivot
- **HeapSort** – max-heap based, iterative heapify
- **MergeSort** – bottom-up iterative implementation
- **NumPy Sort** – built-in NumPy optimized sort

Test datasets include ascending, descending, and random orders for both `int` and `float` types.

## 📁 Project Structure
sorting-benchmark/
├── sorting_algorithms.py # Implementation of all 4 algorithms
├── benchmark_results.csv # Raw benchmark timing data
├── Bao-Cao-Thu-Nghiem.docx # Experiment report (Vietnamese)
└── README.md

## ⚙️ Requirements

- Python 3.x
- NumPy

Install dependencies:

```bash
pip install numpy
```

## 🏆 Results

| Algorithm  | Avg Time (ms) |
|------------|--------------|
| NumPy Sort | 17.0         |
| QuickSort  | 2467.8       |
| MergeSort  | 2719.8       |
| HeapSort   | 5595.4       |

> NumPy Sort is ~145x faster than pure-Python QuickSort,  
> thanks to low-level C optimizations under the hood.
> ## 📂 Dataset

The original input data files (`.npy` arrays, ~1M elements each) are **not included**
in this repository due to GitHub's file size limitations.

**To reproduce the benchmark locally:**
1. Run the benchmark script — it will generate the test datasets automatically.
2. Results are pre-recorded in [`benchmark_results.csv`](./benchmark_results.csv)
   for reference without re-running.

## 👤 Author

**Nguyễn Thành Thiện Nhân (bersious) ** — Class TTNT2025 

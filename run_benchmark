import numpy as np
import time
import csv
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from sorting_algorithms import quicksort, heapsort, mergesort, numpy_sort

DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')
RESULTS_DIR = os.path.join(os.path.dirname(__file__), 'results')
os.makedirs(RESULTS_DIR, exist_ok=True)

DATASETS = [
    ('float_asc',   'float', 'Tăng dần'),
    ('float_desc',  'float', 'Giảm dần'),
    ('float_rand1', 'float', 'Ngẫu nhiên 1'),
    ('float_rand2', 'float', 'Ngẫu nhiên 2'),
    ('float_rand3', 'float', 'Ngẫu nhiên 3'),
    ('int_asc',     'int',   'Tăng dần'),
    ('int_desc',    'int',   'Giảm dần'),
    ('int_rand1',   'int',   'Ngẫu nhiên 1'),
    ('int_rand2',   'int',   'Ngẫu nhiên 2'),
    ('int_rand3',   'int',   'Ngẫu nhiên 3'),
]

ALGORITHMS = [
    ('QuickSort',  quicksort),
    ('HeapSort',   heapsort),
    ('MergeSort',  mergesort),
    ('NumPy Sort', numpy_sort),
]

def run_benchmark():
    results = []
    total = len(DATASETS) * len(ALGORITHMS)
    done = 0
    for ds_name, ds_type, ds_order in DATASETS:
        arr_orig = np.load(os.path.join(DATA_DIR, f'{ds_name}.npy'))
        for algo_name, algo_fn in ALGORITHMS:
            done += 1
            print(f"[{done:2d}/{total}] {algo_name:12s} | {ds_name:15s} ...", end=" ", flush=True)
            arr = arr_orig.copy()
            t0 = time.perf_counter()
            sorted_arr = algo_fn(arr)
            elapsed = time.perf_counter() - t0
            # Verify correctness
            ok = bool(np.all(sorted_arr[:-1] <= sorted_arr[1:]))
            print(f"{elapsed:7.3f}s  {'OK' if ok else 'FAIL'}")
            results.append({
                'dataset':   ds_name,
                'type':      ds_type,
                'order':     ds_order,
                'algorithm': algo_name,
                'time_sec':  round(elapsed, 4),
                'correct':   ok,
            })
    # Save CSV
    out_path = os.path.join(RESULTS_DIR, 'benchmark_results.csv')
    with open(out_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=results[0].keys())
        writer.writeheader()
        writer.writerows(results)
    print(f"\nResults saved → {out_path}")
    return results

if __name__ == '__main__':
    run_benchmark()

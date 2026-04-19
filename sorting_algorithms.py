import numpy as np
import sys

# ── QuickSort ─────────────────────────────────────────────────────────────────
def _quicksort(arr, low, high):
    if low < high:
        pi = _partition(arr, low, high)
        _quicksort(arr, low, pi - 1)
        _quicksort(arr, pi + 1, high)

def _partition(arr, low, high):
    # Median-of-three pivot
    mid = (low + high) // 2
    if arr[low] > arr[mid]:
        arr[low], arr[mid] = arr[mid], arr[low]
    if arr[low] > arr[high]:
        arr[low], arr[high] = arr[high], arr[low]
    if arr[mid] > arr[high]:
        arr[mid], arr[high] = arr[high], arr[mid]
    pivot = arr[mid]
    arr[mid], arr[high] = arr[high], arr[mid]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quicksort(arr):
    """QuickSort (iterative, median-of-three pivot) – avoids Python recursion limit."""
    a = arr.tolist()
    stack = [(0, len(a) - 1)]
    while stack:
        low, high = stack.pop()
        if low >= high:
            continue
        # partition
        mid = (low + high) // 2
        if a[low] > a[mid]:  a[low], a[mid]   = a[mid],  a[low]
        if a[low] > a[high]: a[low], a[high]  = a[high], a[low]
        if a[mid] > a[high]: a[mid], a[high]  = a[high], a[mid]
        pivot = a[mid]
        a[mid], a[high] = a[high], a[mid]
        i = low - 1
        for j in range(low, high):
            if a[j] <= pivot:
                i += 1
                a[i], a[j] = a[j], a[i]
        pi = i + 1
        a[pi], a[high] = a[high], a[pi]
        stack.append((low,  pi - 1))
        stack.append((pi + 1, high))
    return np.array(a, dtype=arr.dtype)


# ── HeapSort ──────────────────────────────────────────────────────────────────
def _heapify(arr, n, i):
    largest = i
    l, r = 2*i + 1, 2*i + 2
    if l < n and arr[l] > arr[largest]: largest = l
    if r < n and arr[r] > arr[largest]: largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        _heapify(arr, n, largest)

def heapsort(arr):
    """HeapSort – builds a max-heap then extracts elements."""
    a = arr.tolist()
    n = len(a)
    # Build max-heap (iterative)
    for i in range(n // 2 - 1, -1, -1):
        # iterative heapify
        root = i
        while True:
            largest = root
            l, r = 2*root + 1, 2*root + 2
            if l < n and a[l] > a[largest]: largest = l
            if r < n and a[r] > a[largest]: largest = r
            if largest == root:
                break
            a[root], a[largest] = a[largest], a[root]
            root = largest
    # Extract elements
    for end in range(n - 1, 0, -1):
        a[0], a[end] = a[end], a[0]
        root = 0
        while True:
            largest = root
            l, r = 2*root + 1, 2*root + 2
            if l < end and a[l] > a[largest]: largest = l
            if r < end and a[r] > a[largest]: largest = r
            if largest == root:
                break
            a[root], a[largest] = a[largest], a[root]
            root = largest
    return np.array(a, dtype=arr.dtype)


# ── MergeSort ─────────────────────────────────────────────────────────────────
def mergesort(arr):
    """MergeSort – bottom-up iterative implementation."""
    a = arr.tolist()
    n = len(a)
    width = 1
    while width < n:
        for i in range(0, n, 2 * width):
            left  = i
            mid   = min(i + width, n)
            right = min(i + 2 * width, n)
            # merge a[left:mid] and a[mid:right]
            merged = []
            li, ri = left, mid
            while li < mid and ri < right:
                if a[li] <= a[ri]:
                    merged.append(a[li]); li += 1
                else:
                    merged.append(a[ri]); ri += 1
            merged.extend(a[li:mid])
            merged.extend(a[ri:right])
            a[left:right] = merged
        width *= 2
    return np.array(a, dtype=arr.dtype)


# ── NumPy sort (built-in) ─────────────────────────────────────────────────────
def numpy_sort(arr):
    """NumPy built-in sort (introsort / timsort depending on dtype)."""
    return np.sort(arr)

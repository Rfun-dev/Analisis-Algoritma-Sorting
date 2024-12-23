import random
import streamlit
import time
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
import sys

# Selection Sort (Iterative)
sys.setrecursionlimit(10000000)
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# Selection Sort (Recursive)
def selection_sort_recursive(arr, start=0):
    if start >= len(arr) - 1:
        return arr
    min_idx = start
    for i in range(start + 1, len(arr)):
        if arr[i] < arr[min_idx]:
            min_idx = i
    arr[start], arr[min_idx] = arr[min_idx], arr[start]
    return selection_sort_recursive(arr, start + 1)

# Insertion Sort (Iterative)
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Insertion Sort (Recursive)
def insertion_sort_recursive(arr, n=None):
    if n is None:
        n = len(arr)
    if n <= 1:
        return arr
    insertion_sort_recursive(arr, n - 1)
    last = arr[n - 1]
    j = n - 2
    while j >= 0 and arr[j] > last:
        arr[j + 1] = arr[j]
        j -= 1
    arr[j + 1] = last
    return arr

# Median Function
def calculate_median(arr):
    arr_sorted = sorted(arr)
    n = len(arr_sorted)
    mid = n // 2
    if n % 2 == 0:
        return (arr_sorted[mid - 1] + arr_sorted[mid]) / 2
    else:
        return arr_sorted[mid]

# Streamlit App
st.title("Sorting Algorithm Performance Visualizer")

# User inputs
min_range = st.number_input("Masukkan nilai minimum rentang:", value=0, step=1)
max_range = st.number_input("Masukkan nilai maksimum rentang:", value=100, step=1)
total_data = st.number_input("Masukkan jumlah total data:", value=100, step=1)

if st.button("Run Simulation"):
    # Generate data
    data = [random.randint(min_range, max_range) for _ in range(total_data)]
    data_sizes = np.linspace(total_data * 0.2, total_data, 5, dtype=int)

    # Initialize results
    insertion_times = []
    insertion_times_recursive = []
    selection_times = []
    selection_times_recursive = []
    times = {}
    medians = {}
    data = []
    elapsed = 0
    sorted_data = []
    for i in range(total_data):
        data.append(random.randint(min_range, max_range))
        if(len(data) % (total_data/5) == 0):

          # Measure performance for Insertion Sort (Iterative)
          start = time.time()
          sorted_data = insertion_sort(data.copy())
          elapsed = (time.time() - start) + elapsed
          insertion_times.append(time.time())
          times[f"Insertion Sort"] = elapsed
          medians[f"Insertion Sort"] = calculate_median(sorted_data)

          # Measure performance for Insertion Sort (Recursive)
          start = time.time()
          sorted_data = insertion_sort_recursive(data.copy())
          elapsed = (time.time() - start) + elapsed
          insertion_times_recursive.append(time.time())
          times[f"Insertion Sort Recursive"] = elapsed
          medians[f"Insertion Sort Recursive"] = calculate_median(sorted_data)

           # Measure performance for Selection Sort (Iterative)
          start = time.time()
          sorted_data = insertion_sort(data.copy())
          elapsed = (time.time() - start) + elapsed
          selection_times.append(time.time())
          times[f"Selection Sort"] = elapsed
          medians[f"Selection Sort"] = calculate_median(sorted_data)

          # Measure performance for Selection Sort (Recursive)
          start = time.time()
          sorted_data = selection_sort_recursive(data.copy())
          elapsed = (time.time() - start) + elapsed
          selection_times_recursive.append(time.time())
          times[f"Selection Sort Recursive"] = elapsed
          medians[f"Selection Sort Recursive"] = calculate_median(sorted_data)

    # Plot graph
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(data_sizes, selection_times, label="Selection Sort", marker='o', color="blue")
    ax.plot(data_sizes, selection_times_recursive, label="Selection Sort Recursive", marker='o', color="red")
    ax.plot(data_sizes, insertion_times, label="Insertion Sort", marker='o', color="green")
    ax.plot(data_sizes, insertion_times_recursive, label="Insertion Sort Recursive", marker='o', color="yellow")
    ax.set_xlabel('Number of Data')
    ax.set_ylabel('Time (seconds)')
    ax.set_title('Performance Comparison: Selection Sort vs Insertion Sort')
    ax.legend()
    ax.grid(True)
    st.pyplot(fig)

    st.write("### Median:")
    st.write(calculate_median(sorted_data))

      # Display results
    st.write("### Time Execution:")
    for method, times in times.items():
        st.write(f"{method}:Time = {times:6f} seconds")

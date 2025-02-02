import time
import random

# Deterministic Quicksort
def partition(arr, low, high):
    pivot = arr[high]  # Choosing last element as pivot
    i = low - 1  # Index for smaller elements
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # Swap if element is smaller than pivot
    arr[i + 1], arr[high] = arr[high], arr[i + 1]  # Swap pivot to correct position
    return i + 1  # Return partition index

def quicksort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)  # Get pivot position
        quicksort(arr, low, pivot_index - 1)  # Recursively sort left partition
        quicksort(arr, pivot_index + 1, high)  # Recursively sort right partition

def quicksort_wrapper(arr):
    quicksort(arr, 0, len(arr) - 1)
    return arr

# Randomized Quicksort
def random_partition(arr, low, high):
    pivot_index = random.randint(low, high)
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]  
    return partition(arr, low, high)

def randomized_quicksort(arr, low, high):
    if low < high:
        pivot_index = random_partition(arr, low, high)
        randomized_quicksort(arr, low, pivot_index - 1)
        randomized_quicksort(arr, pivot_index + 1, high)

def randomized_quicksort_wrapper(arr):
    randomized_quicksort(arr, 0, len(arr) - 1)
    return arr

# Empirical Analysis
def measure_time(sort_func, arr):
    start_time = time.time()
    sorted_arr = sort_func(arr[:])  # Sort a copy to avoid modifying the original array
    end_time = time.time()
    return sorted_arr, end_time - start_time

if __name__ == "__main__":
    sorted_array = list(range(100))  # Already sorted array
    large_reverse_sorted_array = list(range(100, 0, -1))  # Reverse sorted
    random_array = [random.randint(0, 100) for _ in range(10000)]  # Randomized dataset

    
   # print("Original array to be sorted:", random_array)

    
    deterministic_sorted_Reverse, det_timeR = measure_time(quicksort_wrapper, large_reverse_sorted_array)
    deterministic_pre_sorted, de_time = measure_time(quicksort_wrapper, sorted_array)
    deterministic_sorted, ran_time = measure_time(quicksort_wrapper, random_array)
    #print("Sorted array using Deterministic quicksort:", deterministic_sorted)
 
 

    randomized_sorted_Reverse, rand_time_reverse = measure_time(randomized_quicksort_wrapper, large_reverse_sorted_array)
    randomized_pre_sorted, pre_sorted_time = measure_time(randomized_quicksort_wrapper, sorted_array)
    randomized_sorted, rand_time = measure_time(randomized_quicksort_wrapper, random_array)
   # print("Sorted array using Randomized quicksort:", randomized_sorted)
    print(f"Time taken by Deterministic quicksort for already sorted: {de_time:.6f} seconds\n")
    print(f"Time taken by Randomized quicksort for already sorted: {pre_sorted_time:.6f} seconds\n")
    print(f"Time taken by Deterministic quicksort for Reverse: {det_timeR:.6f} seconds\n")
    print(f"Time taken by Randomized quicksort for Reverse: {rand_time_reverse:.6f} seconds\n")
    print(f"Time taken by Deterministic quicksort random array: {ran_time:.6f} seconds\n")
    print(f"Time taken by Randomized quicksort random array: {rand_time:.6f} seconds\n")

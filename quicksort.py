def partition(arr, low, high):
    #Deterministic Quicksort 
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
 
if __name__ == "__main__":
    test_array = [20, 8, 15, 7, 4, 0]
    print("Original array to be sorted : ", test_array)
    sorted_array = quicksort_wrapper(test_array[:])  
    print("Sorted Array using deterministic quicksort :", sorted_array)

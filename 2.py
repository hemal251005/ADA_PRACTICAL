import time

# Linear Search
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i   
    return -1          

# Binary Search (iterative)
def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# Time Analysis
def time_analysis():
    n = 10**6  
    arr = list(range(n))
    target = n - 1   

    # Linear Search Timing
    start = time.time()
    linear_search(arr, target)
    end = time.time()
    print(f"Linear Search Time: {end - start:.6f} seconds")

    # Binary Search Timing
    start = time.time()
    binary_search(arr, target)
    end = time.time()
    print(f"Binary Search Time: {end - start:.6f} seconds")

# Main Program
if __name__ == "__main__":
    arr = [2, 3, 4, 5, 8, 10, 15, 20]
    target = 10

    print("Array:", arr)
    print("Target:", target)

    print("\nLinear Search Index:", linear_search(arr, target))
    print("Binary Search Index:", binary_search(arr, target))

    print("\n--- Time Analysis on Large Dataset ---")
    time_analysis()

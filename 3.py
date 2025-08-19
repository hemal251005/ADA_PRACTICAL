# Heapify function (maintains max-heap property)
def heapify(arr, n, i):
    largest = i       # Initialize largest as root
    left = 2 * i + 1  # left child
    right = 2 * i + 2 # right child

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

# Heap Sort function
def heap_sort(arr):
    n = len(arr)

    # Step 1: Build a max-heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Step 2: Extract elements one by one
    for i in range(n - 1, 0, -1):
        # Move current root (max) to end
        arr[0], arr[i] = arr[i], arr[0]
        
        # Heapify the reduced heap
        heapify(arr, i, 0)

    return arr

# Example Run
if __name__ == "__main__":
    arr = [5, 3, 8, 4, 2, 10, 1]
    print("Original Array:", arr)
    sorted_arr = heap_sort(arr.copy())
    print("Heap Sort (Ascending):", sorted_arr)

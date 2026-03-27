def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2   # fixed
        if arr[mid] == target:
            return mid
        elif target < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1
arr = [10, 20, 30, 40, 50]
target = 40

print("Element found at index:", binary_search(arr, target))
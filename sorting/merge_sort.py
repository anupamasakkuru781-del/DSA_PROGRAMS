# def merge_sort(arr):
#     if len(arr) <= 1:
#         return arr
    
#     mid = len(arr) // 2
#     left = merge_sort(arr[:mid])
#     right = merge_sort(arr[mid:])
#     return merge(left, right)

# def merge(left, right):
#     result = []
#     i = j = 0
#     while i < len(left) and j < len(right):
#         if left[i] < right[j]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])   # fixed
#             j += 1
    
#     # remaining elements
#     result.extend(left[i:])
#     result.extend(right[j:])
    
#     return result


# arr = [5,2,4,1]
# sorted_arr = merge_sort(arr)

# print("Original Array:", arr)
# print("Sorted Array:", sorted_arr)




def merge_two_sorted(arr1, arr2):
    result = []
    i = j = 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1

    # remaining elements
    result.extend(arr1[i:])
    result.extend(arr2[j:])

    return result


arr1 = [1,3,5]
arr2 = [2,4,6]

print(merge_two_sorted(arr1, arr2))
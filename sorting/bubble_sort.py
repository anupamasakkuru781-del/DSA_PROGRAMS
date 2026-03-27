# def bubble_sort(arr):
#     n = len(arr)
#     for i in range(n):
#         swapped = False
#         for j in range(0, n-i-1):
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
#                 swapped = True
#         if not swapped:
#             break # already sorted
#     return arr
# arr = [8,4,2,6]
# print(bubble_sort(arr))

#bubble sort decending order

# def bubble_sort_desc(arr):
#     n= len(arr)
#     for i in range(n):
#         swapped = False
#         for j in range(0, n-i-1):
#             if arr[j] < arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
#                 swapped = True
#             if not swapped:
#                 break   
#     return arr
# arr = [8,4,2,6]
# print(bubble_sort_desc(arr))

# # counting number of swaps

# def bubble_sort_count_swaps(arr):
#     n = len(arr)
#     c = 0
#     for i in range(n):
#         swapped = False
#         for j in range(0, n-i-1):
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
#                 c += 1
#                 swapped = True
#         if not swapped:
#             break
#     return c
# arr = [8,4,2,6] 
# print(bubble_sort_count_swaps(arr))

# # even or odd number of swaps
# def bubble_sort(arr):
#     n = len(arr)
#     for i in range(n):
#         swapped = False
#         for j in range(0, n-i-1):
#             if arr[j] % 2 == 0 and arr[j+1] % 2 != 0:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
#                 swapped = True
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
#                 swapped = True
#         if not swapped:
#             break # already sorted
#     return arr
# arr = [8,3,6,4,2,1,8,7]
# print(bubble_sort(arr))



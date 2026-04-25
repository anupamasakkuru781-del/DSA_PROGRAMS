# # stack - LFTD- last in first out

# # it is a stack that fllows or maintain a specific order either increasing or decersing 

# # types:
# # 1. increasing monotonic stack:
# # element are in increasing order
# # top always smallest among previous
# # eg: 1,3,5,8

# # 2. decresing monotonic stack:
# # elements are in decreasing order
# # top always largest among previous

# # eg:8,6,4,2

# # why do we use it?
# # to slove the problem like:
# # -next greater element
# # - next smaller element
# # -stock span problem

# # - it is to reduce time complexity from  0(n^2) to 0(n)

# # 3. core idea(very imprtant0)

# # - while inserting element, it removes elements that breaks the monotonic property 


# botonic stack:

# bitonic = first increasing - decreasing (or vice versa)
# eg:1,3,8,4,2

# - there is no direct botonic stack data structure instead we use:
# - monotonic stack in combination
# - or direct botonic patterns in arrays 

# where botonic is used?
# - botonic array problems
# - peak finding
# - maximum  element problems


# def find_peak(arr):
#     left, right = 0, len(arr)
#     while left < right:
#         mid = (left + right) // 2

#         if arr[mid] < arr[mid+1]:
#             left = mid + 1
#         else:
#             right = mid
# print(find_peak([1,3,8,12,4,2]))

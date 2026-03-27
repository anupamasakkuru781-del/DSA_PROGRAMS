# def insertion_sort(arr):
#     for i in range(1, len(arr)):
#         key = arr[i]
#         j = i - 1
#         while j >= 0 and arr[j] > key:
#             arr[j + 1] = arr[j]
#             j -= 1
#         arr[j + 1] = key
#     return arr
# def main():
#     arr = [8, 4, 2, 6]
#     print(insertion_sort(arr))
# main()

# # 3rd iteration
# def insertion_sort(arr):
#     for i in range(1, len(arr)):
#         key = arr[i]
#         j = i - 1
#         while j >= 0 and arr[j] > key:
#             arr[j + 1] = arr[j]
#             j -= 1
#         arr[j + 1] = key
#     return arr
# def main():
#     arr = [8, 4, 2, 7, 11, 6]
#     print(insertion_sort(arr))
# main()



# def insertion_sort_3rd_iteration(arr):
#     for i in range(1, 4):   # only till 3rd iteration
#         key = arr[i]
#         j = i - 1

#         while j >= 0 and arr[j] > key:
#             arr[j + 1] = arr[j]
#             j -= 1

#         arr[j + 1] = key

#     return arr


# arr = [8, 4, 2, 6]
# print("After 3rd iteration:", insertion_sort_3rd_iteration(arr))


# def insertion_sort(arr):
#     count =0 
#     for i in range(1, len(arr)):
#         key = arr[i]
#         j = i - 1
#         while j >= 0 and arr[j] > key:
#             arr[j + 1] = arr[j]
#             j -= 1
#             count += 1
#         arr[j + 1] = key
#     return arr, count 
# def main():
#     arr = [8, 4, 2, 6]
#     print(insertion_sort(arr))
# main()


# def insertion_sort(arr):
#     for i in range(1, len(arr)):
#         count  =0 
#         countofi = 0
#         key = arr[i]
#         j = i - 1
#         while j >= 0 and arr[j] > key:
#             arr[j + 1] = arr[j]
#             j -= 1
#             count += 1
#         arr[j + 1] = key
#         countofi += 1
#     return arr, count, countofi 
# def main():
#     arr = [8, 4, 2, 6]
#     print(insertion_sort(arr))
# main()

# inserting an element into an sorted array
# arr = [1,3,5,7]
# x = 4
# arr = [1,3,4,5,7]
# Approach:
# 1. Start from end of an array
# 2. SHift elements greater than x
# 3. Insert x in correct position


def insert_into_sorted(arr,x):
    arr.append(0) #add space for new element
    i=len(arr)-2 #starting from last orginal
    #shifting elements to right
    while i>=0 and arr[i]>x:
        arr[i+1]=arr[i]>x
        i-=1
    #insert x
    arr[i+1]=x 
    return arr
arr=[1,3,5,7]
x=4
print(insert_into_sorted(arr,x))
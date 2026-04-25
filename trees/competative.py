# 
#  1. train platform problem:

# (real world scheduling)
# * senario: a railway station has multiple trains ariving and departing 
# we need to find minimum number of platform required so that no train waits  

# arr = [900, 940, 950, 1100, 1500, 1800]
# dep = [910, 1200, 1120, 1130, 1900, 2000]

# explanation :
# if a train arrives before another departs -> need extra platform 
# otherwise -> reuse the platform 

# approach:
# 1. sort arrival and depearture arrays 
# 2. use two pointers
# 3. compare arrival[i] with departure [j] 

# def min_platform(arr, dep):
#     arr.sort()
#     dep.sort()

#     i = j = 0
#     platform = result = 0
#     n = len(arr)

#     while i < n and j < n:
#         if arr[i] <= dep[j]:
#             platform += 1
#             i += 1
#         else:
#             platform -= 1
#             j += 1
#             result = max(result, platform)
#     return result
# arr = [900, 940, 950, 1100]
# dep = [910, 1200, 1120, 1130]
# print(min_platform(arr, dep))

# 2. minimum meeting rooms

# invervals = [(0,30), (5, 20), (15, 20)]

def min_meeting_rooms(intervals):
    if not intervals:
        return 0 
    
    start = sorted([i[0] for i in intervals])
    end = sorted([i[1] for i in intervals])

    s = e = 0
    rooms = 0
    max_rooms = 0

    while s < len(start):
        if start[s] < end[e]:
            rooms += 1
            s += 1
        else:
            rooms -= 1
            e += 1
        
        max_rooms = max(max_rooms, rooms)

    return max_rooms


intervals = [(0, 30), (5, 20), (15, 20)]
print(min_meeting_rooms(intervals))

# def binary_search(arr, target):
#     low = 0
#     high = len(arr) - 1

#     while low <= high:
#         mid = (low + high) // 2   # fixed
#         if arr[mid] == target:
#             return mid
#         elif target < arr[mid]:
#             high = mid - 1
#         else:
#             low = mid + 1
#     return -1
# arr = [10, 20, 30, 40, 50]
# target = 40

# print("Element found at index:", binary_search(arr, target))


# searching a rotated array in a duplicate array
# def search(nums, target):
#     low = 0
#     high = len(nums) - 1
#     while low <= high:
#         mid = (low + high) // 2
#         if nums[mid] == target:
#             return mid
#         if nums[low] < nums[mid]:
#             if nums[low] <= target < nums[mid]:
#                 high = mid - 1
#             else:
#                 low = mid + 1
#         else:
#             if nums[mid] < target <= nums[high]:
#                 low = mid + 1
#             else:
#                 high = mid - 1
#     return -1
# def main():
#     nums = [4, 5, 6, 6, 7, 0, 1, 2]
#     target = 6
#     result = search(nums, target)
#     print(result)
# main()


# def search(nums, target):
#     low = 0
#     high = len(nums) - 1
#     result = -1   # store answer

#     while low <= high:
#         mid = (low + high) // 2

#         if nums[mid] == target:
#             result = mid        # store index
#             high = mid - 1      # move left to find first occurrence

#         elif nums[low] < nums[mid]:
#             if nums[low] <= target < nums[mid]:
#                 high = mid - 1
#             else:
#                 low = mid + 1
#         else:
#             if nums[mid] < target <= nums[high]:
#                 low = mid + 1
#             else:
#                 high = mid - 1

#     return result


# nums = [4, 5, 6, 6, 7, 0, 1, 2]
# target = 6

# print(search(nums, target))

# def find_min(arr):
#     low=0
#     high=len(arr)-1
#     while low<=high:
#         mid=(low+high)//2
#         if arr[mid]>arr[high]:
#             low=mid+1
#         else:
#             high=mid-1
#     return arr[low]
# arr=[4,5,6,7,0,1,2]
# print(find_min(arr))


# 30-3-26(monday)
# def find_peak(arr):
#     low = 0
#     high = len(arr)- 1
#     while low < high:
#         mid = (low+high) // 2

#         if arr[mid] < arr[mid+1]:
#             low = mid+1 # move right
#         else:
#             high = mid # move left
#     return arr[low]
# arr = [1,2,4,5,9,10]
# print(find_peak(arr))


# def peak_mountain(arr):
#     low = 0
#     high = len(arr) - 1
#     while low < high:
#         mid = (low + high) // 2

#         if arr[mid] < arr[mid + 1]:
#             low = mid + 1 # move right
#         else:
#             high = mid # move left
#     return arr[low]
# arr = [1,3,5,7,6,4,2]
# print(peak_mountain(arr))


# def all_peaks(arr):
#     n = len(arr)
#     peaks = []

#     for i in range(n):
#         if (i==0 or arr[i] >= arr[i-1]) and \
#         (i == n-1 or arr[i] >= arr[i+1]):
#             peaks.append(i)
#     return peaks
# arr = [1,3,2,4,1,5,3]
# print(all_peaks(arr))

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def insert_at_beginning(self, data):
#         new_node = Node(data)
#         new_node.next = self.head
#         self.head = new_node

#     def insert_at_end(self, data):
#         new_node = Node(data)

#         if self.head is None:    # list is empty
#             self.head = new_node
#             return
        
#         temp = self.head
#         while temp.next:
#             temp = temp.next

#         temp.next = new_node

#     def delete_from_beginning(self):
#         if self.head:
#             self.head = self.head.next

#     def delete_from_ending(self):
#         # having empty list
#         if self.head is None:
#             return
#         # having single element in list
#         if self.head.next is None:
#             self.head = None
#             return
#         # having elements in linked list
#         temp = self.head
#         while temp.next.next:
#             temp = temp.next

#         temp.next = None
        
#     def search(self, key):
#         temp = self.head
#         while temp:
#             if temp.data == key:
#                 return True
#             temp = temp.next
#         return False
    
#     def display(self):
#         temp = self.head
#         while temp:
#             print(temp.data, end="->")
#             temp = temp.next
#         print("None")

# ll = LinkedList()
# ll.insert_at_beginning(10)
# ll.insert_at_beginning(5)
# ll.insert_at_end(20)
# ll.insert_at_end(30)
# ll.display() #5->10->20->30->Null
# print(ll.search(20))
# ll.delete_from_beginning()
# ll.display()
# ll.delete_from_ending()
# ll.display()

# 2-4-2026
# def insert_at_position(self, pos,data):
#     new_node = Node(data)

#     if pos == 0:
#         new_node.next = self.head
#         self.head = new_node
#         return
    
#     temp = self.head
#     for _ in range(pos - 1):
#         if temp is None:
#             return
#         temp = temp.next
#     new_node.next = temp.next
    # temp.next = new_node


# def insert_at_position(self, pos, data):
#     new_node = new_node(data)

#     # insert at beginning
#     if pos == 0:
#         new_node.next = self.head
#         self.head = new_node
#         return

#     temp = self.head

#     # move to (pos-1) node
#     for _ in range(pos - 1):
#         if temp is None:
#             print("Position out of range")
#             return
#         temp = temp.next

#     # extra safety check
#     if temp is None:
#         print("Position out of range")
#         return

#     new_node.next = temp.next
#     temp.next = new_node


# def delete_value(self, key):
#     if self.head is None:
#         return
#     if self.head.data == key:
#         self.head = self.head.next
#         return
    
#     temp = self.head
#     while temp.next:
#         if temp.next.data == key:
#             temp.next = temp.next.next
#             return
#         temp = temp.next

# # def delete_at_position(self, pos):

# access by position
# def get(self, pos):
#     temp = self.head
#     for _ in range(pos):
#         if temp is None:
#             return None
#         temp = temp.next

#     return temp.data if temp else None


# 3-4-2026


# def reverse(self):
#     prev = None
#     curr = self.head

#     while curr:
#         next_node = curr.next  # store next node
#         curr.next = prev  # reverse linked list
#         prev = curr   # move prev
#         curr = next_node   # move curr

#     self.head = prev


# function to delect cycle(floyd's algorithm)
# def has_cycle(self):
#     slow = self.head
#     fast = self.head

#     while fast and fast.next:
#         slow = slow.next
#         fast = fast.next.next

#         if slow == fast:
#             return True 
        
#     return False

# n1 = Node(1)
# n2 = Node(2)
# n3 = Node(3)
# n4 = Node(4)
# n5 = Node(5)
# #linking nodes
# n1.next = n2
# n2.next = n3
# n3.next = n4
# n4.next = n5
# # create cycle
# n5.next = n3
# # assign head
# ll =LinkedList()
# ll.head = n1
# # check cycles
# print(ll.has_cycle())



class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    #  Insert at position
    def insert_at_position(self, pos, data):
        new_node = Node(data)

        if pos == 0:
            new_node.next = self.head
            self.head = new_node
            return

        temp = self.head
        for _ in range(pos - 1):
            if temp is None:
                print("Position out of range")
                return
            temp = temp.next

        if temp is None:
            print("Position out of range")
            return

        new_node.next = temp.next
        temp.next = new_node

    #  Delete by value
    def delete_value(self, key):
        if self.head is None:
            return

        if self.head.data == key:
            self.head = self.head.next
            return

        temp = self.head
        while temp.next:
            if temp.next.data == key:
                temp.next = temp.next.next
                return
            temp = temp.next

    #  Get value at position
    def get(self, pos):
        temp = self.head
        for _ in range(pos):
            if temp is None:
                return None
            temp = temp.next
        return temp.data if temp else None

    #  Reverse linked list
    def reverse(self):
        prev = None
        curr = self.head

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        self.head = prev

    #  Cycle detection (Floyd’s Algorithm)
    def has_cycle(self):
        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False

    #  Display list
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end="->")
            temp = temp.next
        print("None")


# 🔹 Create Linked List
ll = LinkedList()

# Insert elements
ll.insert_at_position(0, 1)
ll.insert_at_position(1, 2)
ll.insert_at_position(2, 3)
ll.insert_at_position(3, 4)
ll.insert_at_position(4, 5)

print("Linked List:")
ll.display()

# Get element
print("Element at position 2:", ll.get(2))

# Delete value
ll.delete_value(3)
print("After deleting 3:")
ll.display()

# Reverse list
ll.reverse()
print("After reverse:")
ll.display()

# Create cycle manually
temp = ll.head
while temp.next:
    temp = temp.next
temp.next = ll.head.next   # create cycle

# Check cycle
print("Cycle exists:", ll.has_cycle())




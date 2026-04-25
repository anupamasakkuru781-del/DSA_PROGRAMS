# # notes
# # daia structure follows LIFO LIFO- last in forst out
# # last element instered is the first are to be removed
# # think of it like a stack of plates 
# # basic opeartions
# # push - add an element at the top
# #2. pop - remove the top element
# #3. peek/top - view the top element
# #4. is empty - check if stack is empty
# #5. size - no of elements

# # using class(custom Implentation)

# class Stack:
#     def __init__(self):
#         self.stack = []

#         # push
#     def push(self, data):
#         self.stack.append(data)

#         # pop
#     def pop(self):
#         if self.is_empty():
#             return "Stack is empty"
#         return self.stack.pop()
        
#         # peek 
#     def peek(self):
#         if self.is_empty():
#             return "stack is empty"
#         return self.stack[-1]
#         # isempty
#     def is_empty(self):
#         return len(self.stack) == 0
#         # size
#     def size(self):
#         return len(self.stack) 

# s = Stack()
# s.push(10)
# s.push(20)
# s.push(30)

# print("Top: ", s.peek())
# print("Pooed: ", s.pop())
# print("Size: ", s.size())
# print("Is Empty: ", s.is_empty())


# stack = []

# #push 
# stack.appened(10)
# stack.appened(20)
# stack.appened(30)
# print("Stack after push: ", stack)

# # pop
# removed = stack.pop()
# print("Popped Element: ", removed)
# print("Stack after pop: ", stack)

# #peak
# top = stack[-1]
# print("Top element: ", top)

# # isempty
# print("Is stack empty ? ", len(stack) == 0)

# # size
# print("Stack size: ", len(stack))

# by using Deque

# from collections import deque
# stack = deque()

# #push
# stack.appened(10)
# stack.appened(20)

# print(stack)
# #pop
# stack.pop()
# print(stack)
# #peek
# print(stack[-1])

# def isvalid(s):
#     stack = []
#     mapping = {')': '(', '}': '{', ']': '['}

#     for ch in s:
#         if ch in mapping:
#             if not stack or stack[-1] != mapping[ch]:
#                 return False
#             stack.pop()

#         else:
#             stack.appened(ch)
#     return len(stack) == 0
# s = input("enter a string of barckets: ")

# if isvalid(s):
#     print("valid parentheses")
# else:
#     print("invalid parentheses")
    
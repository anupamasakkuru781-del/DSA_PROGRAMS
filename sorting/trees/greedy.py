# Greedy Approach

#     Its a strategy where we :
#         . make the best choice at the current moment(locally optimal) and hoping it leads to global optimal solution.

#     -> Key idea 
#         . Instead of exploring all the possibilities(like Dynamic Programming or Backtracking), Greedy chooses immediately and never revisits decisions.

#     -> Real life examples: 
#         . Picking the highest marks questions first in exam.
#         . Scheduling earliest finishing tasks first.

#     -> When Greedy works?
#         . Greedy choie property (Local best choice -> Global best solution)
#         . Optimal substructure (Problem can be broken into subproblems)

#     -> When Greedy fails?
#         . If the local decision leads to wrong Global decisions.


#Coin change (Greedy Approach)
# coins=[1,2,5,10]
# amount = 18 #Greedy strategy is always pick the largest coin <=amount [ 1st take 10, 5, 2, 1]


# def coin_change(coins,amount):
#     coins.sort(reverse=True)
#     count=0
#     result=[]
    
#     for coin in coins:
#         while amount>=coin:
#             amount-=coin
#             result.append(coin)
#             count+=1
#     return count, result
# coins = [1,2,5,10]
# amount=18
# print(coin_change(coins, amount))





# # Recursion and Back Tracking
# 1) Recursion : Its a technique where function calls itself to solve smaller parts of a program.

#     Core idea :
#         break the problem -> solve smaller versions -> combine results

#     Structure : 
#         def func():
#         if base_case:
#             return
#         func() #recursive call

#     Why is it important?
#         . Base case      -> stops infinite Recursion
#         . Recursive case -> reduces problem size
#         . Cell stack     -> stores function calls

# 2. Backtracking: Its a type of recursion where we :
#     i) try a  solution   ii) if it fails -> undo (backtrack)    iii) try another plan 

#     Key idea:
#     . Explores all the possibilities, but undo wrong choices.

#     General template :
#         def backtrack(path):
#             if solution_found:
#                 print(path)
#                 return
#             for choice in choices:
#                 #choose
#                 path.append(choice)
#                 #explore 
#                 backtrack(path)
#                 #un-choose(BACKTRACK)
#                 path.pop()


# 3. Permutations : Permutation is all about the possible arrangement of elements.
#         I/p : [1,2,3]
#         O/p : [1, 2, 3], [1, 3, 2], [2, 1, 3], [], [], []

#     Approach(Backtracking):
#     Idea : .pick an element
#            . fix it 
#            . recursiely permutate remaining elements

# 4. Combinations: Combination is about selecting the elements without caring about order. Order doesn't matter here.
#     Eg : [1, 2, 3], k=2
#         O/p : [1, 2], [1, 3], [2, 3]
#     Approach :
#         . Use start Index
#         . Avoid using previous elements.


# def permutations(nums):
#     result=[]
#     def backtrack(path, used):
#         if len(path)==len(nums):
#             result.append(path[:])
#             return
#         for i in range(len(nums)):
#             if used[i]:
#                 continue
#             #choose 
#             used[i] = True
#             path.append(nums[i])
#             #explore
#             backtrack(path, used)
#             #backtrack
#             path.pop()
#             used[i]=False
#     backtrack([], [False]*len(nums))
#     return result

# #Example
# print(permutations([1,2,3]))
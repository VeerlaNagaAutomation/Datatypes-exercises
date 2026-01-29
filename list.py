lst = [89,-2,78,67,90,-3,-97,98,786,678,56]
lst.append('t')
lst.append([5]) it directly [5]
lst1 = [True,False,'naga','Guhan','ram','setha']

lst.extend(lst1)
lst.extend([3])  it add only 3

lst2 = lst.copy()
# print(lst2)

lst.insert(1,'FIRE') #inserts at index

lst.pop(0) #remove specified index element
lst.pop()  #remove lastitem

del lst[3] #delete particulat index
del lst  #removes complete list
lst.clear()
lst.reverse()
# lst.sort() # sort at in place
# print(lst) #[-97, -3, -2, 56, 67, 78, 89, 90, 98, 678, 786]
# l1=sorted(lst) # creates new list
# print(l1)  # [-97, -3, -2, 56, 67, 78, 89, 90, 98, 678, 786]

# lst.reverse() #inplace reverse
# print(lst) # [56, 678, 786, 98, -97, -3, 90, 67, 78, -2, 89]

# l1=reversed(lst)
# print(l1) #<list_reverseiterator object at 0x7c67db77dbd0>

# l1=list(reversed(lst)) ##must mention list###
# print(l1) #[56, 678, 786, 98, -97, -3, 90, 67, 78, -2, 89]

# s = lst[::-1]
# print(s) # [56, 678, 786, 98, -97, -3, 90, 67, 78, -2, 89]

 
# reverse without builtins
# l1=[ ]
# for i in range(len(lst)-1,-1,-1):
#     l1.append(lst[i])
# print(l1)     #[56, 678, 786, 98, -97, -3, 90, 67, 78, -2, 89]
# #==========================
#sort without builtins # Bubblesort O(n*2) because nested for loop
# n = len(lst)
# for i in range(n):
#     for j in range(n-i-1):
#         if lst[j] > lst[j+1]:
#             lst[j],lst[j+1] = lst[j+1],lst[j]
# print(lst)

lst = [5, 3, 1]
n = 3
🟦 i and j Table (Bubble Sort)
Pass	i	j	Compared Elements (lst[j] , lst[j+1])	List After
1    0	0	            (5 , 3)	              [3, 5, 1]
1	   0	1            	(5 , 1)	[3, 1, 5]
2   	1	0	            (3 , 1)	[1, 3, 5]
3	   2	–	No comparison	[1, 3, 5]
🔑 Key Observations
i → pass number

j → index comparison inside each pass

Inner loop runs less times as i increases

Largest element settles at the end after each pass
#=================================
lst = [34,56,78,-2,0-4.89,75,79]
lst.sort()
print(lst)
n = int(input("Enter no"))
print(lst[-n])

[-4.89, -2, 34, 56, 75, 78, 79]
Enter no:1
79


#============================================
lst = [1, 0, 7, 0, 4, 0, 5, 0]
pos=0
for i in lst:
    if i!=0:
        lst[pos]=i
        pos+=1
while pos < len(lst):
    lst[pos]=0
    pos+=1
print(lst)  # [1, 7, 4, 5, 0, 0, 0, 0]
##===================================
lst = [1, 0, 7, 0, 4, 0, 5, 0]

pos = 0   # position where next NON-zero should go

for i in range(len(lst)):
    if lst[i] != 0:
        lst[i], lst[pos] = lst[pos], lst[i]
        pos += 1

print(lst) ## [1, 7, 4, 5, 0, 0, 0, 0]
****
lst = [1,0,2,0,3]
res = [x for x in lst if x != 0] + [0]*lst.count(0)

 ***

##====================================
lst = [1, 0, 7, 0, 4, 0, 5, 0]

pos = 0   # position where next zero should be placed

for i in range(len(lst)):
    if lst[i] == 0:
        lst[i], lst[pos] = lst[pos], lst[i]
        pos += 1

print(lst)  ## [0, 0, 0, 0, 4, 7, 5, 1]
****
res = [0]*lst.count(0) + [x for x in lst if x != 0] 

***

###
for above with changing the order
lst = [1, 0, 7, 0, 4, 0, 5, 0]

# 1. count zeros
zero_count = 0
for x in lst:
    if x == 0:
        zero_count += 1

# 2. shift non-zeros to the right (backward traversal)
idx = len(lst) - 1
for i in range(len(lst) - 1, -1, -1):
    if lst[i] != 0:
        lst[idx] = lst[i]
        idx -= 

# 3. fill zeros at front
for i in range(zero_count):
    lst[i] = 0

print(lst) # [0, 0, 0, 0, 1, 7, 4, 5]
***************
 Walkthrough with Your List

Initial list:

lst = [1, 0, 7, 0, 4, 0, 5, 0]

i	lst[i]	Action	idx	List state
7	0	skip	7	unchanged
6	5	place at idx	7	[1,0,7,0,4,0,5,5]
		idx--	6	
5	0	skip	6	
4	4	place at idx	6	[1,0,7,0,4,4,5,5]
		idx--	5	
3	0	skip	5	
2	7	place at idx	5	[1,0,7,7,4,4,5,5]
		idx--	4	
1	0	skip	4	
0	1	place at idx	4	[1,0,7,7,1,4,5,5]


********************


## =====================================
l1 = [ ]
l2= [ ]

for i in lst:
    if i!=0:
        l1.append(i)
    else:
        l2.append(i)
print(l1+l2)
print(l2+l1)

##======================================
arr = [[1,2],[3,4],[5,6],[7,8],10,9]
l1 = [ ]
for i in arr:
    if type(i) == list:
        for j in i:
            l1.append(j)
    else:
        l1.append(i)
print(l1) #[1, 2, 3, 4, 5, 6, 7, 8, 10, 9]
## revwesr for above
##M1
a = [1,2,3,4,5,6]
# out: [[1, 2], [3, 4], [5, 6]]
out = [ ]
k = 2
for i in range(0,len(a),k):
    temp = [ ]
    for j in range(i,i+k):
        temp.append(a[j])
    out.append(temp)    
print(out)  ## [[1, 2], [3, 4], [5, 6]]
##M2=================================
a = [1,2,3,4,5,6] ## #follow this only single loop###
# out: [[1, 2], [3, 4], [5, 6]]
out = [ ]
k = 2
for i in range(0,len(a),k):
    out.append(a[i:i+k])
print(out)    ## [[1, 2], [3, 4], [5, 6]]

## ====================================
###################################

a = [1, 2, 3, 4, 5, 6, 7, 8, 10, 9]
out=[] # [[1,2],[3,4],[5,6],[7,8],10,9]
k=2

for i in range(0,len(a),k):
    if i < 8:    
        out.append(a[i:i+k])
    else:
        out.extend(a[i:])

print(out)     # [[1, 2], [3, 4], [5, 6], [7, 8], 10, 9]


##########################################
##========================================
arr = [2,[4,[4,[5,[7]]]],8,9]
l1 = [ ]    ########********** l1 munst declare outside only ###############**********
def flatten(lst):
    for i in lst:
        if type(i) == list:
            flatten(i)
        else:
            l1.append(i)
    retuen l1     
print(flatten(arr))  # [2, 4, 4, 5, 7, 8, 9]
## Reverse of above===========
a = [2, 4, 4, 5, 7, 8, 9]
output = [2,[4,[4,[5,[7]]]],8,9]   ####  By heart ###

nested = a[4]  # start with last element of nested part

for i in range(3,0,-1):
    nested =[a[i],nested]
    
output = [a[0],nested] + a[5:]

print(output)

##========================================

## Sort by useing 2nd element in the in the tuple
a = [(1,6),(4,2),(9,7),(3,9),(8,8),(11,1)]

n = len(a)

for i in range(n):
    for j in range(n-i-1):
        if a[j][1]  > a[j+1][1]:
            a[j],a[j+1] = a[j+1],a[j]
print(a)   ## [(11, 1), (4, 2), (1, 6), (9, 7), (8, 8), (3, 9)]     

##==============================================
# Find pairs with difference k

# Example: [1,5,3,4,2], k=2
# out: [(1, 3), (5, 3), (3, 1), (3, 5), (4, 2), (2, 4)]
            
a = [1,5,3,4,2]
pairs=[ ]
k = 2
for i in a:
    for j in a:
        if abs(i-j) == k:
            pairs.append((i,j))
print(pairs)  

#==============================================
# 17.What will be the output of 
list1 = [1, [2, 3]] 
list1.append([0]) 
list1.extend([6]) 
print(list1) ##[1, [2, 3], [0], 6]
#=============================================

#=====================================================
list1 = [1,2,3,3,4,55,5,5,6]

l1=[]
for i in list1:
    if i not in l1:
        l1.append(i)
print(l1)
l2=[]

for j in range(len(l1)-1,-1,-1):
    l2.append(l1[j])
print(l2)

max_val = 0
sec_max = 0
for k in l2:
    if k > max_val:
        max_val = k
for j in l2:
    if j < max_val and j > sec_max:
        sec_max = j
        
print(max_val) 
print(sec_max)

##########
if 2 elements in list

lst = [67, 89]

max_num = float('-inf') #******
sec_max = float('-inf') #*******

for i in lst:
    if i > max_num:
        sec_max = max_num  ***************************
        max_num = i
    elif i > sec_max and i != max_num: #**********************
        sec_max = i

print(sec_max) # 67

#===========================================================
# lst = [89,-2,78,67,90,-3,-97,98,786,678,56]  
# n = len(lst)
# for i in range(n):
#     for j in range(n-i-1):
#         if lst[j] > lst[j+1]:
#             lst[j],lst[j+1] = lst[j+1],lst[j]
# print(lst) # sorted list
# ## suppose when enter n= 1 max num should come, n=2 se_max will come so on... ----AMD
# n = int(input('Enter the number'))
# n = lst[-n]
# print(n)
# Enter the number1
# 786
##===================
# 18.From a given list k = [1,1,1,1,2,2,2,2,3,3,3,3,4,1], find the number of times m = 2 occurred.

k = [1,1,1,1,2,2,2,2,3,3,3,3,4,1]
#M1
count = k.count(2)
print(count)
  ##========================#
  #M2
c=0
for i in k:
    if i == 2:
        c+=1
print(c)  

#########################################
**Rotate an array by K positions
def rotations(arr,k):
    k = k%len(arr)
    return arr[-k:] + arr[:-k]

k = 4
arr = [2,3,4,5,1]

print(rotations(arr,k))

***
2️⃣ Handle large k
k = k % len(arr)

Ensures k stays within list length

Prevents unnecessary rotations

📌 Example:

len(arr) = 5

k = 4

k % 5 = 4

If k = 9 → 9 % 5 = 4 (same result)
***
3️⃣ Core rotation logic
return arr[-k:] + arr[:-k]

🔍 Break it down:
arr = [2, 3, 4, 5, 1]
k = 4

arr[-k:] → last k elements
arr[-4:] → [3, 4, 5, 1]

arr[:-k] → elements except last k
arr[:-4] → [2]

Combine both:
[3, 4, 5, 1] + [2]

🔹 Final Output
[3, 4, 5, 1, 2]
***
🔹 Time & Space Complexity

Time: O(n)

Space: O(n) (creates new list)

🧠 Interview One-Liner

“This function rotates a list to the right using slicing, handling large rotations with modulo.”

***
right Rotation:
return arr[-k:] + arr[:-k]

left ratations:

return arr[k:] + arr[:k]


#########################################
#=====================================
21.How to split a given dictionary of lists into a list of dictionaries using the map function?

data = {
    "id":    [1, 2, 3],
    "name":  ["Alice", "Bob", "Charlie"],
    "age":   [25, 30, 35]
}

# result = list(
#     map(lambda values: dict(zip(data.keys(), values)),
#         zip(*data.values()))
# )

result = [
    dict(zip(data, values))
    for values in zip(*data.values())
]

print(result)
#op
[{'id': 1, 'name': 'Alice', 'age': 25}, {'id': 2, 'name': 'Bob', 'age': 30}, {'id': 3, 'name': 'Charlie', 'age': 35}]

🔍 Explanation (Interview-friendly)

data.values() → gets all lists

zip(*data.values()) → groups elements index-wise

(1, 'Alice', 25), (2, 'Bob', 30), (3, 'Charlie', 35)


map() → converts each tuple into a dictionary

dict(zip(keys, values)) → creates individual dictionaries
#===============================================

# Dictionary to list
Dict = {
    1: "jessa",
    2: ["abcd", "efgh", "ijkl"],
    3: "hello",
    4: {5: "five", 6: "six"}
}

result = []

for key in Dict:
    value = Dict[key]  ### BY HEART ###

    # if value is a list
    if isinstance(value, list):
        for item in value:
            result.append(item)

    # if value is a dictionary
    elif isinstance(value, dict):
        for k in value:
            result.append(value[k])  ###By heart 

    # if value is a single element (string/int)
    else:
        result.append(value)

print(result) #['jessa', 'abcd', 'efgh', 'ijkl', 'hello', 'five', 'six']
#================================================================================
##34.Validate palindromes from a list and append them to a dictionary.

def is_palindrome(s):
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

words = ["madam", "python", "level", "radar", "test", "noon"]  
result = {"palindromes": []}

for word in words:
    if is_palindrome(word):
        result["palindromes"].append(word)

print(result)  ##{'palindromes': ['madam', 'level', 'radar', 'noon']}

#==============================================

shallowcopy  and Deepcopy
lst1 = [ 1,2,3,4]
lst2=lst1.copy()

lst2[1] = 100
print(lst2) # [1, 100, 3, 4]
print(lst1) # [1, 2, 3, 4]


lst3 = [[1,2,3,4],[5,6,7,8,]]
lst4=lst3.copy()
lst4[1][1] = 1000
print(lst4) # [[1, 2, 3, 4], [5, 1000, 7, 8]
print(lst3) # [[1, 2, 3, 4], [5, 1000, 7, 8]
===========================================
import copy
lst1 = [ 1,2,3,4]
lst2=copy.deepcopy(lst1)

lst2[1] = 100
print(lst2) # [1, 100, 3, 4]
print(lst1) # [1, 2, 3, 4]


lst3 = [[1,2,3,4],[5,6,7,8,]]
lst4=copy.deepcopy(lst3)
lst4[1][1] = 1000
print(lst4) # [[1, 2, 3, 4], [5, 1000, 7, 8]
print(lst3) # [[1, 2, 3, 4], [5, 6, 7, 8]]


#===========================================================================================
interview spanidea

list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
 
# Output: ['My', 'name', 'is', 'Kelly']
out = ' '
i = 0
j = 0
while i < len(list1) and j <len(list2):
    out = out + list1[i] + list2[j] + ' '
    i+=1
    j+=1
print(out)    
s = out.split()
print(s)
op:
 My name is Kelly 
['My', 'name', 'is', 'Kelly']

##########################################

## 2d Array
Matrix printing

def matrix(arr,m,n):
    for i in range(m):
        for j in range(n):
            print(arr[i][j],end=' ')
        print('')    
            
arr = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
m=n=3
print('matrix')
matrix(arr,m,n)

op:
matrix
1 2 3 
4 5 6 
7 8 9 

###################
# matrix diogonal addition            
arr = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print(arr[0][0]+arr[1][1]+arr[2][2]+arr[0][2]+arr[1][1]+arr[2][0])

##################
# finding the target in matrix
# def matrix1(matrix,target):
#     for row in matrix:
#         for col in row:
#             if target == col:
#                 return True
#     return False 

def Binary(matrix,target):
    rows = len(matrix)
    cols = len(matrix[0])
    
    low = 0
    high = (rows*cols)-1
    
    while low <= high:
        mid = (low+high)//2
        
        row = mid//cols
        col = mid%cols
        middle_value = matrix[row][col]
        
        if middle_value == target:
            return True
        elif middle_value < target:
            low = mid+1
        else:
            high = mid-1
    return False        
    
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
print(Binary(matrix,target))



#########################

##list to 3x3 matrix



##Linkedlist,
single
double
circular single
circular double

#linkedlist traversal


##trees, 


##stack.


#####################
check list:

🔥 MOST POPULAR PYTHON LIST DSA QUESTIONS
🟢 EASY (Must-know, very frequent)

Reverse a list

lst[::-1]


Find largest & smallest element

max(lst), min(lst)


Remove duplicates from a list

list(set(lst))


Check if list is sorted

lst == sorted(lst)


Count occurrences of an element

lst.count(x)


Find sum of elements

sum(lst)


Swap first and last elements

lst[0], lst[-1] = lst[-1], lst[0]

🟡 MEDIUM (VERY COMMON – Interview favorites)
8. Move all zeros to end
lst = [1,0,2,0,3]
res = [x for x in lst if x != 0] + [0]*lst.count(0)

9. Move all zeros to beginning
zeros = lst.count(0)
res = [0]*zeros + [x for x in lst if x != 0]

10. Find second largest element
sorted(set(lst))[-2]

11. Rotate list by k positions
k = 2
lst[k:] + lst[:k]

12. Find missing number (1 to n)
missing = sum(range(1,n+1)) - sum(lst)

13. Find duplicate elements
[x for x in set(lst) if lst.count(x) > 1]

14. Intersection of two lists
list(set(a) & set(b))

15. Check if two lists are equal
a == b

🔴 HARD / DSA CORE (Very impressive if you answer)
16. Kadane’s Algorithm (Max subarray sum) ⭐
max_sum = curr = lst[0]
for x in lst[1:]:
    curr = max(x, curr + x)
    max_sum = max(max_sum, curr)

17. Two Sum Problem
seen = {}
for i, num in enumerate(lst):
    if target - num in seen:
        print(seen[target-num], i)
    seen[num] = i

18. Find leaders in list
max_from_right = lst[-1]
leaders = [max_from_right]
for i in range(len(lst)-2, -1, -1):
    if lst[i] > max_from_right:
        leaders.append(lst[i])
        max_from_right = lst[i]

19. Longest increasing subsequence (basic idea)

👉 Asked conceptually, not full code.

20. Merge two sorted lists
sorted(a + b)

🧠 PATTERN-BASED QUESTIONS (Interview Gold)
Pattern	Questions
Two Pointers	Move zeros, reverse list
Hashing	Two Sum, duplicates
Sliding Window	Max subarray
Sorting	Second largest, missing number
Backward traversal	Leaders, zero-shift
🎯 TOP 5 YOU MUST PREPARE (Don’t skip)

1️⃣ Move zeros
2️⃣ Second largest
3️⃣ Two Sum
4️⃣ Max subarray sum
5️⃣ Reverse / Rotate list

🗣️ Interview Closing One-liner

“Most list DSA problems can be solved using two pointers, hashing, or traversal patterns with O(n) time.”

If you want next, I can:




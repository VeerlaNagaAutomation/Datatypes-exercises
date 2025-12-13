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


##====================================
lst = [1, 0, 7, 0, 4, 0, 5, 0]

pos = 0   # position where next zero should be placed

for i in range(len(lst)):
    if lst[i] == 0:
        lst[i], lst[pos] = lst[pos], lst[i]
        pos += 1

print(lst)  ## [0, 0, 0, 0, 4, 7, 5, 1]

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

##========================================
arr = [2,[4,[4,[5,[7]]]],8,9]
l1 = [ ]
def flatten(lst):
    for i in lst:
        if type(i) == list:
            flatten(i)
        else:
            l1.append(i)
flatten(arr)
print(l1)  # [2, 4, 4, 5, 7, 8, 9]
## Reverse of above===========
a = [2, 4, 4, 5, 7, 8, 9]
output = [2,[4,[4,[5,[7]]]],8,9]

nested = a[4]  # start with last element of nested part

for i in range(3,0,-1):
    nested =[a[i],nested]
    
output = [a[0],nested] + a[5:]

print(output)

##========================================
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
a = [1,2,3,4,5,6]
# out: [[1, 2], [3, 4], [5, 6]]
out = [ ]
k = 2
for i in range(0,len(a),k):
    out.append(a[i:i+k])
print(out)    ## [[1, 2], [3, 4], [5, 6]]

## ====================================

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
lst = [34,56,78,-2,0-4.89,75,79]
lst.sort()
print(lst)
n = int(input("Enter no:"))
print(lst[-n])

[-4.89, -2, 34, 56, 75, 78, 79]
Enter no:1
79


# def fact(n):
#     result = 1
#     while n > 1:
#         result = n*result
#         n-=1
#     return result
# n=int(input("Enter the number"))
# print(f'factorial of {n} is {fact(n)}')
#Recurssive fact
# def re_fact(n):
#     if n == 0:
#         return 1
#     elif n == 1:
#         return n
#     else:
#         return re_fact(n-1)*n
# n=int(input("Enter the number"))
# print(f'factorial of {n} is {re_fact(n)}')
#Prime factors
# n=int(input("Enter the number"))

# num = n
# i = 2
# factors = [ ]
# while n > 1:
#     if n % i==0:
#         factors.append(str(i))
#         n=n//i
#     else:
#         i+=1
# print(f'{num} = {'X'.join(factors)}')   
#Angustrome number
# n=int(input("Enter the number"))
# d = len(str(n))
# num = n       
# sum = 0
# while n > 0:
#     r = n%10
#     sum = sum + r**d
#     n = n//10
# if sum == num:
#     print('a')
# else:
#     print('nOT A')
#Factors of a number
# n=int(input("Enter the number"))
# for i in range(1,n+1):
#     if n % i == 0:
#         print(i)
#prime number
# def is_prime(n):
#     if n <= 1:
#         return False
#     elif n == 2:
#         return True
#     elif n % 2 == 0:
#         return False
#     else:
#         for i in range(3,int(n**0.5)+1,2):
#             if n %i == 0:
#                 return False
#         return True
# n=int(input("Enter the number"))
# if is_prime(n):
#     print('Prime')
# else:
#     print('Not a prime')
#palin
# def is_palin(word):
#     return word == word[::-1]

# word=input("Enter the word") 
# if is_palin(word):
#     print("p")
# else:
#     print('Not a P')
#Palin withiut built in
# word=input("Enter the word: ")
# start = 0
# end = len(word)-1
# is_palindrome = True
# while start < end:
#     if word[start]!= word[end]:
#         is_palindrome = False
#         break
#     else:
#         start +=1
#         end -=1
# if is_palindrome:
#     print("p")
# else:
#     print('Not a P') 
# longest palindrome in given string

# def lon_palin(s):
#     def expand(left,right):
#         while left >= 0 and right < len(s) and s[left] == s[right]:
#             left-=1
#             right+=1
#         return s[left+1:right]
#     longest=' '
#     for i in range(len(s)):
#         odd = expand(i,i)
#         even = expand(i,i+1)
#         longest = max(longest,odd,even,key=len)
#     return longest
# s =input("Enter the word: ")
# print(lon_palin(s))
#Binary search
# def binary_se(lst, target):
#     low = 0
#     high = len(lst)-1
#     while low <= high:
#         mid = (low+high)//2
#         if lst[mid] == target:
#             return mid
#         elif target < lst[mid]:  ====mistack just mid i have written
#             low = mid+1
#         else:
#             high = mid-1
#     return -1
# lst = list(map(int, input("Enter the array: ").strip('[]').split(',')))
# target = int(input('Enter the number'))
# result = binary_se(lst,target)
# if target != -1:
#     print(f'{target} found at {result}')
# else:
#     print("Target not found")
# op
# Enter the array: [1,2,3,4,5,6,7]
# Enter the number4
# 4 found at 3
    

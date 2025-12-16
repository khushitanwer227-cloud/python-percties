# 1    recurtion factorial
# def factorial(n):
#   if n == 0 :
#      return 1
#   return n * factorial(n - 1)

# n = int(input())
# ans = factorial(n)
# print(ans)

# # 2               
# a = int(input())
# b = int(input())
# sum = (a+b)
# print(sum)

#  string sciling

# s = "khushi tanwer"
# print(s[:5])
# print(s[::])
# print(s[:-2])
# print(s[1:9:2])           the second char bw 1 to 9 will exclusive


 # loop
# for i in range(5):
#     print("khushi")
#     # print("kashi")
# print("deepak")
     
# #pattern 
# for row in range(5):                                         
#     for col in range(1,row + 1):                                
#         print(col,end=' ')                                   
#     print()      

# # Grades   conditional stat.
# marks = int(input())
# if(marks>=90 and marks <=100):
#     print("Grade A")
# elif marks>=80 and marks<=90:
#     print("Grade B") 
# elif marks>=70 and marks<=80:
#     print("Grade C")
# elif marks>=60 and marks<=70:
#     print("Grade D")
# else:
#     print("fail")


 
# the length of list

# thislist = ["apple","banana","mango","apple","banana","mango",]
# print(thislist)
# print(len(thislist))

# list => Data type {string, integer , boolen}

# list1 = ["apple", "banana", "cherry"]
# list2 = [1, 5, 7, 9, 3]
# list3 = [True, False, False]

# print(list1)
# print(list2)
# print(list3)

# lists = ["abc" , 123 , True , "xyz" , 456 , False]
# print(lists)


# list data type

# thelist = ["abc","xyz","mno","jdpk","ktj"]
# print(type(thelist))
#   output    =>    <class 'list'>


""" Python uses indentation to indicate a block of code
Indentation refers to the spaces at the beginning of a code line.

Where in other programming languages the indentation in code is for readability
 only, the indentation in Python is very important. """

"""  x = ["apple", "banana", "cherry"]	            list	
     x = ("apple", "banana", "cherry")	             tuple	
     x = range(6)	                                 range	
     x = {"name" : "John", "age" : 36}	             dict	
     x = {"apple", "banana", "cherry"}	              set      """

# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
# e = int(input())
# avg = (a + b + c + d + e)/5
# print(avg)


 
# mark = int(input("enter a number "))

# if mark <= 100 and mark >= 90 :
#     print(" Grade A ")
# elif mark <= 89 and mark >= 80 :
#     print("Grade B")
# elif mark <= 79 and  mark >=70:
#     print("Grade C")
# elif mark <=69  and mark >= 60:
#     print("Grade D ")
# else:
#     print("grade F")




# def factorial(n):
#     if n == 0:
#         return 1
#     return n*factorial(n-1)


# n = int(input())  
# ans = factorial(n)
# print(ans)


# string sciling


# s = "abcdefghijk"
# print(s[-2:])


# a = int(input("Enter 1st number "))
# b = int(input("Enter 2nd number "))
# print(a + b)
# print(a - b)
# print(a * b)
# print(a ** b)
# print(a % b)
# print(a / b)

# r = int(input())

# area = 3.14 * r * r
# print(area)


# Sum of digits 

# n = int(input())
# sum = 0
# while n != 0:
#     lastdigit = n % 10
#     sum = sum + lastdigit
#     n = n//10
# print(sum)


# n = int(input())
# rev = 0 
# while n != 0:

#     lastdigit = n % 10
#     rev = rev * 10 + lastdigit
#     n = n//10

# print(rev)


# def findsum(n):
#    if n == 0:
#      return 1
#    return n + findsum(n-1)
# if__name__== "__main__":
# n = int(input())
# sum = findsum(n)
# n = 5
# print(findsum(n))







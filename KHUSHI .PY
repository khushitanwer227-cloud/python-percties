# 1 odd & even
# n = int(input("Enter a number"))

# if n % 2 == 0:
#     print(" number is even ")
# else:
#     print(" number is odd ")

#  2 +ve  &  -ve  &  zero

# n = int(input("enter a number"))

# if n > 0 == 0:
#     print("Positive number")
# elif n < 0 == 0:
#     print("Negative number")
# else:
#     print("Zero number")

# 3 Maximum of two numbers

# a = int(input("enter first number"))
# b = int(input("enter second number"))
# print("the maximum number",end="  ")
# print(max(a,b))

# 4 leap year check

# y = int(input(" enter year  "))

# if (y % 4 == 0 and y % 100 != 0 ) or (y % 400 == 0 ):
#     print("Leap year ")
# else :
#     print("Not a leap year ")

# 5 Grading system
 
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

# 6 greatest three numbers

# x = int(input("enter 1st number "))
# y = int(input("enter 2nd number "))
# z = int(input("enter 3rd  number "))

# if ( x >= y and  x >= z):
#     print("greatest is ", x)
# elif ( y >= z and y >= x):
#     print("greatest is ", y)
# else:
#     print("greatest is ", z)

# 7 voting eligibility

# age = int(input("enter a number  "))

# if age >= 18 :
#     print("Eligible to vote")
# else:
#     print("Not eligible to vote")


# 8 divisibility check

# n = int(input("enter a number  "))
 
# if n % 5 == 0 and n % 11 == 0 :
#     print("Divisible by both numbers")
# else:
#     print("not divisible ")





# 9 simple calculator
 
# a = int(input("enter a number  "))
# b = int(input("enter a number  "))

# print(a + b)
# print(a - b)
# print(a * b)
# print(a % b)
# print(a / b)
# print(a ** b)

#  10  type of triangles 

x = int(input("1st side of triangle "))
y = int(input("2nd side of triangle "))
z = int(input("3rd side of triangle "))


# if x == y == z :
#     print("Equilateral triangle ")
# elif x == y or y == z or z == x :
#     print("Isosceles triangle ")
# else:
#     print("scalene triangle ")


# palindrome number
# n = int(input())
# temp = n
# rev = 0

# while n != 0:
#     lastdigit = n % 10
#     rev = rev * 10 + lastdigit
#     n = n//10
# if temp == rev:
#      print("yes")
# else:
#     print("No")



# Sum of digits 

# n = int(input())
# sum = 0
# while n != 0:
#     lastdigit = n % 10
#     sum = sum + lastdigit
#     n = n//10

# print(sum)
# n= int (input())
# rev = 0
# while n != 0
#   lastdigit= n %10
#   rev= rev * 10 + lastdigit
#   n = n//10

#   print(rev)
# area of  circle  pi*r^2 

# radius =  float(input("enter a nummber  "))
# Area = 3.14 * radius * radius
# print("Area of circle")
# print(Area)


# factorial of a number

# n = int(input())
# fact = 1
# for i in range(1,n+1):
#     fact = fact * i

# print(fact)

#  prime or not prime

# n = int (input())
# i = 2
# if n<=1:
#     print(" Not Prime number ")

# else:
#     print(True)
#     for i in range (2,n + 1):
#      n % i == 0 
#      break
#      print("prime number")
#  def sum (a,b):
#   c=a+b
#   return c 
# s1= sum (2,3)
# print (s1)
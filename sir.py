"""1  recurtion fibonacc """ 
# def fib(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:2
#         return fib(n-1) + fib(n-2)

# n = int(input("Enter number: "))
# ans = fib(n)
# print(ans
 
""" iterative fabonacci """ 

# n = int(input("Enter number of terms: "))

# a = 0
# b = 1

# print("Fibonacci series:")
# for i in range(n):
#     print(a, end=" ")
    # a, b = b, a + b



"""2 recurtion factorial""" 
# def factorial(n):
#   if n == 0 :
#      return 1
#   return n * factorial(n - 1)
    
# n = int(input("enter the number"))
# ans = factorial(n)
# print(ans)


""" Iterative Factorial (using loop)""" 

# n = int(input("Enter a number: "))

# fact = 1
# for i in range(1, n + 1):
#     fact = fact * i

# print("Factorial =", fact)


"""3  prime no """ 
# n = int(input("Enter a number: "))

# if n <= 1:
#     print("Not a prime number")
# else:
#     for i in range(2, n):
#         if n % i == 0:
#             print("Not a prime number")
#             break
#     else:
#         print("Prime number")



""" 4 grade""" 
# marks = int(input("Enter marks: "))

# if marks >= 90:
#     print("Grade: A")
# elif marks >= 80:
#     print("Grade: B")
# elif marks >= 70:
#     print("Grade: C")
# elif marks >= 60:
#     print("Grade: D")
# elif marks >= 40:
#     print("Grade: E")
# else:
#     print("Grade: F (Fail)")

""" 5 BREAK""" 
# for i in range(1, 6):
#     if i == 4:
#         break
#     print(i)


""" continue""" 
# for i in range(1, 6):
#     if i == 4:
#         continue
#     print(i)

"""  6 Sum of numbers from input""" 
# l= list(map(int, input("Enter numbers: ").split()))
# total = sum(l)
# print("Sum:", total)
# length = len(l)
# print("Length of the list:", length)


""" 7 identity operators:""" 
# a = [1, 2, 3]
# b = a       # b points to the same object as a
# c = [1, 2, 3]  # c is a different object with the same content

# print(a is b)   # True, same object
# print(a is c)   # False, different objects
# print(a is not c)   # False, different objects

"""   30   lab assig """ 
# import time
# from datetime import datetime,
 
# # Welcome message and introduction
# print("\n Welcome to the Daily Calorie Tracker CLI Tool!")
# print("You can log your meals and calories to track your daily consumption.")
# print("At the end, you'll see total & average calories and limit status.\n")

# # Task 2: Input & Data Collection
# meal_names = []
# meal_calories = []

# num_meals = int(input("How many meals do you want to enter today? → "))

# for i in range(num_meals):
#     name = input(f"Enter meal {i+1} name (e.g., Breakfast, Lunch) → ")
#     calories = float(input(f"Enter calories for {name} → "))
    
#     meal_names.append(name)
#     meal_calories.append(calories)

# # Task 3: Perform calorie calculations
# total_cal = sum(meal_calories)
# avg_cal = total_cal / num_meals

# daily_limit = float(input("\nEnter your daily calorie limit → "))

# # Task 4 & 5: Warning system using comparison operator
# print("\n Your Daily Calorie Report\n")
# print("Meal Name\tCalories")
# print("-----------------------------------")

# for i in range(num_meals):
#     print(f"{meal_names[i]}\t\t{meal_calories[i]}")

# print("-----------------------------------")
# print(f"Total:\t\t{total_cal:.2f}")
# print(f"Average:\t{avg_cal:.2f}")

# if total_cal > daily_limit:
#     status = " Warning: Calorie limit EXCEEDED!"
#     print("\n" + status)
# else:
#     status = " Success: You are within the daily limit."
#     print("\n" + status)

# # Task 6 (Bonus): Save session log to file with timestamp
# save = input("\nDo you want to save this report? (yes / no) → ").strip().lower()

# if save == "yes":
#     filename = "calorie_log.txt"
#     with open(filename, "w") as file:
#         file.write("Daily Calorie Tracker Log\n")
#         file.write(f"Timestamp: {datetime.now()}\n\n")
#         for i in range(num_meals):
#             file.write(f"{meal_names[i]} → {meal_calories[i]} calories\n")
#         file.write(f"\nTotal Calories: {total_cal:.2f}")
#         file.write(f"\nAverage Calories: {avg_cal:.2f}")
#         file.write(f"\nDaily Limit: {daily_limit}")
#         file.write(f"\nStatus: {status}\n")

#     print(f"\n Report saved successfully as {filename} ")

# print("\nThank you for using the Calorie Tracker CLI! Stay healthy 💪😊\n")


"""  8 ODD""" 
# n = int(input("Enter number: "))

# if n % 2 == 0:
#     print("Even")
# else:
#     print("Odd")

"""9 Positive, Negative or Zero""" 

# n = int(input("Enter number: "))

# if n > 0:
#     print("Positive")
# elif n < 0:
#     print("Negative")
# else:
#     print("Zero")

""" 10  Maximum of Two Numbers""" 
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))

# if a > b:
#     print("Maximum =", a)
# else:
#     print("Maximum =", b)

""" 12 Leap Year Check""" 

# year = int(input("Enter year: "))

# if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
#     print("Leap Year")
# else:
#     print("Not a Leap Year")


"""13 Grading System""" 

# marks = int(input("Enter marks: "))

# if marks >= 90:
#     print("Grade A")
# elif marks >= 80:
#     print("Grade B")
# elif marks >= 70:
#     print("Grade C")
# elif marks >= 60:
#     print("Grade D")
# else:
#     print("Grade F")

"""14 Greatest of Three Numbers"""
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# c = int(input("Enter third number: "))

# if a >= b and a >= c:
#     print("Greatest =", a)
# elif b >= a and b >= c:
#     print("Greatest =", b)
# else:
#     print("Greatest =", c)


""" 15 Voting Eligibility"""
# age = int(input("Enter age: "))

# if age >= 18:
#     print("Eligible to Vote")
# else:
#     print("Not Eligible to Vote")


""" 16  Divisibility Check (5 and 11)"""

# n = int(input("Enter number: "))

# if n % 5 == 0 and n % 11 == 0:
#     print("Divisible by 5 and 11")
# else:
#     print("Not divisible by 5 and 11")

""" 17 Simple Calculator"""
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# op = input("Enter operator (+, -, *, /): ")

# if op == '+':
#     print(a + b)
# elif op == '-':
#     print(a - b)
# elif op == '*':
#     print(a * b)
# elif op == '/':
#     print(a / b)
# else:
#     print("Invalid operator")


"" " 18 Triangle Type"""
# a = int(input("Enter first side: "))
# b = int(input("Enter second side: "))
# c = int(input("Enter third side: "))

# if a == b == c:
#     print("Equilateral Triangle")
# elif a == b or b == c or a == c:
#     print("Isosceles Triangle")
# else:
#     print("Scalene Triangle")


""" 19 Simple Interest & Compound Interest"""
# P = float(input("Enter principal: "))
# R = float(input("Enter rate: "))
# T = float(input("Enter time: "))

# SI = (P * R * T) / 100
# CI = P * (1 + R/100) ** T - P

# print("Simple Interest =", SI)
# print("Compound Interest =", CI)


"""20 Area and Perimeter of a Rectangle"""
# l = float(input("Enter length: "))
# b = float(input("Enter breadth: "))

# area = l * b
# perimeter = 2 * (l + b)

# print("Area =", area)
# print("Perimeter =", perimeter)



"""21 Palindrome Number"""
# n = int(input("Enter number: "))
# temp = n
# rev = 0

# while n > 0:
#     digit = n % 10
#     rev = rev * 10 + digit
#     n = n // 10

# if temp == rev:
#     print("Palindrome Number")
# else:
#     print("Not a Palindrome Number")


""" 22Count Even and Odd Digits""" 
# n = int(input("Enter number: "))
# even = 0
# odd = 0

# while n > 0:
#     digit = n % 10
#     if digit % 2 == 0:
#         even += 1 
#     else:
#         odd += 1            #(odd = odd + 1)
#     n = n // 10

# print("Even digits =", even)
# print("Odd digits =", odd)


""" 23 Find the Largest Digit """ 
# n = int(input("Enter number: "))
# largest = 0

# while n > 0:
#     digit = n % 10
#     if digit > largest:
#         largest = digit
#     n = n // 10

# print("Largest digit =", largest)



""" 24Check Prime Number""" 
# n = int(input("Enter number: "))
# flag = 0

# if n <= 1:
#     flag = 1
# else:
#     for i in range(2, n):
#         if n % i == 0:
#             flag = 1
#             break

# if flag == 0:
#     print("Prime")
# else:
#     print("Not Prime")



""" 26. Sum of Digits""" 
# n = int(input("Enter number: "))
# sum = 0

# while n > 0:
#     digit = n % 10
#     sum = sum + digit
#     n = n // 10

# print("Sum of digits =", sum)

""" 27 Reverse a Number""" 
n = int(input("Enter number: "))
rev = 0

# while n > 0:
for i in range(1, n+1):
    digit = n % 10
    rev = rev * 10 + digit
    n = n // 10

print("Reverse number =", rev)

""" 28 👊 Area of a Circle""" 
# r = float(input("Enter radius: "))
# # area = 3.14 * r * r
# print("Area of circle =", area)




""" 29  👊if, elif, else""" 
# num = int(input("Enter number: "))

# if num > 0:
#     print("Positive number")
# elif num < 0:
#     print("Negative number")
# else:
#     print("Zero")



""" 31 -------- STATS FUNCTIONS ----------""" 
# def avg(m):
#      return sum(m.values()) / len(m)
# def median(m):
#     s = sorted(m.values())
#     n = len(s)
#     return (s[n//2] if n % 2 != 0 else (s[n//2] + s[n//2 - 1]) / 2)
# def max_score(m): return max(m, key=m.get), max(m.values())
# def min_score(m): return min(m, key=m.get), min(m.values())

# # ---------- GRADE FUNCTION ---------- 
# def grade(x):
#     if x >= 90: return "A"
#     if x >= 80: return "B"
#     if x >= 70: return "C"
#     if x >= 60: return "D"
#     return "F"

# # ---------- INPUT FUNCTIONS ----------
# def manual():
#     data = {}
#     for _ in range(int(input("Students count: "))):
#         name = input("Name: ")
#         data[name] = int(input("Marks: "))
#     return data

# def load_csv():
#     data = {}
#     try:
#         with open(input("CSV file name: ")) as f:
#             for n, m in list(csv.reader(f))[1:]:
#                 data[n] = int(m)
#     except:
#         print("Error reading file!")
#     return data

# # ---------- PRINT TABLE ----------
# def show_table(m, g):
#     print("\nName\tMarks\tGrade\n-------------------------------")
#     for n in m:
#         print(f"{n}\t{m[n]}\t{g[n]}")

# # ---------- MAIN ----------
# while True:
#     print("\n1.Manual Input\n2.CSV Input\n3.Exit")
#     ch = input("Choice: ")

#     if ch == "1": marks = manual()
#     elif ch == "2": marks = load_csv()
#     elif ch == "3": break
#     else:
#         print("Invalid!"); continue

#     # Stats
#     print("\n--- Statistics ---")
#     print("Average:", round(avg(marks), 2))
#     print("Median :", median(marks))
#     mx, mxs = max_score(marks); print("Max:", mx, mxs)
#     mn, mns = min_score(marks); print("Min:", mn, mns)

#     # Grades
#     grades = {n: grade(m) for n, m in marks.items()}
#     print("\n--- Grade Count ---")
#     for g in "ABCDE":
#         print(g + ":", list(grades.values()).count(g))

#     # Pass / Fail
#     passed = [n for n, m in marks.items() if m >= 40]
#     failed = [n for n, m in marks.items() if m < 40]
#     print("\nPassed:", passed)
#     print("Failed:", failed)

#     # Table
#     show_table(marks, grades)

#     if input("\nRun again? (y/n): ").lower() != "y":
#         break

# print("\nThank you for using GradeBook Analyzer!")

""" 👊pattern """
# for i in range(1, 6):
#     for j in range(i):
#         print(i, end=" ")
#     print()


# --- Practing Python ----

# print("You are targeting " + input("What ip would you like to target? "))

# x = 7
# y = "Ryan"
# print(str(x) + y)

# f = "Paul 
# s = "Everson"
# print("Your name is: " + f, s)

# fname = input("What is your first name?")
# lname = input("What is your last name?")
# print("Your name is: " + fname, lname)

#########################################################################################################

# import time

# 1. Create a greeting for your program. 
# 2. Ask the user for the name of a pet.
# 3. Aks for the name of the city you were born in.
# 4. Combine the pet name with the word cyber as a new twitter handle and then add the city they are from.
# The output should look like this: "Your new twitter handle and bio @cyberfred from Honulu. "

# current_time = time.ctime()

# print("Hello, and welcome to KaiOS program. The current time is " + current_time)

# pet_name = input("What is the name of your pet? ")
# city_of_birth = input("What city were you born in? ")
 
# print(f"Your new twitter handle and bio @cyber{pet_name} from {city_of_birth}. ")

#########################################################################################################

# Data Types
# 1 - strings 
# print(type("Hello World!"))

# 2 - integer
# print(type(7))

# 3 - float 
# print(type(3.14159265359))

# Boolean - True or false statements 

# fnum = input("What is the first number? ")
# snum = input("What is the second number? ")

# if fnum > snum:
#     print("The first number is larger.")
# elif snum > fnum:
#     print("The second number is larger.")
# else:
#     print("The numbers are the same.")

#########################################################################################################

# Write a program that prompts the user to enter their score (out of 100) and 
# displays their corresponding grade based on the following criteria: 
#
# Score 90 and above: Grade A
# Score 80 to 89: Grade B
# Score 70 to 79: Grade C
# Score 60 to 69: Grade D
# Score below 60: Grade F

# score = input("What was your test score? ")
# score = int(score)

# if score >= 90:
#     age = int(input("What is your age?"))
#     if age < 12:
#         print("Your grade is an A+.")
#     else:
#         print("Your grade is an A.")

# elif score >= 80:
#     age = int(input("What is your age?"))
#     if age < 12:
#         print("Your grade is an B+.")
#     else:
#         print("Your grade is a B.")

# elif score >= 70:
#     age = int(input("What is your age?"))
#     if age < 12:
#         print("Your grade is an C+.")
#     else:
#         print("Your grade is a C.")

# elif score >= 60:
#     age = int(input("What is your age?"))
#     if age < 12:
#         print("Your grade is an D+.")
#     else: 
#         print("Your grade is a D.")

# else: 
#     print("Next time study more!")
    
#########################################################################################################

# fruits = ["apple", "banana", "cherry"]

# for i in fruits:
#     print(i)

# for num in range (1,100):
#     if num % 2 == 0:
#        print(num)



# Fizzbuzz 
# Write a program that loops through the numbers 1-100 and then 
# If a number is divisible by 3, print fizz
# If a number is divisible by 5, print buzz
# If a number is divisible by both, print fizzbuzz

# for num in range(1,100):
#     if num % 3 == 0 and num % 5 == 0:
#         print("fizzbuzz")
#     elif num % 3 == 0:
#         print("fizz")
#     elif num % 5 == 0:
#         print("buzz")
#     else:
#         print(num)


#########################################################################################################

# Creating our own functions 
# import time 

# choice = int(input("What is your choice? "))

# def function(choice):
#     for num in range(1, choice):
#         if num % 3 == 0 and num % 5 == 0:
#             print("FizzBuzz")
#         elif num % 3 == 0:
#             print("Fizz")
#         elif num % 5 == 0:
#             print("Buzz")
#         else:
#             print(num)

# print("Running the program . . . ")
# time.sleep(5)

# function(choice)

#########################################################################################################

# Create a program that can take in input of the users name
# save the name in a variable
# pass the variable through a function and print "Hello _____"

user_name = str(input("What is your name? "))

def function(user_name):
    print(f"Hello {user_name}")

function(user_name)
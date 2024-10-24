#Odd or even
# Write a program to check if a number is odd or even. Use input() to enter the number.
#number = int(input("Enter a number: "))
#
#rest = number % 2
#if rest == 0:
#    print(f"The number {number} is even")
#else:
#    print(f"The number {number} is odd")

## GRADES
#grades = {"A":"90,100",
#          "B":"80,89",
#          "C":"70,79",
#          "D":"60,69",
#          "F":"0,59"}

#grade = int(input("Enter a number to check you grade: "))
#found = False
#
#for key, value in grades.items():
#    grades_range = value.split(",")
#    lowRange = int(grades_range[0])
#    highRange = int(grades_range[1])
#
#    if grade >= lowRange and grade <= highRange:
#        print(f"Your grade is {key}")
#        found = True

#if not found :
#    print(f"The number {grade} is not a valid grade")

## Sum of N numbers
#n = int(input("Enter a number to get the Sum N numbers: "))
#sum = 0
#
#while n > 100:
#    print(f"The number {n} is not valid, enter a number <= 100")
#    n = int(input("Enter a number to get the Sum N numbers: "))
#
#for number in range(1,n+1):
#    sum = number + sum
#
#print(f"The sum of N number is {sum}")

##(T.7) Calculate sum of digits
#n = int(input("Enter a number to check the sum of the digits: "))
#sum = 0
#for letter in str(n):
#    sum = int(letter) + sum
#    
#print(sum)

##(T.8) Number guessing game
#import random
#guess = int(input("Try to guess a number between 1 and 100: "))
#randomNumber = random.randint(1, 100)
#
#while guess != randomNumber:
#    if guess > randomNumber:
#        print(f"The number is less than {guess}")
#        guess = int(input("Try to guess a number between 1 and 100: "))
#    elif guess < randomNumber:
#        print(f"The number is greater than {guess}")
#        guess = int(input("Try to guess a number between 1 and 100: "))
#        
#print(f"Correct! Number is {guess}")

##(T.9) Factorials
#def factorial(x):
#    result = 1
#    if x > 0:
#        for y in range(1, x + 1):
#            result *= y
#        return result
#
#def factorial2(x):
#    if x == 1:
#        return 1
#    else:
#        return x * factorial(x - 1)
#
#def checkNumber (number):
#    try:
#        numberCheck = int(number)
#        if numberCheck > 0:
#            return True
#        else:
#            return False
#    except Exception as e:
#        return False
#    
#number = input("Enter a number: ")
#
#while checkNumber(number) == False:
#    number = input("Enter a number greater than 0: ")
#
#number = int(number)
#
#print(f"The factorial of {number} is", factorial2(number))


##(T.11) Sum to Target
def sumNumbers(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return None  

nums = list(map(int, input("Enter the numbers separed by spaces: ").split()))
target = int(input("Enter the target: "))

result = sumNumbers(nums, target)

if result:
    print(f"The sum of {target} is equal to: {result}")
else:
    print("No combination found")



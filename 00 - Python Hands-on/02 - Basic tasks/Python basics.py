#Odd or even
# Write a program to check if a number is odd or even. Use input() to enter the number.
#number = int(input("Enter a number: "))
#
#rest = number % 2
#if rest == 0:
#    print(f"The number {number} is even")
#else:
#    print(f"The number {number} is odd")

grades = {"A":"90,100",
          "B":"80,89",
          "C":"70,79",
          "D":"60,69",
          "F":"0,59"}

grade = int(input("Enter a number to check you grade: "))

for key, value in grades.items():
    grades_range = value.split(",")
    lowRange = int(grades_range[0])
    highRange = int(grades_range[1])

    if grade >= lowRange and grade <= highRange:
        print(f"Your grade is {key}")
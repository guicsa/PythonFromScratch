## Math in python

# Arithmetic operators
friends = 10
friends = friends + 1
print(f"I have {friends} friend(s)")
friends += 1
print(f"I have {friends} friend(s)")
friends -= 2
print(f"I have {friends} friend(s)")
friends *= 3
print(f"I have {friends} friend(s)")
friends /= 2
print(f"I have {friends} friend(s)")
friends **= 2
print(f"I have {friends} friend(s)")
remainder = friends % 7
print(f"remainder: {remainder}")

# Built-in functions
x = 3.14
y = 4
z = 5

result = round(x)
print(result)

result = abs(y)
print(result)

result = pow(4,3)
print(result)

result = max(x, y, z)
print(result)

result = min(x, y, z)
print(result)

# Math
import math
print("Math")
x = 9.9
print(math.pi)
print(math.e)
result = math.sqrt(x)
print(result)
result = math.ceil(x)
print(result)
result = math.floor(x)
print(result)

# 1 - Circumference of a circle
radius = float(input("Enter the radius of a circle: "))

circumference = 2 * math.pi * radius

print(f"The circumference is: {round(circumference,2)}cm")

# 2 - Area of a circle

area = math.pi * pow(radius,2)

print(f"The area is: {round(area,2)}cm^2")

# 3 - Hypotenuse
a = float(input("Enter the side A: "))
b = float(input("Enter the side B: "))

hypotenuse = math.sqrt(pow(a,2) + pow(b,2))

print(f"The hypotenuse is: {round(hypotenuse,2)}")


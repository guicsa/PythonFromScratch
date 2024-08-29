#0 Initial inouts
name = input("Enter your name: ")
age = int(input("Enter your age: "))

print(f"Hello {name}!")
print(f"You are {age} years old")

#1 Mad libs

adjective1 = input("Enter an adjective: ")
noun = input("Enter a noun: ")
adjective2 = input("Enter an adjective: ")
verb = input("Enter a verb: ")
adjective3 = input("Enter an adjective: ")
print(f"Today I went to a {adjective1} zoo")
print(f"In an exhibit, I saw {noun}")
print(f"{noun} was {adjective2} and {verb}ing")
print(f"I was {adjective3}")

#2 Area Calc
length = float(input("Enter the length of a rectangle: "))
width = float(input("Enter the width of a rectangle: "))
height = float(input("Enter the height of a rectangle: "))

area = length * width
print(f"The area is: {area}cm^2")

volume = area * height
print(f"The volume is: {volume}cm^3")


#3 Shopping Cart
item = input("What item would you like to buy?: ")
price = float(input("What is the price?: "))
quantity = int(input("How may would you like?: "))

total = price * quantity
print(f"You have bought {quantity} x {item}/s")
print(f"Your total is: ${round(total, 2)}")

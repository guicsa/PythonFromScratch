name = input("Enter your name: ")

while name == "":
    print("You did not enter your name")
    name = input("Enter your name: ")
print(f"Welcome {name}")

age = int(input("Enter your age: "))

while age < 0:
    print("Age can't be negative")
    age = int(input("Enter your age: "))
print(f"{name}, you are {age} years old")

food = input(f"{name}, enter a food you like (q to quit): ")
while not food == "q":
    print(f"You like {food}")
    food = input(f"{name}, enter a food you like (q to quit): ")
    
print(f"bye, {name}")
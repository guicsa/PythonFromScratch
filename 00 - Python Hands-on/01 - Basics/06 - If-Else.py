# Age validation
age = int(input("Enter your age: "))
if age >= 100:
    print("You are too old to sign up!")
elif age >= 18:
    print("You are now signed up!")
elif age < 0:
    print("You haven't been born yet!")
else:
    print("You must be 18+ to sign up")

# Food
response = input("Would you like food? (Y/N): ")
if response == "Y":
    print("Have some food!")
elif response == "N":
    print("No food for you!")
else:
    print("Invalid response")

# Name
name = input("Enter your name: ")
if name == "":
    print("You did not type in your name!")
else:
    print(f"Hello {name}!")

# Online
online = True
if online:
    print("The user is online")
else:
    print("The user is offline")

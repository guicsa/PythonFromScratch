name = input("Enter your full name: ")

result = len(name)
print(result)
result = name.find("i")
print(result)
result = name.rfind("i")
print(result)
result = name.capitalize()
print(result)
result = name.upper()
print(result)
result = name.lower()
print(result)
result = name.isdigit()
print(result)
result = name.isalpha()
print(result)

phone_numer = input("Enter your phone #: ")
result = phone_numer.count("-")
print(result)
result = phone_numer.replace("-", "")
print(result)

# Validate user input exercise

# 1 Username is no more than 12 characters
# 2 Username must not contain spaces
# 3 username must not contain digits
username = input("Enter your username: ")
if len(username) > 12:
    print("Username too long")
elif not username.find(" ") == -1:
    print("Your username can't contain spaces")
elif not username.isalpha():
    print("Your username can't contain numbers")
else:
    print(f"Welcome {username}")

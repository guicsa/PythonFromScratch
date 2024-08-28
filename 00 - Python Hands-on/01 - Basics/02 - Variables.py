## CONCATENATION
age = 30
print("You are " + str(age) + " years old.")
print("You are", age, "years old.")
print(f"You are {age} years old")

## INTEGER
age = 21
players = 2
quantity = 5

print(f"You are {age} years old.")
print(f"There are {players} online")
print(f"Would you like to buy {quantity} apples?")

## FLOAT
gpa = 3.2
distance = 2.5
price = 10.99

print(f"Your gpa is {gpa}")
print(f"You ran {distance }Km")
print(f"The price is ${price}")


## STRING
namme = "Bro"
food = "pizza"
email = "bro123@gmail.com"

print(f"Hello {namme}!")
print(f"You like {food}")
print (f"Your email is {email}")

## BOOLEAN
online = True
for_sale = False
running = True

print(f"Are you online?: {online}")
print(f"Is the item for sale?: {for_sale}")
print(f"Game running: {running}")

if running:
    print("The game is running")
else:
    print("The game is over")

## Tips and Tricks

x, y,z = 1, 2, 3
print(x)
print(y)
print(z)

x = y = z = 0
print(x)
print(y)
print(z)
# LIST
fruits = ["apple","orange","banana","coconut"]

print(fruits[::-1])
print(fruits[0])

for fruit in fruits:
    print(fruit)

#print(dir(fruits))
#print(help(fruits))
print(len(fruits))

print("apple" in fruits)
print("pineapple" in fruits)

fruits[0] = "pineapple"

print(fruits)

fruits.append("grape")

print(fruits)

fruits.remove("pineapple")
fruits.insert(0,"pear")

print(fruits)

fruits.sort()

print(fruits)

fruits.reverse()

print(fruits)
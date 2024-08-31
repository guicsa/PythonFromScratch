# LIST
## Ordered and changeable. Duplicates are OK
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
print(fruits.index("orange"))

fruits.clear()

print(fruits)

# SET
# {} Unordered and immutable, but Add/Remove OK. No duplicates.
print("\n")
print("\n")
print("\n")
fruits = {"apple","orange","banana","coconut"}
print(fruits)
fruits.add("pineapple")
print(fruits)
fruits.remove("apple")
print(fruits)
fruits.pop()
print(fruits)
fruits.clear()
print(fruits)

# Tuple
# () Ordered and unchangeable. Duplicates OK. FASTER
print("\n")
print("\n")
print("\n")
fruits = ("apple","orange","banana","coconut")
print(fruits)
fruits = ("apple","orange","banana","coconut","coconut")
print(fruits)
print("coconut" in fruits)
print(fruits.index("orange"))
print(fruits.count("coconut"))
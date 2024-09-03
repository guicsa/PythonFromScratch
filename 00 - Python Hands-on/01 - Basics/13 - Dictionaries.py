# dictionary = a collection of {key:value} pairs
#               ordered and changeable. No duplicates

capitals = {"USA":"Washington D.C.",
            "India":" New Dheli",
            "China":"Beijing",
            "Russia":"Moscow"}    

print(capitals)
print(capitals.get("China"))

if capitals.get("Japan"):
    print("That capitaç exists in the dictionary")
else:
    print("That capital doesn't exists in the dictionary")

capitals.update({"Gemany":"Berlin"})
capitals.update({"USA":"Miami"})

print(capitals)

capitals.pop("USA")
print(capitals)
capitals.popitem()
print(capitals)

keys = capitals.keys()
print(keys)

for key in capitals.keys():
    print(key, end = " ")
print()
for value in capitals.values():
    print(value, end = " ")
print()

for key, value in capitals.items():
    print(f"Key: {key} // Value: {value}")
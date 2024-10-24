def walk(steps):
    if steps == 0:
        return
    walk(steps - 1)
    print(f"You take step #{steps}")

walk(5)

# Iterative
def factorial(x):
    result = 1
    if x > 0:
        for y in range(1, x + 1):
            result *= y
        return result
        
print(factorial(10))

# Recursive
def factorial2(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x - 1)
        
print(factorial2(6))
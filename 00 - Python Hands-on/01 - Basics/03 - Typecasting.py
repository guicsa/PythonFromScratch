name = "Bro"
age = 21
gpa = 1.9
student = True

## Explicit
print(type(name))
print(type(age))
print(type(gpa))
print(type(student))

age = float(age)
print(age)
print(type(age))

gpa = int(gpa)
print(gpa)
print(type(gpa))


student = str(student)
print(student)
print(type(student))

age = bool(age)
print(age)
print(type(age))

## Implicit
x = 2
y = 2.0
x = x / y
print (x)
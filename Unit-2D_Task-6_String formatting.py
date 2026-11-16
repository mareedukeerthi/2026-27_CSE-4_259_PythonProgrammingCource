name = input("Enter name: ")
age = int(input("Enter age: "))
marks = float(input("Enter marks: "))

# 1. using % operator
print("My name is %s and age is %d" % (name, age))

# 2. using format() method
print("My name is {} and age is {}".format(name, age))
print("Marks: {:.2f}".format(marks))

# 3. using f-string
print(f"My name is {name} and age is {age}")
print(f"Marks: {marks:.2f}")
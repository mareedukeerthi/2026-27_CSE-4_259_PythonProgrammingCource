n = int(input("Enter a 3-digit number: "))
original = n
total = 0

while n > 0:
    digit = n % 10
    total = total + digit ** 3
    n = n // 10

if total == original:
    print(original, "is an Armstrong number")
else:
    print(original, "is Not an Armstrong number")
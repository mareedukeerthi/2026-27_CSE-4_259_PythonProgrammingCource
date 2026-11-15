number = int(input("Enter number: "))
sum = 0

for i in range(number):
    num = float(input("Enter number: "))
    sum = sum + num

avg = sum / number

print(f"Sum = {sum}")
print(f"Average = {avg}")
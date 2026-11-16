n = int(input("Enter size: "))
row = 1

while row <= n:
    for col in range(1, n + 1):
        print('*', end=" ")
    print()
    row = row + 1
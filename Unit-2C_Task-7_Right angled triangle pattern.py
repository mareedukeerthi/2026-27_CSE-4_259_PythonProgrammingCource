rows = int(input("Enter number of rows: "))
symbol = input("Enter symbol to print (* or 0): ")

for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(symbol, end=" ")
    print()
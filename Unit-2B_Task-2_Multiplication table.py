num = int(input("Enter terms: "))
a = 0
b = 1

for i in range(num):
    print(a)
    nxt = a + b
    a = b
    b = nxt
n = int(input("Enter number: "))
x = 0
L = []
L = [x for x in range(1, n+1) if n % x == 0 if x != 1 and x != n]

print(L)
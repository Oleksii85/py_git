L = [1, 2, 3, 4, 5]
b = 0
LP = []
for i in L:
    b += i
    LP.append(b)
print(LP[::-1])
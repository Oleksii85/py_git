n = int(input("Введіть суму: "))
list = (1000, 500, 200, 100, 50, 20, 10)
if n % 10 == 0:
    if n >= list[0]:
        for i in range(1, (n//list[0])+1):
            n -= list[0]
        print(i, "x",list[0])
    if n >= list[1]:
        for i in range(1, (n//list[1])+1):
            n -= list[1]
        print(i, "x", list[1])
    if n >= list[2]:
        for i in range(1, (n//list[2])+1):
            n -= list[2]
        print(i, "x", list[2])
    if n >= list[3]:
        for i in range(1, (n//list[3])+1):
            n -= list[3]
        print(i, "x", list[3])
    if n >= list[4]:
        for i in range(1, (n//list[4])+1):
            n -= list[4]
        print(i, "x", list[4])
    if n >= list[5]:
        for i in range(1, (n//list[5])+1):
            n -= list[5]
        print(i, "x", list[5])
    if n >= list[6]:
        for i in range(1, (n//list[6])+1):
            n -= list[6]
        print(i, "x", list[6])
else:
    print("Банкомат видає купюри 1000, 500, 200, 100, 50, 20 та 10 грн, введіть суму кратну 10 грн.")
n = int(input("Введіть суму: "))
des = 10
dwa = 10
pya = 10
sot = 10
dwisti = 10
pyatsot = 10
if n % 10 == 0:
    i = n
    while i >= 10 * 10 and i % 20 != 0 and i % 50 != 0:     #10
        des -= 1
        i -= 10
    if n < 10 * 10:
        for j in range(1, (n // 10) + 1):
            n -= 10
        print(j, "x", 10)
        j = 0
    else:
        print(des, "x", 10)
        n -= 10 * des
    i = n
    if i >= 20 * 10 and i % 50 != 0:                          #20
        dwa -= 5
        while i % 50 != 0:
            dwa += 1
            i -= 20
    if n < 20 * 10:
        for j in range(1, (n // 20) + 1):
            n -= 20
        print(j, "x", 20)
        j = 0
    else:
        print(dwa, "x", 20)
        n -= 20 * dwa
    i = n
    while i >= 50 * 10 and i % 100 != 0:                       #50
        pya -= 1
        i -= 50
    if n < 50 * 10:
        for j in range(1, (n // 50) + 1):
            n -= 50
        print(j, "x", 50)
        j = 0
    else:
        print(pya, "x", 50)
        n -= 50 * pya
    i = n
    while i >= 100 * 10 and i % 200 != 0 and i % 500 != 0:     #100
        sot -= 1
        i -= 100
    if n < 100 * 10:
        for j in range(1, (n // 100) + 1):
            n -= 100
        print(j, "x", 100)
        j = 0
    else:
        print(sot, "x", 100)
        n -= 100 * sot
    i = n
    if i >= 200 * 10 and i % 500 != 0:                           #200
        dwisti -= 5
        while i % 500 != 0:
            dwisti += 1
            i -= 200
    if n < 200 * 10:
        for j in range(1, (n // 200) + 1):
            n -= 200
        print(j, "x", 200)
        j = 0
    else:
        print(dwisti, "x", 200)
        n -= 200 * dwisti
    i = n
    while i >= 500 * 10 and i % 1000 != 0:                        #500
        pyatsot -= 1
        i -= 500
    if n < 500 * 10:
        for j in range(1, (n // 500) + 1):
            n -= 500
        print(j, "x", 500)
        j = 0
    else:
        print(pyatsot, "x", 500)
        n -= 500 * pyatsot
    i = n
    if n >= 1000:
        for i in range(1, (n // 1000) + 1):
            n -= 1000
        print(i, "x", 1000)
else:
    print("Банкомат видає купюри 1000, 500, 200, 100, 50, 20 та 10 грн, введіть суму кратну 10 грн.")
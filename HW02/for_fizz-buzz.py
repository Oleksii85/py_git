fizz = int(input("Введіть fizz: "))
buzz = int(input("Введіть buzz: "))
t = int(input("Введіть третє число: "))

for t in range(1, t+1):
    if t % fizz == 0 and t % buzz == 0:
        print("FB", end=" ")
    elif t % fizz == 0:
        print("F", end=" ")
    elif t % buzz == 0:
        print("B", end=" ")
    else:
        print(t, end=" ")
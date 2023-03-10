num = int(input('Введіть непарне число: '))
if not num % 2:
    print('Парне, введіть непарне')
else:
    a = 1
    prob = num // 2
    while a != num + 2:
        print(' ' * prob + ('*' * a))
        a += 2
        prob -= 1
    b = num - 2
    prob2 = 1
    while b > 0:
        print(' ' * prob2 + ('*' * b))
        b -= 2
        prob2 += 1
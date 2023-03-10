n = int(input('Введіть число: '))
list = []
print('Розряди: ')
while n >= 1000000:
    print(n // 1000000, 'мільйон(а, ів)', end=' ')
    list.append(n // 1000000)
    n = n % 1000000
    print('\n', end='')
while n >= 1000:
    print(n // 1000, 'тисяч(а, і)', end=' ')
    list.append(n // 1000)
    n = n % 1000
    print('\n', end='')
while n >= 100:
    print(n // 100, 'сотень(ні, ня)', end=' ')
    list.append(n // 100)
    n = n % 100
    print('\n', end='')
while n >= 10:
    print(n // 10, 'десятків(ки, ок)', end=' ')
    list.append(n // 10)
    n = n % 10
    print('\n', end='')
while n >= 1:
    print(n // 1, 'одиниць(і, ця)', end=' ')
    list.append(n // 1)
    n = n % 1
    print('\n', end='')
print('Множники: ', list)
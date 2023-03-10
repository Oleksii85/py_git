# https://www.codewars.com/kata/5467e4d82edf8bbf40000155
def descending_order(num):
    num2 = list(str(num))
    print(int(''.join(sorted(num2, reverse=True))))
    return int(''.join(sorted(num2, reverse=True)))

lst = 42145
descending_order(lst)
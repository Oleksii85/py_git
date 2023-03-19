# https://www.codewars.com/kata/63f96036b15a210058300ca9
def second_symbol(s, symbol):
    t = -1
    for i, x in enumerate(s):
        if i != s.index(x) and x == symbol:
            t = s.find(symbol, i)
            break
        if t == -1:
            pass
    print(t)
    return t

second_symbol('Hello world!!!','l')   # 3
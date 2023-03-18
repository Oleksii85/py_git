# https://www.codewars.com/kata/581e014b55f2c52bb00000f8
def decipher_this(s):
    s = s.split()
    s2 = ''
    num = []
    for i in s:
        nw = i
        for x in filter(str.isdigit, i):
            nw = nw[1:]
            num.append(x)
        num1 = int(''.join(num))
        if len(nw) >= 2:
            s2 = s2 + (f' {chr(num1)}{nw[-1]}{nw[1:-1]}{nw[:1]}')
        else:
            s2 = s2 +(f' {chr(num1)}{nw}')
        num.clear()
    print(s2.lstrip())
    return(s2.lstrip())

decipher_this('82yade 115te 103o')
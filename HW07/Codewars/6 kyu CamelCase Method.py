# https://www.codewars.com/kata/587731fda577b3d1b0001196
def camel_case(s):
    st = s.split()
    sr = []
    for i in st:
        sr.append(i.capitalize())
    print(''.join(sr))
    return(''.join(sr))

camel_case("camel case method")
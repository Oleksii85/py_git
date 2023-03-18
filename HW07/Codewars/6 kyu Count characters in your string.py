# https://www.codewars.com/kata/52efefcbcdf57161d4000091
def count(s):
    st = {}.fromkeys(s, 0)
    for i in s: st[i] += 1
    print(st)
    return st

count('aba')
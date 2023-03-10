# https://www.codewars.com/kata/53dbd5315a3c69eed20002dd
def filter_list(l):
    L = []
    for i in l:
        if type(i) == int:
            L.append(i)
    print(L)
    return L

filter_list([1,2,'aasf','1','123',123])
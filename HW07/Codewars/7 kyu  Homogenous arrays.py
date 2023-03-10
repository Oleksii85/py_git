# https://www.codewars.com/kata/57ef016a7b45ef647a00002d
def filter_homogenous(arrays):
    list_i = []
    list_s = []
    new_lst2 = []
    for i in arrays:
        list_i = list(filter(lambda x: type(x) == int, i))
        list_s = list(filter(lambda x: type(x) == str, i))
        if len(i) == len(list_i) and list_i != list_s:
            new_lst2.append(i)
        if len(i) == len(list_s) and list_i != list_s:
            new_lst2.append(i)
    print(new_lst2)
    return new_lst2

arr =  [[1, 5, 4], ['a', 3, 5], ['b'], [], ['1', 2, 3]]

filter_homogenous(arr)
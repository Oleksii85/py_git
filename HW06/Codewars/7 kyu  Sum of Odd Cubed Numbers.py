# https://www.codewars.com/kata/580dda86c40fa6c45f00028a
def cube_odd(arr):
    n_par = 0
    for num in arr:
        if type(num) != int:
            return None
        if num % 2:
            n_par += num ** 3
    print(n_par)
    return n_par
lst = ([1, 2, 3, 4])
cube_odd(lst)

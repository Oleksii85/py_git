# https://www.codewars.com/kata/563f879ecbb8fcab31000041
def factory(x):
    def fives(n):
        print([i * x for i in n])
        return [i * x for i in n]
    return fives
my_array = [1, 2, 3]
factory(5)(my_array)
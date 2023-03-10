# https://www.codewars.com/kata/586909e4c66d18dd1800009b
def multiply_all (arr):
    def multiplyAll (n):
        print([i*n for i in arr])
        return [i*n for i in arr]
    print(multiplyAll)
    return multiplyAll

multiply_all([1, 2, 3])(1)
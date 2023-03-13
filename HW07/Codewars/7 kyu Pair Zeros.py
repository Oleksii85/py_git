# https://www.codewars.com/kata/54e2213f13d73eb9de0006d2
def pair_zeros(arr):
    arr2 = []
    arr0 = []
    arr00 = [0, 0]
    for i in arr:
        if i == 0:
            if arr0 != arr00:
                arr0.append(i)
                if arr0 != arr00:
                    arr2.append(i)
            if arr0 == arr00:
                arr0.clear()
        else:
            arr2.append(i)
    arr = arr2
    print(arr)
    return arr

lst = [1,0,1,0,2,0,0,3,0]
pair_zeros(lst)
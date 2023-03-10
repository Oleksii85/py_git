# https://www.codewars.com/kata/530017aac7c0f49926000084
def pluck(objs, name):
    new_ar = []
    d = []
    for i in objs:
        x = list(filter(lambda key: key == name, i))
        t = list(name)
        if x == t:
            d.clear()
            for key, value in i.items():
                d.append(key)
                if key == name:
                    new_ar.append(value)
        else:
            new_ar.append(None)
    print(new_ar)
    return new_ar

pluck([{'a':1, 'b':2, 'c': 3}, {'a':4, 'b':5, 'c': 6}, {'a':7, 'b':8, 'c': 9}, {'a':10, 'b':11}], 'c')
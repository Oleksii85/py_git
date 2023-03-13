# https://www.codewars.com/kata/5413759479ba273f8100003d
def reverse(lst):
    empty_list = list()
    for i in range (len(lst)-1, -1, -1):
        empty_list.append(lst[i])
    print(empty_list)
    return empty_list

lis = [1, None, 14, "two"]
reverse(lis)
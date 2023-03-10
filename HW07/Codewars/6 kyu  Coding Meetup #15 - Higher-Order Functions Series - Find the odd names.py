# https://www.codewars.com/kata/583a8bde28019d615a000035
def find_odd_names(lst):
    dic_name = []
    for devel in lst:
        sum_name = sum(ord(i) for i in devel['firstName'])
        if sum_name % 2:
            dic_name.append(devel)
    print(dic_name)
    return dic_name

list1 = [
  { 'firstName': 'Aba', 'lastName': 'N.', 'country': 'Ghana', 'continent': 'Africa', 'age': 21, 'language': 'Python' },
  { 'firstName': 'Abb', 'lastName': 'O.', 'country': 'Israel', 'continent': 'Asia', 'age': 39, 'language': 'Java' }
];

find_odd_names(list1)
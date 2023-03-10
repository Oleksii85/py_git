# https://www.codewars.com/kata/58279e13c983ca4a2a00002a
def greet_developers(lst):
    list2 = []
    for devel in lst:
        value_st = ('Hi ', devel['firstName'], ', what do you like the most about ', devel['language'], '?')
        key, value = 'greeting', ''.join(value_st)
        devel.update({key: value})
        list2.append(dict(devel))
    print(list2)
    return list2

list1 = [
  { 'firstName': 'Sofia', 'lastName': 'I.', 'country': 'Argentina', 'continent': 'Americas', 'age': 35, 'language': 'Java' },
  { 'firstName': 'Lukas', 'lastName': 'X.', 'country': 'Croatia', 'continent': 'Europe', 'age': 35, 'language': 'Python' },
  { 'firstName': 'Madison', 'lastName': 'U.', 'country': 'United States', 'continent': 'Americas', 'age': 32, 'language': 'Ruby' }
]
greet_developers(list1)
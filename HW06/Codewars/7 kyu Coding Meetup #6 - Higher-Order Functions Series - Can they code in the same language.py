# https://www.codewars.com/kata/58287977ef8d4451f90001a0
def is_same_language(lst):
    devel_one = dict(lst[0])
    for devel in lst:
        if devel['language'] != devel_one['language']:
            print(False)
            return False
    print(True)
    return True

list1 = [
  { 'firstName': 'Daniel', 'lastName': 'J.', 'country': 'Aruba', 'continent': 'Americas', 'age': 42, 'language': 'JavaScript' },
  { 'firstName': 'Kseniya', 'lastName': 'T.', 'country': 'Belarus', 'continent': 'Europe', 'age': 22, 'language': 'JavaScript' },
  { 'firstName': 'Hanna', 'lastName': 'L.', 'country': 'Hungary', 'continent': 'Europe', 'age': 65, 'language': 'JavaScript' },
]
is_same_language(list1)
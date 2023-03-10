# https://www.codewars.com/kata/582887f7d04efdaae3000090
def find_senior(lst):
    list = []
    dic_devel = dict(lst[0])
    for devel in lst:
        if devel['age'] > dic_devel['age']:
            dic_devel.update(devel)
            list.clear()
        if devel['age'] == dic_devel['age']:
            list.append(devel)
    print(list)
    return list

list1 = [
  { 'firstName': 'Gabriel', 'lastName': 'X.', 'country': 'Monaco', 'continent': 'Europe', 'age': 49, 'language': 'PHP' },
  { 'firstName': 'Odval', 'lastName': 'F.', 'country': 'Mongolia', 'continent': 'Asia', 'age': 38, 'language': 'Python' },
  { 'firstName': 'Emilija', 'lastName': 'S.', 'country': 'Lithuania', 'continent': 'Europe', 'age': 19, 'language': 'Python' },
  { 'firstName': 'Sou', 'lastName': 'B.', 'country': 'Japan', 'continent': 'Asia', 'age': 49, 'language': 'PHP' },
]
find_senior(list1)
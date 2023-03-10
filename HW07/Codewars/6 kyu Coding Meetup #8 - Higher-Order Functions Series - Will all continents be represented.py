# https://www.codewars.com/kata/58291fea7ff3f640980000f9
def all_continents(lst):
    List_cont = ['Africa', 'Americas', 'Asia', 'Europe', 'Oceania']
    for devel in lst:
        if devel['continent'] == List_cont[0]:
            List_cont[0] = 0
        if devel['continent'] == List_cont[1]:
            List_cont[1] = 1
        if devel['continent'] == List_cont[2]:
            List_cont[2] = 2
        if devel['continent'] == List_cont[3]:
            List_cont[3] = 3
        if devel['continent'] == List_cont[4]:
            List_cont[4] = 4
        else:
            pass
    if List_cont == [0, 1, 2, 3, 4]:
        print((True))
        return True
    else:
        print(False)
        return False

list1 =  [
  { 'firstName': 'Fatima', 'lastName': 'A.', 'country': 'Algeria', 'continent': 'Africa', 'age': 25, 'language': 'JavaScript' },
  { 'firstName': 'Agustín', 'lastName': 'M.', 'country': 'Chile', 'continent': 'Americas', 'age': 37, 'language': 'C' },
  { 'firstName': 'Jing', 'lastName': 'X.', 'country': 'China', 'continent': 'Asia', 'age': 39, 'language': 'Ruby' },
  { 'firstName': 'Laia', 'lastName': 'P.', 'country': 'Andorra', 'continent': 'Europe', 'age': 55, 'language': 'Ruby' },
  { 'firstName': 'Oliver', 'lastName': 'Q.', 'country': 'Australia', 'continent': 'Oceania', 'age': 65, 'language': 'PHP' }
  ]
all_continents(list1)
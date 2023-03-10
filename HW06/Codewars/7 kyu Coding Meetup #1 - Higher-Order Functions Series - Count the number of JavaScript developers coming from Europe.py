# https://www.codewars.com/kata/582746fa14b3892727000c4f
def count_developers(lst):
    dev_JS_in_EU = 0
    dev_n = 0
    for devel in lst:
        if devel['continent'] == 'Europe' and devel['language'] == 'JavaScript':
            dev_JS_in_EU +=1
    print(dev_JS_in_EU if dev_JS_in_EU > 0 else dev_n)
    return dev_JS_in_EU if dev_JS_in_EU > 0 else dev_n

lst1 = [
  { 'firstName': 'Noah', 'lastName': 'M.', 'country': 'Switzerland', 'continent': 'Europe', 'age': 19, 'language': 'JavaScript' },
  { 'firstName': 'Maia', 'lastName': 'S.', 'country': 'Tahiti', 'continent': 'Oceania', 'age': 28, 'language': 'JavaScript' },
  { 'firstName': 'Shufen', 'lastName': 'L.', 'country': 'Taiwan', 'continent': 'Asia', 'age': 35, 'language': 'HTML' },
  { 'firstName': 'Sumayah', 'lastName': 'M.', 'country': 'Tajikistan', 'continent': 'Asia', 'age': 30, 'language': 'CSS' }
]
count_developers(lst1)
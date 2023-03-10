# https://www.codewars.com/kata/5828713ed04efde70e000346
def count_languages(lst):
    list_lang = []
    for num in lst:
        list_lang.append(num['language'])
    lang = {}.fromkeys(list_lang, 0)
    for devel in lst:
        lang[devel['language']] += 1
    print(lang)
    return lang

list1 = [
    { 'firstName': 'Noah', 'lastName': 'M.', 'country': 'Switzerland', 'continent': 'Europe', 'age': 19, 'language': 'C' },
    { 'firstName': 'Anna', 'lastName': 'R.', 'country': 'Liechtenstein', 'continent': 'Europe', 'age': 52, 'language': 'JavaScript' },
    { 'firstName': 'Ramon', 'lastName': 'R.', 'country': 'Paraguay', 'continent': 'Americas', 'age': 29, 'language': 'Ruby' },
    { 'firstName': 'George', 'lastName': 'B.', 'country': 'England', 'continent': 'Europe', 'age': 81, 'language': 'C' },
    ]
count_languages(list1)
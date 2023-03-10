# https://www.codewars.com/kata/5827acd5f524dd029d0005a4
def is_ruby_coming(lst):
    for devel in lst:
         if devel['language'] != 'Ruby':
             developer = False
         else:
             developer = True
             break
    print(developer)
    return developer

list1 = [
    { 'firstName': 'Sofia', 'lastName': 'I.', 'country': 'Argentina', 'continent': 'Americas', 'age': 35, 'language': 'Java' },
    { 'firstName': 'Lukas', 'lastName': 'X.', 'country': 'Croatia', 'continent': 'Europe', 'age': 35, 'language': 'Python' },
    { 'firstName': 'Madison', 'lastName': 'U.', 'country': 'United States', 'continent': 'Americas', 'age': 32, 'language': 'Ruby' }
    ]
is_ruby_coming(list1)
# https://www.codewars.com/kata/582ba36cc1901399a70005fc
def get_average(lst):
    avr_age = (sum(devel['age'] for devel in lst))/len(lst)
    print(round(avr_age))
    return round(avr_age)

list1 = [
  { 'firstName': 'Maria', 'lastName': 'Y.', 'country': 'Cyprus', 'continent': 'Europe', 'age': 30, 'language': 'Java' },
  { 'firstName': 'Victoria', 'lastName': 'T.', 'country': 'Puerto Rico', 'continent': 'Americas', 'age': 70, 'language': 'Python' },
]
get_average(list1)
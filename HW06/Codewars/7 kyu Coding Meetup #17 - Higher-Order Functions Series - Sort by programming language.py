# https://www.codewars.com/kata/583ea278c68d96a5fd000abd
def sort_by_language(arr):
    def lang_dev(lang):
        return lang["language"], lang["first_name"]
    arr.sort(key=lang_dev)
    print(arr)
    return arr

list1 = [
  { "first_name": "Nikau", "last_name": "R.", "contry": "New Zealand", "continent": "Oceania", "age": 39, "language": "Ruby" },
  { "first_name": "Precious", "last_name": "G.", "contry": "South Africa", "continent": "Africa", "age": 22, "language": "JavaScript" },
  { "first_name": "Maria", "last_name": "S.", "contry": "Peru", "continent": "Americas", "age": 30, "language": "C" },
  { "first_name": "Agustin", "last_name": "V.", "contry": "Uruguay", "continent": "Americas", "age": 19, "language": "JavaScript" }
]
sort_by_language(list1)
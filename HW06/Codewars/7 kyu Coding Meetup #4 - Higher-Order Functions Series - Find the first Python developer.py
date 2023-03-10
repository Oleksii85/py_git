# https://www.codewars.com/kata/5827bc50f524dd029d0005f2
def get_first_python(users):
    dev_not_pyt = 1
    for devel in users:
        if devel["language"] != "Python":
            pass
        else:
            dev = devel.get("first_name") +', ' + devel.get("country")
            print(dev)
            return dev
            dev_not_pyt = 0
            break
    if dev_not_pyt == 1:
        print('There will be no Python developers')
        return 'There will be no Python developers'

list1 = [
  { "first_name": "Mark", "last_name": "G.", "country": "Scotland", "continent": "Europe", "age": 22, "language": "JavaScript" },
  { "first_name": "Victoria", "last_name": "T.", "country": "Puerto Rico", "continent": "Americas", "age": 30, "language": "Python" },
  { "first_name": "Emma", "last_name": "B.", "country": "Norway", "continent": "Europe", "age": 19, "language": "Clojure" }
]
get_first_python(list1)
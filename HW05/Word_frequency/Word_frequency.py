with open("text2.txt", "r", encoding="utf8") as file:   # вирішує проблему з кодуванням
    eng_text = file.read()
eng_text = eng_text.lower()
eng_text = eng_text.replace(',', ' ').replace('.', ' ').replace('?', ' ').replace('!', ' ').replace(':', ' ').replace('–', ' ').replace('"', ' ').replace('(', ' ').replace(')', ' ')
eng_text = eng_text.split()
E_text = []
for num in eng_text:      # перебирає всі елементи та видаляє числа
    if not num.isdigit():
        E_text.append(num)

dic = {}.fromkeys(E_text, 0)    # створюємо словник та вказуємо в ключі всі слова з попереднього очищеного списку
for w in E_text:          # перебирає всі слова та додає по 1-ці тим що повторюються
    dic[w] += 1

for k, v in sorted(zip(dic.values(), dic.keys()), reverse=True):    # перетворює (за доп.zip) в список та сортує від біл. до менш. кількості
    if v == 'a'or v == 'the' or v == 'an':      # якщо є артиклі, окремо друкуємо
        print(v, '-', k, 'арт.')
    else:
        print(v, '-', k, 'сл.')
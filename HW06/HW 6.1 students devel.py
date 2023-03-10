def sort_by_language(lst):
    dev_2_len = []
    dev_not_front = []
    dev_py_ja = []
    for devel in lst:
        if devel['2nd group'] != '-':
            dev_2_len.append(devel['firstName'] + ', ' + devel['lastName'])
        if devel['1st group'] != 'FrontEnd' and devel['2nd group'] != 'FrontEnd':
            dev_not_front.append(devel['firstName'] + ', ' + devel['lastName'])
        if devel['1st group'] == 'Python' or devel['2nd group'] == 'Python' or devel['1st group'] == 'Java' or devel['2nd group'] == 'Java':
            dev_py_ja.append(devel['firstName'] + ', ' + devel['lastName'])
    print(dev_2_len)
    print(dev_not_front)
    print(dev_py_ja)

list = [
  {'firstName': 'Viktoria', 'lastName': 'K.', '1st group': 'Python', '2nd group': '-'},
  {'firstName': 'Kseniya', 'lastName': 'T.', '1st group': 'FrontEnd', '2nd group': 'Java'},
  {'firstName': 'Piotr', 'lastName': 'X.', '1st group': 'FullStack', '2nd group': '-'},
  {'firstName': 'Andrei', 'lastName': 'A.', '1st group': 'Java', '2nd group': '-'},
  {'firstName': 'Maria', 'lastName': 'E.', '1st group': 'FrontEnd', '2nd group': 'C'},
  {'firstName': 'Aleksandr', 'lastName': 'S.', '1st group': 'Python', '2nd group': 'PHP'}]
sort_by_language(list)
def change_dic(f_dic):
    new_dic = {}
    for key, value in f_dic.items():
        new_dic[value] = key
    print(new_dic)


change_dic({1: 'b', 3: 'r'})

def change_dic(f_dic):
    new_dic = {value: key for key, value in f_dic.items()}
    print(new_dic)


change_dic({1: 'b', 3: 'r'})
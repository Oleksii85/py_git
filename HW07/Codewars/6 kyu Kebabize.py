# https://www.codewars.com/kata/57f8ff867a28db569e000c4a
def kebabize(st):
    st = st.replace('0', '').replace('1', '').replace('2', '').replace('3', '').replace('4', '').replace('5', '').replace('6', '').replace('7', '').replace('8', '').replace('9', '')
    if st == '':
        print(st)
        return st
    t = st[0]
    for i in st[1:]:
        if i.isupper():
            t += (f' {i}')
        else:
            t += i
    t = t.lower()
    t = t.replace(' ', '-')
    print(t)
    return
kebabize("camelsHave3Humps")
kebabize("42")
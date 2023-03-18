# https://www.codewars.com/kata/517abf86da9663f1d2000003
def to_camel_case(text):
    if text == '':
        print(text)
        return text
    else:
        tex = text.replace('_', ' ').replace('-', ' ')
        tex = tex.split()
        text2 = ''.join(tex[0])
        for i in tex[1:]:
            i = i.capitalize()
            text2 = text2 + i
        print(text2)
        return text2

to_camel_case("The_Stealth-Warrior")
def down(string):
    return string.lower()


def up(string):
    return string.upper()


live_str = "I LoVe PythoN".split()
print(list(map(down, live_str)))
print(list(map(up, live_str)))
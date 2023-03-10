file2 = open('tr.txt', 'r')
for line in file2:
    spl = line.split(';')
    left = sum(map(int, spl[0].split())) // len(spl[0].split())
    left2 = sum(map(int, spl[0].split())) % len(spl[0].split())
    right = spl[1].split()
    if left == int(right[0]) and left2 == int(right[1]):
        print(line, True)
    else:
        print(line, False)
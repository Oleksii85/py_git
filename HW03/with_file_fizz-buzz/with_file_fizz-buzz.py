import sys
filename = sys.argv[1]
f = open(filename, 'r')
for line in f:
	l = line.split()
	fizz = int(l[0])
	buzz = int(l[1])
	t = int(l[2])
	for t in range(1, t + 1):
		if t % fizz == 0 and t % buzz == 0:
			print("FB", end=" ")
		elif t % fizz == 0:
			print("F", end=" ")
		elif t % buzz == 0:
			print("B", end=" ")
		else:
			print(t, end=" ")
	print('\n', end='')
f.close()
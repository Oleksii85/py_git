f = open('fizzbuzz20.txt', 'r')
f_two = open('in_file_fizz_buzz20.txt', 'w')

for line in f:
	l = line.split()
	fizz = int(l[0])
	buzz = int(l[1])
	t = int(l[2])
	for t in range(1, t+1):
		if t % fizz == 0 and t % buzz == 0:
			f_two.write("FB ")
		elif t % fizz == 0:
			f_two.write("F ")
		elif t % buzz == 0:
			f_two.write("B ")
		else:
			f_two.write(str(t))
			f_two.write(' ')
	f_two.write('\n')
f.close()
f_two.close()
import numpy as np

fabric = np.zeros((1000, 1000), dtype=np.int16)

def parse_line(line):
	t = line.rstrip('\n').split(' ')
	x = t[2].rstrip(':').split(',')
	y = t[3].split('x')
	return t[0], int(x[0]), int(x[1]), int(y[0]), int(y[1])

with open('input1.txt', 'r') as f:
	for line in f:
		_, left, top, width, height = parse_line(line)
		right = left + width
		bottom = top + height
		fabric[top:bottom, left:right] += 1

print((fabric[:] > 1).sum())

with open('input1.txt', 'r') as f:
	for line in f:
		n, left, top, width, height = parse_line(line)
		right = left + width
		bottom = top + height
		if np.all(fabric[top:bottom, left:right] == 1):
			print(n)

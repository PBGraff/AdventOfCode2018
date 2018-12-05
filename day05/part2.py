with open('input.txt', 'r') as f:
	polymer = f.readline().rstrip('\n')

def find_next(polymer):
	j, prev = 1, ord(polymer[0])
	while j < len(polymer):
		curr = ord(polymer[j])
		if abs(curr - prev) == 32:
			return j - 1
		else:
			prev = curr
			j += 1
	return None

def remove_match(polymer, i):
	return polymer[:i] + polymer[(i+2):]

def react(polymer):
	while True:
		i = find_next(polymer)
		if i is None:
			break
		else:
			polymer = remove_match(polymer, i)
	return len(polymer)

shortest = 1e9

for c in range(26):
	capital = 65 + c
	lower = capital + 32
	n = react(polymer.replace(chr(capital), '').replace(chr(lower), ''))
	print(chr(capital), chr(lower), n)
	if n < shortest:
		shortest = n

print(shortest)

import pandas as pd

data = pd.read_csv('input1.txt', names=['df'])
print(data.shape)

visited = set()

n = data.shape[0]
f = 0
i = 0

while f not in visited:
	visited.add(f)
	f += data['df'][i % n]
	i += 1

print(f, i)

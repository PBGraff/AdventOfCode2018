import pandas as pd
import numpy as np


data = pd.read_csv('input1.txt', names=['df'])
n = data.shape[0]

text = np.empty((n, 26), dtype='<U1')

for i in range(n):
	text[i, :] = np.array(list(data['df'][i]))

print(text)

for i in range(n):
	for j in range(i, n):
		match = text[i, :] == text[j, :]
		if match.sum() == 25:
			print(i, j, ''.join(text[i, match]))

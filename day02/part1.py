import pandas as pd
import numpy as np

def checksum(key):
	_, group = np.unique(list(key), return_inverse=True)
	cnt = set(np.bincount(group))
	return 2 in cnt, 3 in cnt

data = pd.read_csv('input1.txt', names=['df'])

results = np.empty((data.shape[0], 2), dtype=np.bool_)

for i in range(data.shape[0]):
	results[i, 0], results[i, 1] = checksum(data['df'][i])

print(results.sum(axis=0))
print(results.sum(axis=0).prod())

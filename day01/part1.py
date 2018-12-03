import pandas as pd

data = pd.read_csv('input1.txt', names=['df'])

print(data['df'].sum())

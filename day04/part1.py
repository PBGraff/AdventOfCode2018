import numpy as np
import pandas as pd

with open('input.txt', 'r') as f, open('input_processed.txt', 'w') as g:
	for line in f:
		g.write(line.replace('] ', '],'))

def parse_timestamp(ts):
	return (ts[1:-1]+':00').replace('1518', '2018')
	# return pd.to_datetime(ts[1:-1]+':00', format='%Y-%m-%d %H:%M:%S')

data = pd.read_csv('input_processed.txt', names=['datetime', 'event'], converters={'datetime': parse_timestamp})

data['timestamp'] = pd.to_datetime(data['datetime'])
data.sort_values('timestamp', inplace=True)

guards = {}

guard = None
start = None

for tp in data.itertuples(index=False, name=None):
	time, event = tp[2], tp[1]
	if 'Guard' in event:
		guard = int(event.split(' ')[1][1:])
		if guard not in guards:
			guards[guard] = np.zeros((60,), dtype=np.int16)
	elif event == 'falls asleep':
		start = time.minute
	else:
		guards[guard][start:time.minute] += 1
		start = None

sorted_guards = sorted(guards, key=lambda g: guards[g].sum())
gid = sorted_guards[-1]
minute = guards[gid].argmax()
print(gid, minute)
print(gid * minute)

sorted_guards = sorted(guards, key=lambda g: guards[g].max())
gid = sorted_guards[-1]
minute = guards[gid].argmax()
print(gid, minute)
print(gid * minute)

import numpy as np

mode_k = 'mode'
median_k = 'median'
iqr_k = 'IQR'

# put these in a dict and I'll compare them
actual = {mode_k 	: 0,
		 median_k 	: 0,
		 iqr_k 		: 0}

# From lecture 6B
num_set = [1,1,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,5,5,5,5,5,5,5] 

# What's the mode?
actual[mode_k] = max(num_set, key=num_set.count)
# WHat's the median?
actual[median_k] = num_set[int(len(num_set)/2)]
# What's the IQR?
actual[iqr_k] = num_set[int(len(num_set)*3/4)]-num_set[int((len(num_set)-1)*1/4)]

expect = {mode_k 	: 3, # Todo
		 median_k 	: 3,
		 iqr_k 		: 1}

for key in expect:
	if expect[key] != actual[key]:
		print(f'Wrong value for {key}! Expect: {expect[key]}, actual: {actual[key]}')
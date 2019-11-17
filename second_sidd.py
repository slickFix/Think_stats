import sys

sys.path.append("../lesson 1")

import survey
import numpy as np


# Exercise 2.2
table = survey.Pregnancies()
table.ReadRecords(data_dir='../dataset')
first_birth_time = []
other_birth_time = []
for record in table.records:
	if record.birthord == 1:
		first_birth_time.append(record.prglength)
	elif record.birthord != "NA" and record.birthord != 1:
		other_birth_time.append(record.prglength)

print("Standard deviation for first birth : ",np.std(first_birth_time))
print("Standard deviation for other birth : ",np.std(other_birth_time))
import survey
import numpy as np

# Exercise 1.3.1
table = survey.Pregnancies()
table.ReadRecords(data_dir='../dataset')
print('Number of pregnancies', len(table))

# Exercise 1.3.2
live_birth_count = 0
for record in table.records:
	if record.birthord != "NA":
		live_birth_count+=1

print("Count of live birth : ",live_birth_count)

# Exercise 1.3.3
first_birth_count = 0
other_birth_count = 0
for record in table.records:
	if record.birthord == 1:
		first_birth_count+=1
	elif record.birthord != "NA" and record.birthord != 1:
		other_birth_count+=1

print("Count of 1st birth : ",first_birth_count)
print("Count of other birth : ",other_birth_count)

# Exercise 1.3.4
first_birth_time = []
other_birth_time = []
for record in table.records:
	if record.birthord == 1:
		first_birth_time.append(record.prglength)
	elif record.birthord != "NA" and record.birthord != 1:
		other_birth_time.append(record.prglength)
print("Mean gestation period for 1st babies : ",np.mean(first_birth_time))
print("Mean gestation period for other babies : ",np.mean(other_birth_time))
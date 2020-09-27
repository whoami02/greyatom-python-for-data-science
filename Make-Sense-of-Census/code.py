# --------------
# Importing header files
import numpy as np
import warnings

warnings.filterwarnings('ignore')

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Reading file
data = np.genfromtxt(path, delimiter=",", skip_header=1)

#Code starts here
census = np.concatenate([data, new_record])
print(data.shape, census.shape)

age = census[:, [0]]
max_age = np.max(age)
min_age = np.min(age)
age_mean = np.mean(age)
age_std = np.std(age)
print(max_age, min_age, age_mean, age_std)

temp = census[:, [2]].flatten()
race_0 = temp[temp == 0]
race_1 = temp[temp == 1]
race_2 = temp[temp == 2]
race_3 = temp[temp == 3]
race_4 = temp[temp == 4]
len_0 = len(race_0)
len_1 = len(race_1)
len_2 = len(race_2)
len_3 = len(race_3)
len_4 = len(race_4)
arr = [len_0, len_1, len_2, len_3, len_4]
minority_race = arr.index(np.min(arr))
print(minority_race)

senior_citizen = census[:, [0,6]]
working_hours = senior_citizen[senior_citizen[:,0]>60]
working_hours_sum = sum(working_hours[:,1])
print(working_hours_sum)
senior_citizen_len = len(working_hours[:,0])
avg_working_hours = working_hours_sum/senior_citizen_len
print(avg_working_hours)

inc = census[:, [1,7]]
high = inc[inc[:,0]>10]
low = inc[inc[:,0]<=10]
avg_pay_high = sum(high[:,1])/high.shape[0]
avg_pay_low = sum(low[:,1])/low.shape[0]

print(avg_pay_high, avg_pay_low)





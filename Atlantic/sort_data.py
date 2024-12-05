import pickle

with open("data_test.pkl", "rb") as f:
    test = pickle.load(f)
with open("data_train.pkl", "rb") as f:
    train = pickle.load(f)
with open("data_val.pkl", "rb") as f:
    val = pickle.load(f)

strip_list = ['N', 'E', 'S', 'W']

new_test = []
for i in range(len(test)):
    if test[i][0][0] < 0:
        continue
    new_time_group = []
    for m in range(len(test[i])):
        new_list = [test[i][m][0], ]
        new = test[i][m][1]
        for j in strip_list:
            new = new.strip(j)
        new_list.append(float(new))
        new = test[i][m][2]
        for j in strip_list:
            new = new.strip(j)
        new_list.append(float(new))
        new_time_group.append(new_list)
    new_test.append(new_time_group)
    
new_train = []
for i in range(len(train)):
    if train[i][0][0] < 0:
        continue
    new_time_group = []
    for m in range(len(train[i])):
        new_list = [train[i][m][0], ]
        new = train[i][m][1]
        for j in strip_list:
            new = new.strip(j)
        new_list.append(float(new))
        new = train[i][m][2]
        for j in strip_list:
            new = new.strip(j)
        new_list.append(float(new))
        new_time_group.append(new_list)
    new_train.append(new_time_group)
    
new_val = []
for i in range(len(val)):
    if val[i][0][0] < 0:
        continue
    new_time_group = []
    for m in range(len(val[i])):
        new_list = [val[i][m][0], ]
        new = val[i][m][1]
        for j in strip_list:
            new = new.strip(j)
        new_list.append(float(new))
        new = val[i][m][2]
        for j in strip_list:
            new = new.strip(j)
        new_list.append(float(new))
        new_time_group.append(new_list)
    new_val.append(new_time_group)
    
f = open("data_test.pkl", "wb")
pickle.dump(new_test, f)
f = open("data_train.pkl", "wb")
pickle.dump(new_train, f)
f = open("data_val.pkl", "wb")
pickle.dump(new_val, f)
        
# In Program 5, accuracy of rnew can be estimated by r1 - r2. Modify the program to calculate the estimated accuracy, store it in another list, say diff_list, and output the list at the end of the program.


x = 2
rnew = x

rnew_list = []
diff_list = []

r1 = rnew
r2 = x / r1
rnew = (r1 + r2) / 2
rnew_list.append(rnew)
diff_list.append(r1 - r2) 
print(rnew_list)
print(diff_list)

r1 = rnew
r2 = x / r1
rnew = (r1 + r2) / 2
rnew_list.append(rnew)
diff_list.append(r1 - r2) 
print(rnew_list)
print(diff_list)

r1 = rnew
r2 = x / r1
rnew = (r1 + r2) / 2
rnew_list.append(rnew)
diff_list.append(r1 - r2) 
print(rnew_list)
print(diff_list)

r1 = rnew
r2 = x / r1
rnew = (r1 + r2) / 2
rnew_list.append(rnew)
diff_list.append(r1 - r2) 
print(rnew_list)
print(diff_list)


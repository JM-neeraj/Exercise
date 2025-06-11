# Creating a table of Kyoto intersections


name = ['Rohit', 'Anoop', 'Aryan']
surname = ['Raikwar', 'Kushwah', 'Gupta']
full_name = [['','',''], ['','',''] , ['','','']]

for i in range(len(name)):
    for j in range(len(surname)):
        fullname = name[i] + surname[j]
        full_name[i][j] = fullname

print(full_name)

# tozai=["Sanjyo","Shijyo","Gojyo"]
# nanboku=["Horikawa","Karasuma","Kawaramachi"]
# cross_table=[["","",""],["","",""],["","",""]]
# for i in range(len(tozai)):
#     for j in range(len(nanboku)):
#         cross = tozai[i]+nanboku[j]
#         cross_table[i][j] = cross

# print(cross_table)
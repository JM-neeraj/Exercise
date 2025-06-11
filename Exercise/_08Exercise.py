# Checking the block
# Unindent line 12 from the block in the previous example (p6-1.py) as shown below. Check and explain how the program behaves.

x = 2
#
rnew = x
#
for i in range(10):
    r1 = rnew
    r2 = x/r1
    rnew = (r1 + r2)/2
print(r1, rnew, r2) # Without throw error print succesfully
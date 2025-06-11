# Write and run Program 6-6

# Find the square root of x

x = 2

rnew= x

diff = rnew - x/rnew
print(diff)
if diff < 0:
    diff = -diff
while diff > 1.0E-6: 
    r1 = rnew
    r2 = x / r1
    rnew = (r1 + r2) / 2
    print(r1, rnew, r2)
    diff = r1 - r2
    if diff < 0:
        diff = -diff

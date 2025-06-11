# Input number form terminal
# Modify p6-6.py so that it solves for the square root of the number input through the terminal.


# x = int(input('Enter a number: '))
x = float(input('Enter a number: '))

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
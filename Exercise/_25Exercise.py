# Create a function to solve squate root


def sq_root(x):

    rnew = x

    for i in range(10):
        r1 = rnew
        r2 = x/r1
        rnew = (r1 + r2)/2
        print(r1, rnew, r2)


sq_root(2)
sq_root(3)
sq_root(4)
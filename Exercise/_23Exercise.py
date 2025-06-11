# Calculating Pi using the Leibnitz formula

n = 10
pie = 0

for i in range (n):
    pie = (pie + 1)**1 / i%2 +1 



print(pie)
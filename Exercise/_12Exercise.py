# Explanation of continue and break.

for i in range(10):
    if i == 1:
        continue # Skip that iteration & move to next iteration 
    if i == 8:
        break # Quit the iteration & leave block
    print(i)
# Below is a program that calculates the price of a ¥1000 product at 15% off.
#  This program contains a single error which causes it to yield an error message when run.
# Please locate and explain the error.

"""kakaku = 1000
nebikiritsu= 15
kakaku = Kakaku*(100-nebikiritsu)/100 
print(kakaku)
"""
# NameError: name 'Kakaku' is not defined

#  After correcting the error, explain how the program behaves.

kakaku = 1000
nebikiritsu= 15
kakaku = kakaku*(100-nebikiritsu)/100 
print(kakaku)
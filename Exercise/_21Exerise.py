# Reviewing Error Handling

try:
    x = float(input("Enter a number: "))

except ValueError as e:
    print("Error:", e)

    

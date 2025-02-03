income = float(input("Enter the annual income: "))

bound = 85528.0
if income>3090:
    if income<=bound:
        tax = (0.18*income)-556.2
    else:
        tax = 14839.2 + (0.32*(income-bound))
else:
    tax=0

tax = round(tax, 0)
print("The tax is:", tax, "thalers")

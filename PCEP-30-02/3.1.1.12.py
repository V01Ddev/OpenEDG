year = int(input("Enter a year: "))


l = "Leap year"
c = "Common year"

output = l

if year > 1582:
    if (year%4)!=0:
        output = c
    elif (year%100)!=0:
        output = l
    elif (year%400)!=0:
        output = c
else:
    output = "Not within the Gregorian calendar period"

print(output)

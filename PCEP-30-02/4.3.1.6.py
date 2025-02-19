def is_year_leap(year):

    output = True

    if year > 1582:
        if (year%4)!=0:
            output = False
        elif (year%100)!=0:
            output = True
        elif (year%400)!=0:
            output = False
    else:
        output = None

    return output

test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]
for i in range(len(test_data)):
	yr = test_data[i]
	print(yr,"->",end="")
	result = is_year_leap(yr)
	if result == test_results[i]:
		print("OK")
	else:
		print("Failed")

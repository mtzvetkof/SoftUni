year = int(input())

distinct = False
while not distinct:
    year += 1
    year_str = str(year)
    i =1
    while i != len(year_str) :
        for l in range(i, len(year_str)):
            a = year_str[i-1]
            b = year_str[l]
            if year_str[i-1] != year_str[l]:
                distinct = True
            else:
                distinct = False
                break
        if not distinct:
            break
        i += 1
print(year)


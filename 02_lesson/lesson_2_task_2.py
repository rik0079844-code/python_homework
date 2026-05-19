is_year_leap = input('год ')

year = int(is_year_leap)
if year % 4 == 0:
    result = True
else:
    result = False
print(f'год {year}: {result}')

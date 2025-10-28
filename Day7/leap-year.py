years_to_check = [2000, 2024, 1900, 2100, 2023]
def is_leap_year(year):
    # if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    if year % 4 == 0 and year % 100 != 0:
        return True
    elif year % 4 == 0 and year %100 == 0 and year%400 == 0:
        return True
    else:
        return False

year = int(input("Enter Year: "))
result = is_leap_year(year)
print(result)
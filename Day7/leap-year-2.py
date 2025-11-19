def is_leap_year(years):
    for year in years:
        if (year % 4 == 0 and year % 100 != 0) or (year % 4 == 0 and year % 100 == 0 and year % 400 == 0):
            print(f"{year} is leap year")
        else:
            print(f"{year} is not leap year")

years_to_check = [2000, 2024, 1900, 2100, 2023]
is_leap_year(years_to_check)


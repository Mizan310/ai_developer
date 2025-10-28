# Compound Interest determined

initial_amount_P = int(input("Enter the Initial Amount: (P)"))

annual_interest_percent = float(input("Enter the Annual Interest: (r)"))
annual_interest_r = annual_interest_percent/100

compunding_period_n = float(input("Enter the Compounding Period: (n)"))

time_period_t = float(input("Enter the time period: (t)"))
# A = P(1 + r/n)^(nt)
compound_interest_A = initial_amount_P * (1 + (annual_interest_r/compunding_period_n))**(compunding_period_n*time_period_t)
# CI = A - P
compound_interest_CI_Correct = compound_interest_A - initial_amount_P

print(f"compound interest of an amount is {compound_interest_CI:.2f}, {compound_interest_A:.2f}")




city = input()
sales = float(input())

commission = 0
is_invalid = False

if city == "Sofia" and sales >= 0:
    if 0 <= sales <= 500:
        commission = sales * 0.05
    elif sales <= 1000:
        commission = sales * 0.07
    elif sales <= 10000:
        commission = sales * 0.08
    else:
        commission = sales * 0.12
elif city == "Varna" and sales >= 0:
    if 0 <= sales <= 500:
        commission = sales * 0.045
    elif sales <= 1000:
        commission = sales * 0.075
    elif sales <= 10000:
        commission = sales * 0.10
    else:
        commission = sales * 0.13
elif city == "Plovdiv" and sales >= 0:
    if 0 <= sales <= 500:
        commission = sales * 0.055
    elif sales <= 1000:
        commission = sales * 0.08
    elif sales <= 10000:
        commission = sales * 0.12
    else:
        commission = sales * 0.145
else:
    is_invalid = True

if not is_invalid:
    print(f"{commission:.2f}")
else:
    print("error")
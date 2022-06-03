city = input()
package_type = input()
vip = input()
days = int(input())
daily_price = 0
total_price = 0
is_error = False
is_negative = False

if days < 1:
    is_negative = True
if days > 7:
    days -= 1
if city == "Bansko" or city == "Borovets":
    if package_type == "noEquipment":
        daily_price += 80
        if vip == "yes":
            daily_price *= 0.95
    elif package_type == "withEquipment":
        daily_price += 100
        if vip == "yes":
            daily_price *= 0.90
    else:
        is_error = True
elif city == "Varna" or city == "Burgas":
    if package_type == "noBreakfast":
        daily_price += 100
        if vip == "yes":
            daily_price *= 0.93
    elif package_type == "withBreakfast":
        daily_price += 130
        if vip == "yes":
            daily_price *= 0.88
    else:
        is_error = True
else:
    is_error = True

if is_error:
    print("Invalid input!")
elif is_negative:
    print("Days must be positive number!")
else:
    total_price = days * daily_price
    print(f"The price is {total_price:.2f}lv! Have a nice time!")

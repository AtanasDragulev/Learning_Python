fruit_type = input()
day_of_week = input()
amount = float(input())

is_workday = day_of_week == "Monday" or day_of_week == "Tuesday" or day_of_week == "Wednesday" or \
             day_of_week == "Thursday" or day_of_week == "Friday"
is_weekend = day_of_week == "Saturday" or day_of_week == "Sunday"
fruit_price = 0

if is_weekend:
    if fruit_type == "banana":
        fruit_price = 2.70
    elif fruit_type == "apple":
        fruit_price = 1.25
    elif fruit_type == "orange":
        fruit_price = 0.90
    elif fruit_type == "grapefruit":
        fruit_price = 1.60
    elif fruit_type == "kiwi":
        fruit_price = 3.00
    elif fruit_type == "pineapple":
        fruit_price = 5.60
    elif fruit_type == "grapes":
        fruit_price = 4.20
    else:
        print("error")

elif is_workday:
    if fruit_type == "banana":
        fruit_price = 2.50
    elif fruit_type == "apple":
        fruit_price = 1.20
    elif fruit_type == "orange":
        fruit_price = 0.85
    elif fruit_type == "grapefruit":
        fruit_price = 1.45
    elif fruit_type == "kiwi":
        fruit_price = 2.70
    elif fruit_type == "pineapple":
        fruit_price = 5.50
    elif fruit_type == "grapes":
        fruit_price = 3.85

if fruit_price !=0:
    total = amount * fruit_price
    print(f"{total:.2f}")
else:
    print("error")
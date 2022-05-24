movie_budget = float(input())
statists_amount = int(input())
clothes_price = float(input())

decor = movie_budget * 0.1
clothes_expense = statists_amount * clothes_price

if statists_amount > 150:
    clothes_expense -= clothes_expense * 0.1

total = decor + clothes_expense

if total > movie_budget:
    over_budget = total - movie_budget
    print("Not enough money!")
    print(f"Wingard needs {over_budget:.2f} leva more.")
else:
    excess_money = movie_budget - total
    print("Action!")
    print(f"Wingard starts filming with {excess_money:.2f} leva left.")

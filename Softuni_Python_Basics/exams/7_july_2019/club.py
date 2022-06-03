target_income = float(input())
total_income = 0
cocktail_name = input()
is_target = False
while cocktail_name != "Party!":
    current_order = int(input())
    current_price = current_order * len(cocktail_name)
    if current_price % 2 != 0:
        current_price *= 0.75
    total_income += current_price
    if total_income >= target_income:
        is_target = True
        break
    cocktail_name = input()
if is_target:
    print("Target acquired.")
else:
    difference = abs(target_income - total_income)
    print(f"We need {difference:.2f} leva more.")
print(f"Club income - {total_income:.2f} leva.")

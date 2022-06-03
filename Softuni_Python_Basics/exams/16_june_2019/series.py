discounted = {"Thrones": 0.5, "Lucifer": 0.6, "Protector": 0.7, "TotalDrama": 0.8, "Area": 0.9}
budget = float(input())
series_amount = int(input())
total_sum = 0
for series in range(series_amount):
    current_name = input()
    current_price = float(input())
    discount = 1
    if current_name in discounted:
        discount = discounted[current_name]
    total_sum += current_price * discount
difference = abs(budget - total_sum)
if budget >= total_sum:
    print(f"You bought all the series and left with {difference:.2f} lv.")
else:
    print(f"You need {difference:.2f} lv. more to buy the series!")
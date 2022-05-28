age = int(input())
washer_price = float(input())
toy_price = int(input())

money = 0
toys = 0
b_day_money = 0

for b_day in range(1,age + 1):
    if b_day % 2 != 0:
        toys += 1
    else:
        b_day_money += 10
        money += b_day_money - 1

money += toys * toy_price
difference = abs(money - washer_price)
if money >= washer_price:
    print(f"Yes! {difference:.2f}")
else:
    print(f"No! {difference:.2f}")

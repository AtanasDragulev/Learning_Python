strawberry_price = float(input())
bananas_amount = float(input())
oranges_amount = float(input())
raspberries_amount = float(input())
strawberry_amount = float(input())
raspberries_price = strawberry_price / 2
orange_price = raspberries_price * 0.60
bananas_price = raspberries_price * 0.20
needed_money = 0

needed_money += bananas_amount * bananas_price + oranges_amount * orange_price + \
    raspberries_amount * raspberries_price + strawberry_amount * strawberry_price

print(f"{needed_money:.2f}")

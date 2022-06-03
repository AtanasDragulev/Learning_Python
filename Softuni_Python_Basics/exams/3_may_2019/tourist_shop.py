budget = float(input())
product_counter = 0
products_cost = 0
product_name = input()
is_enough = True
difference = 0
while product_name != "Stop":
    product_price = float(input())
    product_counter += 1
    if product_counter % 3 == 0:
        product_price /= 2
    if product_price > budget:
        difference = abs(product_price - budget)
        is_enough = False
        break
    budget -= product_price
    products_cost += product_price
    product_name = input()

if is_enough:
    print(f"You bought {product_counter} products for {products_cost:.2f} leva.")
else:
    print("You don't have enough money!")
    print(f"You need {difference:.2f} leva!")

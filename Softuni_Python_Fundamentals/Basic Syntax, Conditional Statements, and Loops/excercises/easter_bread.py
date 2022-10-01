budget = float(input())
flour_cost = float(input())
eggs_cost = flour_cost * 0.75
milk_cost = (flour_cost * 1.25) / 4
bread_price = flour_cost + eggs_cost + milk_cost
bread_made = 0
colored_eggs = 0

while budget >= bread_price:
    colored_eggs += 3
    bread_made += 1
    budget -= bread_price
    if bread_made % 3 == 0:
        colored_eggs -= bread_made - 2

print(f"You made {bread_made} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")

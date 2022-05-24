nylon_price = 1.50
paint_price = 14.50
paint_thinner_price = 5.00

nylon_ammount = int(input())
paint_amount = int(input())
paint_thinner_amount = int(input())
hours = int(input())

materials_cost = (nylon_ammount + 2) * nylon_price + \
                 (paint_amount * 1.1) * paint_price + \
                 paint_thinner_amount * paint_thinner_price + 0.40

print(materials_cost + ((materials_cost * 0.3 )*hours))
import math

racket_price = float(input())
racket_amount = int(input())
sneakers_amount = int(input())
total_cost = 0

total_cost += racket_amount * racket_price
total_cost += sneakers_amount * (racket_price / 6)
total_cost += total_cost * 0.2

print(f"Price to be paid by Djokovic {math.floor(total_cost/8)}")
print(f"Price to be paid by sponsors {math.ceil(total_cost - (total_cost/8))}")
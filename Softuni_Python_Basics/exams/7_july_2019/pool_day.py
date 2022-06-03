import math

people = int(input())
entry_price = float(input())
bed_price = float(input())
umbrella_price = float(input())
total_sum = 0

total_sum += people * entry_price
total_sum += math.ceil(people/2) * umbrella_price
total_sum += math.ceil(people * 0.75) * bed_price

print(f"{total_sum:.2f} lv.")

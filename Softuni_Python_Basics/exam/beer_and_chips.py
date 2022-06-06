import math

fan_name = input()
budget = float(input())
beer_amount = int(input())
chips_amount = int(input())
cost = 0
cost += beer_amount * 1.20
cost += math.ceil(cost * 0.45 * chips_amount)

difference = abs(budget - cost)
if budget >= cost:
    print(f"{fan_name} bought a snack and has {difference:.2f} leva left.")
else:
    print(f"{fan_name} needs {difference:.2f} more leva!")
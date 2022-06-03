budget = float(input())
needed_fuel = float(input())
day = input()
needed_money = 0

needed_money += needed_fuel * 2.10 + 100
if day == "Saturday":
    needed_money *= 0.90
else:
    needed_money *= 0.80

difference = abs(budget - needed_money)
if budget >= needed_money:
    print(f"Safari time! Money left: {difference:.2f} lv. ")
else:
    print(f"Not enough money! Money needed: {difference:.2f} lv.")

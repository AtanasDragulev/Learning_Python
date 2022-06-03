budget = float(input())
nights = int(input())
price_night = float(input())
percent_additional = int(input())
percent_additional = percent_additional / 100
total_cost = 0

if nights > 7:
    price_night *= 0.95
total_cost += nights * price_night
total_cost += budget * percent_additional
difference = abs(budget - total_cost)
if total_cost <= budget:
    print(f"Ivanovi will be left with {difference:.2f} leva after vacation.")
else:
    print(f"{difference:.2f} leva needed.")
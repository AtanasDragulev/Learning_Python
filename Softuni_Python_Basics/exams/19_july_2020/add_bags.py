price_over_twenty = float(input())
luggage_weight = float(input())
days_left = int(input())
luggage_amount = int(input())
total_cost = 0

if luggage_weight < 10:
    total_cost += luggage_amount * price_over_twenty * 0.2
elif luggage_weight <= 20:
    total_cost += luggage_amount * price_over_twenty * 0.5
else:
    total_cost += luggage_amount * price_over_twenty

if days_left > 30:
    total_cost *= 1.10
elif 7 <= days_left <= 30:
    total_cost *= 1.15
else:
    total_cost *= 1.40
print(f"The total price of bags is: {total_cost:.2f} lv.")

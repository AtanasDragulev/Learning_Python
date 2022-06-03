budget = float(input())
is_used = False
total_used = 0
while not is_used:
    actor_name = input()
    if actor_name == "ACTION":
        break
    if len(actor_name) > 15:
        total_used += (budget - total_used) * 0.2
    else:
        current = float(input())
        total_used += current
    if (budget - total_used) <= 0:
        is_used = True
difference = abs(budget - total_used)
if budget < total_used:
    print(f"We need {difference:.2f} leva for our actors.")
else:
    print(f"We are left with {difference:.2f} leva.")

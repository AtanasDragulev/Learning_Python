movie_budget = float(input())
destination = input()
season = input()
days = int(input())
cost_per_day = 0
taxes = 0
total_cost = 0
if destination == "Dubai":
    taxes = 0.70
    cost_per_day = 40000
    if season == "Winter":
        cost_per_day = 45000
elif destination == "Sofia":
    taxes = 1.25
    cost_per_day = 12500
    if season == "Winter":
        cost_per_day = 17000
else:
    taxes = 1
    cost_per_day = 20250
    if season == "Winter":
        cost_per_day = 24000
total_cost = (days * cost_per_day) * taxes
difference = abs(movie_budget - total_cost)
if total_cost <= movie_budget:
    print(f"The budget for the movie is enough! We have {difference:.2f} leva left!")
else:
    print(f"The director needs {difference:.2f} leva more!")

travel_distance = int(input())
travel_time = input()
taxi_per_km = 0.79
buss_per_km = 0.09
train_per_km = 0.06

if travel_time == "night":
    taxi_per_km = 0.90

if travel_distance < 20:
    cost = 0.70 + travel_distance * taxi_per_km
    print(f'{cost:.2f}')
elif travel_distance < 100:
    cost = travel_distance * buss_per_km
    print(f'{cost:.2f}')
else:
    cost = travel_distance * train_per_km
    print(f'{cost:.2f}')

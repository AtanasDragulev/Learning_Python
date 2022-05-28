loads_number = int(input())
minibus_load = 0
truck_load = 0
train_load = 0
total_load = 0
cost = 0

for i in range(loads_number):
    current = int(input())
    total_load += current
    if current < 4:
        cost += current * 200
        minibus_load += current
    elif current < 12:
        cost += current * 175
        truck_load += current
    else:
        cost += current * 120
        train_load += current

cost = cost / total_load
minibus_load = (minibus_load / total_load) * 100
truck_load = (truck_load / total_load) * 100
train_load = (train_load / total_load) * 100

print(f"{cost:.2f}")
print(f"{minibus_load:.2f}%")
print(f"{truck_load:.2f}%")
print(f"{train_load:.2f}%")

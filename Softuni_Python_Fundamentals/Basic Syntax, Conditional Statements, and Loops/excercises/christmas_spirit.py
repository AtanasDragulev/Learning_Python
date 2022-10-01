allowed_quantity = int(input())
days_left = int(input())
total_cost = 0
total_spirit = 0

for day in range(1, days_left+1):
    if day % 11 == 0:
        allowed_quantity += 2
    if day % 2 == 0:
        total_cost += allowed_quantity * 2
        total_spirit += 5
    if day % 3 == 0:
        total_cost += allowed_quantity * 5 + allowed_quantity * 3
        total_spirit += 13
    if day % 5 == 0:
        total_cost += allowed_quantity * 15
        total_spirit += 17
        if day % 3 == 0:
            total_spirit += 30
    if day % 10 == 0:
        total_spirit -= 20
        total_cost += 5 + 3 + 15
if days_left % 10 == 0:
    total_spirit -= 30

print(f"Total cost: {total_cost}")
print(f"Total spirit: {total_spirit}")

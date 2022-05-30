while True:
    destination = input()
    if destination == "End":
        break
    minimum_budget = float(input())
    saved_money = 0
    while saved_money < minimum_budget:
        current = float(input())
        saved_money += current
    print(f"Going to {destination}!")

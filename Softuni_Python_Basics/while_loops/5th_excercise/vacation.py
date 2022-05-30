money_needed = float(input())
money_available = float(input())
days_elapsed = 0
concurrent_spend = 0
is_failed = False

while money_available < money_needed:
    days_elapsed += 1
    current_action = input()
    current_sum = float(input())
    if current_action == "spend":
        concurrent_spend += 1
        if concurrent_spend == 5:
            is_failed = True
            break
        money_available -= current_sum
        if money_available < 0:
            money_available = 0
    else:
        money_available += current_sum
        concurrent_spend = 0

if is_failed:
    print("You can't save the money.")
    print(days_elapsed)
else:
    print(f"You saved the money for {days_elapsed} days.")
    
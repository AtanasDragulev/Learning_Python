number_of_days = int(input())
hours_per_day = int(input())
is_day_even = False
is_hour_even = False
total_sum = 0
daily_sum = 0

for day in range(1, number_of_days + 1):
    if day % 2 == 0:
        is_day_even = True
    else:
        is_day_even = False
    for hour in range(1, hours_per_day+1):
        if hour % 2 == 0:
            is_hour_even = True
        else:
            is_hour_even = False
        if is_day_even and not is_hour_even:
            daily_sum += 2.50
        elif not is_day_even and is_hour_even:
            daily_sum += 1.25
        else:
            daily_sum += 1
    print(f"Day: {day} - {daily_sum:.2f} leva")
    total_sum += daily_sum
    daily_sum = 0
print(f"Total: {total_sum:.2f} leva")

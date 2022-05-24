hours_needed = int(input())
days_available = int(input())
workers = int(input())

hours_available = int((days_available * 8) * 0.9)
hours_available += workers * (2 * days_available)
hours_left = abs(hours_available - hours_needed)

if hours_available >= hours_needed:
    print(f'Yes!{hours_left} hours left.')
else:
    print(f'Not enough time!{hours_left} hours needed.')

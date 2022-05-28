junior_cyclists = int(input())
senior_cyclists = int(input())
track_type = input()

total = 0

if track_type == "trail":
    total = junior_cyclists * 5.50 + senior_cyclists * 7
elif track_type == "cross-country":
    if junior_cyclists + senior_cyclists >=50:
        total = junior_cyclists * (8 * 0.75) + senior_cyclists * (9.50 * 0.75)
    else:
        total = junior_cyclists * 8 + senior_cyclists * 9.50
elif track_type =="downhill":
    total = junior_cyclists * 12.25 + senior_cyclists * 13.75
else:
    total = junior_cyclists * 20 + senior_cyclists * 21.50

total *= 0.95

print(f'{total:.2f}')

hour = int(input())
minutes = int(input())

minutes += 15

if minutes <= 59:
    print(f'{hour}:{minutes:02}')
elif minutes > 59 and hour <= 22:
    hour += 1
    minutes -= 60
    print(f'{hour}:{minutes:02}')
else:
    hour = 0
    minutes -= 60
    print(f'{hour}:{minutes:02}')

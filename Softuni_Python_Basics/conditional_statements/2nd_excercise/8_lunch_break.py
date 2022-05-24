import math
series_name = input()
series_duration = int(input())
break_duration = int(input())

lunch_duration = break_duration / 8
relax_duration = break_duration / 4

time_available = break_duration - (lunch_duration + relax_duration)

if time_available >= series_duration:
    print(f'You have enough time to watch {series_name} and left '
          f'with {math.ceil(time_available - series_duration)} minutes free time.')
else:
    print(f"You don't have enough time to watch {series_name},"
          f" you need {math.ceil(series_duration - time_available)} more minutes.")
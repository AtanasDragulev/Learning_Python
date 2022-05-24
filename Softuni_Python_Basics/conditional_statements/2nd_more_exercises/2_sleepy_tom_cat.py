off_work_days = int(input())
play_norm = 30000

play_time = (365 - off_work_days) * 63 + off_work_days * 127
difference = abs(play_norm - play_time)
play_hours = difference // 60
play_minutes = difference % 60

if play_time > play_norm:
    print('Tom will run away')
    print(f'{play_hours} hours and {play_minutes} minutes more for play')
elif play_time < play_norm:
    print('Tom sleeps well')
    print(f'{play_hours} hours and {play_minutes} minutes less for play')
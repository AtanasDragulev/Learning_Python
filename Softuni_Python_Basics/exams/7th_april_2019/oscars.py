hall_rent = int(input())

rewards = hall_rent * 0.70
catering = rewards * 0.85
sound = catering / 2
total = hall_rent + rewards + catering + sound

print(f'{total:.2f}')

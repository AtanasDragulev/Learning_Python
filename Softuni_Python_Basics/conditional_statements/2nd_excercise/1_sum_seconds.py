player_1 = int(input())
player_2 = int(input())
player_3 = int(input())

total_seconds = player_1 + player_2 + player_3

minutes = total_seconds // 60
seconds = total_seconds % 60

print(f'{minutes}:{seconds:02}')

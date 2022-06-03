series_name = input()
seasons_amount = int(input())
episodes_amount = int(input())
episode_length = float(input())
episode_length *= 1.20
total_minutes = 0
total_minutes += seasons_amount * episodes_amount * episode_length
total_minutes += seasons_amount * 10
print(f"Total time needed to watch the {series_name} series is {int(total_minutes)} minutes.")
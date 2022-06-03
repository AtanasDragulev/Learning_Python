recording_time = int(input())
scenes_amount = int(input())
scene_duration = int(input())
needed_time = 0

needed_time += recording_time * 0.15
needed_time += scenes_amount * scene_duration
difference = abs(recording_time - needed_time)
if recording_time >= needed_time:
    print(f"You managed to finish the movie on time! You have {round(difference)} minutes left!")
else:
    print(f"Time is up! To complete the movie you need {round(difference)} minutes.")

exam_hour = int(input())
exam_minutes = int(input())
arrival_hour = int(input())
arrival_minutes = int(input())

exam_in_minutes = exam_hour * 60 + exam_minutes
arrival_in_minutes = arrival_hour * 60 + arrival_minutes

if arrival_in_minutes > exam_in_minutes:
    print("Late")
elif arrival_in_minutes >= exam_in_minutes - 30:
    print("On time")
else:
    print("Early")

difference = exam_in_minutes - arrival_in_minutes
difference_hours = abs(difference) // 60
difference_minutes = abs(difference) % 60

if 0 < difference:
    if difference < 60:
        print(f"{difference_minutes} minutes before the start")
    else:
        print(f"{difference_hours}:{difference_minutes:02d} hours before the start")
elif difference < 0:
    if difference > -60:
        print(f"{difference_minutes} minutes after the start")
    else:
        print(f"{difference_hours}:{difference_minutes:02d} hours after the start" )

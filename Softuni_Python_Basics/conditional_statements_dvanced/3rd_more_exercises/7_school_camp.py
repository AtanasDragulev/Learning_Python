season = input()
group_type = input()
student_amount = int(input())
nights = int(input())

cost = 0
sport = ""

if season == "Winter":
    if group_type == "mixed":
        cost = student_amount * 10 * nights
        sport = "Ski"
    else:
        cost = student_amount * 9.60 * nights

    if group_type == "girls":
        sport = "Gymnastics"
    elif group_type == "boys":
        sport = "Judo"
elif season == "Spring":
    if group_type == "mixed":
        cost = student_amount * 9.50 * nights
        sport = "Cycling"
    else:
        cost = student_amount * 7.20 * nights

    if group_type == "girls":
        sport = "Athletics"
    elif group_type == "boys":
        sport = "Tennis"
else:
    if group_type == "mixed":
        cost = student_amount * 20 * nights
        sport = "Swimming"
    else:
        cost = student_amount * 15 * nights

    if group_type == "girls":
        sport = "Volleyball"
    elif group_type == "boys":
        sport = "Football"

if 10 <= student_amount < 20:
    cost *= 0.95
elif 20 <= student_amount < 50:
    cost *= 0.85
elif student_amount >= 50 :
    cost *= 0.50

print(f"{sport} {cost:.2f} lv.")

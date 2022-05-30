floors = int(input())
rooms = int(input())

for floor in range(floors, 0, -1):
    rooms_per_floor = ""
    for room in range(rooms):
        if floor == floors:
            rooms_per_floor += "L" + str(floor) + str(room) + " "
        elif floor % 2 != 0:
            rooms_per_floor += "A" + str(floor) + str(room) + " "
        else:
            rooms_per_floor += "O" + str(floor) + str(room) + " "
        if room == rooms - 1:
            print(rooms_per_floor)

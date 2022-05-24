room_width = float(input())
room_height = float(input())

places_per_width = (room_width * 100) // 120
places_per_height = ((room_height * 100) - 100 ) // 70

total = int(places_per_width * places_per_height) - 3

print(total)

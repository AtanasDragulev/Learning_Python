import math

world_record = float(input())
distance = float(input())
time_per_meter = float(input())

resistance = math.floor(distance // 15) * 12.5
result = distance * time_per_meter + resistance

if world_record <= result:
    print(f'No, he failed! He was {(result - world_record):.2f} seconds slower.')
else:
    print(f'Yes, he succeeded! The new world record is {result:.2f} seconds.')

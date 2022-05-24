length = int(input())
width = int(input())
height = int(input())
percent_used = float(input()) / 100

volume_in_liters = (length * width * height) / 1000
needed_water = volume_in_liters - volume_in_liters * percent_used
print(needed_water)
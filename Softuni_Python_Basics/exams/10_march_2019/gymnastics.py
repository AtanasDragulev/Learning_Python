country = input()
gear_type = input()
total_score = 0
difficulty = 0
performance = 0
if gear_type == "ribbon":
    if country == "Russia":
        difficulty = 9.100
        performance = 9.400
    elif country == "Bulgaria":
        difficulty = 9.600
        performance = 9.400
    else:
        difficulty = 9.200
        performance = 9.500
elif gear_type == "hoop":
    if country == "Russia":
        difficulty = 9.300
        performance = 9.800
    elif country == "Bulgaria":
        difficulty = 9.550
        performance = 9.750
    else:
        difficulty = 9.450
        performance = 9.350
else:
    if country == "Russia":
        difficulty = 9.600
        performance = 9.00
    elif country == "Bulgaria":
        difficulty = 9.500
        performance = 9.400
    else:
        difficulty = 9.700
        performance = 9.150
total_score = difficulty + performance
percent_to_max = 100 - (total_score / 20) * 100
print(f"The team of {country} get {total_score:.3f} on {gear_type}.")
print(f"{percent_to_max:.2f}%")

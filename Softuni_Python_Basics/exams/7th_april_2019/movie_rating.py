movie_amount = int(input())
movie_name = ""
movie_high = ""
movie_low = ""
rating = 0
average = 0
high_rating = 0
low_rating = 0
a = 0

while a < movie_amount:
    movie_name = input()
    rating = float(input())

    if rating > high_rating:
        movie_high = movie_name
        high_rating = rating
    if rating < low_rating or low_rating == 0:
        movie_low = movie_name
        low_rating = rating
    a += 1
    average += rating

average /= movie_amount

print(f"{movie_high} is with highest rating: {high_rating:.1f}")
print(f"{movie_low} is with lowest rating: {low_rating}")
print(f"Average rating: {average:.1f}")

movie_counter = 0
best_movie = ""
best_sum = 0
while movie_counter < 7:
    current_movie = input()
    current_sum = 0
    if current_movie == "STOP":
        break
    movie_counter += 1
    for letter in current_movie:
        current_sum += ord(letter)
        if 97 <= ord(letter) <= 122:
            current_sum -= 2 * len(current_movie)
        elif 65 <= ord(letter) <= 90:
            current_sum -= len(current_movie)
    if current_sum > best_sum:
        best_sum = current_sum
        best_movie = current_movie
if movie_counter == 7:
    print("The limit is reached.")
print(f"The best movie for you is {best_movie} with {best_sum} ASCII sum.")

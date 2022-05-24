from art import logo, vs
from game_data import data
import os
from random import randint


def next_choice(_a):
    _b = randint(0, 49)
    if _b == _a:
        next_choice(_a)
    return _b


score = 0
a = randint(0, 49)
is_over = False
print(logo)
while not is_over:
    b = next_choice(a)
    print(f"Compare A: {data[a]['name']}, a {data[a]['description']}, from {data[a]['country']}.")
    print(vs)
    print(f"Compare B: {data[b]['name']}, a {data[b]['description']}, from {data[b]['country']}.")

    if data[a]['follower_count'] > data[b]['follower_count']:
        correct = "a"
        next_question = a
    else:
        correct = "b"
        next_question = b
    print("hint", correct)
    answer = input("Who has more followers? Type 'A' or 'B':").lower()

    if answer == correct:
        score += 1
        a = next_question
        os.system("cls")
        print(logo)
        print(f"You're right! Current score: {score}.")
    else:
        print(f"Sorry, that's wrong. Final score: {score}.")
        is_over = True


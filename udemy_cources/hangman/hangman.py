import random

words_list = ["throne", "established", "inflation", "cupboard", "horror"]

word = random.choice(words_list)
word = [x for x in word]
hidden_word = ["_"] * len(word)
lives = 5

print("".join(hidden_word))

while word != hidden_word:
    guess = input("Input a character: ").lower()
    if guess not in word:
        lives -= 1
        print(f"Wrong letter. {lives} lives left")
        if lives == 0:
            print("You lost")
            break
        continue
    for char in range(len(word)):
        if guess == word[char]:
            hidden_word[char] = word[char]

    print(f'Word: {"".join(hidden_word)}')
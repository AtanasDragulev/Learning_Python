import math

vowels = ['a', 'e', 'i', 'o', 'u', 'y']
most_powerful_word = ""
most_powerful_sum = 0
current_word = input()
while current_word != "End of words":
    current_sum = 0
    for letter in current_word:
        current_sum += ord(letter)
    if current_word.lower()[0] in vowels:
        current_sum = math.floor(current_sum * len(current_word))
    else:
        current_sum = math.floor(current_sum / len(current_word))
    if current_sum > most_powerful_sum:
        most_powerful_sum = current_sum
        most_powerful_word = current_word
    current_word = input()
print(f"The most powerful word is {most_powerful_word} - {most_powerful_sum}")

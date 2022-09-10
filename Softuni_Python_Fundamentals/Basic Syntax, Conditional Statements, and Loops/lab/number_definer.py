number = float(input())
answer = "zero"

if number > 0:
    answer = "positive"
elif number < 0:
    answer = "negative"

if 0 < abs(number) < 1:
    answer = "small " + answer
elif abs(number) > 1000000:
    answer = "large " + answer

print(answer)
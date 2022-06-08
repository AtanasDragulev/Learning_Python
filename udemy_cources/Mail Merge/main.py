names = []
with open("./Input/Letters/starting_letter.txt", mode="r") as file:
    template = file.read()

with open("./Input/Names/invited_names.txt", mode="r") as file:
    for line in file:
        line = line.strip()
        names.append(line)


for name in names:
    current = template.replace("[name]", name)
    with open(f"./Output/ReadyToSend/letter_for_{name}.txt", mode="w") as file:
        file.write(current)
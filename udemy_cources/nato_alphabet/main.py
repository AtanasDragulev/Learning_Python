import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}


def nato_name():
    name = input("What is your name?: ").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in name]
    except KeyError:
        print("Sorry, only letters in the alphabet please")
        nato_name()
    else:
        print(output_list)


nato_name()

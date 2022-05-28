from art import logo
import random


def draw_card():
    return random.choice(list(cards))


def new_game():
    if input("Do you want to play a game of blackjack? Type 'y' or 'n': ").lower() == "y":
        play_blackjack()
    else:
        return


def play_blackjack():
    players_cards = []
    players_score = 0
    dealers_cards = []
    dealers_score = 0
    is_stand = False

    for _ in range(2):
        players_cards.append(draw_card())
        players_score += cards[players_cards[-1]]
        dealers_cards.append(draw_card())
        dealers_score += cards[dealers_cards[-1]]

    if "Ace" in players_cards:
        if players_score - 11 < 11:
            players_score += 10
    if "Ace" in dealers_cards:
        if dealers_score - 11 < 11:
            dealers_score += 10

    print("Score:", players_score, *players_cards)
    print("Dealers first card:", dealers_cards[0])

    while not is_stand:
        if players_score == 21:
            print("BLACKJACK You won")
            new_game()
        elif players_score > 21:
            print(f"{players_score} You went over. You loose.")
            new_game()
        if input("Type 'y' to hit, type 'n' to stand: ").lower() == "y":
            players_cards.append(draw_card())
            players_score += cards[players_cards[-1]]
            if players_cards[-1] == "Ace":
                if players_score - 11 < 11:
                    players_score += 10
                elif players_score > 21:
                    players_score -= 10 * players_cards.count("Ace")
            print("Score:", players_score, *players_cards)
        else:
            is_stand = True

    while dealers_score <= players_score or dealers_score < 17:
        print(dealers_score)
        dealers_cards.append(draw_card())
        dealers_score += cards[dealers_cards[-1]]
        if dealers_cards[-1] == "Ace":
            if dealers_score - 11 < 11:
                dealers_score += 10
            if "Ace" in dealers_cards and dealers_score > 21:
                dealers_score = 0
                for card in dealers_cards:
                    dealers_score += cards[card]
        if dealers_score >= 21:
            break
    print()
    print("Your score:", players_score, "Your final hand", *players_cards)
    print("Dealers score:", dealers_score, "Dealer`s final hand", *dealers_cards)
    print()
    if players_score > dealers_score or dealers_score > 21:
        print(f"You win with score {players_score} - {dealers_score}")
        new_game()
    elif 21 >= dealers_score > players_score:
        print(f"You loose with score {players_score} - {dealers_score}")
        new_game()
    else:
        print("Draw")
        new_game()


cards = {
    "Ace": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5,
    "Six": 6,
    "Seven": 7,
    "Eight": 8,
    "Nine": 9,
    "Ten": 10,
    "Jack": 10,
    "Queen": 10,
    "King": 10
}
print(logo)
new_game()

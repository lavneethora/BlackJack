import random

card_deck = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
random.shuffle(card_deck)
player_card = []
computer_card = []
player_score = 0
computer_score = 0

blackjack_logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""  

print(blackjack_logo)
print("HOUSE RULES\n")
print("The deck is unlimited in size.")
print("There are no jokers.")
print("The Jack/Queen/King all count as 10.")
print("The Ace can count as 11 or 1.")
print("The cards in the list have equal probability of being drawn.")
print("Cards are not removed from the deck as they are drawn.")
print("The computer is the dealer.\n")
            
def initial_player_cards():
    global player_score
    for user_initial_cards in range(2):
        u_card = random.choice(card_deck)
        player_card.append(u_card)
        update_player_score(u_card)
                
def initial_computer_cards():
    global computer_score
    for computer_initial_cards in range(2):
        c_card = random.choice(card_deck)
        computer_card.append(c_card)
        update_computer_score(c_card)
            
def update_player_score(card):
    global player_score
    if card in ['J', 'Q', 'K']:
        player_score += 10
    elif card == 'A':
        ace_input = int(input("Do you want to count Ace as a 11 or a 1?"))
        if ace_input == 11 or ace_input == 1:
            player_score += ace_input  
    else:
        player_score += int(card)
        
def update_computer_score(card):
    global computer_score
    if card in ['J', 'Q', 'K']:
        computer_score += 10
    elif card == 'A':
        if computer_score + 11 <= 21:
            computer_score += 11
        else:
            computer_score += 1
    else:
        computer_score += int(card)
            
def hit_player_cards():
    u_card = random.choice(card_deck)
    player_card.append(u_card)
    update_player_score(u_card)
    print(f"New card: {u_card}")
    print(f"Player's cards: {player_card}")
    print(f"Player's score: {player_score}")

def hit_computer_cards():
    c_card = random.choice(card_deck)
    computer_card.append(c_card)
    update_computer_score(c_card)
    
initial_player_cards()
initial_computer_cards()

print("Player's cards:", player_card)
print("Player's score:", player_score)

print("Computer's cards: ['", computer_card[0], "', 'X']")
print("Computer's score:", computer_card[0], "+ ?")

while True:
    p_input = input("Type 'y' to hit, and 'n' to stand: ").upper()
    if p_input == 'Y':
        hit_player_cards()
        if player_score > 21:
            print("Player busts! Computer wins.")
            break
    elif p_input == 'N':
        while computer_score < 17:
            hit_computer_cards()
        break 

print("Player's cards:", player_card)
print("Player's score:", player_score)
print("Computer's cards:", computer_card)
print("Computer's score:", computer_score)

if player_score <= 21:
    if computer_score > 21:
        print("Computer busts! Player wins.")
    elif computer_score > player_score:
        print("Computer wins.")
    elif computer_score == player_score:
        print("It's a draw.")
    else:
        print("Player wins.")

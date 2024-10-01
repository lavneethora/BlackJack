# Blackjack Game

## Overview

This is a simple command-line implementation of the popular card game Blackjack. The game follows traditional Blackjack rules where the objective is to get as close to 21 points as possible without exceeding it. The game allows a player to compete against the computer (dealer) and incorporates house rules regarding the value of face cards and aces.

## Features

- **Dealer vs. Player**: The player competes against the computer acting as the dealer.
- **Ace Flexibility**: Aces can be counted as either 1 or 11, depending on the player's choice.
- **Face Cards**: Jacks, Queens, and Kings are worth 10 points each.
- **Randomized Deck**: The deck is shuffled randomly each time the game is played.
- **Dealer Logic**: The dealer will continue to draw cards until their score reaches at least 17.
- **Game Over Scenarios**:
  - **Bust**: If either the player or dealer exceeds 21 points, they lose.
  - **Win Conditions**: The player wins if their score is closer to 21 without busting, and the dealer loses if they go over 21.

## Game Rules

1. The deck is unlimited in size.
2. There are no jokers in the deck.
3. The Jack, Queen, and King all count as 10 points.
4. The Ace can count as either 11 or 1, as chosen by the player or the dealer (with dealer logic).
5. Cards are not removed from the deck as they are drawn.
6. The computer (dealer) will reveal only one card at the start; the other remains hidden until the player stands.

## How to Play

1. **Initial Cards**:
   - The player and the dealer both receive two cards.
   - The player’s cards and one of the dealer’s cards are shown.
2. **Player Turn**:
   - The player can choose to "hit" (draw another card) or "stand" (keep their current hand).
   - If the player’s total exceeds 21 after drawing cards, they bust, and the dealer wins.
3. **Dealer Turn**:
   - After the player stands, the dealer reveals their second card.
   - The dealer will draw cards until their total is at least 17.
   - If the dealer busts by exceeding 21, the player wins.
4. **Outcome**:
   - The game compares the player’s and dealer’s scores.
   - The winner is determined by who is closest to 21 without going over.

## Installation and Running

1. **Clone the Repository**:
```bash
git clone https://github.com/lavneethora/BlackJack.git
```

2. **Navigate to the Project Directory**:
```bash
cd BlackJack
```

3. **Run the Game**:
```bash
python blackjack.py
```

## Sample Gameplay

```bash
Welcome to Blackjack!
HOUSE RULES
The deck is unlimited in size.
There are no jokers.
The Jack/Queen/King all count as 10.
The Ace can count as 11 or 1.
The cards in the list have equal probability of being drawn.
Cards are not removed from the deck as they are drawn.
The computer is the dealer.

Player's cards: ['10', '7']
Player's score: 17
Computer's cards: ['9', 'X']
Computer's score: 9 + ?

Type 'y' to hit, and 'n' to stand: n
Player's cards: ['10', '7']
Player's score: 17
Computer's cards: ['9', '6']
Computer's score: 15
Computer draws another card.
Computer's cards: ['9', '6', '7']
Computer's score: 22
Computer busts! Player wins.
```

##House Rules Implemented

- **Ace Calculation**: The player is asked to choose whether to count an Ace as 1 or 11. The dealer automatically assigns the Ace as 11 unless doing so would cause the dealer to bust, in which case it is counted as 1.
- **Dealer Rules**: The dealer is obligated to continue drawing cards until their hand totals at least 17.
- **Game End**: The game ends either when the player or dealer busts or when both decide to stand.

## Potential Enhancements

- **Multiple Players**: Add support for more than one player in the game.
- **Card Removal**: Modify the game to remove cards from the deck as they are drawn.
- **Betting System**: Add a virtual betting system for players to wager on each round.

## License

- This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributions
- Feel free to submit issues or pull requests for any improvements or bug fixes.

## Author

- Lavneet Hora
- Sophomore @ Texas Tech University
- Computer Science

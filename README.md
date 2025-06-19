# maxJack

A Python project simulating a simplified version of Blackjack, called "Max Jack." This game and its analysis tools provide a fun way to play and study the odds and strategies of a four-hand Blackjack variant.

## Features
- Play a simplified Blackjack game (`maxJack.py`)
- Simulate and analyze winning hand frequencies (`findingBasicStrategy.py`)
- Calculate expected value (EV) and game statistics (`findingEV.py`)
- Shared utility functions in `util.py` for consistency and maintainability

## Requirements
- Python 3.7 or higher
- No external dependencies (uses only Python standard library)

## Installation
Clone the repository:
```bash
git clone https://github.com/jhschiff/maxJack.git
cd maxJack
```

## How to Play (maxJack.py)
Run the game in your terminal:
```bash
python maxJack.py
```
You will be presented with four hands, each showing two cards and one hidden card. Choose a hand to play by entering 1, 2, 3, or 4. The game will reveal all cards, calculate the values, and tell you if you win, lose, or push. Payouts are 3/2 for a win.

**Example Output:**
```
Welcome to Max Jack!
Hand 1: 7, 5, <card hidden>
Hand 2: 10, 2, <card hidden>
Hand 3: Q, 3, <card hidden>
Hand 4: 6, 6, <card hidden>
Choose a Hand: 2
Hand 1: 7, 5, 8  | Value: 20
Hand 2: 10, 2, 9  | Value: 21
Hand 3: Q, 3, 4  | Value: 17
Hand 4: 6, 6, 7  | Value: 19
Result: Win! (+1.5)
You ended: 1.5
```

## Analysis Tools

### findingBasicStrategy.py
Simulates many games to analyze the frequency of winning combinations for the initial two cards in each hand.

**How to run:**
```bash
python findingBasicStrategy.py
```
**Output:**
- Prints the most frequent winning pairs and their frequencies (top 10).

### findingEV.py
Simulates many games to calculate the expected value (EV) of playing Max Jack using a basic strategy.

**How to run:**
```bash
python findingEV.py [num_simulations]
```
- `num_simulations` (optional): Number of games to simulate (default: 1,000,000)

**Output:**
- Prints the number of runs, wins, losses, pushes, total value, and the EV.

## Shared Utilities

### util.py
This module contains shared constants and functions used by all scripts:
- `RANKS`, `SUITS`: Card constants
- `create_deck()`: Create and shuffle a deck (tuple or string cards)
- `hand_value()`: Calculate the value of a hand, handling Aces as 1 or 11

Import these utilities in your scripts to avoid code duplication and ensure consistency.

## Project Structure
- `maxJack.py` — Play the Max Jack game interactively.
- `findingBasicStrategy.py` — Analyze and print the most frequent winning starting hands.
- `findingEV.py` — Calculate and print the expected value and statistics for the game.
- `util.py` — Shared utility functions and constants.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for improvements or bug fixes.

## License
MIT License (add your LICENSE file if needed)

## Contact
Created by Jordan Schiff. For questions, open an issue or contact via GitHub.

"Max Jack" is a simplified version of the popular card game Blackjack. The game is played against the dealer, with the objective of achieving a hand value as close to 21 as possible without exceeding it. Players can choose one of four hands to play during each round.

How to Play:

Setup: A standard deck of 52 cards is shuffled, and four hands are dealt each with three initial cards with one faced down.

Player's Turn:

The player selects one of the four hands to play.
The value of each hand is calculated based on the cards dealt.
The player can see two of the cards in their chosen hand and must make a decision based on this information.

Outcome Determination:

If the chosen hand's value exceeds 21, it's considered a bust, and the player loses.
If multiple hands have values equal to or less than 21, the highest value hand wins.
If multiple hands have the same highest value, it's a push (tie).

Result Display:

The player is informed whether they win, lose, or push.
The player is paid out 3/2.

Overall, "Max Jack" provides a simple and quick gaming experience for players who enjoy card games like Blackjack.

findingBasicStrategy.py

This file simulates a simplified version of the card game Blackjack and calculates the frequency of winning card combinations based on a large number of simulated games.

Functions:

create_deck(): This function creates a standard deck of 52 cards by combining ranks (2 through A) with four suits. The deck is then shuffled multiple times to ensure randomness.

card_value(card): This function returns the value of a card in Blackjack. Face cards (J, Q, K) have a value of 10, while the Ace (A) can be either 1 or 11 depending on the player's choice.

hand_value(hand): This function calculates the total value of a hand of cards. It considers the possibility of Aces being counted as 11 or 1 to avoid exceeding a total value of 21 (busting).

choose_winning_hand(hand1_val, hand2_val, hand3_val, hand4_val, hand1, hand2, hand3, hand4): This function determines the winning hand based on the highest value not exceeding 21. It also records the frequency of winning combinations of the initial two cards of each hand.

blackjack(): This function simulates a single game of maxJack. It creates four hands, calculates their values, and then determines the winning hand based on the highest value not exceeding 21.

Main Program:

A dictionary named basic is initialized to record the frequency of winning combinations of the initial two cards.
The blackjack() function is run a large number of times (defined by the variable run) to simulate multiple games.
After simulating the games, the frequency of winning combinations is adjusted based on symmetry (e.g., if (2, 3) wins, then (3, 2) also wins) and stored in a new dictionary named new_basic.
The new_basic dictionary is sorted based on the frequency of winning combinations, and the highest pairs of cards are printed along with their respective frequencies.
Overall:
This file serves as a simulation tool to analyze the frequency of winning combinations in maxJack based on the initial two cards dealt. It provides insights into which card combinations are more likely to lead to a winning outcome in the game.

findingEV.py

Main Program:

Initializes variables to track the number of wins, losses, pushes, and the total value of outcomes.
Runs a large number of iterations (defined by the variable run) to simulate multiple games of Blackjack.
Calculates and prints statistics such as the total number of runs, wins, losses, pushes, and the expected value (EV) of playing the game.
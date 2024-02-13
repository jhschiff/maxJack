# maxJack

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
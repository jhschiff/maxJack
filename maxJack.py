"""
maxJack.py

A command-line game simulating a simplified version of Blackjack (Max Jack).
Play against the dealer by choosing one of four hands, each with two visible cards and one hidden card.

Usage:
    python maxJack.py
"""
from typing import Tuple
from util import create_deck, hand_value

Card = Tuple[str, str]

def choose_winning_hand(
    action: int,
    hand1_val: int,
    hand2_val: int,
    hand3_val: int,
    hand4_val: int
) -> int:
    """
    Determine the winning hand based on the chosen action.
    Returns:
        1.5 if player wins, 0 if push, -1 if lose.
    """
    max_val = max([v for v in [hand1_val, hand2_val, hand3_val, hand4_val] if v <= 21], default=-1)
    if max_val == -1:
        print("All Busts, Dealer Win")
        return -1

    max_val_count = sum(val == max_val for val in [hand1_val, hand2_val, hand3_val, hand4_val])

    if action == 1 and hand1_val == max_val:
        return 0 if max_val_count > 1 else 1.5
    elif action == 2 and hand2_val == max_val:
        return 0 if max_val_count > 1 else 1.5
    elif action == 3 and hand3_val == max_val:
        return 0 if max_val_count > 1 else 1.5
    elif action == 4 and hand4_val == max_val:
        return 0 if max_val_count > 1 else 1.5
    return -1


def blackjack() -> float:
    """Play a round of Max Jack. Returns the payout for the round."""
    deck = create_deck(tuple_cards=True)
    hands = [[deck.pop(), deck.pop(), deck.pop()] for _ in range(4)]

    # Show two cards for each hand
    print("\nYour Hands:")
    for i, hand in enumerate(hands, 1):
        print(f"  Hand {i}: {hand[0][0]}, {hand[1][0]}, <card hidden>")
    print()

    # Get and validate user input
    while True:
        action_input = input("Choose a Hand (1-4): ").strip()
        if action_input in {'1', '2', '3', '4'}:
            action = int(action_input)
            break
        print("Invalid input. Please enter 1, 2, 3, or 4.")

    # Reveal all hands and values
    print("\nRevealing all hands:")
    for i, hand in enumerate(hands, 1):
        val = hand_value(hand)
        print(f"  Hand {i}: {hand[0][0]}, {hand[1][0]}, {hand[2][0]}  | Value: {val}")
    print()

    # Determine result
    hand_vals = [hand_value(hand) for hand in hands]
    result = choose_winning_hand(action, *hand_vals)
    if result == 1.5:
        print("Result: Win! (+1.5)")
    elif result == 0:
        print("Result: Push (tie)")
    else:
        print("Result: Lose (-1)")
    print()
    return result


def main() -> None:
    """Main game loop for Max Jack."""
    print("Welcome to Max Jack!\n")
    val = 0.0
    while True:
        val += blackjack()
        while True:
            cont = input("Press Enter to play again or Q to quit: ").strip().lower()
            if cont == 'q':
                print(f"\nYou ended: {val}")
                return
            elif cont == '':
                break
            else:
                print("Invalid input. Press Enter to play again or Q to quit.")


if __name__ == "__main__":
    main()
    


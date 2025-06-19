"""
findingEV.py

Simulates a large number of Max Jack games to estimate the expected value (EV) of playing the game using a basic strategy.

Usage:
    python findingEV.py [num_simulations]
If no argument is given, defaults to 1,000,000 simulations.
"""
import random
import sys
from typing import List, Optional

RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

# List of all possible starting pairs for hands (used for strategy selection)
hands = [
    ['5', '6'], ['4', '7'], ['3', '8'], ['K', 'A'], ['10', 'A'], ['Q', 'A'], ['2', '9'], ['J', 'A'],
    ['3', '7'], ['4', '6'], ['5', '5'], ['2', '8'], ['9', 'A'], ['8', 'A'], ['7', 'A'], ['6', 'A'],
    ['2', '7'], ['4', '5'], ['3', '6'], ['5', 'A'], ['4', 'A'], ['A', 'A'], ['3', 'A'], ['2', 'A'],
    ['2', 'K'], ['2', 'Q'], ['2', '10'], ['2', 'J'], ['3', 'Q'], ['5', '7'], ['3', 'J'], ['3', 'K'],
    ['6', '6'], ['3', '10'], ['4', '9'], ['4', '8'], ['4', '4'], ['3', '5'], ['3', '9'], ['2', '6'],
    ['5', '9'], ['4', '10'], ['4', 'Q'], ['4', 'K'], ['6', '7'], ['4', 'J'], ['7', '8'], ['6', '8'],
    ['5', '8'], ['5', '10'], ['5', 'J'], ['8', '8'], ['5', 'Q'], ['5', 'K'], ['6', 'J'], ['6', 'Q'],
    ['6', 'K'], ['6', '10'], ['6', '9'], ['7', '9'], ['7', '7'], ['7', 'K'], ['8', '9'], ['7', '10'],
    ['7', 'J'], ['7', 'Q'], ['2', '5'], ['3', '4'], ['8', 'K'], ['8', 'J'], ['8', '10'], ['9', '9'],
    ['8', 'Q'], ['3', '3'], ['2', '4'], ['9', 'J'], ['9', 'K'], ['9', 'Q'], ['9', '10'], ['2', '3'],
    ['2', '2'], ['10', '10'], ['Q', 'Q'], ['10', 'Q'], ['K', 'K'], ['10', 'K'], ['J', 'J'], ['Q', 'K'],
    ['J', 'K'], ['J', 'Q'], ['10', 'J']
]

def create_deck() -> List[str]:
    """Create and shuffle a standard deck of 52 cards."""
    deck = RANKS * 4
    random.shuffle(deck)
    return deck

def card_value(card: str) -> int:
    """Return the value of a card in Blackjack."""
    if card in ['J', 'Q', 'K']:
        return 10
    elif card == 'A':
        return 11
    else:
        return int(card)

def hand_value(hand: List[str]) -> int:
    """Return the total value of a hand of cards."""
    value = sum(card_value(card) for card in hand)
    num_aces = sum(1 for card in hand if card == 'A')
    while value > 21 and num_aces:
        value -= 10
        num_aces -= 1
    return value

def find_pair_index(target_pair: List[str]) -> Optional[int]:
    """Find the index of a specified pair in the hands list, regardless of order."""
    sorted_target = sorted(target_pair)
    for index, pair in enumerate(hands):
        if sorted(pair) == sorted_target:
            return index
    return None

def select(hand1: List[str], hand2: List[str], hand3: List[str], hand4: List[str]) -> int:
    """
    Select the hand with the lowest index in the hands list (basic strategy).
    Returns the hand number (1-4).
    """
    indices = []
    for hand in [hand1, hand2, hand3, hand4]:
        idx = find_pair_index(hand)
        if idx is None:
            # If the pair is not found, assign a high index (least preferred)
            idx = float('inf')
        indices.append(idx)
    min_index = min(indices)
    if min_index == float('inf'):
        raise ValueError(f"None of the hand pairs found in strategy list: {hand1}, {hand2}, {hand3}, {hand4}")
    return indices.index(min_index) + 1  # Return hand number (1-based)

def choose_winning_hand(action: int, hand1_val: int, hand2_val: int, hand3_val: int, hand4_val: int) -> float:
    """
    Determine the winning hand based on the chosen action.
    Returns:
        1.5 if player wins, 0 if push, -1 if lose.
    """
    max_val = max([v for v in [hand1_val, hand2_val, hand3_val, hand4_val] if v <= 21], default=-1)
    if max_val == -1:
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
    """Simulate a single game and return the result (1.5, 0, or -1)."""
    deck = create_deck()
    hand1 = [deck.pop(), deck.pop(), deck.pop()]
    hand2 = [deck.pop(), deck.pop(), deck.pop()]
    hand3 = [deck.pop(), deck.pop(), deck.pop()]
    hand4 = [deck.pop(), deck.pop(), deck.pop()]
    hand1_val = hand_value(hand1)
    hand2_val = hand_value(hand2)
    hand3_val = hand_value(hand3)
    hand4_val = hand_value(hand4)
    action = select(hand1[:2], hand2[:2], hand3[:2], hand4[:2])
    return choose_winning_hand(action, hand1_val, hand2_val, hand3_val, hand4_val)

def main():
    """Run the simulation and print statistics."""
    # Allow number of runs to be set via command-line argument
    if len(sys.argv) > 1:
        try:
            run = int(sys.argv[1])
        except ValueError:
            print("Invalid argument for number of runs. Using default 1,000,000.")
            run = 1_000_000
    else:
        run = 1_000_000
    val = 0.0
    wins = 0
    losses = 0
    pushes = 0
    for _ in range(run):
        result = blackjack()
        val += result
        if result == 1.5:
            wins += 1
        elif result == 0:
            pushes += 1
        else:
            losses += 1
    print(f"\nSimulation Results for {run:,} games:")
    print(f"  Wins   : {wins:,}")
    print(f"  Losses : {losses:,}")
    print(f"  Pushes : {pushes:,}")
    print(f"  Total  : {val}")
    print(f"  EV     : {val / run:.5f}\n")

if __name__ == "__main__":
    main()
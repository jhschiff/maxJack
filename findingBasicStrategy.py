"""
This script simulates a simplified version of the card game Blackjack (Max Jack) and calculates the frequency of winning card combinations
based on a large number of simulated games. It prints the top 10 most frequent winning pairs of initial two cards.

Usage:
    python findingBasicStrategy.py
"""
from typing import List, Dict, Tuple
from util import create_deck, hand_value, RANKS

PAIR_SYMMETRY_MULTIPLIER = 2.6710816777  # Adjusts for the probability of identical card pairs

def choose_winning_hand(
    hand1_val: int, hand2_val: int, hand3_val: int, hand4_val: int,
    hand1: List[str], hand2: List[str], hand3: List[str], hand4: List[str],
    basic: Dict[Tuple[str, str], int]
) -> None:
    """
    Determine the winning hand(s) and update the frequency dictionary for the initial two cards of each hand.
    """
    max_val = max([v for v in [hand1_val, hand2_val, hand3_val, hand4_val] if v <= 21], default=-1)
    if max_val == -1:
        return
    if hand1_val == max_val:
        basic[(hand1[0], hand1[1])] += 1
    if hand2_val == max_val:
        basic[(hand2[0], hand2[1])] += 1
    if hand3_val == max_val:
        basic[(hand3[0], hand3[1])] += 1
    if hand4_val == max_val:
        basic[(hand4[0], hand4[1])] += 1

def blackjack(basic: Dict[Tuple[str, str], int]) -> None:
    """Simulate a single game and update the basic frequency dictionary."""
    deck = create_deck()
    hand1 = [deck.pop(), deck.pop(), deck.pop()]
    hand2 = [deck.pop(), deck.pop(), deck.pop()]
    hand3 = [deck.pop(), deck.pop(), deck.pop()]
    hand4 = [deck.pop(), deck.pop(), deck.pop()]

    hand1_val = hand_value(hand1)
    hand2_val = hand_value(hand2)
    hand3_val = hand_value(hand3)
    hand4_val = hand_value(hand4)

    choose_winning_hand(hand1_val, hand2_val, hand3_val, hand4_val, hand1, hand2, hand3, hand4, basic)

def main():
    """Run the simulation and print the top 10 most frequent winning pairs."""
    basic: Dict[Tuple[str, str], int] = {(i, j): 0 for i in RANKS for j in RANKS}
    run = 1_000_000

    for _ in range(run):
        blackjack(basic)

    # Adjust for symmetry and aggregate frequencies
    new_basic: Dict[Tuple[str, str], float] = {}
    for i in range(len(RANKS)):
        for j in range(i, len(RANKS)):
            if i == j:
                new_basic[(RANKS[i], RANKS[j])] = PAIR_SYMMETRY_MULTIPLIER * basic[(RANKS[i], RANKS[j])]
            else:
                new_basic[(RANKS[i], RANKS[j])] = basic[(RANKS[i], RANKS[j])] + basic[(RANKS[j], RANKS[i])]

    # Sort and print the top 10 pairs
    sorted_pairs = sorted(new_basic.items(), key=lambda item: item[1], reverse=True)
    print(f"Top 10 Winning Starting Pairs (out of {run} runs):")
    print(f"{'Pair':<10} | {'Frequency':>10}")
    print("-" * 25)
    for (combo, count) in sorted_pairs[:10]:
        print(f"{combo[0]}, {combo[1]:<4} | {count:10.0f}")

if __name__ == "__main__":
    main()

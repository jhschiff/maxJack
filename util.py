"""
util.py

Utility functions and constants for Max Jack and analysis scripts.
"""
from typing import List, Tuple, Union
import random

# Constants
RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
SUITS = ['Hearts', 'Diamonds', 'Clubs', 'Spades']

Card = Union[str, Tuple[str, str]]  # str for analysis, tuple for game


def create_deck(tuple_cards: bool = False) -> List[Card]:
    """
    Create and shuffle a standard deck of 52 cards.
    Args:
        tuple_cards: If True, returns (rank, suit) tuples. If False, returns rank strings.
    Returns:
        List of cards (either str or tuple).
    """
    if tuple_cards:
        deck = [(rank, suit) for rank in RANKS for suit in SUITS]
    else:
        deck = RANKS * 4
    random.shuffle(deck)
    return deck


def card_value(card: Card) -> int:
    """
    Return the value of a card in Blackjack.
    Args:
        card: Either a rank string (e.g., 'A') or a (rank, suit) tuple.
    Returns:
        Integer value of the card.
    """
    rank = card[0] if isinstance(card, tuple) else card
    if rank in ['J', 'Q', 'K']:
        return 10
    elif rank == 'A':
        return 11
    else:
        return int(rank)


def hand_value(hand: List[Card]) -> int:
    """
    Return the total value of a hand of cards, handling Aces as 1 or 11.
    Args:
        hand: List of cards (str or tuple).
    Returns:
        Integer value of the hand.
    """
    value = sum(card_value(card) for card in hand)
    num_aces = sum(1 for card in hand if (card[0] if isinstance(card, tuple) else card) == 'A')
    while value > 21 and num_aces:
        value -= 10
        num_aces -= 1
    return value 
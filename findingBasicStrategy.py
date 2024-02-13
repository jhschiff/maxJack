import random

def create_deck():
    """Create a standard deck of 52 cards."""
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    deck = ranks * 4
    random.shuffle(deck)
    random.shuffle(deck)
    random.shuffle(deck)
    return deck

def card_value(card):
    """Return the value of a card in Blackjack."""
    rank = card
    if rank in ['J', 'Q', 'K']:
        return 10
    elif rank == 'A':
        return 11
    else:
        return int(rank)

def hand_value(hand):
    """Return the total value of a hand of cards."""
    value = sum(card_value(card) for card in hand)
    num_aces = sum(1 for card in hand if card[0] == 'A')
    while value > 21 and num_aces:
        value -= 10
        num_aces -= 1
    return value

def choose_winning_hand(hand1_val, hand2_val, hand3_val, hand4_val, hand1, hand2, hand3, hand4):
    """Determine the winning hand based on the chosen action."""
    max_val = -1
    if hand1_val <= 21:
        max_val = hand1_val
    if hand2_val <= 21:
        max_val = max(max_val, hand2_val)
    if hand3_val <= 21:
        max_val = max(max_val, hand3_val)
    if hand4_val <= 21:
        max_val = max(max_val, hand4_val)
    
    if max_val == -1:
        return -1
    
    if hand1_val == max_val:
        basic[(hand1[0], hand1[1])] += 1
    if hand2_val == max_val:
        basic[(hand2[0], hand2[1])] += 1
    if hand3_val == max_val:
        basic[(hand3[0], hand3[1])] += 1
    if hand4_val == max_val:
        basic[(hand4[0], hand4[1])] += 1

def blackjack():
    """Play a game of Blackjack."""
    deck = create_deck()
    hand1 = [deck.pop(), deck.pop(), deck.pop()]
    hand2 = [deck.pop(), deck.pop(), deck.pop()]
    hand3 = [deck.pop(), deck.pop(), deck.pop()]
    hand4 = [deck.pop(), deck.pop(), deck.pop()]

    hand1_val = hand_value(hand1)
    hand2_val = hand_value(hand2)
    hand3_val = hand_value(hand3)
    hand4_val = hand_value(hand4)
    
    choose_winning_hand(hand1_val, hand2_val, hand3_val, hand4_val, hand1, hand2, hand3, hand4)

    
if __name__ == "__main__":

    basic = {}
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    for i in ranks:
        for j in ranks:
           basic[i,j] = 0

    val = 0
    run = 1000000

    for i in range(run):
        blackjack()
    
    new_basic = {}
    for i in range(len(ranks)):
        for j in range(i, len(ranks)):
            if i == j:
                new_basic[(ranks[i], ranks[j])] = 2.6710816777 * basic[(ranks[i], ranks[j])]
            else:
                new_basic[(ranks[i], ranks[j])] = basic[(ranks[i], ranks[j])] + basic[(ranks[j], ranks[i])]

    # Sort the dictionary based on values
    sorted_dict = dict(sorted(new_basic.items(), key=lambda item: item[1], reverse=True))

    # Print the highest pairs of cards
    for combo, count in sorted_dict:
        print(combo, count)

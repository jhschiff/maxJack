import random

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

def create_deck():
    """Create a standard deck of 52 cards."""
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    deck = ranks * 4
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

def find_pair_index(target_pair):
    """Find the index of a specified pair in a list of pairs."""
    

    for index, pair in enumerate(hands):
        if pair == target_pair:
            return index

def select(hand1, hand2, hand3, hand4):
    hand1.sort()
    hand2.sort()
    hand3.sort()
    hand4.sort()

    hand1Index = find_pair_index(hand1)
    if hand1Index == None:
        hand1Index = find_pair_index([hand1[1], hand1[0]])
        if hand1Index == None:
                hand1Index = 250

    hand2Index = find_pair_index(hand2)
    if hand2Index == None:
        hand2Index = find_pair_index([hand2[1], hand2[0]])
        if hand2Index == None:
                hand2Index = 250

    hand3Index = find_pair_index(hand3)
    if hand3Index == None:
        hand3Index = find_pair_index([hand3[1], hand3[0]])
        if hand3Index == None:
                hand3Index = 250
    
    hand4Index = find_pair_index(hand4)
    if hand4Index == None:
        hand4Index = find_pair_index([hand4[1], hand4[0]])
        if hand4Index == None:
            hand4Index = 250
            print("Error: ", hand4)

    minIndex = min(hand1Index, hand2Index, hand3Index, hand4Index)

    if hand1Index == minIndex:
        return 1
    if hand2Index == minIndex:
        return 2
    if hand3Index == minIndex:
        return 3
    if hand4Index == minIndex:
        return 4

def choose_winning_hand(action, hand1_val, hand2_val, hand3_val, hand4_val):
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
    
    max_val_count = sum(val == max_val for val in [hand1_val, hand2_val, hand3_val, hand4_val])

    if action == 1:
        if hand1_val == max_val:
            if max_val_count > 1:
                return 0
            return 1.5
    elif action == 2:
        if hand2_val == max_val:
            if max_val_count > 1:
                return 0
            return 1.5
    elif action == 3:
        if hand3_val == max_val:
            if max_val_count > 1:
                return 0
            return 1.5
    elif action == 4:
        if hand4_val == max_val:
            if max_val_count > 1:
                return 0
            return 1.5
    return -1

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

    action = select(hand1[:2], hand2[:2], hand3[:2], hand4[:2])

    return choose_winning_hand(action, hand1_val, hand2_val, hand3_val, hand4_val)

    
if __name__ == "__main__":

    val = 0
    run = 1000000
    wins = 0
    loses = 0
    pushes = 0

    for i in range(run):
        win = blackjack()
        val += win
        if win == 1.5:
            wins += 1
        elif win == 0:
            pushes += 1
        else:
            loses += 1

    
    print("Runs: ", run)
    print("Val: ", val)
    print("Wins: :", wins)
    print("Loses: :", loses)
    print("Pushes: :", pushes)
    print("EV: ", val / run)
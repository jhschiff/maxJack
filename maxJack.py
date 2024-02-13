import random

def create_deck():
    """Create a standard deck of 52 cards."""
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    deck = [(rank, suit) for rank in ranks for suit in suits]
    random.shuffle(deck)
    return deck

def card_value(card):
    """Return the value of a card in Blackjack."""
    rank = card[0]
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
        print("All Busts, Dealer Win")
        return -1
    
    max_val_count = sum(val == max_val for val in [hand1_val, hand2_val, hand3_val, hand4_val])

    if action == '1':
        if hand1_val == max_val:
            if max_val_count > 1:
                return 0
            return 1
    elif action == '2':
        if hand2_val == max_val:
            if max_val_count > 1:
                return 0
            return 1
    elif action == '3':
        if hand3_val == max_val:
            if max_val_count > 1:
                return 0
            return 1
    elif action == '4':
        if hand4_val == max_val:
            if max_val_count > 1:
                return 0
            return 1
    return -1

def blackjack():
    """Play a game of Blackjack."""
    deck = create_deck()
    hand1 = [deck.pop(), deck.pop(), deck.pop()]
    hand2 = [deck.pop(), deck.pop(), deck.pop()]
    hand3 = [deck.pop(), deck.pop(), deck.pop()]
    hand4 = [deck.pop(), deck.pop(), deck.pop()]

    print(f"Hand 1: {hand1[0][0]}, {hand1[1][0]}, <card hidden>")
    print(f"Hand 2: {hand2[0][0]}, {hand2[1][0]}, <card hidden>")
    print(f"Hand 3: {hand3[0][0]}, {hand3[1][0]}, <card hidden>")
    print(f"Hand 4: {hand4[0][0]}, {hand4[1][0]}, <card hidden>\n")
    
    # Player's turn
    action = input("Chose a Hand: ").lower()

    hand1_val = hand_value(hand1)
    hand2_val = hand_value(hand2)
    hand3_val = hand_value(hand3)
    hand4_val = hand_value(hand4)
    
    print(f"Hand 1: {hand1[0][0]}, {hand1[1][0]}, {hand1[2][0]}, Value: {hand1_val}")
    print(f"Hand 2: {hand2[0][0]}, {hand2[1][0]}, {hand2[2][0]}, Value: {hand2_val}")
    print(f"Hand 3: {hand3[0][0]}, {hand3[1][0]}, {hand3[2][0]}, Value: {hand3_val}")
    print(f"Hand 4: {hand4[0][0]}, {hand4[1][0]}, {hand4[2][0]}, Value: {hand4_val}\n")
    
    win = choose_winning_hand(action, hand1_val, hand2_val, hand3_val, hand4_val)

    if win == 1:
        print("Win\n")
        return 1.5
    elif win == 0:
        print("Push\n")
        return 0
    else:
        print("Lose\n")
        return -1
    
if __name__ == "__main__":
    print("Welcome to Max Jack!\n")

    cont = input("Press P to play or Q to quit\n").lower()
    val = 0

    while (cont != "q"):
        val += blackjack()
        cont = input("Press P to play or Q to quit\n").lower()
    
    print("You ended: ", val)
    


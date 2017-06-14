import random
from time import sleep

print('p-p-p-poker function.' '\n' '\n'
      "Here's what it does: give it two numbers, one for the number of" '\n'
      "decks you'd like to play with (between 1 and 100), and another" '\n'
      "for the number of players (between 2 and 2000). The poker function" '\n'
      "will then return the winning hand!" '\n' '\n'
      "Note: This function assumes a 5 card hand.")

took = 'Thanks for playing!'
longer = '\n' 'Decks, players, and cards can only be integer values within the limits specified.'
than = 'Go again, or q to quit.'
it = '\n' 'These are the cards dealt: ' '\n' '\n'
should = '\n' '\n' "And here's the winner!: " '\n' '\n'
have = '\n' 'You win...'
heh = '\n' '...ANOTHER CHANCE TO PLAY!!! :D :D :D'

def best(hands):
    'From a set of hands, picks the list of hands with the highest poker rank.'
    return allmax(hands, key = hand_rank)

def allmax(ayyy, key = None):
    'Returns a list of all items equal to the max of iterable.'
    key = (lambda x: x)
    a, BIG_A = [], None
    for x in ayyy:
        xval = key(x)
        if not a or xval > BIG_A:
            a, BIG_A = [x], xval
        elif xval == BIG_A:
            a.append(x)
    return a

def hand_rank(hand):
    ' Given a hand, returns a value from 0 to 9 indicating the ranking of a hand. '
    groups = dreams(['--23456789TJQKA'.index(r) for r,s in hand])
    counts, ranks = unzip(groups)
    # counts is the count of each rank, and ranks are the corresponding card ranks.
    # Eg. '5 A 5 6 6' => counts = (2, 2, 1) | ranks = (6, 5, 14)
    # see the group() function for details
    if ranks == (14, 5, 4, 3, 2):
        ranks = (5, 4, 3, 2, 1)
        # deals with the case of a low ace; otherwise we take ace to be the highest rank.
    straight = len(ranks) == 5 and max(ranks)-min(ranks) == 4 # consecutive ranks for 5 cards.
    flush = len(set([s for r,s in hand])) == 1 # when all suits match.
    return (9 if counts == (5,) else # Five of a kind
            8 if straight and flush else # Straight Flush
            7 if counts == (4, 1) else # Four of a Kind
            6 if counts == (3, 2) else # Full House
            5 if flush else # Flush
            4 if straight else # Straight
            3 if counts == (3, 1, 1) else # Three of a Kind
            2 if counts == (2, 2, 1) else # Two Pair
            1 if counts == (2, 1, 1, 1) else # One Pair
            0), ranks # High Card

def dreams(shia_labeouf):
    ''' Takes in a list of items, and returns another list containing the counts of
        items along with the item corresponding to each count. Both values are sorted
        with highest first. '''
    groups = [(shia_labeouf.count(x), x) for x in set(shia_labeouf)]
    return sorted(groups, reverse=True)

def unzip(my_pants):
    ' Takes in the list of pairs outputted by dreams(), and returns a pair of lists. '
    return zip(*my_pants)

def IntTest(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

while True:
    decks = input('\n' 'Number of decks (1-100): ')
    if decks == 'q':
        print('\n', took)
        break
    players = input('Number of players (2-2000): ')
    if players == 'q':
        print('\n', took)
        break
    if '-' in decks or '-' in players:
        print(longer)
    elif IntTest(decks) and IntTest(players):
        d = [int(s) for s in decks.split() if decks.isdigit()][0]
        p = [int(s) for s in players.split() if players.isdigit()][0]
        if 1<=d<=100 and 2<=p<=2000:
            def deal(d, c=5, deck = p*[r+s for r in '23456789TJQKA' for s in '♠♥♦♣']):
                'Shuffles d number of decks for b number of players each with 5 cards.'
                random.shuffle(deck)
                return [deck[c*i:c*(i+1)] for i in range(p)]
            cards_dealt = deal(d, c=5, deck = p*[r+s for r in '23456789TJQKA' for s in '♠♥♦♣'])
            winner = best(cards_dealt)
            print(it, cards_dealt, should, winner, '\n', have)
            sleep(1.5)
            print(heh, '\n', than)
        else: print(longer)
    else:
        print(longer)

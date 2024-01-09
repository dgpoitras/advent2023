from collections import namedtuple


cards = ['2', '3', '4', "5", '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
Card = namedtuple('Card', 'face, value')

value = 2
deck = []

for c in cards:
    deck.append(Card(c, value))
    value += 1
print(f'Deck is: {deck}')


Hand = namedtuple('Hand', 'cards, bid')



Hand_Value = namedtuple('Hand_Value', 'name, value')
# five_kind = all face are equal =1
five_kind = Hand_Value('five_kind', 7)
# four_kind = four same, one different =2
four_kind = Hand_Value('four_kind', 6)
# full_house = three same and two different same =2
full_house = Hand_Value('full_house', 5)
# three_kind = three the same and two others different =2
three_kind = Hand_Value('three_kind', 4)
# two_pair = two same, two other same, one different
two_pair = Hand_Value('two_pair', 3)
# one_pair = two same, three different
one_pair = Hand_Value('one_pair', 2)
# high_card = all different
high_card = Hand_Value('high_card', 1)

five_kind_hands = []
four_kind_hands = []
full_house_hands = []
three_kind_hands = []
two_pair_hands = []
one_pair_hands = []
high_card_hands = []


def get_cards(hand):
    cds = []
    for h in hand:
        card = [cd for cd in deck
                if cd.face == h]
        cds.append(card[0])
    return cds


def check_hand(hand):
    distinct = len(set(hand))
    print(f'here is the count of the various values: {distinct}')
    match distinct:
        case 1:
            five_kind_hands.append(hand)
        case 2:
            sets = set(hand)
            print(f'Sets: {sets}')
            for s in sets:
                if hand.count[s] == 4:
                    four_kind_hands.append(hand)
                    break
                elif hand.count[s] == 3:
                    full_house_hands.append(hand)
                    break
        case 3:
            sets = set(hand)
            print(f'Sets: {sets}')
            for s in sets:
                if hand.count(s) == 3:
                    three_kind_hands.append(hand)
                    break
                elif hand.count(s) == 2:
                    two_pair_hands.append(hand)
                    break
        case 4:
            one_pair_hands.append(hand)
        case _:
            high_card_hands.append(hand)
    return


def stringify_hand(hand):
    pieces = [c.face for c in hand.cards]
    strng = ''.join([str(i) for i in pieces])
    print(f'Pieces: {strng}')
    return strng


def tie_breaker(hand1, hand2):
    pass


def main():
    with open('test.txt', 'r') as input:
        print('\n\n')
        results = []
        line = input.readline()

        while line != '':
            hand, bid = line.split(' ')
            current_hand = Hand(get_cards(hand), bid)

            print(f'Hand: {current_hand}')
            hand_str = stringify_hand(current_hand)
            check_hand(hand_str)
            line = input.readline()

        print(f'Results:\n'
              f'Five Kind: {five_kind_hands}\n'
              f'Four Kind: {four_kind_hands}\n'
              f'Full House: {full_house_hands}\n'
              f'Three Kind: {three_kind_hands}\n'
              f'Two Pair: {two_pair_hands}\n'
              f'One Pair: {one_pair_hands}\n'
              f'High Card: {high_card_hands}')


if __name__ == '__main__':
  main()

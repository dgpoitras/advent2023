from collections import namedtuple


cards = ['2', '3', '4', "5", '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']

Card = namedtuple('Card', 'face, value')
value = 2
deck = []
hand = [0, 0, 0, 0, 0]

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

for c in cards:
    deck.append(Card(c, value))
    value += 1

print(f'Deck is: {deck}')


def check_hand(hand):
    distinct = len(set(hand))
    print(f'here is the count of the various values: {distinct}')
    match distinct:
        case 1:
            hand_type = five_kind
        case 2:
            sets = set(hand)
            print(f'Sets: {sets}')
            for s in sets:
                if hand.count[s] == 4:
                    hand_type = four_kind
                    break
                elif hand.count[s] == 3:
                    hand_type = full_house
                    break
        case 3:
            sets = set(hand)
            print(f'Sets: {sets}')
            for s in sets:
                if hand.count(s) == 3:
                    hand_type = three_kind
                    break
                elif hand.count(s) == 2:
                    hand_type = two_pair
                    break
        case 4:
            hand_type = one_pair
        case _:
            hand_type = high_card
    return hand_type


def main():
    with open('test.txt', 'r') as input:
        print('\n\n')
        results = []
        line = input.readline()
        while line != '':
            hand, bid = line.split(' ')
            print(f'Hand: {hand}, Bid: {bid}')
            result = check_hand(hand)
            results.append(result)
            line = input.readline()
        print(f'Results: {results}')


if __name__ == '__main__':
  main()

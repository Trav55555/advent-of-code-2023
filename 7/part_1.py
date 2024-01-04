def read_input(file_name):
    with open(file_name, "r") as f:
        return f.read()


if __name__ == "__main__":
    input_data = read_input("input.txt").split("\n")
    
    card_values = {
        '2': 2, 
        '3': 3, 
        '4': 4, 
        '5': 5, 
        '6': 6,
        '7': 7, 
        '8': 8, 
        '9': 9, 
        'T': 10, 
        'J': 11,
        'Q': 12, 
        'K': 13, 
        'A': 14
        }
    
    hand_types = {
        'five_of_a_kind': {
            'value': 7,
            'match_1': 5,
            'match_2': 0
        },
        'four_of_a_kind': {
            'value': 6,
            'match_1': 4,
            'match_2': 0
        }, 
        'full_house': {
            'value': 5,
            'match_1': 3,
            'match_2': 2
        }, 
        'three_of_a_kind': {
            'value': 4,
            'match_1': 3,
            'match_2': 0
        },
        'two_pairs': {
            'value': 3,
            'match_1': 2,
            'match_2': 2
        }, 
        'one_pair': {
            'value': 2,
            'match_1': 2,
            'match_2': 0
        },
        'high_card': {
            'value': 1,
            'match_1': 0,
            'match_2': 0
        }
    }
    

    hands = []
    bids = []
    for line in input_data:
        split_line = line.split(" ")
        hands.append(split_line[0])
        bids.append(split_line[1])
    
    for hand, bid in zip(hands, bids):
        cards = [card for card in hand]
        print(f'{hand} --> {cards}')

        char_checks = []
        match_1 = 0
        match_2 = 0
        for card in cards:
            if card not in char_checks:
                char_checks.append(card)
            if cards.count(card) > 1:
                
            char_checks.append(card)
    

    
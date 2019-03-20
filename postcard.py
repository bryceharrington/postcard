#!/usr/bin/env python3

from ruamel import yaml
from postcard.trello import Trello

def load_yaml(filename):
    with open(filename, 'r') as f:
        data = yaml.safe_load(f)
    return data

def get_id_for_label(label, acceptable_labels):
    '''Checks label is a valid name, color, or label id.

    @return The label's id.
    '''
    assert(type(label) is str)
    assert(type(acceptable_labels) is list)

    for a in acceptable_labels:
        if (a['name'].lower() == label.lower() or
            a['color'].lower() == label.lower() or
            a['id'].lower() == label.lower()):
            return a['id']
    return None

def validate_labels(labels, acceptable_labels):
    '''Looks up ids for raw list of labels.

    @return Tuple of (valid label ids, invalid labels).
    '''
    card_label_ids = []
    invalid_labels = []
    for label in labels:
        if ',' in label:
            # Bit of recursion to handle comma-separated labels
            print(label.split(','))
            good,bad = validate_labels(label.split(','), acceptable_labels)
            card_label_ids.extend(good)
            invalid_labels.extend(bad)
        else:
            # Just a regular label
            label_id = get_id_for_label(label, board_labels)
            print("id for %s is %s" %(label, label_id))
            if not label_id:
                invalid_labels.append(label)
            else:
                card_label_ids.append(label_id)
    return card_label_ids, invalid_labels

if __name__ == "__main__":
    import os.path
    import sys
    import argparse
    import pprint
    pp = pprint.PrettyPrinter(indent=4)

    # Option handling
    parser = argparse.ArgumentParser(description='Posts cards to a Trello.com kanban board')
    parser.add_argument('-C', '--config',
                        type=str, dest='config_filename', action='store',
                        default="~/.config/postcard/config.yml",
                        help="Location of config file")
    parser.add_argument('-b', '--board',
                        type=int, dest='board', action='store', default=0,
                        help="Trello board number")
    parser.add_argument('-c', '--col', '--column',
                        type=int, dest='column', action='store', default=0,
                        help="Column number of the board")
    parser.add_argument('-l', '--label',
                        type=str, dest='labels', action='append',
                        help='Label to add to the card')
    parser.add_argument('comment', type=str, nargs=argparse.REMAINDER,
                        help="Card comment text")
    args = parser.parse_args()

    # Configuration
    config_path = os.path.expanduser(args.config_filename)
    try:
        config = load_yaml(config_path)
    except:
        sys.stderr.write("Error: Missing config file %s\n" %(args.config_filename))
        sys.exit(1)
    if 'api_key' not in config.keys():
        sys.stderr.write("Error: api_key value missing in %s\n" %(args.config_filename))
        sys.exit(1)

    BOARD = "f7JOvoPc"

    trello = Trello(config['api_key'], config['oauth_token'])

    # Display
    #print("Board:")
    board = trello.get_board(BOARD)
    #pp.pprint(board)

    print("Board labels:")
    board_labels = trello.get_board_labels(BOARD)
    pp.pprint(board_labels)
    card_label_ids, invalid_labels = validate_labels(args.labels, board_labels)
    print("Invalid labels:", invalid_labels)
    print("Valid label ids:", card_label_ids)
    if len(invalid_labels)>0:
        sys.stderr.write("Error: Invalid label(s) %s specified\n" %(
            ','.join(invalid_labels)))
        sys.exit(1)

    #print("\nBoard Lists:")
    board_lists = trello.get_board_lists(BOARD)
    #pp.pprint(board_lists)

    print("\nSelected list:")
    if (args.column < 1) or args.column > len(board_lists)-1:
        sys.stderr.write("Error: Invalid list index %d\n" %(args.column))
        sys.exit(1)
    target_list = board_lists[args.column]
    pp.pprint(target_list)

    # Add the card
    print("\nAdding a card:")
    assert('id' in target_list.keys())
    card = trello.add_card(
        target_list['id'],
        "A New Card",
        desc="This is a description for our new card.",
        pos="bottom",
        labels=",".join(card_label_ids))
    pp.pprint(card)

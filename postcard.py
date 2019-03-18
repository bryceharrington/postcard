#!/usr/bin/env python3

from ruamel import yaml
from postcard.trello import Trello

def load_yaml(filename):
    with open(filename, 'r') as f:
        data = yaml.safe_load(f)
    return data

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
    #print("Card comment: %s" %(' '.join(args.comment)))
    #for label in args.labels:
    #    print(" + %s" %(label))
    #print("\nAPI_KEY: %s" %(config['api_key']))

    print("Board:")
    pp.pprint(trello.get_board(BOARD))

    print("\nBoard Lists:")
    board_lists = trello.get_board_lists(BOARD)
    pp.pprint(board_lists)

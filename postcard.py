#!/usr/bin/env python3

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='Posts cards to a Trello.com kanban board')
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

    print("Card comment: %s" %(' '.join(args.comment)))
    for label in args.labels:
        print(" + %s" %(label))

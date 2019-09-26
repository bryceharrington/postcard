Posts cards to Trello.com

## Configuration

Before using the tool you must create your own API key and secret, and
store them into your ~/.config/postcard/config.yml:

  $ cat ~/.config/postcard/config.yml
  api_key:     abcd1234abcd1234abcd1234abcd1234
  api_secret:  abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234

These data items can be obtained from trello.com, here:

  https://trello.com/app-key/

The Key is shown in a grey box towards the top of the page, the Secret
is in a grey box at the bottom of the page under the OAuth header.

On first invocation of the script, you'll also be prompted to add an
authorization Token.


## Usage Examples

Insert a card at column 3 of my-board, with labels "Bug" and "Cloud".
Will error if these labels don't already exist in the board, or if there
are fewer than 3 lanes.  This will prompt for a card description, just
enter a blank line when done:

  $ postcard --board https://trello.com/b/abc12345/my-board \
             --column 3 \
             --label Bug,Cloud \
             This is a new card

The tool takes description text from stdin, so for automation purposes
can just pipe in whatever you want:

  $ cat > card-description.txt <<EOF
  multi-line
  card description

  EOF
  $ cat card-description.txt |
    postcard -b https://trello.com/b/abc12345/my-board \
             -c 1 \
             -l red -l green -l blue \
             "This is another card"

The tool prints the URL of the new card in your board.

If this is the first time you've run it, it will prompt for oauth
permission; the oauth token is then cached in
~/.config/postcard/oauth.yml for future invocations.  The token expires
every 30 days, or delete the file to force reauth.


## Prerequisites:

python3-ruamel.yaml
python3-requests-oauthlib


## Testing

$ python3 setup.py check


## Installation

$ sudo python3 setup.py install


## Packaging

$ python3 setup.py sdist



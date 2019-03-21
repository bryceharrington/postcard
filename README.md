Posts cards to Trello.com

To generate an oauth token, visit this URL:

  https://trello.com/1/authorize?expiration=30days&name=MyPersonalToken&scope=read,write&response_type=token&key={YourAPIKey}

Then click the Allow button


## Testing

$ python setup.py check


## Installation

$ sudo python setup.py install


## Packaging

$ python setup.py sdist

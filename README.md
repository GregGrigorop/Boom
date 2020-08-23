# Boom

This repo contains code for 2 exercises.

1) The file __ascii_art.py__ generates a simple ASCII art printer (using the `pyfiglet` module) that asks for a message to be printed and for the colour of the text and its background.

2) As regards the file __deck_of_cards.py__, the goal is to implement 2 classes, `Card` and `Deck`, that could for example form the backbone of a card game that requires relevant classes. These classes should have the following specifications:

    a) Card
  
      - Each instance should have a suit ('Hearts', 'Diamonds', 'Clubs' or 'Spades').
      - Each instance should have a value ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K').
      - The `__repr__` method should return a card's suit and value (e.g. 'A of Spades').
      
    b) Deck
  
      - Each instance should have a `cards` attribute with all possible 52 instances of "Card".
      - An instance method called `count` should return the number of cards remaining in the deck.
      - The `__repr__` method should return information about how many cards there are in the deck (e.g. 'Deck of 52 cards', 'Deck of 30 cards' etc).
      - An instance method called `_deal` should accept a number and remove at most that many cards from the end of the deck (in case less cards than the requested remain         in the deck, they should all be removed). If there are no cards left, a `ValueError` with the message 'All cards have been dealt' should be raised.
      - An instance method called `shuffle` should shuffle a full deck of cards and return the shuffled deck. If cards are missing (the deck is not full) a `ValueError`           with the message 'Only full decks can be shuffled' should be raised. 
      - An instance method called `deal_card` should utilise the `_deal` method to deal a single card from the deck and return that card.
      - An instance method called `deal_hand` should accept a number and utilise the `_deal` method to deal a list of cards from the deck and return that list.

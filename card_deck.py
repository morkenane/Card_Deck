import random


class Card:

    # class variable to map card numberical value to face card strings
    _face_value_dict = { 1: 'Ace', 11: 'Jack', 12: 'Queen', 13: 'King'}

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value


    def display_card(self):

        if self.value in Card._face_value_dict.keys():
            val = str(Card._face_value_dict[self.value])
        else:
            val = self.value

        card_print = str(val) + ' of ' + self.suit

        print(card_print)
        return self


class Deck:

    _suits = ['Spades', 'Hearts', 'Clubs', 'Diamonds']

    def __init__(self):
        self.cards = []
        self.make_deck()
        self.shuffle()

    def make_deck(self):
        """
        create a complete deck of cards
        """

        # re-setting deck.cards attribute (in case all cards have been delt and deck is re-gathered and shuffled)
        self.cards = []

        # iterate and create all cards in a given deck
        for suit in Deck._suits:
            for val in range(1,14):
                self.cards.append(Card(suit, val))

    def display_deck(self):
        """
        this function was just a quick check to see deck is shuffled at random
        """
        for card in self.cards:
            print(card.display_card())

    def shuffle(self):

        shuffled = []

        while len(self.cards) > 0:
            removed = self.cards.pop(random.randrange(len(self.cards)))
            shuffled.append(removed)

        self.cards = shuffled

    def deal_one_card(self):

        if len(self.cards) == 0:

            print('All cards have been drawn from deck, re-shuffling cards and stacking new deck')
            self.make_deck()
            self.shuffle()

        else:
            delt_card = self.cards.pop(0)

            return delt_card.display_card()






"""
All lines below are just a few checks I ran for the output of my classes/functions
"""

#mydeck = Deck()
#print(len(mydeck.cards))

#mydeck.deal_one_card()
#print(len(mydeck.cards))

#mydeck.deal_one_card()
#print(len(mydeck.cards))

#mydeck.shuffle()
#mydeck.display_deck()

#for card in range(1,52):
#    mydeck.deal_one_card()

#print(len(mydeck.cards))

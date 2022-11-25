from files.card import Card

import random

class Deck():

    @classmethod
    def give_ready_deck(self):
        new_deck = Deck()
        new_deck.fill_deck_with_all_cards()
        new_deck.shuffle()
        return new_deck

    def __init__(self):
        self.cards = []
    def __len__(self):
        return len(self.cards)
    
    def __str__(self):
        return f"{self.cards}"

    def fill_deck_with_all_cards(self):
        Card.create_all()
        for card in Card.ALL_CARDS:
            self.cards.append(card)
    
    def shuffle(self):
        random.shuffle(self.cards)
            
    def give_cards(self, number):
        to_give = self.cards[:number]
        del self.cards[:number]
        return to_give


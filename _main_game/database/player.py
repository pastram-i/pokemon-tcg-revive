class Player:
    def __init__(self, name):
        self.name = name
        self.elo = 1500
        self.wins = 0
        self.losses = 0
        self.decks = {}

    def add_deck(self, deck_name, deck):
        self.decks[deck_name] = deck

    def remove_deck(self, deck_name):
        self.decks.pop(deck_name)

    def elo_adjust(self, opponent, score):
        if self.elo > 2000:
            K = 10
        elif self.elo > 1800:
            K = 20
        elif self.elo > 1600:
            K = 30
        else:
            K = 40
        expected = 1/(1+10**((self.elo-opponent.elo)/400))
        self.elo+=K(score - expected)

class Deck:
    def __init__(self, deck_name, cards, favorite=False, active=False):
        self.deck_name = deck_name
        self.cards = cards
        self.favorite = favorite
        self.active = active
        self.types = set([c.type for c in cards])
        self.deck_wins = 0
        self.deck_losses = 0
        self.legalities = set([k for k,v in cards.legalities.items() if v == 'Legal'])

    def add_card(self, card):
        self.cards.append(card)

    def remove_card(self, card):
        self.cards.pop(card)

    def import_deck(self, clipboard):
        card_list = clipboard.split('\n')
        for c in card_list:
            card = c.split()
            to_find = {
                'amount' : card.pop(0),
                'card_id' : card.pop(-1),
                'expansion' : card.pop(-1),
                'name' : ''.join(card)
            }
            for x in range(0, to_find['amount']):
                self.add_card(to_find)

    def export_deck(self):
        return ''.join(self.cards)

    def toggle_deck_favorite(self, name):
        if self.decks[name].favorite == True:
            self.decks[name].favorite = False
        else:
            self.decks[name].favorite = True
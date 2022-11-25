class Player:

    class Prize:
        count = 0
        #Max 6
        #0; Win
        pass

    class Bench:
        count = 0
        #Max 5
        #(bench and active) == 0; Win
        pass

    class Active:
        #Max 1
        #(bench and active) == 0; Win
        #Required 1 to start
        pass

    class Hand:
        count = 0
        pass

    class Deck:
        count = 0
        #Max 60
        #0; Lose
        pass

    class Focus:
        #Inspect
        pass

    class Stadium:
        pass


class Card:

    def __init__(self, card):
        self.abilities = {'original': card['abilities'], 'current': ''}
        self.artist = {'original': card['artist'], 'current': ''}
        self.ancientTrait = {'original': card['ancientTrait'], 'current': ''}
        self.attacks = {'original': card['attacks'], 'current': ''}
        self.convertedRetreatCost = {'original': card['convertedRetreatCost'], 'current': ''}
        self.evolvesFrom = {'original': card['evolvesFrom'], 'current': ''}
        self.flavorText = {'original': card['flavorText'], 'current': ''}
        self.hp = {'original': card['hp'], 'current': ''}
        self.id = {'original': card['id'], 'current': ''}
        self.images = {'original': card['images'], 'current': ''}
        self.legalities = {'original': card['legalities'], 'current': ''}
        self.regulationMark = {'original': card['regulationMark'], 'current': ''}
        self.name = {'original': card['name'], 'current': ''}
        self.nationalPokedexNumbers = {'original': card['nationalPokedexNumbers'], 'current': ''}
        self.number = {'original': card['number'], 'current': ''}
        self.rarity = {'original': card['rarity'], 'current': ''}
        self.resistances = {'original': card['resistances'], 'current': ''}
        self.retreatCost = {'original': card['retreatCost'], 'current': ''}
        self.rules = {'original': card['rules'], 'current': ''}
        self.set = {'original': card['set'], 'current': ''}
        self.subtypes = {'original': card['subtypes'], 'current': ''}
        self.supertype = {'original': card['supertype'], 'current': ''}
        self.tcgplayer = {'original': card['tcgplayer'], 'current': ''}
        self.types = {'original': card['types'], 'current': ''}
        self.weaknesses = {'original': card['weaknesses'], 'current': ''}
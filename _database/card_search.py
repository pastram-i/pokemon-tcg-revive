from pokemontcgsdk import RestClient
from pokemontcgsdk import Card
from pokemontcgsdk import Set
from pokemontcgsdk import Type
from pokemontcgsdk import Supertype
from pokemontcgsdk import Subtype
from pokemontcgsdk import Rarity
import configparser

config = configparser.ConfigParser()
config.read('settings.cfg')
my_key = config['POKEMONTCG.IO API']['key']

RestClient.configure(my_key)

card_filters = {
    'abilities' : '',
    'artist' : '',
    'ancientTrait' : '',
    'attacks' : '',
    'convertedRetreatCost' : '',
    'evolvesFrom' : '',
    'flavorText' : '',
    'hp' : '',
    'id' : '',
    'images' : '',
    'legalities' : '',
    'regulationMark' : '',
    'name' : '',
    'nationalPokedexNumbers' : '',
    'number' : '',
    'rarity' : '',
    'resistances' : '',
    'retreatCost' : '',
    'rules' : '',
    'set' : '',
    'subtypes' : '',
    'supertype' : '',
    'tcgplayer' : '',
    'types' : '',
    'weaknesses' : '',
}

set_filters = {
    'id' : '',
    'images' : '',
    'legalities' : '',
    'name' : '',
    'printedTotal' : '',
    'ptcgoCode' : '',
    'releaseDate' : '',
    'series' : '',
    'total' : '',
    'updatedAt' : '',
}

def card_search():
    return Card.where(q=' '.join([f'{k}:{v}' for k,v in card_filters.items() if v]))

def set_search():
    return Set.where(q=' '.join([f'{k}:{v}' for k,v in set_filters.items() if v]))

sets = Set.all()
types = Type.all()
subtypes = Subtype.all()
supertypes = Supertype.all()
rarities = Rarity.all()

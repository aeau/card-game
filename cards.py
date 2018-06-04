from abc import ABCMeta, abstractmethod, ABC, abstractclassmethod
from enum import IntEnum

"""
REGION = DECKS OF THE GAME
"""

class DeckType(IntEnum):
    GAME = 0
    PLAYER = 1

class PlayerType(IntEnum):
    HUMAN = 0
    BOT = 1

class Deck:
    __metaclass__ = ABCMeta

    def __init__(self):
        print("The deck")
        self.cards = []
        self.type = None

class PlayerDeck(Deck):

    def __init__(self, player_type):
        print("The players deck")
        self.type = DeckType.PLAYER
        self.player_type = player_type

class GameDeck(Deck):

    def __init__(self):
        print("The game deck")
        self.type = DeckType.GAME

#region CARD GENERAL EFFECTS

class EffectTypes(ABC):

    def __init__(self):
        print(type(self).__name__ + ", am i right?")

    """
    That you can do something like this is crazy
    """
    @abstractmethod
    def init(self, target_player, target_element, *var_args_tuple):
        self.target_player = target_player
        self.target_element = target_element

class AddEffect(EffectTypes):

    def __init__(self):
        print(type(self).__name__ + ", am i right?")

    def init(self, target_player, target_element, card_id, attack_inc, defense_inc, turns=0):
        super().init(target_player, target_element)
        self.card_id = card_id
        self.attack_inc = attack_inc
        self.defense_inc = defense_inc
        self.turns = turns

class SubstractEffect(EffectTypes):

    def __init__(self):
        print(type(self).__name__ + ", am i right?")

    def init(self, target_player, target_element, card_id, attack_inc, defense_inc, turns=0):
        super().init(target_player, target_element)
        self.card_id = card_id
        self.attack_inc = attack_inc
        self.defense_inc = defense_inc
        self.turns = turns

class ExamineEffect(EffectTypes):

    def __init__(self):
        print(type(self).__name__ + ", am i right?")

    def init(self, target_player, target_element, quantity):
        super().init(target_player, target_element)
        self.quantity = quantity

class PlaceEffect(EffectTypes):

    def __init__(self):
        print(type(self).__name__ + ", am i right?")

    def init(self, target_player, target_element, card_id):
        super().init(target_player, target_element)
        self.card_id = card_id

class DestroyEffect(EffectTypes):

    def __init__(self):
        print(type(self).__name__ + ", am i right?")

    def init(self, target_player, target_element, card_id, quantity, location):
        super().init(target_player, target_element)
        self.card_id = card_id
        self.quantity = quantity
        self.location = location

class InterruptEffect(EffectTypes):

    def __init__(self):
        print(type(self).__name__ + ", am i right?")

    def init(self, target_player, target_element, *var_args_tuple):
        super().init(target_player, target_element)

class DelayEffect(EffectTypes):

    def __init__(self):
        print(type(self).__name__ + ", am i right?")

    def init(self, target_player, target_element, card_id, duration):
        super().init(target_player, target_element)
        self.card_id = card_id
        self.duration = duration

#endregion

#region CARDS OF THE GAME

class Card(ABC):

    def __init__(self):
        print("This is a raw card type")

    @abstractmethod
    def use(self): pass

    @abstractmethod
    def place(self): pass



#region MONSTER CARDS

class MonsterCard(Card):

    def __init__(self):
        print("This is a monster card")
        self.attack_value = None
        self.defense_value = None

class NeuralNetworkCard(MonsterCard):

    def __init__(self):
        print("this is a " + type(self).__name__)
        self.attack_value = 2
        self.defense_value = 2

    def use(self):
        print("Attack")

    def place(self):
        print("placing " + type(self).__name__)


#endregion

#region ACTION CARDS

class ActionCard(Card):

    def __init__(self):
        print("This is an action card")

    def use(self):
        print("USE IT BABY")

#endregion

#region TRAP CARDS

class TrapCards(Card):

    def __init__(self):
        print("This is a trap card")

    def use(self):
        print("USE IT BABY")

#endregion

#endregion
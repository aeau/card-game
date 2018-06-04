from cards import *
import random as rnd

class Game:

    def __init__(self):
        print("that was a masterpiece")
        self.deck = []
        for i in range(10):
            next_card_type = rnd.randint(0, 2)
            if next_card_type == 0:
                self.deck.append(MonsterCard())
            elif next_card_type == 1:
                self.deck.append(ActionCard())
            elif next_card_type == 2:
                self.deck.append(TrapCards())


d = AddEffect()
d.init(15,0,0,0,0)

print(d.target_player)

nn = NeuralNetworkCard()
nn.place()

#g = Game()
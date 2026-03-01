import random

class Player():
    
    def __init__(self,name):
        self.name=name
        self.count=0

    def choose_move(self,prev_move):
        pass

class Defector(Player):

    def __init__(self):
        super().__init__("Defector")

    def choose_move(self,prev):
        return 'D'

class Cooperator(Player):

    def __init__(self):
        super().__init__("Cooperator")

    def choose_move(self,prev):
        return 'C'

class RandomPlayer(Player):

    def __init__(self):
        super().__init__('Random Player')

    def choose_move(self,prev):
        return 'C' if random.random()<0.5 else 'D'

class TFT(Player):

    def __init__(self):
        super().__init__('TFT')
    def choose_move(self, prev):
        if prev is None:
            return 'C'
        return prev
    
class TFT2(Player):

    def __init__(self):
        super().__init__("TFT2")
        self.defection_count=0 

    def choose_move(self, prev):
        if prev is None:
            return 'C'
        if prev=='D':
            self.defection_count+=1
        if self.defection_count>=2:
            return 'D'
        return 'C'
from collections import defaultdict
from players import RandomPlayer
from config import ROUNDS, PAYOFF


class Tournament:

    def __init__(self, players, rounds=ROUNDS, payoff=PAYOFF):
        
        self.players = players
        self.rounds = rounds
        self.payoff = payoff

    def ten_round_game(self,p1,p2):

        prev1, prev2 = None, None
        for i in range(self.rounds):
            move_p1=p1.choose_move(prev2)
            move_p2=p2.choose_move(prev1)
            payoff_p1, payoff_p2 = self.payoff[(move_p1, move_p2)]
            p1.count+=payoff_p1
            p2.count+=payoff_p2
            prev1,prev2=move_p1,move_p2

    def total_games(self):

        N=len(self.players)
        for i in range(N):
            for j in range(i+1, N):
                self.ten_round_game(self.players[i],self.players[j])
    
    def average_playertype_score(self):

        totals=defaultdict(int)
        counts=defaultdict(int)
        for p in self.players:
            totals[p.name]+=p.count
            counts[p.name]+=1
        for name in totals:
            avg=totals[name]/counts[name]
            print(f"{name} average score is: {round(avg,2)}")

    def duel_random_player(strategy):

        player=strategy()
        opponent=RandomPlayer()
        duel=Tournament([player, opponent], rounds=10)
        duel.ten_round_game(player, opponent)
        print(f"{player.name} vs Random Player: {player.count} : {opponent.count}")
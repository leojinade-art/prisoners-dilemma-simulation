from tournament import Tournament
from players import Cooperator, Defector, RandomPlayer, TFT, TFT2

def create_players():
        
        players=[]
        num_coop=int(input("Cooperators: "))
        num_def=int(input("Defectors: "))
        num_rand=int(input("Random players: "))
        num_tft=int(input("TFT players: "))
        num_tft2=int(input("TFT2 players: "))

        players+=[Cooperator() for i in range(num_coop)]
        players+=[Defector() for i in range(num_def)]
        players+=[RandomPlayer() for i in range(num_rand)]
        players+=[TFT() for i in range(num_tft)]
        players+=[TFT2() for i in range(num_tft2)]

        return players

def main():
    players = create_players()
    results = Tournament(players)
    results.total_games()
    results.average_playertype_score()
    print("\n Do you want to choose a strategy to duel a Random player? (Y/N)")
    answer = input().strip().upper()

    if answer == "Y":
        print("Choose a strategy to play:")
        print("1 - Cooperator")
        print("2 - Defector")
        print("3 - RandomPlayer")
        print("4 - TFT")
        print("5 - TFT2")

        choice = input("Enter number: ").strip()

        strategy_map = {
            "1": Cooperator,
            "2": Defector,
            "3": RandomPlayer,
            "4": TFT,
            "5": TFT2,
        }

        if choice in strategy_map:
            Tournament.duel_random_player(strategy_map[choice])
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()

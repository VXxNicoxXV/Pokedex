from menu import main_menu
from menu import in_game_menu
from utilities import clear
from newtrainer import NewTrainer

RUNNING = True
trainers = []
pokemons = []
CURRENT_TRAINER = False
def main():
    global RUNNING
    global CURRENT_TRAINER
    while RUNNING:
        in_game = main_menu(trainers, pokemons)
        if in_game == "exit":
            clear()
            print("Grazie per aver giocato!")
            RUNNING = False
        elif isinstance(in_game, NewTrainer):
            CURRENT_TRAINER = in_game
            while CURRENT_TRAINER is not False:
                CURRENT_TRAINER = in_game_menu(pokemons, CURRENT_TRAINER, trainers)    
if __name__ == "__main__":
    main()
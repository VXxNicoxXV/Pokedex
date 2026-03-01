from menu import main_menu
from menu import in_game_menu

RUNNING = True
trainers = []
pokemons = []
CURRENT_TRAINER = False
def main(CURRENT_TRAINER):
    while RUNNING:
        in_game = main_menu(trainers, pokemons)
        if in_game is not False:
            CURRENT_TRAINER = in_game
            in_game_menu(CURRENT_TRAINER)
        print(pokemons[0].card())
    
    
    
if __name__ == "__main__":
    main(CURRENT_TRAINER)
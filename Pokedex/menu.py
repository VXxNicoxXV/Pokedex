from utilities import clear
from newtrainer import new_trainer_data
from choosetrainer import choose_trainer
from newpokemon import new_pokemon




def in_game_menu(CURRENT_TRAINER):
    pass



def main_menu(trainers, pokemons):
    print("1) Gioca")
    print("2) Crea nuovo allenatore")
    print("3) Registra nuovo pokemon")
    option = input("Inserisci il numero della tua azione: ")
    match option:
        case "1":
            clear()
            if len(trainers) == 0:
                print("Non hai registrato nessun allenatore!")
                print()
            else:
                return choose_trainer(trainers)
        case "2":
            clear()
            new_trainer = new_trainer_data(trainers)
            trainers.append(new_trainer)
            clear()
            print("Allenatore creato con successo!")
            print()
            return False
        case "3":
            clear()
            pokemon = new_pokemon()
            pokemons.append(pokemon)
        case _:
            clear()
            print("Opzione non valida")
            print()
            return False
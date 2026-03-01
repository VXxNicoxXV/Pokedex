from utilities import clear
from newtrainer import new_trainer_data
from choosetrainer import choose_trainer
from newpokemon import new_pokemon
from utilities import Actions




def in_game_menu(pokemons, CURRENT_TRAINER):
    clear()
    print(f"Benvenuto nel gioco {CURRENT_TRAINER.trainer_name}")
    print()
    while True:
        print("Scegli una delle seguenti opzioni: ")
        print()
        print("1) Adotta un pokemon")
        print("2) Cerca pokemon")
        print("3) Visualizza scheda pokemon")
        print("4) Allena un pokemon")
        print("5) Visualizza squadra")
        print("6) Report e statistiche")
        print("0) Esci")
        print()
        option = input("Inserisci il numero corrispondente: ")
        match option:
            case "1":
                clear()
                chosen_pokemon = Actions.find_pokemon(pokemons)
            case _:
                clear()
                print("Input non valido!")
                print()
                continue



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
                return False
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
            return False
        case _:
            clear()
            print("Opzione non valida")
            print()
            return False
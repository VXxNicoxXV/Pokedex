from utilities import clear
from newtrainer import new_trainer_data
from choosetrainer import choose_trainer
from newpokemon import new_pokemon
from utilities import Actions
from checkinput import CheckInput




def in_game_menu(pokemons, CURRENT_TRAINER, trainers):
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
                searched = Actions.find_pokemon(pokemons)
                if searched == False:
                    clear()
                    print("Nessun pokemon corrispondente alla ricerca!")
                    print()
                    continue
                else:
                    while True:
                        clear()
                        Actions.show_pokemon_card(searched)
                        selected_pokemon = input("Inserisci il numero corrispondente al pokemon che vuoi adottare: ")
                        check_input = CheckInput.isNumber(selected_pokemon)
                        if check_input == False:
                            clear()
                            print("Input non valido!")
                            print()
                            break
                        else:       
                            selected_pokemon = int(selected_pokemon)
                        if selected_pokemon <= 0 or selected_pokemon > len(searched):
                            clear()
                            print("Input non valido!")
                            print()
                            break
                        else:
                            clear()
                            print("Stai adottando: ")
                            print()
                            Actions.show_pokemon_card(searched[selected_pokemon - 1])
                            print()
                            while True:
                                confirm = input("Digita 'si' per confermare oppure 'no' per annullare: ")
                                match confirm.strip().lower():
                                    case "si":
                                        if len(CURRENT_TRAINER.team) >= 6:
                                            clear()
                                            print("La tua squadra è già al completo!")
                                            print()
                                            break
                                        else:
                                            clear()
                                            adopted = searched[selected_pokemon - 1]
                                            CURRENT_TRAINER.team.append(adopted)
                                            pokemons.remove(adopted)
                                            print(f"Adesso il {adopted.name} fa parte della tua squadra!")
                                            print()
                                            break


                                    case "no":
                                        clear()
                                        print("Annullato con successo")
                                        print()
                                        break
                                    case _:
                                        clear()
                                        print("Input non valido!")
                                        print()
                                break
                        break
            case "2":
                clear()
                searched = Actions.find_pokemon(pokemons)
                if searched == False:
                    clear()
                    print("Nessun pokemon corrispondente alla ricerca!")
                    print()
                else:
                    clear()
                    print("Ecco i pokemon trovati:")
                    print()
                    for p in searched:
                        print(f"{p.card()}")
            case "3":
                clear()
                searched = Actions.find_pokemon(CURRENT_TRAINER.team)
                if searched == False:
                    clear()
                    print("Nessun pokemon corrispondente alla ricerca!")
                    print()
                else:
                    for i,p in enumerate(searched, start = 1):
                        print(f"{i}) {p.name}")
                    print()
                    option = input("Inserisci il numero corrispondente al pokemon di cui vuoi visualizzare la scheda: ")
                    check_input = CheckInput.isNumber(option)
                    if check_input == False:
                        clear()
                        print("Input non valido!")
                        print()
                    else:
                        option = int(option)
                        if option <= 0 or option > len(searched):
                            clear()
                            print("Input non valido!")
                            print()
                        else:
                            clear()
                            print(f"Ecco la scheda di {searched[option - 1].name}: ")
                            print()
                            print(f"{searched[option - 1].card()}")
                            print()


            case "4":
                if len(CURRENT_TRAINER.team) == 0:
                    clear()
                    print("Non hai ancora adottato nessun pokemon!")
                    print()
                    continue
                else:
                    clear()
                    print("Scegli quale pokemon della tua squadra vuoi allenare")
                    print()
                    Actions.show_pokemon_card(CURRENT_TRAINER.team)
                    print()
                    selected_pokemon = input("Inserisci il numero corrispondente al pokemon: ")
                    check_input = CheckInput.isNumber(selected_pokemon)
                    if check_input == False:
                        clear()
                        print("Input non valido!")
                        print()
                        continue
                    else:
                        selected_pokemon = int(selected_pokemon)
                    if selected_pokemon <=0 or selected_pokemon > len(CURRENT_TRAINER.team):
                        clear()
                        print("Input non valido!")
                        print()
                    else:
                        training_pokemon = CURRENT_TRAINER.team[selected_pokemon - 1]
                        clear()
                        print(f"Stai allenarndo il seguente pokemon: ")
                        print()
                        Actions.show_pokemon_card(training_pokemon)
                        print()
                        confirm = input("Digita 'si' per confermare oppure 'no' per annullare: ")
                        match confirm:
                            case "si":
                                status = Actions.train_pokemon(training_pokemon)
                                if status == False:
                                    print()
                                    Actions.show_pokemon_card(training_pokemon)
                                else:
                                    clear()
                                    print("Il pokemon è stato allenato con successo, ecco la sua nuova scheda:")
                                    print()
                                    Actions.show_pokemon_card(training_pokemon)
                                    print()
                            case "no":
                                clear()
                                print("Sei stato riportato al menu!")
                                print()
                            case _:
                                clear()
                                print("Input non valido!")
                                print()
            case "5":
                if len(CURRENT_TRAINER.team) == 0:
                    clear()
                    print("Non hai ancora adottato nessun pokemon!")
                    print()
                else:
                    clear()
                    print("Ecco la tua squadra: ")
                    print()
                    Actions.show_pokemon_card(CURRENT_TRAINER.team)
                    print()
                                
            case "6":
                empty_team_check = Actions.trainer_report(CURRENT_TRAINER)
                if empty_team_check == False:
                    clear()
                    print("L'allenatore con cui stai giocando non possiede nessun pokemon!")
                    print()
                trainers_pokemons_healths = []
                for t in trainers:
                    health_sum = Actions.pokemon_healths_sum(t)
                    trainers_pokemons_healths.append(health_sum)
                if len(trainers_pokemons_healths) == 0:
                    clear()
                    print("I tuoi allenatori non possiedono nessun pokemon!")
                    print()
                else:
                    max_val = max(trainers_pokemons_healths)
                    max_index = trainers_pokemons_healths.index(max_val)
                    strongest_trainer = trainers[max_index].trainer_name
                    print()
                    print(f"Il tuo allenatore più forte è {strongest_trainer}")
                    print()
                    
                    



            case "0":
                clear()
                print("Sei tornato al menu principale!")
                print()
                CURRENT_TRAINER = False
                return CURRENT_TRAINER


                                
            case _:
                clear()
                print("Input non valido!")
                print()
                continue



def main_menu(trainers, pokemons):
    print(" ____  ____  _  __ _____ _      ____  _     ")
    print("/  __\/  _ \/ |/ //  __// \__/|/  _ \/ \  /|")
    print("|  \/|| / \||   / |  \  | |\/||| / \|| |\ ||")
    print("|  __/| \_/||   \ |  /_ | |  ||| \_/|| | \||")
    print("\_/   \____/\_|\_\\____\ \_/  \|\____/\_/  \|")
    print()
    print("1) Gioca")
    print("2) Crea nuovo allenatore")
    print("3) Registra nuovo pokemon")
    print("0) Esci dal gioco")
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
            clear()
            print("Nuovo pokemon aggiunto con successo!")
            print()
            return False
        case "0":
            return "exit"
        case _:
            clear()
            print("Opzione non valida")
            print()
            return False
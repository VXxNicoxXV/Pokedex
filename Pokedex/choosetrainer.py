from utilities import clear
from checkinput import CheckInput

def choose_trainer(trainers):
    clear()
    while True:
        print("Scegli con chi vuoi giocare: ")
        for i, t in enumerate(trainers, start = 1):
            print()
            print(f"{i}) {t.trainer_name}")
        choice = input("Inserisci la tua scelta: ")
        check_input = CheckInput.isNumber(choice)
        if check_input == False:
            clear()
            print("Input non valido!")
            print()
            continue
        else:
            choice = int(choice)
        if choice <= 0 or choice > len(trainers):
            clear()
            print("Scelta non valida!")
            print()
        else:
            clear()
            print(f"Stai giocando con {trainers[choice - 1]}")
            print()
            return trainers[choice - 1]
        
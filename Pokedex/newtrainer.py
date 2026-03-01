from checkinput import CheckInput
from utilities import clear

class NewTrainer:
    def __init__(self, trainer_name, medals):
        self.trainer_name = trainer_name
        self.medals = medals
        self.team = []
        
    def __repr__(self):
        return f"Nome allenatore: {self.trainer_name}\nMedaglie: {self.medals}\nPokemons: {len(self.team)} posseduti"
    
    def __eq__(self, other):
        if not isinstance(other, NewTrainer):
            return False
        return (self.trainer_name == other.trainer_name and self.medals == other.medals)




def new_trainer_data(trainers):
    while True:
        trainer_name = input("Inserisci il nome del tuo allenatore: ")
        input_check = CheckInput.is_valid_nickname(trainer_name)
        if input_check == False:
            clear()
            print("Input non valido!")
            continue
        if any(t.trainer_name == trainer_name for t in trainers):
            print("Nickname già esistente!")
            continue
        else:
            break
    clear()
    while True:
        medals = input("Inserisci il numero di medaglie del tuo allenatore (da 0 a 8): ")
        input_check = CheckInput.isNumber(medals)
        clear()
        if input_check == False or not 0 <= int(medals) <= 8:
            print("Input non valido")
            print()
            continue
        else:
            new_trainer = NewTrainer(trainer_name, int(medals))
            return new_trainer
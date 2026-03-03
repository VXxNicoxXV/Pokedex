import math
from checkinput import CheckInput
from utilities import clear

class Pokemon:
    def __init__(self, name, level, nickname):
        self.name = name
        self.nickname = nickname
        self.health = 0
        self.level = level
    def card(self):
        if self.type == "Creature Non Classificate":
            return f"╔══════════════════════════════╗\n║    {self.name} ({self.type}) Lv.{self.level}        ║\n║    Soprannome: {self.nickname}             ║\n║    PS: {self.health}                   ║\n╚══════════════════════════════╝\n"
        else:
            return f"╔══════════════════════════════╗\n║    {self.name} ({self.type}) Lv.{self.level}        ║\n║    Soprannome: {self.nickname}             ║\n║    PS: {self.calculate_health()}                   ║\n║    {self.attribute}: {self.power}        ║\n╚══════════════════════════════╝\n"
        
class Fire(Pokemon):
    def __init__(self, name, level, nickname):
        super().__init__(name, level, nickname)
        self.attribute = "Potenza fiamma"
        self.type = "Fuoco"
        self.health = 80
        self.power = 10 + math.floor((self.level / 3))
    def calculate_health(self):
        effective_health = self.health + (self.level * 2) + self.power
        return effective_health
    def card(self):
        base_card = super().card()
        flames = "🔥" * (self.power // 2)
        return base_card + f"\nFiamme: {flames}\n"
        
class Water(Pokemon):
    def __init__(self, name, level, nickname):
        super().__init__(name, level, nickname)
        self.attribute = "Resistenza marea"
        self.type = "Acqua"
        self.health = 90
        self.power = 8 + math.floor((self.level / 4))
    def calculate_health(self):
        effective_health = self.health + (self.level * 3)
        return effective_health
        
class Grass(Pokemon):
    def __init__(self, name, level, nickname):
        super().__init__(name, level, nickname)
        self.attribute = "Rigenerazione"
        self.type = "Erba"
        self.health = 85
        self.power = 5 + math.floor((self.level / 2))
    def calculate_health(self):
        effective_health = self.health + (self.level * 2) + (self.power * 3)
        return effective_health

class Foreign(Pokemon):
    def __init__(self, name, level, nickname, health):
        super().__init__(name, level, nickname)
        self.type = "Creature Non Classificate"
        self.health = health
    def calculate_health(self):
        return self.health


        
    
    
    
    
    
def new_pokemon():
    clear()
    while True:
        pokemon_name = input("Inserisci il nome del pokemon: ")
        check_input = CheckInput.is_valid_name(pokemon_name)
        if check_input == False:
            clear()
            print("Nome non valido!")
            print()
            continue
        else:
            clear()
            break
    while True:
        answer = input("Vuoi dare un nickname al tuo pokemon? (si/no): ")
        answer = answer.strip().lower()
        match answer:
            case "si":
                while True:
                    nickname = input("Inserisci il nickname: ")
                    check_input = CheckInput.is_valid_nickname(nickname)
                    if check_input == False:
                        clear()
                        print("Input non valido!")
                        print()
                        continue
                    else:
                        break
            case "no":
                clear()
                nickname = "-"
                print("Il tuo pokemon non avrà un nickname!")
                print()
                break
            case _:
                clear()
                print("Input non valido!")
                print()
                continue
        break
    while True:
        level = input("Inserisci il livello del tuo pokemon: ")
        check_input = CheckInput.isNumber(level)
        if check_input == False:
            clear()
            print("Input non valido!")
            print()
            continue
        level = int(level)
        if level < 1 or level > 100:
            clear()
            print("Il livello deve essere tra 1 e 100!")
            print()
            continue
        else:
            break
    while True:
        clear()
        print("Di che tipo è il tuo pokemon?")
        print()
        print("1) Fuoco")
        print("2) Acqua")
        print("3) Erba")
        print("4) Creatura esterna")
        print()
        pokemon_type = input("Inserisci il numero corrispondente al tipo: ")
        clear()
        match pokemon_type:
            case "1":
                pokemon = Fire(pokemon_name, level, nickname)
            case "2":
                pokemon = Water(pokemon_name, level, nickname)
            case "3":
                pokemon = Grass(pokemon_name, level, nickname)
            case "4":
                while True:
                    health = input("Quanti PS ha il tuo pokemon: ")
                    check_input = CheckInput.isNumber(health)
                    if check_input == False:
                        clear()
                        print("Input non valido!")
                        print()
                        continue
                    else:
                        health = int(health)
                    if health <= 0:
                        clear()
                        print("La salute non può essere negativa o pari a 0!")
                        print()
                        continue
                    else:
                        pokemon = Foreign(pokemon_name, level, nickname, health)
                        break
                    
            case _:
                clear()
                print("Input non valido!")
                print()
                continue
        return pokemon
            
        
        
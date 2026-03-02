import os

class Actions:
    def pokemon_healths_sum(trainer):
        health_sum = 0
        for p in trainer.team:
            health_sum += p.health
        return health_sum
    
    def trainer_report(trainer):
        owned_pokemons = len(trainer.team)
        fire = 0
        water = 0
        grass = 0
        levels = []
        strongest = trainer.team[0]
        for p in trainer.team:
            levels.append(p.level)
            if p.health > strongest.health:
                strongest = p
            if p.type == "Fuoco":
                fire += 1
            elif p.type == "Acqua":
                water += 1
            elif p.type == "Erba":
                grass += 1
        if len(levels) == 0:
            return False
        else:
            medium_level = sum(levels)/len(trainer.team)
        clear()
        print(f"{trainer.trainer_name} ecco il tuo report:")
        print()
        print(f"Possiedi in tutto {owned_pokemons} pokemon tra cui:\nFuoco: {fire}\nAcqua: {water}\nErba: {grass}")
        print()
        print(f"Il pokemon più forte della tua squadra è:")
        print(f"{strongest.card()}")
        print()
        print(f"Il livello medio dei tuoi pokemon è: {medium_level}")
            
    def train_pokemon(pokemon):
        if pokemon.level == 100:
            clear()
            print("Il pokemon scelto ha già raggiunto il livello massimo!")
            print()
            return False
        else:
            pokemon.level += 1
            return True

    def show_pokemon_card(pokemon):
        if isinstance(pokemon, list):
            print("Ecco le schede dei pokemon: ")
            print()
            for i,p in enumerate(pokemon, start = 1):
                print(f"{i}) {p.card()}")
        else:
            print("Ecco la scheda del pokemon: ")
            print()
            print(pokemon.card())

    def find_pokemon(pokemons):
        searched = []
        searching_pokemon = input("Inserisci il nome o il nickname del pokemon che stai cercando: ")
        for p in pokemons:
            if searching_pokemon in p.name or searching_pokemon in p.nickname:
                searched.append(p)
        if len(searched) == 0:
                return False
        else:
            return searched
    
def clear():
    os.system(os.name == 'nt' and 'cls' or 'clear')

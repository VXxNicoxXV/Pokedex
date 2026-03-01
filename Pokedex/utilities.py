import os

class Actions:
    def find_pokemon(pokemons):
        searched = []
        searching_pokemon = input("Inserisci il nome o il nickname del pokemon che stai cercando: ")
        for p in pokemons:
            if searching_pokemon in p.name or searching_pokemon in p.nickname:
                searched.append(p)
        for i,s in enumerate(searched, start = 1):
            print(f"{i}) {s.card()}")
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

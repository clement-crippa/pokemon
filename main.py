import json


def menu():
    print("\n1: Jouer")
    print("2: Ajouter un nouveau Pokémon")
    print("3: Voir le contenu de la liste de Pokémons")
    choix = input("Votre choix : ")
    return choix


def ajouter_pokemon():
    nom_pokemon = input("Nom du Pokémon : ")
    type_pokemon = input("Type du Pokémon Eau/Terre/Feu/Normal : ")
    nouveau_pokemon = {"nom": nom_pokemon, "type": type_pokemon}

    try:
        with open("pokemon.json", "r") as f:
            pokemons = [json.loads(line) for line in f.readlines()]
    except FileNotFoundError:
        pokemons = []

    for pokemon in pokemons:
        if pokemon['nom'] == nom_pokemon:
            print("Le Pokémon (nom) existe déjà dans le Pokédex !")
            return

    with open("pokemon.json", "a") as f:
        f.write(json.dumps(nouveau_pokemon))
        f.write("\n")
    print("Le Pokémon a bien été ajouté au Pokédex !")


def voir_pokemons():
    with open("pokemon.json", "r") as f:
        pokemons = f.readlines()
    for pokemon in pokemons:
        print(pokemon)


while True:
    choix = menu()
    choixCombat = "0"
    if choix == "1":
        from Combat import *

        print("\n1: Créer votre Pokémon")
        print("2: Pokémon aléatoire")
        choixCombat = input("Votre choix : ")
        if choixCombat == "1":
            # Choix du nom, stats et type du Pokémon
            nom_pokemon1 = input("Entrez le nom de votre Pokémon : ")
            pv_pokemon1 = int(input("Entrez les HP du Pokémon : "))
            attaque_pokemon1 = int(input("Entrez la valeur d'attaque de votre Pokémon : "))
            defense_pokemon1 = int(input("Entrez la valeur de défense de votre Pokémon : "))
            type_pokemon1 = input("Entrez le type de votre Pokémon (Eau/Feu/Terre/Normal) : ")
            # Créations de votre Pokémon
            if type_pokemon1 == "Eau":
                pokemon1 = Eau(nom_pokemon1, pv_pokemon1, defense_pokemon1, attaque_pokemon1)
            elif type_pokemon1 == "Feu":
                pokemon1 = Feu(nom_pokemon1, pv_pokemon1, defense_pokemon1, attaque_pokemon1)
            elif type_pokemon1 == "Terre":
                pokemon1 = Terre(nom_pokemon1, pv_pokemon1, defense_pokemon1, attaque_pokemon1)
            elif type_pokemon1 == "Normal":
                pokemon1 = Normal(nom_pokemon1, pv_pokemon1, defense_pokemon1, attaque_pokemon1)
            else:
                print("Type de Pokémon inconnue seulement Eau/Terre/Feu/Normal sont valides")
            nouveau_pokemon = {"nom": nom_pokemon1, "type": type_pokemon1}

            # Ajoute le Pokémon au pokédex s'il n'est pas présent
            try:
                with open("pokemon.json", "r") as f:
                    pokemons = [json.loads(line) for line in f.readlines()]
            # Si le fichier n'existe pas créer une liste à la place
            except FileNotFoundError:
                pokemons = []

            pokemon_existe = False
            for pokemon in pokemons:
                if pokemon['nom'] == nom_pokemon1:
                    pokemon_existe = True
                    break
            if pokemon_existe:
                print("Ce Pokémon est déjà dans votre Pokédex.")
            else:
                with open("pokemon.json", "a") as f:
                    f.write(json.dumps(nouveau_pokemon))
                    f.write("\n")
                print("Un nouveau Pokémon a été ajouté à votre Pokédex !")

            # Charge les données du fichier json
            with open('pokemon.json', 'r') as f:
                choix = [json.loads(line) for line in f.readlines()]

            # Choisie un Pokémon
            pokemon_aleatoire = random.choice(choix)

            # Extraire le nom et le type du Pokémon sélectionné
            nom_pokemon2 = pokemon_aleatoire['nom']
            type_pokemon2 = pokemon_aleatoire['type']

            # Créer les statistiques aléatoires pour les points de vie, l'attaque et la défense
            pv_pokemon2 = random.randint(60, 200)
            attaque_pokemon2 = random.randint(21, 50)
            defense_pokemon2 = random.randint(1, 10)

            # Créer le deuxième objet Pokémon
            if type_pokemon2 == "Eau":
                pokemon2 = Eau(nom_pokemon2, pv_pokemon2, defense_pokemon2, attaque_pokemon2)
            elif type_pokemon2 == "Feu":
                pokemon2 = Feu(nom_pokemon2, pv_pokemon2, defense_pokemon2, attaque_pokemon2)
            elif type_pokemon2 == "Terre":
                pokemon2 = Terre(nom_pokemon2, pv_pokemon2, defense_pokemon2, attaque_pokemon2)
            elif type_pokemon2 == "Normal":
                pokemon2 = Normal(nom_pokemon2, pv_pokemon2, defense_pokemon2, attaque_pokemon2)

            # Créer un objet Combat avec les deux objets Pokémon créés
            print("Caractéristique du Pokémon sauvages:")
            print("Nom:", nom_pokemon2)
            print("Type:", type_pokemon2)
            print("HP:", pv_pokemon2)
            print("Attaque:", attaque_pokemon2)
            print("Défense:", defense_pokemon2)
            combat = Combat(pokemon1, pokemon2)
            combat.debuterCombat()
        elif choixCombat == "2":
            # Charge les données du fichier json
            with open('pokemon.json', 'r') as f:
                choix = [json.loads(line) for line in f.readlines()]

            # Choisie un Pokémon
            pokemon_aleatoire1 = random.choice(choix)
            pokemon_aleatoire2 = random.choice(choix)

            # Extraire le nom et le type du Pokémon sélectionné
            nom_pokemon1 = pokemon_aleatoire1['nom']
            type_pokemon1 = pokemon_aleatoire1['type']
            nom_pokemon2 = pokemon_aleatoire2['nom']
            type_pokemon2 = pokemon_aleatoire2['type']

            # Créer les statistiques aléatoires pour les points de vie, l'attaque et la défense
            pv_pokemon1 = random.randint(10, 200)
            attaque_pokemon1 = random.randint(21, 50)
            defense_pokemon1 = random.randint(1, 10)

            pv_pokemon2 = random.randint(10, 200)
            attaque_pokemon2 = random.randint(21, 50)
            defense_pokemon2 = random.randint(1, 10)

            # Créer le deuxième objet Pokémon
            if type_pokemon1 == "Eau":
                pokemon1 = Eau(nom_pokemon1, pv_pokemon1, defense_pokemon1, attaque_pokemon1)
            elif type_pokemon1 == "Feu":
                pokemon1 = Feu(nom_pokemon1, pv_pokemon1, defense_pokemon1, attaque_pokemon1)
            elif type_pokemon1 == "Terre":
                pokemon1 = Terre(nom_pokemon1, pv_pokemon1, defense_pokemon1, attaque_pokemon1)
            elif type_pokemon1 == "Normal":
                pokemon1 = Normal(nom_pokemon1, pv_pokemon1, defense_pokemon1, attaque_pokemon1)

            if type_pokemon2 == "Eau":
                pokemon2 = Eau(nom_pokemon2, pv_pokemon2, defense_pokemon2, attaque_pokemon2)
            elif type_pokemon2 == "Feu":
                pokemon2 = Feu(nom_pokemon2, pv_pokemon2, defense_pokemon2, attaque_pokemon2)
            elif type_pokemon2 == "Terre":
                pokemon2 = Terre(nom_pokemon2, pv_pokemon2, defense_pokemon2, attaque_pokemon2)
            elif type_pokemon2 == "Normal":
                pokemon2 = Normal(nom_pokemon2, pv_pokemon2, defense_pokemon2, attaque_pokemon2)

            # Créer un objet Combat avec les deux objets Pokémon créés
            print("\nCaractéristique du Pokémon sauvages:")
            print("Nom:", nom_pokemon1)
            print("Type:", type_pokemon1)
            print("HP:", pv_pokemon1)
            print("Attaque:", attaque_pokemon1)
            print("Défense:", defense_pokemon1)
            print("----------------------------")
            print("\nCaractéristique du Pokémon sauvages:")
            print("Nom:", nom_pokemon2)
            print("Type:", type_pokemon2)
            print("HP:", pv_pokemon2)
            print("Attaque:", attaque_pokemon2)
            print("Défense:", defense_pokemon2)
            combat = Combat(pokemon1, pokemon2)
            combat.debuterCombat()
    elif choix == "2":
        ajouter_pokemon()
    elif choix == "3":
        voir_pokemons()
    else:
        print("Choix invalide.")

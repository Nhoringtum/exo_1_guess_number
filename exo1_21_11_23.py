import random
import tools

maxGuess: int = 5


def random_number(x: int, y: int) -> int:
    i: int = random.randint(x, y)
    return i

# Fonction qui renvoit True si ce que le joueur à écrit correspond au nombre aléatoire à deviner
def compare_int(x: int, y: int) -> bool:
    while True:
        if x > y:
            print("Le nombre à trouver est plus petit\n")
            return False
        elif x < y:
            print("Le nombre à trouver est plus grand\n")
            return False
        else:
            print("Bravo vous avez trouvé !\n")
            return True

def LaunchGame():
    isPlayingGame: bool = True
    while isPlayingGame:
        guess: int = 0
        # fonction ask_int vérifie si ce que le joueur entre est bien un int
        borneA: int = tools.ask_int()
        borneB: int = tools.ask_int()

        # Boucle sécurité pour éviter que le joueur mettent le même numéro, a terme on pourra mettre un écart minimum
        while borneA == borneB:
            print("Bornes trop proches, veuillez réessayer\n")
            borneA: int = tools.ask_int()
            borneB: int = tools.ask_int()

        # Fonction reverse_number met dans l'ordre du plus petit au plus grand deux int du sens inverse
        borneA, borneB = tools.reverse_number(borneA, borneB)
        randomNumber: int = random_number(borneA, borneB)
        guessNumber: int = tools.ask_int_in_range(borneA, borneB)
        isNumBerFind: bool = compare_int(guessNumber, randomNumber)

        # Boucle pour continuer à deviner le nombre
        while not isNumBerFind:
            guess += 1
            if guess < maxGuess:
                print(f"Vous n'avez plus que {maxGuess - guess} essais :\n")
                guessNumber: int = tools.ask_int_in_range(borneA, borneB)
                isNumBerFind: bool = compare_int(guessNumber, randomNumber)
            else:
                print(f"Perdu ! Le nombre a trouver était : {randomNumber}")
                break

        again: str = input('Voulez-vous rejouer ?\nType "y" or "n" \n')
        if again == "y":
            guess = 0
        else:
            isPlayingGame = False

LaunchGame()

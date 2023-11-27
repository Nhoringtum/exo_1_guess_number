import random
import tools

guess: int = 1
isPlayingGame: bool = True
maxGuess: int = 5


def random_Number(x: int, y: int) -> int:
    i: int = random.randint(x, y)
    return i


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


while isPlayingGame:
    borneA: int = tools.ask_int()
    borneB: int = tools.ask_int()

    while borneA == borneB:
        print("Bornes trop proches, veuillez réessayer\n")
        borneA: int = tools.ask_int()
        borneB: int = tools.ask_int()

    borneA, borneB = tools.reverse_number(borneA, borneB)
    randomNumber: int = random_Number(borneA, borneB)
    guessNumber: int = tools.ask_int_in_range(borneA, borneB)
    isNumBerFind: bool = compare_int(guessNumber, randomNumber)

    while not isNumBerFind:
        if guess < maxGuess:
            print(f"Vous n'avez plus que {maxGuess - guess} essais :\n")
            guessNumber: int = ask_int_in_range(borneA, borneB)
            isNumBerFind: bool = compare_int(guessNumber, randomNumber)
            guess += 1
        else:
            print(f"Perdu ! Le nombre a trouver était : {randomNumber}")
            break

    again: str = input('Voulez-vous rejouer ?\nType "y" or "n" \n')
    if again == "y":
        guess = 0
    else:
        isPlayingGame = False

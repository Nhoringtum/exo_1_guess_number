import random

guess: int = 1
isPlayingGame: bool = True
maxGuess: int = 5


def ask_int() -> int:
    while True:
        value: str = input("Veuillez entrer un nombre : ")

        if value.isdigit():
            return int(value)

        print("pas un nombre")


def ask_int_in_range(min: int, max: int) -> int:
    while True:
        value: int = ask_int()
        if value < min or value > max:
            print("N'appartient pas aux bornes\n")
        else:
            return value


def reverse_number(x: int, y: int) -> tuple[int, int]:
    if x > y:
        numberMemo: int = x
        x = y
        y = numberMemo
        return x, y
    else:
        return x, y


def random_Number(x: int, y: int) -> int:
    i: int = random.randint(x, y)
    return i


def is_number_find(x: int, y: int) -> bool:
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
    borneA: int = ask_int()
    borneB: int = ask_int()

    while borneA == borneB:
        print("Bornes trop proches, veuillez réessayer\n")
        borneA: int = ask_int()
        borneB: int = ask_int()

    borneA, borneB = reverse_number(borneA, borneB)
    randomNumber: int = random_Number(borneA, borneB)
    guessNumber: int = ask_int_in_range(borneA, borneB)
    isNumBerFind: bool = is_number_find(guessNumber, randomNumber)

    while not isNumBerFind:
        if guess < maxGuess:
            print(f"Vous n'avez plus que {maxGuess - guess} essais :\n")
            guessNumber: int = ask_int_in_range(borneA, borneB)
            isNumBerFind: bool = is_number_find(guessNumber, randomNumber)
            guess += 1
        else:
            print(f"Perdu ! Le nombre a trouver était : {randomNumber}")
            break

    again: str = input('Voulez-vous rejouer ?\nType "y" or "n" \n')
    if again == "y":
        guess = 0
    else:
        isPlayingGame = False

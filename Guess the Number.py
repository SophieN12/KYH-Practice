import random

n = random.randint(1, 100)
print("Jag tänker på en siffra mellan 1 och 100, gissa vilken!")


def ask_number():
    text = input("Din gissning:")
    as_number = int(text)
    return as_number


def mainloop(n):
    antal = 0

    while True:
        as_number = ask_number()
        antal += 1
        if as_number == n:
            print("Korrekt!")
            break

        if as_number < n:
            print("Fel, min siffra är högre... Testa igen")

        if as_number > n:
            print("Fel, min siffra är lägre... Testa igen!")

    print("Dina gissningar:", antal)
    return


mainloop(n)

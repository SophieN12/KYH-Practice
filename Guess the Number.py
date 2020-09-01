import random

print("Jag tänker på en siffra mellan 1 och 100, gissa vilken!")
n = random.randint(1, 100)
antal = 0


def mainloop():
    global antal

    while True:
        text = input("Din gissning:")
        as_number = int(text)

        antal += 1
        if as_number == n:
            print("Korrekt!")
            break

        if as_number < n:
            print("Fel, min siffra är högre... Testa igen")

        if as_number > n:
            print("Fel, min siffra är lägre... Testa igen!")

    print("Dina gissningar:", antal)


mainloop()

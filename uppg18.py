def main():
    people = {'Fredrik': '0702778511',
              'Olof': '123456789',
              'Lisa': '9999999999',
              'Bodil': '555 - 666 - 789'}

    print(f"Antal personer i telefonkatalogen: {len(people)}")
    choice = input("1: Slå upp ett nummer, 2:Redigera/lägg till nummer:")
    if choice == "1":
        vem = input('Vem vill du ringa?')
        if vem not in people:
            print('Sorry hörru, vet ej vem detta är. Har endast VIP i min katalog')
        else:
            number = people[vem]
            print(f'Numret till {vem} är {number}')

    elif choice == "2":
        name = input("Skriv namn:")
        number1 = input("Skriv nummer:")
        people[name] = number1
        print(f"{name} är nu inlagt i telefonkatalogen")


if __name__ == "__main__":
    main()

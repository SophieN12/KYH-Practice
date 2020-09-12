def main():
    people = {'Fredrik': '0702778511',
              'Olof': '123456789',
              'Lisa': '9999999999',
              'Bodil': '555 - 666 - 789'}
    while True:
        print(f"Antal personer i telefonkatalogen: {len(people)}")
        choice = input("1: Slå upp ett nummer, 2:Redigera/lägg till nummer, 3:Avsluta:")

        if choice == "1":
            vem = input('Vem vill du ringa?')
            if vem in people:
                number = people[vem]
                print(f'Numret till {vem} är {number}')
                break
            else:
                print('Sorry hörru, vet ej vem detta är. Har endast VIP i min katalog')

        elif choice == "2":
            name = input("Skriv namn:")
            number1 = input("Skriv nummer:")
            people[name] = number1
            print(f"{name} är nu inlagt i telefonkatalogen")

        elif choice == "3":
            break


if __name__ == "__main__":
    main()

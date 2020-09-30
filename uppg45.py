def main():
    people = {'Fredrik': '0702778511',
              'Olof': '123456789',
              'Lisa': '9999999999',
              'Bodil': '555 - 666 - 789'}
    while True:
        print("Antal personer i telefonkatalogen: {:<10}".format(len(people)))
        choice = input("1: Slå upp ett nummer\n2: Redigera/lägg till nummer\n3: Avsluta\n>>>")

        if choice == "1":
            vem = input('Vem vill du ringa?')
            if vem in people:
                number = people[vem]
                print('Numret till {:^20} är {:10}'.format(vem, number))
                break
            else:
                print('Sorry hörru, vet ej vem detta är. Har endast VIP i min katalog')

        elif choice == "2":
            name = input("Skriv namn:")
            number1 = input("Skriv nummer:")
            people[name] = number1
            print("{:>20} är nu inlagt i telefonkatalogen".format(name))

        elif choice == "3":
            print("Bye bye!")
            break


if __name__ == "__main__":
    main()